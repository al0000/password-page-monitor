from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import threading
from time import sleep


class DSMMonitor:
    def __init__(self, interval):
        self.interval = interval

    def monitor(self):
        threading.Timer(self.interval, self.monitor).start()
        self.password_page()

    def password_page(self):
        first = requests.get(
            "https://eflash-us.doverstreetmarket.com/password", allow_redirects=False)
        sleep(self.interval)
        second = requests.get(
            "https://eflash-us.doverstreetmarket.com/password", allow_redirects=False)
        if (first.status_code != second.status_code):
            if second == 200:
                webhook = DiscordWebhook(
                    url='WEBHOOK URL HERE')
                embed = DiscordEmbed(
                    title='Password Page Down', description="https://eflash-us.doverstreetmarket.com")
                webhook.add_embed(embed)
                webhook.execute()
            else:
                webhook = DiscordWebhook(
                    url='WEBHOOK URL HERE')
                embed = DiscordEmbed(
                    title='Password Page Up', description="https://eflash-us.doverstreetmarket.com")
                webhook.add_embed(embed)
                webhook.execute()


f = DSMMonitor(5)
f.password_page()
