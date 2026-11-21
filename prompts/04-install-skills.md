# 04 · Install skills and plugins

See [SKILLS.md](../SKILLS.md) for what each one does. Install only what you'll use. For a job search, start with this repo's kit and the Anthropic built-ins. Add the build skills when you start a coding project.

```text
Install these into my job-search repo so every cloud session has them:
1. This repo's plugin:  /plugin marketplace add artur115/ai-copilot-setup
                        /plugin install job-search-kit@ai-copilot-setup
2. From glebis/claude-skills, copy tdd and feature-factory into .claude/skills/
   and keep their MIT license file.
3. addyosmani/agent-skills as a plugin (marketplace addyosmani/agent-skills,
   plugin agent-skills@addy-agent-skills).
Record each source repo and commit in .claude/SKILLS-SOURCES.md, commit, and show
me how to check the skills loaded.
```

Optional, on your Mac: **one** coding method, `superpowers@claude-plugins-official`, plus `ponytail@ponytail` for short code. ECC, mattpocock-skills and andrej-karpathy-skills do the same job as superpowers; pick one of them *instead*, never several. See [Why I don't stack coding-style plugins](../SKILLS.md#why-i-dont-stack-coding-style-plugins).

Optional, for app projects: `expo@claude-plugins-official`, and `app-map` / `app-release` from glebis/claude-skills.
