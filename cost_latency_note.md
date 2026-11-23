# Cost and Latency Note

## API-call estimate
The program sends one Gemini request per student request in the normal successful path. For 20 requests, that is approximately 20 API calls. If an API call fails or returns invalid data, the program retries once, so the upper bound for 20 requests is 40 calls. If both attempts fail, the local fallback is used.

## Latency estimate
A typical text extraction request may take roughly 1–5 seconds, depending on network conditions, model load and request size. For 20 requests, the successful sequential run may take approximately 20–100 seconds, plus any retry delays. This is an estimate, not a guaranteed service level.

## Cost estimate
The exact cost depends on the selected Gemini model, input/output token counts, account tier and current provider pricing. With a free-tier key and within its quotas, the direct API charge may be zero; quotas and availability can change. For a paid tier, estimate:
`daily cost = (input tokens × input price + output tokens × output price) / 1,000,000`
Use the provider's current pricing page before presenting a numeric paid-cost estimate. This project does not hard-code a price that may become outdated.

## Measurement for the showcase
Record the actual number of requests, API calls, retries, elapsed time and model name from a live run. Do not present the rough estimates above as measured results.
