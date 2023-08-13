import os
import json
from datetime import datetime, timedelta

import boto3
import requests
from bs4 import BeautifulSoup
from pytube import YouTube


def make_request(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.status_code, resp
    print(
        f"Request to {url} failed with status code: {resp.status_code} content: {resp.content}"
    )
    return resp.status_code, None


def get_title_for_program(program_url):
    print(f"Requesting html for {program_url}")
    html = requests.get(program_url).text
    soup = BeautifulSoup(html)
    title = soup.find("meta", {"name": "title"})
    print(f"Title found on page: {title}")
    return (
        title["content"]
        if title
        else program_url.replace("/", "_").replace(".", "_").replace(":", "")
    )


def download_youtube_audio_to_file(program_url):
    print("Starting download")
    path = (
        YouTube(program_url)
        .streams.filter(only_audio=True)
        .filter(file_extension="mp4")
        .order_by("abr")
        .desc()
        .first()
        .download(output_path="/tmp/")
    )
    return path


def upload_youtube_audio_to_s3(file_path, title):
    print(f"uploading file at path: {file_path} to s3")
    s3_client = boto3.client("s3")
    s3_path = f"{title}.mp4"
    with open(file_path, "rb") as file:
        s3_client.upload_fileobj(file, os.environ["BUCKET_NAME"], s3_path)
    return s3_path


def lambda_handler(event, context):
    if len(event["Records"]) > 1:
        raise Exception("More than one record received")

    print("Starting function")

    message = event["Records"][0]
    body = json.loads(message["body"])

    title = get_title_for_program(body["program_url"])
    file_path = download_youtube_audio_to_file(body["program_url"])
    s3_path = upload_youtube_audio_to_s3(file_path, title)

    if os.environ["SNS_TOPIC_ARN"]:
        print("sending download notification to SNS queue")
        s3 = boto3.client("s3")

        # expiry in 1 week
        seconds = 604800
        presigned_url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": os.environ["BUCKET_NAME"], "Key": s3_path},
            ExpiresIn=seconds,
        )
        time_in_1_week = datetime.now() + timedelta(seconds=seconds)
        sns = boto3.client("sns")
        sns.publish(
            TopicArn=os.environ["SNS_TOPIC_ARN"],
            Message=f"YT Audio download completed for {title}.\n\nlink: {presigned_url}\n[expires in 1 week {time_in_1_week.strftime('%d/%m/%Y, %H:%M:%S')}]",
            Subject=f"YT Audio download complete | {title[:60]}",
        )

    return {"statusCode": 200, "body": "M4S download complete"}
