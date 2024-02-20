# discord-ocr-bot

discord ocr bot on Render's web-server
- reference
  - https://github.com/RockyLogic/Discord-OCR-Bot
  - https://qiita.com/Pumila/items/2f64c06d6d8a4f802390

履歴
- 2024/02/20
  - Render上でエラー。

  '''
  Traceback (most recent call last):
  File "/discord-ocr-bot/main.py", line 13, in <module>
    from keep_alive import keep_alive

    ~中略~
  File "/usr/local/lib/python3.11/site-packages/flask/app.py", line 30, in <module>
    from werkzeug.urls import url_quote
  ImportError: cannot import name 'url_quote' from 'werkzeug.urls' (/usr/local/lib/python3.11/site-packages/werkzeug/urls.py)
  '''

  - https://qiita.com/croquette0212/items/02d50cd77932f5a0aae1
  - を参考に、Werkzeug==2.3.7 へダウングレード