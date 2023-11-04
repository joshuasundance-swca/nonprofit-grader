FROM python:3.11-slim-bookworm

RUN apt-get update && \
    apt-get install libmagic-dev poppler-utils tesseract-ocr -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN adduser --uid 1000 --disabled-password --gecos '' appuser
USER 1000

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:$PATH"

RUN pip install --user --no-cache-dir --upgrade pip

COPY ./requirements.txt /home/appuser/requirements.txt
RUN pip install --user --no-cache-dir  --upgrade -r /home/appuser/requirements.txt

CMD ["/bin/bash"]
