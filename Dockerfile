python:3.7-alpine

RUN useradd -ms /bin/bash strava-ytd

WORKDIR /home/strava-ytd

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY strava-ytd.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP strava-ytd.py

RUN chown -R strava-ytd:strava-ytd ./
USER strava-ytd

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
