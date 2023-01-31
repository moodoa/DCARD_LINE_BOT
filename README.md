# DCARD_LINE_BOT
使用 LINE 機器人查詢 DCARD 特定看板的熱門文章(支援關鍵字搜尋)

![alt text](https://i.imgur.com/kr0mTNg.png)

## app.py
* 透過 [LINE Messaging API](https://developers.line.biz/en/services/messaging-api/) 建立 [DCARD](https://www.dcard.tw/f) 熱門文章機器人
* [基本設定請參考](https://github.com/line/line-bot-sdk-python)
* 使用 NGROK 對應 flask 500 port 建立 https Webhook URL


## Requirements
python >= 3.7

## Installation
`pip install -r requriements.txt`

## usage
* 關於 line bot 的設定
* 1.Channel secret 在 Basic Settings 裡面可以找到，Channel access token 則是在 Messaging API 裡面。
![alt text](https://cdn-images-1.medium.com/max/1000/1*ZWscTYpEzFrDh25-C4DPUw.png)
* 2.Messaging API 裡面的 Use webhook 要打開。
* 3.Webhook URL 輸入由 ngrok 產生的url，後面要加/callback。
![alt text](https://cdn-images-1.medium.com/max/1000/1*3woQVYFoiDh2r6f-Ic-syg.png)

* 關於 Flask 和 Ngrok 的設定
* 1.開啟終端機，進到工作資料夾後輸入：`PS D:\dir> flask run` 預設路徑會是在 127.0.0.1:5000。如：` * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
* 2.打開下載好的 Ngrok，輸入：`ngrok http http://127.0.0.1:5000/`會跳出以下資訊：
![alt text](https://cdn-images-1.medium.com/max/1000/1*nuD9yOzAC5c21ZvCWDK_iw.png)
* 其中 forwardi之後的 https 網址放到 Webhook URL。如此便完成 LINE bot 架設。

![alt text](https://i.imgur.com/VEX2mOq.png)
* 在對話框輸入`看板名稱(英文)`，取得該看板熱門文章 top 10，若要搜尋特定文章則使用`關鍵字@看板`搜尋
![alt text](https://i.imgur.com/kr0mTNg.png)


