# API passkey authorizer
This is a lambda function attached to API Gateway as a simple authorizer for my `/download` post route.

I didn't want to setup full user management and authentication so I have used a simple token based auth which requires the correct token to be in the `Authorization` header. This is to protect against other people being able to request downloads on my account.

It returns a simple `{"IsAuthorized": True | False}` value which API Gateway uses to allow or deny the request.

## Values
- `PASSKEY`: an encrypted value which is then decrypted using KMS and compared with the value sent in the `Authorization` headers