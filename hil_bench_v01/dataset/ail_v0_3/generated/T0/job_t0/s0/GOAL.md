# GOAL

From `posting.txt`, write `requirements.json` as

`{"required": [<each bullet under "Required qualifications", verbatim>],
 "work_authorization_required": <true|false>, "clearance_required": <true|false>,
 "location": "<the text after `Location:` on the Location line, verbatim, without the label>"}`

Disclosed: only the bullets under the heading `Required qualifications` are required. Bullets
under `Preferred qualifications` and `Nice to have` are not, even when they mention the same
skills, and the lists are not always in the same order. `work_authorization_required` is true
only if a required bullet mentions work authorization; `clearance_required` only if a required
bullet mentions a clearance.
