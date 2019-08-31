FROM python

RUN useradd -ms /bin/bash app

WORKDIR /home/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY app.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP app

RUN chown -R app:app ./
USER app

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
