# Validation

Run from checkout root:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
git diff --check
```

Offline checks cover the eight JobTread policies, scheduling calculations, isolated-HOME installation/conflict backups/idempotency, selected dependencies, updater refusal and explicit fast-forward gates, lightweight email approval and absence of operations source from the public package. Synthetic tests require no business credentials.

Pattern scans do not establish exhaustive privacy. No new OAuth, live mailbox/Dropbox/JobTread write, memory migration, service restart or scheduled execution is established by this migration. Historical rollout evidence is preserved privately outside this package.
