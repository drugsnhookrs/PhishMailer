#!/usr/bin/env python3
#Created By BiZken

#Normal Import
import time
import os
import sys 

#emails:
from Core.eletter import Instagram
from Core.eletter import Facebook
from Core.eletter import Gmail
from Core.eletter import Twitter
from Core.eletter import AskFM
from Core.eletter import Webhost000
from Core.eletter import Blockchain
from Core.eletter import Spotify
from Core.eletter import Rockstar
from Core.eletter import Dreamteam
from Core.eletter import RiotGames
from Core.eletter import Steam
from Core.eletter import Gamehag
from Core.eletter import GmailActivity
from Core.eletter import SnapchatSimple
from Core.devicemenu import Linkedin
from Core.devicemenu import Dropbox
from Core.ipmenu import Discord
from Core.ipmenu import Paypal1
from Core.ipmenu import Snapchat

#EmailSender:
from Core.mailer import NormalEmail

from Core.helper.color import red, green, white, blue, numbering

os.system("clear")
print(green + """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~
 PhishMailer Version 1.2     .                     .              |
 Coded By BiZken             .                     .              |
 bizken@protonmail.com       .   /                  .  ___        |
          .                   . /--\ /                /   \       |
          .                    <o)  =<               /     \      J
          .                     \__/ \              (__O_O__)
 |  |    .                       \                    |||||
  \/        Y           )                             |||||
  |  /!-!\  |          (                           \_///| \\__/
   \|     |/            )                           _// |  \_
    _\___/_            (   (                         / /
   / /   \ \            )   )
^^^^^^^^^^^^^^^^\      (   (
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\                /^^
                                                   ^^^^^^^^^^^^^^^^ """)

time.sleep(0.5)
print(green + "[" + red + "!" + green + "]" + white + "More Versions Will Come Soon Stay Updated, Follow My Github\n")
print(white + "options:")
print(numbering(1) + white + " Instagram" + green + "\t\t\t" + numbering(11) + white + " Paypal")
print(numbering(2) + white + " Facebook"  + green + "\t\t\t" + numbering(12) + white + " Discord")
print(numbering(3) + white + " Gmail"     + green + "\t\t\t" + numbering(13) + white + " Spotify")
print(numbering(4) + white + " Gmail (simple)" + green + "\t\t" + numbering(14) + white + " Blockchain")
print(numbering(5) + white + " Twitter"        + green + "\t\t\t" + numbering(15) + white + " RiotGames")
print(numbering(6) + white + " Snapchat" + green + "\t\t\t" + numbering(16) + white + " Rockstar")
print(numbering(7) + white + " Snapchat (simple)" + green + "\t\t" + numbering(17) + white + " AskFM")
print(numbering(8) + white + " Steam"     + green + "\t\t\t" + numbering(18) + white + " 000Webhost")
print(numbering(9) + white + " Dropbox"   + green + "\t\t\t" + numbering(19) + white + " Dreamteam")
print(numbering(10) + white + " Linkedin" + green + "\t\t\t" + numbering(20) + white + " Gamehag")
print(green + "-----------------------------------------------------------------------")
print(numbering(30) + white + " Send Phishing Email")
print(numbering(99) + red + " EXIT")
print(numbering(1337) + white + " Info\n")

print(green)
mailPick = int(input("root@phishmailer:~ " + white))

if mailPick == 1:
	Instagram()

elif mailPick == 2:
	Facebook()
	
elif mailPick == 3:
	Gmail()

elif mailPick == 4:
	GmailActivity()

elif mailPick == 5:
	Twitter()

elif mailPick == 6:
	Snapchat()

elif mailPick == 7:
	SnapchatSimple()

elif mailPick == 8:
	Steam()
	
elif mailPick == 9:
	Dropbox()
	
elif mailPick == 10:
	Linkedin()
	
elif mailPick == 11:
	Paypal1()
	
elif mailPick == 12:
	Discord()
	
elif mailPick == 13:
	Spotify()
	
elif mailPick == 14:
	Blockchain()
	
elif mailPick == 15:
	RiotGames()
	
elif mailPick == 16:
	Rockstar()
	
elif mailPick == 17:
	AskFM()

elif mailPick == 18:
	Webhost000()

elif mailPick == 19:
	Dreamteam()
	
elif mailPick == 20:
	Gamehag()

elif mailPick == 30:
	NormalEmail()

elif mailPick == 99:
	os.system("clear")
	print("Hope I See You Soon")
	print("Happy Phishing")
	sys.exit()

elif mailPick == 1337:
	print("\n" + green + "[" + white + "+" + green + "]" + white + " This Tool Was Created So People Would Have It Easier To Launch Phishing Attacks")
	print("\n" + green + "[" + white + "+" + green + "]" + white + " I Do Not Take Any Responsibility For Your Actions")
	print("\n" + green + "[" + white + "+" + green + "]" + white + " But I Don't Give A F*ck About What You Do")
	print("\n" + green + "[" + white + "+" + green + "]" + white + " More Emails Will Come Soon!")
	print("\n" + green + "[" + white + "+" + green + "]" + white + " Contact:")
	print(green + "[" + white + "+" + green + "]" + white + " Wickr: BiZken")
	print(green + "[" + white + "+" + green + "]" + white + " Email: bizken@protonmail.com")
	print(green + "[" + white + "+" + green + "]" + white + " Github: BiZken [https://github.com/BiZken]")
	
else:
	print("\nSomething Went Wrong There Partner")
	print("Are You Ok? Did You Fell Out The Boat And Started Drowning?")
	sys.exit()
