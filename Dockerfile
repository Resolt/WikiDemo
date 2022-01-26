FROM airdock/python-poetry:latest as requirements

WORKDIR /reqs

COPY poetry.lock ./
COPY pyproject.toml ./
RUN poetry export --format requirements.txt --output requirements.txt


FROM python:3.8-slim

WORKDIR /app

ADD wiki ./wiki
ADD wiki_demo ./wiki_demo
ADD templates ./templates
COPY start_app.sh ./
COPY manage.py ./

COPY --from=requirements /reqs/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm requirements.txt

CMD ["./start_app.sh"]