FROM ubuntu:latest
MAINTAINER Jeff Bradley
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /stockAlerter
WORKDIR /stockAlerter
RUN pip install Flask
RUN pip install requests
ENTRYPOINT ["python"]
CMD ["getQuoteFromService.py"]
