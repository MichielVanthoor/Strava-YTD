#!/bin/sh
echo Starting the engines!
exec gunicorn -b 0.0.0.0:$PORT --access-logfile - --error-logfile - de-uitdaging:app
