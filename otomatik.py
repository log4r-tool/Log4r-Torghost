#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

os.system("apt install figlet")
os.system("clear")
os.system("figlet DNS IP MAC MYS")
print("""
Bu araçla otomatik olarak IP Adres değiştirebilirsiniz, değeri saniye olarak girin.
""")

sure = input("IP Değişim Süre(saniye) : ")

os.system("macchanger -r eth0")
os.system("python3 torghost.py -s")
os.system("sudo chattr -i /etc/resolv.conf")
os.system("clear")
print("Yeni IP Adres :")
print("-----------------------------")
os.system("curl icanhazip.com")
print("-----------------------------")

while True:
	time.sleep(sure)
        os.system("macchanger -r eth0")
	os.system("python3 torghost.py -s")
        os.system("sudo chattr +i /etc/resolv.conf")	
        os.system("clear")
	print("Yeni IP Adres :")
	print("-----------------------------")
	os.system("curl icanhazip.com")
	print("-----------------------------")