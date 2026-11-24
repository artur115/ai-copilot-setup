# Screen a list of companies ("N. Name - URL" lines, or a saved LinkedIn post) via public Greenhouse/Ashby/Lever job APIs.
# Usage: python3 tools/screen_boards.py <list.txt|post.html> <out.json>
import re, json, sys, urllib.request, urllib.error, html
from concurrent.futures import ThreadPoolExecutor
src = open(sys.argv[1], encoding="utf-8", errors="ignore").read()
m = re.search(r'<script type="application/ld\+json">(.*?)</script>', src, re.S)
body = json.loads(m.group(1))['articleBody'] if m else src  # a saved LinkedIn post page, or a plain text list
cos = re.findall(r'^\d+\.\s+(.+?)\s+-\s+(\S+)$', body, re.M)
UA = {'User-Agent': 'Mozilla/5.0'}
def get(url, timeout=20):
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout)
        return r.geturl(), r.read().decode('utf-8', 'ignore')
    except urllib.error.HTTPError as e: return getattr(e, 'url', url), ''
    except Exception: return url, ''
def resolve(u):
    if 'lnkd.in' not in u: return u
    final, page = get(u)
    if 'lnkd.in' in final:  # LinkedIn interstitial page holds the target
        m = re.search(r'href="(https?://(?!lnkd\.in|www\.linkedin)[^"]+)"', page)
        return html.unescape(m.group(1)) if m else final
    return final
TITLE = re.compile(r'\b(data|analytics)\b.*\b(engineer|engineering|platform|architect)|\bhead of (data|analytics)|\bdirector,? (of )?(data|analytics)|\bdata (platform|infrastructure)', re.I)
LEVEL = re.compile(r'\b(staff|principal|lead|manager|director|head|senior staff|vp)\b', re.I)
LOC_OK = re.compile(r'remote|united states|\bus\b|usa|u\.s\.|anywhere|north america|americas|houston|austin|texas|\btx\b', re.I)
LOC_BAD = re.compile(r'\b(emea|europe|uk|india|apac|canada only|germany|poland|brazil|london|berlin|dublin|amsterdam|singapore|australia|japan|mexico|argentina)\b', re.I)
def match(title, loc):
    return bool(TITLE.search(title) and LEVEL.search(title) and LOC_OK.search(loc or '') and not (LOC_BAD.search(loc or '') and not re.search(r'us|united states|remote', loc or '', re.I)))
assert match('Staff Data Engineer', 'Remote - US') and not match('Software Engineer', 'Remote') and not match('Staff Data Engineer', 'London, UK') and match('Manager, Analytics Engineering', 'Remote (United States)')
def slugs(name, url):
    cands = []
    m = re.search(r'(?:greenhouse\.io/(?:embed/job_board\?for=)?|ashbyhq\.com/|lever\.co/)([A-Za-z0-9_.-]+)', url)
    if m: cands.append(m.group(1))
    base = re.sub(r'[^a-z0-9]', '', name.lower())
    cands += [base, name.lower().replace(' ', '-'), name.lower().split()[0]]
    return list(dict.fromkeys(c for c in cands if c))
def jobs_for(name, url):
    out = []
    for s in slugs(name, url):
        _, t = get(f'https://boards-api.greenhouse.io/v1/boards/{s}/jobs')
        if t.startswith('{') and '"jobs"' in t:
            for j in json.loads(t)['jobs']: out.append((j['title'], (j.get('location') or {}).get('name', ''), j['absolute_url'], j.get('updated_at', '')[:10], 'greenhouse:'+s))
            break
        _, t = get(f'https://api.ashbyhq.com/posting-api/job-board/{s}?includeCompensation=true')
        if t.startswith('{') and '"jobs"' in t:
            for j in json.loads(t)['jobs']:
                loc = j.get('location', '') + (' Remote' if j.get('isRemote') else '')
                out.append((j['title'], loc, j['jobUrl'], (j.get('publishedAt') or '')[:10], 'ashby:'+s))
            break
        _, t = get(f'https://api.lever.co/v0/postings/{s}?mode=json')
        if t.startswith('[') and len(t) > 2:
            for j in json.loads(t):
                c = j.get('categories', {})
                out.append((j['text'], (c.get('location') or '') + ' ' + (j.get('workplaceType') or ''), j['hostedUrl'], '', 'lever:'+s))
            break
    return out
def work(c):
    name, url = c
    real = resolve(url)
    js = jobs_for(name, real)
    return {'company': name, 'careers': real, 'board': js[0][4] if js else None, 'total': len(js),
            'matches': [dict(title=t, location=l, url=u, date=d) for t, l, u, d, _ in js if match(t, l)]}
with ThreadPoolExecutor(8) as ex: res = list(ex.map(work, cos))
json.dump(res, open(sys.argv[2], 'w'), indent=1)
print(len(cos), 'companies;', sum(1 for r in res if r['board']), 'boards found;', sum(len(r['matches']) for r in res), 'matching jobs')
for r in res:
    for m in r['matches']: print(f"{r['company']} | {m['title']} | {m['location'][:40]} | {m['date']} | {m['url']}")
print('NO BOARD:', ', '.join(r['company'] for r in res if not r['board']))
