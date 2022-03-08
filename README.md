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
* 在對話框輸入`熱門看板`，機器人回應當前熱門看板 top 10
![alt text](https://i.imgur.com/VEX2mOq.png)
* 在對話框輸入`看板名稱(英文)`，取得該看板熱門文章 top 10，若要搜尋特定文章則使用`關鍵字@看板`搜尋
![alt text](https://i.imgur.com/kr0mTNg.png)


