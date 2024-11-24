import requests
from config.settings import settings

whook = "https://dace1f6d1358cd.lhr.life"

r = requests.get(
    f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_KEY}/setWebhook?url={whook}/"
)

print(r.json())
