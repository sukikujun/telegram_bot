import requests

# Bot のトークン（BotFather から取得）
TOKEN = "7967246535:AAFw_iD1W-D7q7esYDoso9PGt5Qq2i_kFew"

# グループの Chat ID（getUpdates で取得）
CHAT_ID = "-1002410256375"

# 送信するメッセージ
MESSAGE = "こんにちは！ボットからのメッセージです 🎉"

# Telegram API URL
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# メッセージを送信
response = requests.post(URL, data={"chat_id": CHAT_ID, "text": MESSAGE})

# 結果を表示
print(response.json())

