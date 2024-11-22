import requests
from config.settings import settings

whook = "https://7eb660a6c4273e.lhr.life"

r = requests.get(
    f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_KEY}/setWebhook?url={whook}/"
)

print(r.json())
