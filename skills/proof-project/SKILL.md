---
name: proof-project
description: Turns one resume claim (for example "raised LTV 38%" or "cut warehouse cost 40%") into a small public GitHub project that shows the method on synthetic data, with tests, CI and a results-first README, so a recruiter can click through and check it. Use when the user says "build a proof project", "back up this resume line", "make a portfolio project for this claim", or wants a project that matches a target job.
---

# Proof project

Goal: a recruiter reads one resume line, clicks the link, and within a minute sees the method, the result and that it runs.

## 1. Pin down the claim

Ask for the exact resume line and:
- the metric, the before and after, and the time frame
- the method they really used (model, test, pipeline, tool)
- what they are allowed to share. Default: nothing from the employer; all data synthetic.

If the claim has no number or no method, help them sharpen it first. Never make up a result.

## 2. Plan small

Propose a plan the user approves before you write code:
- **Data:** a generator script that plants the behaviour behind the claim (seeded, so results reproduce).
- **Method:** the same technique they used, in plain SQL or Python that runs on a laptop (DuckDB, pandas, scikit-learn). No cloud account needed.
- **Proof:** tests for the logic (pytest or similar) and a GitHub Actions workflow that runs them.
- **README:** opens with a results table, then one section per question, then "how to run" in three commands. A line that says the data is synthetic.

Keep it to what one weekend of work could produce. Two or three questions, not ten.

## 3. Build

Build in small steps with tests first for the core logic (use the `tdd` skill if installed). Commit as you go. Make `make all` (or one script) regenerate the data, run the analysis and write the charts.

## 4. Ship

- Create the public repo (or ask the user to create it if this session can't).
- Check CI passes and the README renders with its charts.
- Add the project to the resume's Projects section and the user's site, linked from the claim it proves.

## Example

[artur115/social-commerce-ltv](https://github.com/artur115/social-commerce-ltv) backs up "+38% new-buyer LTV from social channels": GA4-style synthetic events, DuckDB SQL, six attribution models including Markov, a 180-day LTV model and a CUPED A/B test, with 18 pytest tests and GitHub Actions CI.
