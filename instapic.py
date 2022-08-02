from instabot import Bot
import os
from colorama import Fore
import pyfiglet
os.system("clear")
bot = Bot()
out = pyfiglet.figlet_format("InstaBot")
print(Fore.RED+out)
print(Fore.CYAN+ """
         ooo
        / : \\
       / o0o \\
 _____"~~~~~~~"_____
 \+###|U * * U|###+/
  \...!(.>..<)!.../
   ^^^^o|   |o^^^^
+=====}:^^^^^:{=====+#
.____  .|!!!|.  ____.
|#####:/" " "\:#####|
|#####=|  O  |=#####|
|#####>\_____/<#####|
 ^^^^^   | |   ^^^^^
         o o
         CODED BY SECURIST0x01
""")
user = input(Fore.MAGENTA+"Username : ")
passwd = input(Fore.MAGENTA+"Password : ",)
img = input(Fore.YELLOW+"Image Path [Example /root/aa.jpg] : ")
exp = input(Fore.WHITE+"Explanation : ")
bot.login(username=user, password=passwd)

bot.upload_photo(img, caption=exp)
