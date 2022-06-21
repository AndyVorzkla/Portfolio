FROM python:3.10

ENV PYTHONUNBUFFERED=1
WORKDIR code/

RUN mkdir ./staticfiles/ && groupadd -r web && useradd -d /code -r -g web web
COPY ./requirements /code/requirements.txt
RUN pip install -r /code/requirements.txt && rm -rf /root/.cache/pip

COPY . /code

RUN chown web:web -R /code && chmod +x /code/entrypoint.sh

USER web

ENTRYPOINT ["sh", "/code/entrypoint.sh"]
