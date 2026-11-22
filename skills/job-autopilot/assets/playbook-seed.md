# Application playbook

Runs read this first and add one dated line per new lesson. Never store passwords, emails or phone numbers here.

## Sites and ATS
- LinkedIn Easy Apply only offers resumes saved in LinkedIn unless the form shows "Upload resume". If it can't take
  the tailored PDF, apply on the company's own site instead.
- Resume upload with Claude in Chrome: if `file_upload` refuses a local path ("only files this session is allowed to
  read"), stage the file first (`device_stage_files`) and upload the returned staged path.
- Ashby refuses a second application to the same company: check Gmail for a confirmation first.
- Workday, iCIMS, Taleo, SuccessFactors need a candidate account (see the account rule in the routine).
- Some companies cap applications (e.g. 3 per 6 months): note it in the sheet before applying to a second role there.
- Email-only postings: write the email as a Gmail draft with the job link; log "Needs you: send draft + attach resume".
- Aggregator reposts (Joblet, RemoteHunter, TalentHop and similar) are noise: find the original posting.
- LinkedIn "Top job picks" can be empty when the profile is thin: rely on searches.

## Environment
- Runs often can't run git in the mounted folder (lock files, "Operation not permitted"): write files only; the
  Mac's auto-sync commits and pushes.

## LinkedIn outreach
