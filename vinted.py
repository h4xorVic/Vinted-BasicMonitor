from pyVinted import Vinted
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from colorama import Fore


def main():
    a = 0
    b = int(input("How many items you want : "))
    Param = input("Url of your research : ")
    url = "https://discord.com/api/webhooks/971507252060110878/tgrZYdCZXOd0DMGpQ96KGoQEm4u6jsxETeIZyAsiYTFSCykVM-4yr9c_z6zHEA4k3_L2" # Url de ton webhook 

    vinted = Vinted("fr")
    items = vinted.items.search(Param, b, 5)
    while a != b:
        for i in items:
            time.sleep(0.35) # Vinted bypass la limite de requete de vinted pas le temp d'utiliser des proxy
            a = a+1
            webhook = DiscordWebhook(
                url=url, content="", username="Bot vinted")
            embed = DiscordEmbed(
                title=i.title, description=i.url, color=None)
            embed.set_thumbnail(url=i.photo)
            embed.set_author(
                name="By Vic",
                url="https://github.com/VicLearnPy",
                icon_url="https://zupimages.net/up/22/16/ijxh.jpg",)
            embed.add_embed_field(name="Marque", value=i.brand_title, inline=True)
            embed.add_embed_field(name="Prix", value=i.price, inline=True)
            embed.add_embed_field(name="Devise", value= i.currency)
            webhook.add_embed(embed)
            webhook.execute()
            print(Fore.GREEN + "[BOT]Articles find : " + i.url)


if __name__ == "__main__":
    main()
    input("\nDone...Press a touch to close the programm")
