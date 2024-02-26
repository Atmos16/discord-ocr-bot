FROM python:3.11
WORKDIR /discord-ocr-bot
COPY requirements.txt /discord-ocr-bot/
RUN pip install -r requirements.txt
COPY . /discord-ocr-bot
RUN which tesseract
RUN echo under maintanance...
# CMD python main.py

