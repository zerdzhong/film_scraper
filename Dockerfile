FROM python:3

WORKDIR /usr/src/app


COPY LICENSE ./
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["docker-entrypoint.sh"]