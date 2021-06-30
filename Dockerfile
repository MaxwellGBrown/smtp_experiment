FROM python:3.9

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONPATH=/usr/src/app

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

COPY . .

# https://stackoverflow.com/q/29663459/2834973
# Using this to avoid using "-t"
# because for some reason output isn't appearing in detached mode.
# (perhaps my old docker version?)
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python"]
CMD ["server.py", "--host", "0.0.0.0"]

EXPOSE 587
