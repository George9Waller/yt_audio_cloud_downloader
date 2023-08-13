FROM public.ecr.aws/lambda/python:3.11
RUN yum install git -y
RUN pip install requests
RUN pip install boto3
RUN pip install "git+https://github.com/pytube/pytube.git@7877cc636ad1a0009ea731dcebedcb018cdb1cbb"
RUN pip install beautifulsoup4
COPY lambda_function.py ./
CMD [ "lambda_function.lambda_handler" ]
