FROM python:3.8-slim

WORKDIR /app

ADD wiki ./wiki
ADD wiki_demo ./wiki_demo
COPY start_api.sh ./
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm requirements.txt

CMD ["./start_app.sh"]