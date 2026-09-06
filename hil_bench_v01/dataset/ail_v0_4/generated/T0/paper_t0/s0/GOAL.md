# GOAL

Check citation **[4]** in `manuscript.md` against entry `ref4` in `references.bib` and write
`citation_check.json` as `{"citation": <number>, "consistent": <true|false>, "discrepancies": [<field names>]}`.

Disclosed rules: compare exactly four fields -- `author` (the first author's surname), `year`, `venue`
(the journal or proceedings name) and `pages` (the page range, in order). A field is a discrepancy
if the in-text attribution and the bib entry differ on it. `consistent` is true only if the
discrepancy list is empty. Check only the citation named above; other citations may also be wrong
and are not asked about.
