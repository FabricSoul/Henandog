FROM python:3.10

WORKDIR .

COPY . .

RUN pip3 install --no-cache-dir -r ./requirements.txt

CMD [ "python3.10", "bot.py" ]
