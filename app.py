from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)
    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    keyword = event.message.text.lower()
    hot_forums, all_forums = get_hot_forum()
    if keyword == "熱門看板":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=hot_forums))

    else:
        if "@" in keyword:
            searching_word = keyword.split("@")[0]
            forum = keyword.split("@")[1]
            if forum in all_forums:
                popular_articles = get_searching_word_articles(searching_word, forum)
                line_bot_api.reply_message(
                    event.reply_token, TextSendMessage(text=popular_articles)
                )
        else:
            if keyword in all_forums:
                popular_articles = get_forum_popular_articles(keyword)
                line_bot_api.reply_message(
                    event.reply_token, TextSendMessage(text=popular_articles)
                )


def get_hot_forum():
    data = requests.get("https://www.dcard.tw/service/api/v2/forums").json()
    data = sorted(data, key=lambda x: x["subscriptionCount"], reverse=True)
    all_forums = []
    for info in data:
        all_forums.append(info["alias"])
    hot_forums = "DCARD 熱門看板 top 10:\n\n"
    for idx in range(10):
        hot_forums += f"{data[idx]['alias']} ({data[idx]['name']})\n"
    hot_forums += "請輸入看板名稱(英文)來取得熱門文章"
    return hot_forums, all_forums


def get_articles(forum):
    forum = forum.lower()
    data = requests.get(
        f"https://www.dcard.tw/service/api/v2/forums/{forum}/posts?popular=true&limit=100"
    ).json()
    try:
        data = sorted(data, key=lambda x: x["createdAt"], reverse=True)
    except:
        pass
    return data


def get_forum_popular_articles(forum):
    data = get_articles(forum)
    top_10_articles = []
    for d in data:
        try:
            if d["school"] not in ["客服小天使", "小天使"]:
                top_10_articles.append(d)
                if len(top_10_articles) == 10:
                    break
        except:
            pass
    popular_articles = f"{forum} 板熱門文章 top 10:\n\n"
    for article in top_10_articles:
        popular_articles += (
            f"{article['title']}\nhttps://www.dcard.tw/f/{forum}/p/{article['id']}\n\n"
        )
    return popular_articles


def get_searching_word_articles(searching_word, forum):
    data = get_articles(forum)
    articles = []
    for d in data:
        try:
            if (
                searching_word in f'{d["title"]} {d["excerpt"]}'
                or searching_word in d["topics"]
            ):
                articles.append(d)
                if len(articles) == 10:
                    break
        except:
            pass
    searching_articles = f"{forum} 板關於 {searching_word} 的文章:\n\n"
    for article in articles:
        searching_articles += (
            f"{article['title']}\nhttps://www.dcard.tw/f/{forum}/p/{article['id']}\n\n"
        )
    return searching_articles


if __name__ == "__main__":
    app.run()
