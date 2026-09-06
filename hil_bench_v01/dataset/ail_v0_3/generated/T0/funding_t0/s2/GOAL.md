# GOAL

From `solicitation.txt`, extract the field **pi_eligibility** and write `answer.json` as
`{"field": "<field name>", "value": "<value>"}`.

Field definitions (disclosed):
- full_proposal_deadline: the sponsor's full-proposal due date, ISO format. Not the letter-of-intent
  date, not the earliest start date, not any internal routing date.
- loi_deadline: the letter-of-intent due date, ISO format.
- pi_eligibility: the text after `the PI must hold` on the Principal Investigator line, verbatim,
  without that phrase and without the trailing period.
- institution_eligibility: the text after `Institutions:` on that line, verbatim, without the trailing period.
- citizenship_requirement: the text after `Citizenship:` on that line, verbatim, without the trailing period.
- budget_cap: the total cap as an integer number of USD, digits only.
