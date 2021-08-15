FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt

COPY ./ ./

ENTRYPOINT ["/usr/local/bin/python3"]
CMD ["api.py"]
