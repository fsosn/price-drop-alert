FROM python:3.12.4-alpine3.20

COPY . .

RUN pip install -r requirements.txt

RUN crontab /src/mycron

RUN touch /tmp/out.log

CMD crond && tail -f /tmp/out.log