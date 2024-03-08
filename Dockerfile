FROM python:3.11
WORKDIR /discord-ocr-bot
COPY requirements.txt /discord-ocr-bot/
RUN pip install -r requirements.txt
COPY ./tessdata /pytesseract
COPY . /discord-ocr-bot
CMD python main.py

