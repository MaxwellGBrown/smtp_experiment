# SMTP Example

Demonstration of an SMTP server implemented with python's socket library.

## Quickstart

- Run the server

  ```
  docker build --tag smtp_experiment .
  docker run -d -v $(pwd):/usr/src/app -p 8888:587 --rm --name smtp_experiment smtp_experiment
  ```

- Run the client

  ```
  python client.py 8888
  ```
