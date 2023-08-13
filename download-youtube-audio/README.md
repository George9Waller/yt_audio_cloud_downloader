# Download YouTube audio
This is a lambda function which takes the program url from events in the SQS queue and uses the `pytube` library to download the audio stream and upload it to an S3 bucket. It also uses `BeautifulSoup` to get the video title from the video page html.

This function then sends an SNS message with a presigned url to download the file when it has completed. I have subscribed to the SNS topic so I receive these emails whenever a download has occurred. The S3 bucket I am using also has a lifecycle policy to delete the downloads after 1 week so I do not incur charges for storing all my downloads forever.

This lambda function is a bit different as to install extra packages to run in lambda you either have to make a layer for your function to run in or upload it as a docker image. I have ended up uploading it as a docker image using the `serverless` framework as the layers I made didn't end up working.

## Values
- `BUCKET_NAME`: the name of your bucket to upload the audio files to
- `SNS_TOPIC_ARN`: the arn for your SNS topic to send download urls to