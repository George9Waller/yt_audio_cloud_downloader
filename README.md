# Cloud based YouTube audio downloader
A serverless hosted solution for asynchronously downloading the audio from YouTube videos with a nice browser extension to trigger downloads when on a video's page _(for personal use)_

## Demo
### Browser extension
https://github.com/George9Waller/yt_audio_cloud_downloader/assets/54817483/67dcd1d2-c58d-4da7-9b10-92371295e9ba

### SNS Email example
```
Subject: YT Audio download complete | [video_title]
YT Audio download completed for Rick Astley - [video_title].

link: [presigned_get_url_for_file]
[expires in 1 week 20/08/2023, 11:11:36]
```

## Components
- [Browser extension] [firefox-extension](https://github.com/George9Waller/yt_audio_cloud_downloader/tree/master/firefox-extension)
- [Lambda] [options-handler-with-cors](https://github.com/George9Waller/yt_audio_cloud_downloader/tree/master/options-handler-with-cors)
- [Lambda] [api-passkey-authorizer](https://github.com/George9Waller/yt_audio_cloud_downloader/tree/master/api-passkey-authorizer)
- [Lambda] [trigger-youtube-audio-download](https://github.com/George9Waller/yt_audio_cloud_downloader/tree/master/trigger-youtube-audio-download)
- [Lambda] [download-youtube-audio](https://github.com/George9Waller/yt_audio_cloud_downloader/tree/master/download-youtube-audio)

## Architecture
I wanted an easy and quick way to download audio to my computer where I could just click a button and it would happen. I decided used my recent learning about AWS cloud services to make a cloud solution which was cost effective.

By using mostly managed services and serverless lambda functions I have very few costs besides the actual download compute time. I even have the downloads S3 bucket set to auto delete after 1 week.

Below is a diagram outlining the flow to download an audio file.

![YT Audio downloader diagram](https://github.com/George9Waller/yt_audio_cloud_downloader/assets/54817483/8f60e437-f00f-45a6-88dc-b56ca51c9894)
