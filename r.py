import requests
from config.settings import settings

data = {
    "chat_id": settings.ADMIN_CHAT_ID,
    "text": "Hello from Python script",
}
r = requests.post(
    f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_KEY}/sendMessage", data=data
)
print(r.status_code())
