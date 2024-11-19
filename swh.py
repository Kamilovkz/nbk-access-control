import requests
from config.settings import settings

whook = "https://57d877d3351739.lhr.life/"

r = requests.get(
    f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_KEY}/setWebhook?url={whook}"
)

print(r.json())
