# Options handler with CORS
This is a lambda function which just returns some `CORS` headers to allow API requests to work.

For my web extension implementation I am using the JS `fetch` method to make API calls to trigger downloads. This automatically sends an `OPTIONS` request ahead of posting the data which requires a valid response with `CORS` headers.