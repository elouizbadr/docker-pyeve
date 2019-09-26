FROM python:slim-stretch
LABEL maintainer="ELOUIZ BADR <belouiz@irevolution.com>"

ARG PORT=3000

COPY . .

RUN echo "Building image with PORT=${PORT}" && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE ${PORT}

CMD [ "python", "run.py" ]
