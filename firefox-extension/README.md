# Firefox extension
This is a basic firefox extension which can detect if it has been opened on a YouTube video page and make API requests to AWS to trigger a download of the audio.

## Values
- `triggerDownload.js`
  - `API_GATEWAY_URL`: AWS API Gateway url in your account
  - `AUTH_KEY`: The un-encrypted key you have setup in the api-passkey-authorizer environment variables