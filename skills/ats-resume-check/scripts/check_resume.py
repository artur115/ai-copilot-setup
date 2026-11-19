#!/usr/bin/env python3
"""Check a resume PDF for common ATS problems.

Usage: python3 check_resume.py resume.pdf
Needs: pip install pypdf
Reports page count, fonts (flags Type 3 and non-embedded fonts), how much text
can be extracted, the first lines of extracted text, and the links found.
"""
import re
import sys

try:
    from pypdf import PdfReader
except ImportError:
    sys.exit("Install pypdf first: pip install pypdf")


def fonts_on_page(page):
    found = {}
    res = page.get("/Resources") or {}
    fonts = res.get("/Font") or {}
    for ref in fonts.values():
        f = ref.get_object()
        name = str(f.get("/BaseFont", "?")).lstrip("/")
        subtype = str(f.get("/Subtype", "?")).lstrip("/")
        embedded = False
        desc = f.get("/FontDescriptor")
        if subtype == "Type0":
            desc_font = f["/DescendantFonts"][0].get_object()
            desc = desc_font.get("/FontDescriptor")
            subtype = "Type0/" + str(desc_font.get("/Subtype", "?")).lstrip("/")
        if desc is not None:
            d = desc.get_object()
            embedded = any(k in d for k in ("/FontFile", "/FontFile2", "/FontFile3"))
        if subtype == "Type3":
            embedded = True
        found[name] = (subtype, embedded)
    return found


def main(path):
    r = PdfReader(path)
    problems = []
    print(f"Pages: {len(r.pages)}")
    if len(r.pages) > 2:
        problems.append("More than 2 pages. Most recruiters expect 1 to 2.")

    fonts = {}
    for p in r.pages:
        fonts.update(fonts_on_page(p))
    print("\nFonts:")
    for name, (sub, emb) in sorted(fonts.items()):
        print(f"  {name:40s} {sub:22s} {'embedded' if emb else 'NOT embedded'}")
        if "Type3" in sub:
            problems.append(f"Type 3 font {name}: some ATS parsers read it as gibberish. Re-export with a TrueType or OpenType font.")
        elif not emb:
            problems.append(f"Font {name} is not embedded; text may render or parse differently.")

    text = "\n".join((p.extract_text() or "") for p in r.pages)
    words = re.findall(r"[A-Za-z]{2,}", text)
    print(f"\nExtractable words: {len(words)}")
    if len(words) < 150:
        problems.append("Very little extractable text. The resume may be an image or use outlined text.")
    odd = sum(1 for ch in text if ord(ch) > 0x2FFF and not ch.isspace())
    if text and odd / max(1, len(text)) > 0.02:
        problems.append("Many unusual characters in extracted text; check fonts and ligatures.")
    print("\nFirst lines as an ATS would read them:")
    for line in [l for l in text.splitlines() if l.strip()][:12]:
        print("  | " + line[:100])

    links = []
    for p in r.pages:
        for a in p.get("/Annots") or []:
            a = a.get_object()
            uri = (a.get("/A") or {}).get("/URI")
            if uri:
                links.append(str(uri))
    print(f"\nClickable links ({len(links)}):")
    for u in links:
        print("  " + u)
    if not links:
        problems.append("No clickable links. Add your site, LinkedIn and GitHub as real links.")

    print("\nResult:")
    if problems:
        for pr in problems:
            print("  FIX: " + pr)
        return 1
    print("  OK: no ATS problems found by these checks.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
