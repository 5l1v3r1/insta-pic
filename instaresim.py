from instabot import Bot
import os
os.system("clear")
#coded by saep
bot = Bot()
user = input("Kullanıcı Adı : ")
passwd = input("Şifre : ")
resim = input("Resim Yolu [Örn /root/aa.jpg] : ")
aciklama = input("Açıklama : ")
bot.login(username=user, password=passwd)

bot.upload_photo(resim, caption=aciklama)
