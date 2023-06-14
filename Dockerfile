FROM python:3.10
WORKDIR /app

COPY requirements.txt .
COPY /s3Uploader .
COPY /s3Uploader/tests .

RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate && pip3 install --no-cache-dir -r requirements.txt"

ENV PATH="/app/venv/bin:$PATH"
ENV FLASK_APP="main.py"
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]