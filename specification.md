# One-page Specification — Extension Request Sorter

## Purpose
Build a console-based Python tool that reads student assignment-extension requests, extracts key details using an LLM, checks those facts in Python, and sorts requests into three administrative queues. The tool never approves or rejects an extension; faculty retain the final decision.

## Inputs
1. `requests.csv`: `id,date,request`; at least 20 student-style requests, including incomplete requests.
2. `courses.csv`: `code,name`; the valid course codes for the semester.
3. `GEMINI_API_KEY`: stored in a local `.env` file, never in source code or GitHub.

## LLM output contract
The LLM must return exactly one JSON object:
`{"course":"CS101","days":2,"reason":"medical","summary":"Requests 2 days for CS101, medical reason"}`

- `course`: exact code written in the request, or null.
- `days`: explicitly stated whole number 1–30 (digits or number word), or null. Never calculate from a date or weekday.
- `reason`: medical, family, technical, event, workload, or other. Use other if absent; never guess.
- `summary`: no more than 15 words; no illness names, diagnoses, treatment details, or people's names.

## Policy (Python only)
1. Missing course or days → `needs_more_info`.
2. Days ≤ 3 and reason is medical, family, or technical → `within_policy`.
3. All other complete requests → `needs_faculty_review`.

## Fact and privacy checks
Python keeps a course only if it is listed in `courses.csv` and explicitly appears in the original request. It keeps days only if the same number is explicitly written in the request. Python generates a neutral summary from checked fields rather than trusting potentially sensitive LLM summary text. Original request text is excluded from `results.csv` and aggregate `summary.txt`; it appears only in `review_queue.csv` for authorised course faculty.

## Outputs
- `results.csv`: all requests, extracted fields, recommendation and safe summary.
- `review_queue.csv`: all requests not within policy, including original request text for course faculty.
- `summary.txt`: aggregate counts by recommendation, reason and course; no request text.

## Human accountability
The tool provides administrative sorting support only. It cannot verify the truth of the reason or supporting evidence. Faculty review the queue and make all final decisions.
