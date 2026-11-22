# 17 · Marketing kit

56 marketing skills with one skill per job, curated from three MIT repos so they don't compete or contradict each other. Details and sources: [plugins/marketing-kit](../plugins/marketing-kit/README.md).

Install (Claude Code on your Mac, or a project's cloud session):

```
/plugin marketplace add artur115/ai-copilot-setup
/plugin install marketing-kit@ai-copilot-setup
```

Then paste this into the project for your product or brand:

```text
Set up my product marketing context with the product-marketing skill.
Draft it from this repo if there is one, then ask me what's wrong or missing.
Push for the exact words my customers use. Save it as .agents/product-marketing.md.
Then suggest the first three marketing tasks for this week, each naming the one
skill from marketing-kit that does it.
```

Good next prompts:

| You want | Say |
|---|---|
| Posts for the week | "Plan this week's TikTok and Instagram posts" (`social`) |
| Creators | "Find and vet 10 micro creators for a gifting round" (`influencer-marketing`) |
| A launch or drop | "Plan the launch for the new collection" (`launch`, `offers`) |
| Emails | "Write the welcome series and a restock email; don't send anything" (`email-marketing-bible`) |
| Ads | "Should I run Meta ads yet, and with what budget?" (`ads`, `ad-creative`) |
| TikTok Shop | "Optimize my TikTok Shop listing for this product" (`tiktok-shop-listing-optimization`) |

Rules:
- Install **one** marketing kit. Don't add zubair-trabzada/ai-marketing-claude or nexscope's full set alongside it; see "Considered, not included" in the kit README.
- Nothing goes to a list until you type "send it" (the email skill's send gate). Read every post and email before it goes out.
- API keys for ad or email platforms go in the environment's credential form or a `.env` file, never in chat.
- A repo with its own `BRAND.md`, agents or approval script keeps its rules: they win over any skill. Add the two lines from "Checked against the rest of this setup" in the kit README to that repo's `CLAUDE.md`.
- With superpowers installed, "plan my launch" may start with its brainstorming questions. Say "use the launch skill" to go straight to it.
