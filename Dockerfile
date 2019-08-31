FROM python:3.7-alpine

WORKDIR /home/strava-ytd

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY strava-ytd.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP strava-ytd.py

ENTRYPOINT ["./boot.sh"]
