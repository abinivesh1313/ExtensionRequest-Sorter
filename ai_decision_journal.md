# AI Decision Journal

| Decision | Options considered | Decision and reason |
|---|---|---|
| LLM responsibility | Let AI decide the outcome; or extract only facts | AI extracts course, explicit days, reason and a short summary. Python alone applies the policy, matching the specification. |
| Output format | Free-form text; structured JSON | JSON with exactly four keys makes validation predictable. |
| Missing information | Guess likely values; or use null | Use null when not explicitly supported by the request. |
| Days from dates | Calculate a duration from a weekday/date; or require a stated number | Require a written number of days. A date such as Monday is not a day count. |
| Course validation | Trust the model; or compare with the course file | Python checks both the semester course list and the original request. |
| Privacy | Reuse the model's summary; or create a neutral summary in Python | Python creates the output summary from checked fields to avoid copying illness names, treatment details or people's names. |
| API failure | Stop the entire run; or retry and fall back | Retry once, then use a conservative local fallback so the batch can complete. |
| Human responsibility | Automatically approve/reject; or route for human judgment | The tool only sorts. Faculty make every final decision. |
