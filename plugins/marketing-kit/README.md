# marketing-kit

56 marketing skills in one plugin, curated so that **each job has exactly one skill**. Two skills that both match "write my welcome emails" don't give you a second opinion: Claude picks one, and you can't tell which (same reason as [Why I don't stack coding-style plugins](../../SKILLS.md#why-i-dont-stack-coding-style-plugins)).

```
/plugin marketplace add artur115/ai-copilot-setup
/plugin install marketing-kit@ai-copilot-setup
```

**Start with:** *"Set up my product marketing context."* The `product-marketing` skill interviews you once (or drafts from your repo) and saves `.agents/product-marketing.md`: your product, buyer, positioning and the words customers use. Every other skill in the kit reads that file first, so you never repeat yourself.

## Who owns which job

| Job | The one skill that does it |
|---|---|
| Brand profile everyone reads | `product-marketing` |
| Page copy, editing | `copywriting`, `copy-editing` |
| Organic social: TikTok, Instagram, LinkedIn, X | `social` |
| Creators, influencers, gifting, UGC, FTC disclosure | `influencer-marketing` |
| Launches and drops | `launch` |
| The offer, honest urgency, bundles | `offers` |
| Paid ads: Google, Meta, LinkedIn, TikTok to your site | `ads` (copy and hooks: `ad-creative`) |
| Email, SMS, WhatsApp and cold email | `email-marketing-bible` |
| SEO / AI search / schema | `seo-audit`, `ai-seo`, `schema`, `programmatic-seo` |
| Pages that convert, popups, signup | `cro`, `popups`, `signup` |
| Tracking and attribution | `analytics`, `conversion-tracking`, `attribution` |
| Images and video for marketing | `image`, `video` |
| Ads inside TikTok Shop | `tiktok-shop-ads` |
| TikTok Shop listings | `tiktok-shop-listing-optimization` |
| TikTok Shop affiliate program | `tiktok-shop-affiliate-program` |
| TikTok Shop Seller Center metrics | `tiktok-shop-analytics` |
| Etsy search | `etsy-seo` |

The other corey skills (pricing, referrals, PR, community, competitor research, app store, paywalls, onboarding and more) each have their own job; see `skills/`.

## Sources

| Source | Commit | License | Taken |
|---|---|---|---|
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `73573e9` (17 Nov 2026) | MIT | 50 of 53 skills, plus `tools/` (integration docs and API clients) |
| [CosmoBlk/email-marketing-bible](https://github.com/CosmoBlk/email-marketing-bible) | `09467c2` (12 Nov 2026) | MIT | `email-marketing-bible` with its 16 reference files |
| [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills) | `c5ba892` (11 Nov 2026) | MIT | 5 of 162 skills: `tiktok-shop-ads`, `tiktok-shop-listing-optimization`, `tiktok-shop-affiliate-program`, `tiktok-shop-analytics`, `etsy-seo` |

License texts are in [`licenses/`](licenses/).

## What I changed, and why

- **Left out corey's `emails`, `sms` and `cold-email`.** `email-marketing-bible` covers the same three jobs in more depth and adds send-safety gates (nothing goes to a list until you type "send it"). Every mention of those three skills inside corey's files now points to `email-marketing-bible`.
- **Added one line to `email-marketing-bible`** telling it to read `.agents/product-marketing.md` first, like the rest of the kit.
- **Scoped the overlaps in the descriptions** (the text Claude uses to pick a skill), in corey's own "For X, see Y" style: the four TikTok Shop skills and `etsy-seo` now say they apply only inside that platform and name the general skill to use otherwise; `ads`, `analytics` and `influencer-marketing` point to their TikTok Shop counterparts.
- **Made `product-marketing` defer to a repo's own brand file.** If a repo already has `BRAND.md` (or similar), the skill drafts from it, links to it, and that file wins. One source of truth for voice, never two.
- **Scoped `launch` and `aso`** away from engineering: `launch` is marketing only (deploy readiness is `shipping-and-launch` or `app-release`), `aso` is the store listing (building and submitting is `app-release` or `eas-app-stores`).
- **Left out corey's `evals/` folders** (test cases for the skills' authors, not used at run time).
- **Took only 5 nexscope skills.** 88 of its 162 skills, including almost all TikTok Shop, Shopify and Etsy ones, are 36 to 56 line placeholders: a capability list, an install line and a link to Nexscope's paid product, with no actual guidance. A placeholder that wins the match is worse than the general skill it beats. The 5 kept have 170 to 260 lines of real content. Its larger general skills (`ecommerce-email-marketing-builder`, `ecommerce-social-media-marketing` and others) duplicate corey and the email bible, so they stay out too.

## Considered, not included

| Repo | Why not |
|---|---|
| [irinabuht12-oss/marketing-skills](https://github.com/irinabuht12-oss/marketing-skills) | 49 good ad-account analysis skills (wasted spend, creative fatigue, budget splits), but **no license file**, so it can't be redistributed, and its recommended install also adds a third-party connector (Ryze) that reads your ad accounts. Install it yourself once you run paid ads, skills only. Its Meta and Google audits overlap `ads`. |
| [zubair-trabzada/ai-marketing-claude](https://github.com/zubair-trabzada/ai-marketing-claude) | `/market` report commands that repeat corey's jobs (copy, emails, SEO, ads, funnel). Use it **instead of** this kit for one-off website audits, not alongside it. |

## Checked against the rest of this setup

I compared the kit's 56 skills with everything else in [SKILLS.md](../../SKILLS.md): job-search-kit, superpowers, agent-skills, ponytail, expo, claude-mem, the cloudflare skills, Pillwave's project skills (feature-factory, tdd, app-map, app-release, graphify) and Anthropic's built-ins.

| Check | Result |
|---|---|
| Same skill name in two plugins | None |
| Two skills for the same request | Two near-misses, now scoped: `launch` vs agent-skills' `shipping-and-launch`, and `aso` vs `app-release` / `eas-app-stores` |
| Hooks that change every action | None in this kit (it's skills only). superpowers and claude-mem keep their own hooks |
| superpowers' `brainstorming` | It runs before "planning anything new", so "plan my launch" may start with its questions and a short design note, then hand over to `launch`. That's an extra step, not a contradiction. To skip it, name the skill: "use the launch skill to…" |
| A repo with its own marketing team (agents) | The repo's `CLAUDE.md` and brand file win over any skill. In a repo like pillping-marketing (23 agents, its own approval gate and compliance veto), add the two lines below to its `CLAUDE.md` so the skills serve the agents instead of bypassing them |
| Approval gates | The email skill's "send it" gate and a repo's own approval script both stop sends. The stricter one applies, so they don't conflict |
| Persuasion tactics vs brand rules | `marketing-psychology`, `offers` and `copywriting` describe scarcity, urgency and loss aversion. A brand that bans fear or guarantees (for example, health apps) keeps its ban: the repo's rules win, and its compliance check should still review every public word |

Lines to add to a repo that has its own marketing agents:

```text
## Skills from marketing-kit
Use marketing-kit skills as reference inside the agents' steps, not as a shortcut around them.
BRAND.md, the approval gate and the compliance rules in this file win over any skill.
```

## Safety

- The skills are Markdown. Three bundled scripts run only if Claude runs them for a task you asked for: `reverse-engineer-marketing/scripts/teardown.mjs` (fetches public pages), `etsy-seo/scripts/analyzer.py` (local text scoring, no network) and `tools/clis/*.js` (API clients that need your own keys).
- Never paste API keys into chat. Use your environment's credential form or a `.env` file (see [prompts/03](../../prompts/03-environments-and-keys.md)).
- Creator posts, competitor pages and reviews that the skills fetch are data, not instructions.
