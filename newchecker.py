
import time

import os

import sys

from os import system

import random

import string

from discord import webhook



useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",

            "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",

            "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",

            "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",

            "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",

            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",

            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",

            "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",

            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",

            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",

            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",

            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",

            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",

            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",

            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",

            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",

            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",

            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",

            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",

            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",

            "Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",

            "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",

            "Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",

            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",

            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",

            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",

            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",

            "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",

            "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",

            "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",

            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",

            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",

            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",

            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",

            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",

            "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",

            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",

            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",

            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",

            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",

            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",

            "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",

            "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2",

            "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",

            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",

            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",

            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",

            "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",

            "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",

            "Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",

            "Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",

            "Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",

            "Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",

            "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",

            "Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2",

            "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",

            "Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0",

            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",

            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",

            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",

            "Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",

            "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",

            "Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",

            "Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",

            "Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",

            "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",

            "Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",

            "Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",

            "Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",

            "Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",

            "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",

            "Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",

            "Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",

            "Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",

            "Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",

            "Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",

            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",

            "Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",

            "Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",

            "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",

            "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",

            "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15",

            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8",

            "Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7",

            "Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5",

            "Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",

            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)",

            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",

            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)",

            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11",

            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",

            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",

            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2",

            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",

            "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)",

            "Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9",

            "Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",

            "Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",

            "Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",

            "Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",

            "Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",

            "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",

            "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",

            "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",

            "Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",

            "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",

            "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",

            "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",

            "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",

            "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",

            "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",

            "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",

            "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",

            "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",

            "Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",]

proxy_list=['89.140.125.17:80','8.218.242.27:59394','139.59.1.14:3128','194.233.73.106:443','103.168.52.1:1337','194.233.69.126:443','178.124.208.8:3128','150.129.171.35:30093','212.46.230.102:6969','50.206.25.111:80','103.109.58.54:8080','139.162.78.109:3128','47.88.77.62:8080','195.191.246.198:53281','88.198.50.103:3128','5.189.165.226:9999','181.129.52.156:42648','109.167.134.253:30710','118.98.65.146:8081','190.152.5.126:53040','170.238.255.90:31113','185.142.67.23:8080','81.24.92.10:53281','195.138.73.54:44017','129.226.113.45:59394','88.198.24.108:3128','113.130.126.2:31932','88.132.34.230:53281','185.208.172.146:1080','50.206.25.106:80','94.73.239.124:55443','88.198.50.103:8080','8.218.95.237:59394','203.75.190.21:80','191.96.42.80:3128','20.47.108.204:8888','124.107.167.225:8080','43.255.113.232:83','50.206.25.104:80','83.151.2.50:3128','180.250.170.210:59778','176.9.75.42:8080','176.110.121.90:21776','139.162.78.109:8080','88.198.24.108:8080','187.108.39.64:6666','46.4.96.137:8080','94.244.28.246:31280','116.90.229.186:35561','194.233.73.104:443','195.46.164.179:8118','194.233.69.41:443','31.173.94.93:43539','50.206.25.110:80','154.16.63.16:3128','23.107.176.100:32180','43.134.200.122:59394','83.13.251.149:8080','62.205.134.57:30008','46.198.132.228:21231','109.173.102.90:8000','135.148.120.146:8088','116.103.46.15:4004','43.255.113.232:84','50.246.120.125:8080','181.129.183.19:53281','5.252.161.48:3128','68.185.57.66:80','195.209.131.19:46372','144.217.75.65:8800','13.212.167.151:8000','85.26.146.169:80','139.59.1.14:8080','005.252.161.48:8080','131.161.68.37:31264','176.9.119.170:8080','46.4.96.137:3128','49.12.43.32:5555','176.111.73.57:8081','185.201.88.128:6969','85.195.104.71:80','159.203.61.169:3128','101.32.204.67:59394','68.188.59.198:80','154.16.63.16:8080','172.107.96.30:443','93.117.72.27:43631','43.134.213.254:59394','8.218.80.41:59394','176.9.119.170:3128','77.37.157.204:8000','103.145.34.10:55443','176.9.75.42:3128','78.129.239.197:808','8.218.95.30:59394','194.32.128.66:55443','220.87.222.238:8118','191.96.42.80:8080','187.190.64.42:31442','140.227.122.55:59394','181.196.205.250:38178','116.251.214.12:443']#line:249



d = ['1', '2']

k = random.choice(d)

if k == '1':

    letter1 = chr(random.randint(ord('a'), ord('z')))

    letter2 = chr(random.randint(ord('a'), ord('z')))

    letter3 = chr(random.randint(ord('1'), ord('9')))

    letter4 = chr(random.randint(ord('a'), ord('z')))

    letter5 = chr(random.randint(ord('a'), ord('z')))

    letter6 = chr(random.randint(ord('a'), ord('z')))

    letter7 = chr(random.randint(ord('1'), ord('9')))

    letter8 = chr(random.randint(ord('1'), ord('9')))

    letter9 = chr(random.randint(ord('1'), ord('9')))

    letter10 = chr(random.randint(ord('1'), ord('9')))

    user = letter1+letter2+letter3+letter4+letter5+letter6+letter7+letter8+letter9+letter10

elif k == '2':

    letter1 = chr(random.randint(ord('1'), ord('9')))

    letter2 = chr(random.randint(ord('a'), ord('z')))

    letter3 = chr(random.randint(ord('1'), ord('9')))

    letter4 = chr(random.randint(ord('a'), ord('z')))

    letter5 = chr(random.randint(ord('1'), ord('9')))

    letter6 = chr(random.randint(ord('a'), ord('z')))

    letter7 = chr(random.randint(ord('1'), ord('9')))

    letter8 = chr(random.randint(ord('1'), ord('9')))

    letter9 = chr(random.randint(ord('a'), ord('a')))

    letter10 = chr(random.randint(ord('1'), ord('9')))

    user = letter1+letter2+letter3+letter4+letter5+letter6+letter7+letter8+letter9+letter10



try:

    import colorama

    from colorama import Fore, init
    
except:

    try:

        os.system('pip install colorama')

        import colorama

        from colorama import Fore, init

    except:

        print('pip is not installed.... Redownload python and check "add to path')



try:

    import threading

    from threading import Thread

except:

    try:

        os.system('pip install threading')

        import threading

        from threading import Thread

    except:

        print('pip is not installed.... Redownload python and check "add to path')



try:

    import discord_webhook

    from discord_webhook import DiscordEmbed, DiscordWebhook

except:

    try:

        os.system('pip install discord_webhook')

        import discord_webhook

        from discord_webhook import DiscordEmbed, DiscordWebhook

    except:

        print('pip is not installed.... Redownload python and check "add to path')


import urllib3
try:

    import requests

    from requests import session

except:

    try:

        os.system('pip install requests')

        import requests

        from requests import session

    except:

        print('pip is not installed.... Redownload python and check "add to path')





try:

    import asyncio

except:

    try:

        os.system('pip install asyncio')

        import requests

    except:

        print('pip is not installed.... Redownload python and check "add to path')



from typing import List



try:

    import crayons

except:

    try:

        os.system('pip install crayons')

        import crayons

    except:

        print('pip is not installed.... Redownload python and check "add to path')





try:

    import aiohttp

except:

    try:

        os.system('pip install aiohttp')

        import aiohttp

    except:

        print('pip is not installed.... Redownload python and check "add to path')





try:

    import queue

except:

    try:

        os.system('pip install queue')

        import queue

    except:

        print('pip is not installed.... Redownload python and check "add to path')





try:

    import ctypes

except:

    try:

        os.system('pip install ctypes')

        import ctypes

    except:

        print('pip is not installed.... Redownload python and check "add to path')







try:

    import discord_webhook

    from discord_webhook import DiscordEmbed, DiscordWebhook

except:

    try:

        os.system('pip install discord_webhook')

        import discord_webhook

        from discord_webhook import DiscordEmbed, DiscordWebhook

    except:

        print('pip is not installed.... Redownload python and check "add to path')
import sys

from colorama import Fore, init
init()







usernames = queue.Queue()
sid = queue.Queue()

P = []
session = requests.session()
for i in open('proxies.txt', 'r').read().splitlines():
            P.append(i)


def clear():

    os.system('cls') if os.name == 'nt' else os.system('clear')


print(f'''
            {Fore.RED}Aims TikTok Checker{Fore.RESET}            
            ''')
os.system('title discord.gg/aim')

userlist = input(f'[{Fore.RED}INPUT{Fore.RESET}] Username List: ')
    
ssid = input(f'[{Fore.RED}INPUT{Fore.RESET}]SSID: ')

for line in open(userlist, 'r'):

    usernames.put(line.strip())
huk = input(f'[{Fore.RED}INPUT{Fore.RESET}] Webhook: ')
def checker():
    while True:

        user = usernames.get()

        ua = random.choice(useragents)

        headers = {

     'user-agent': f'{ua}'

    }
        Proxy = random.choice(P)
        Proxy.strip()
        prox = {'http': 'http://' + Proxy}
        print(prox)
        url = f'https://www.tiktok.com/@{user}/'
        req = requests.head(url, headers=headers, proxies=prox)

        smsg = str(req.status_code)

        print(smsg)

        if req.status_code == 404:

                ua = random.choice(useragents)

                prox = {'http': 'http://' + (random.choice(proxy_list))}

                head = {
                    'authority': 'www-useast1a.tiktok.com',
                    'method': 'GET',
                    'path': f'/node/share/user/@{user}',
                    'scheme': 'https',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'cookie': 'd_ticket=8408a0952531c676f843d70545371459ee8c5; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22version%22:%22v3%22}; passport_csrf_token=9aa9a8348fe924b1ae9d5c8a87274bff; passport_csrf_token_default=9aa9a8348fe924b1ae9d5c8a87274bff; sid_guard=68882c0198d337e1a29c5a4976503bb3%7C1646509559%7C5184000%7CWed%2C+04-May-2022+19%3A45%3A59+GMT; uid_tt=774e7c6b48285bb1ab789b51d8895f0e3f88fe0310fa972e707ae6b690d87203; uid_tt_ss=774e7c6b48285bb1ab789b51d8895f0e3f88fe0310fa972e707ae6b690d87203; sid_tt=68882c0198d337e1a29c5a4976503bb3; sessionid=68882c0198d337e1a29c5a4976503bb3; sessionid_ss=68882c0198d337e1a29c5a4976503bb3; sid_ucp_v1=1.0.0-KDA1NWY5MzJmNzcyYmIxZjA2MzI5ZDU2MWRhMzIyZWU2MDViZWJjMzUKIAiFiN2uor23tl4Q9_uOkQYYswsgDDC4xLPzBTgEQOoHEAQaB3VzZWFzdDUiIDY4ODgyYzAxOThkMzM3ZTFhMjljNWE0OTc2NTAzYmIz; ssid_ucp_v1=1.0.0-KDA1NWY5MzJmNzcyYmIxZjA2MzI5ZDU2MWRhMzIyZWU2MDViZWJjMzUKIAiFiN2uor23tl4Q9_uOkQYYswsgDDC4xLPzBTgEQOoHEAQaB3VzZWFzdDUiIDY4ODgyYzAxOThkMzM3ZTFhMjljNWE0OTc2NTAzYmIz; store-idc=useast5; store-country-code=us; tt-target-idc=useast5; cmpl_token=AgQQAPPdF-RMpY5SM02t5Z08-GAe3hURf4fZYMCzaA; _abck=03065DA619543EFC61D82B593449F88D~0~YAAQbHd+aKf+AZ9/AQAA7L0NwwcAw1s4aZaGzBlwHCwR3US31JlK9AUNullDiqVPZjnfPgp3fXWRE6467OeE3lhEIQuUHj8ScUKP8ghpdM6yNRpBfoDp0EzkLYCmyca/qchycP6cj96weYI/GA0metVZRnZULdfRhqG99UrRJYeE7M2dRBXUwYPq+MXYGIbACGiXM29iatOiY4xQKU2k/H9rn/EUh6WNREDCwT7OnSASFevdosPvqRs5hDkdEcecSHia6qZPhM4esDS0dVMhWjWUyKbIFURL64XBTAFPJTL5xRRMombDLcUsw8zpu6ynn1my2Hir2PNBzK6E3LDDD5kCG/uf4hAlp9WNBCGjBx8v8uWPZsTgvhqGJet4xwwNfMraNUCpqNOTt3iUImvsQb5KmtoMX9Vv~-1~-1~-1; tt_csrf_token=FHGm9YRR2Ck33mGh1B5ax-ka; ak_bmsc=01277BBEC696534609C1F417DAF9F6EC~000000000000000000000000000000~YAAQRGV0aPVHPpp/AQAA5ym4ww9Io62tfOLrlUMHanYORNWlWbD8co4/+wQKlTmQMYjOSG0kR1bWbx+xrGp9vSziUHt1zilaRdxkNEh7q85eBYIycWOmJWoaS8/C3qfVr7S6dDZARlPeH0vV5LmAZx8FZtJ+wi+sjHw6yas9c0gY/bqIvy1QwBsPh/7A7Nwyi10fbBD38T3XYz2/+Q86AZJSVRLFW8jdo2KORml40ecSHk0SQ97Vl0cg3P7P5tSydWw0ogul2ZFirAvkk0eVpobfg+qvnxc9rR1SQ19qAlIWxA4EfaLcxLbxoz90uiSKzETwl2vXUhCRF105xHj+I0GrVcdYx9Gvgo3YQm07KARhd/5DO7a9kns5Yy6LgiJ0+4zAauNObwEK+4Y=; ttwid=1%7C50KhaGqGfi71WR3vFBmbF_UTKhuKeFxiWUWvg7T16Qc%7C1648256104%7C645943f62c513826782c40f00db2bc10a13cd054b0bc24652eb4b1e6939aa34c; bm_sv=FE16FBB742AFD4FDB7DDB64FA8C1B7AE~Unba/2oW8CqiDdOSWhAch3UX3pT/KIEYv9EhPseQBadFCZl3TjqT8CU+MTWHyhOxktufj6V85eq7ylnl9hBS936eORG32v3PlBMZuFGYWIhvR00RSgte72rJzhO5aHrczuqjEpBlYPmLmkmSeB8Gvr5sAu/b0z5QSz+opxmdmoU=; odin_tt=605250765a9815b4b690ec68a805f2db17c5c0aab4def34aa156bf7c3a83fa9e92561a553618a44d3032f648f1ad55c0245fe5b30e90f7bb875dc77a15819b90; bm_sz=633F35D2E96CCD6CB7326E555414C284~YAAQXmV0aEPTcr5/AQAA77DTww/B1HBT48l6L9vU3fCzKdtFO3UDIln8tRXZ/doduhD7bMMD0XQVHY8+2aZ5iGvmApHvSFmfp2VH8YQYMAwGWZY1UGN+HeVLPcKxMX3Ai42wnC2o/GSMmfAfltKqRGhG75wE1ydTm35xZsRSBcmIUIjlgjlsjPo/HlGbfb+xoIDKQ47hDkwQzCkKcsslwMgX73g1CEYu9aW3yso1NF3uzbrN3DBqxMcxkv3bbPhmxNURpi6cA0kkVZJ1DNmWwTb3h4A4saxwYiSKLMa5HDWayHt0qH68+KxNy5FmZXNPmZcE6liWfjbK77E=~3753025~3355203; msToken=Z_dgRuq92kPpuRfWtBuRH_rRp56rKE-WL2eAduBvt8iAmJw4U3-65F8CH0069_CJOfrFsEKzH0PW6TiBVCOKsHDRWfS9PTrSGTW7nZHIXLatTR3cyxsYAekC75rHsI_tkjtkww==',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'User-Agent': f'{ua}'
            }
                url = f'https://www-useast1a.tiktok.com/node/share/user/@{user}?'
                resp = requests.get(url, headers=head, proxies=prox)

                data = str(resp.text)
                #print(data)
                if "10202" in data:
                    print(f'{Fore.GREEN} {user} is available{Fore.RESET}')
                    iid = random.randint(1000000000000000000,9999999999999999999)
                    did = random.randint(1000000000000000000,9999999999999999999)
                    rrl = f'https://api16-normal-useast5.us.tiktokv.com/passport/login_name/update/?iid={iid}device_id={did}&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=230703&version_name=23.7.3&device_platform=android&ab_version=23.7.3&ssmix=a&device_type=ASUS_Z01QD&device_brand=Asus&language=en&os_api=25&os_version=7.1.2&openudid=bd4e533512b02ec3&manifest_version_code=2022307030&resolution=900*1600&dpi=300&update_version_code=2022307030&_rticket=1648901404142&current_region=GB&app_type=normal&sys_region=US&mcc_mnc=23430&timezone_name=America%2FChicago&residence=GB&ts=1648901403&timezone_offset=-21600&build_number=23.7.3&region=US&uoo=0&app_language=en&carrier_region=GB&locale=en&op_region=GB&ac2=wifi&host_abi=x86&cdid=5f34dd51-232a-472e-8cc5-ef560e7cb718&support_webview=1&okhttp_version=4.1.73.25-tiktok'
                    heed = {
                            'accept-encoding': 'gzip',
                            'connection': 'Keep-Alive',
                            'content-length': '67',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'cookie': f'install_id=7077690108980512517; ttreq=1$16712bc52888671480b83464d6314b91fe6a72c8; passport_csrf_token=c660f333e9107ce790329ca694a83452; passport_csrf_token_default=c660f333e9107ce790329ca694a83452; tt-target-idc=useast5; store-idc=useast5; store-country-code=us; d_ticket=4c74ebf655247453f231b25e30af3c594297b; multi_sids=7059046590115234822%3A39a34a4a50d4f09d67d86a846840ce27%7C7081427588536042539%3A0ff6c00a6ce7d800061e52f8fb85de93%7C7081423268818437166%3A{ssid}; cmpl_token=AgQQAPNSF-RPsLJ4qlYiKR0X-FiZvOWN_4TZYMDOrQ; odin_tt=9dcf48626ef178c8058c6eb5045248d161709ab4ae288d38a85e54d2c09ce8fbfb7ac953c6187630b364b77b89a4ad6fbea8effe8f11ab7391e7a44660756059d5c822497e9d1dd120e2c25f3b12d337; sid_guard={ssid}%7C1648901391%7C5184000%7CWed%2C+01-Jun-2022+12%3A09%3A51+GMT; uid_tt=bb78adcb04ce2a6456a1670b60f28188d70fbafe25dd228ec14cd6fccdcc0efd; uid_tt_ss=bb78adcb04ce2a6456a1670b60f28188d70fbafe25dd228ec14cd6fccdcc0efd; sid_tt={ssid}; sessionid={ssid}; sessionid_ss={ssid}; msToken=gopxM0f4wha2XrHwdxjT0cJJLaWkpCzCzxsBo2rsX1RZaUOgVUZA6YJT2rBaTiDVlogyyzmKXGtJiN1IZnC9DRV_LRn6OBNUZ5j0IaX4KQM=',
                            'host': 'api16-normal-useast5.us.tiktokv.com',
                            'multi_login': '1',
                            'passport-sdk-version': '19',
                            'sdk-version': '2',
                            'user-agent': 'com.zhiliaoapp.musically/2022307030 (Linux; U; Android 7.1.2; en_US; ASUS_Z01QD; Build/N2G48H;tt-ok/3.10.0.2)',
                            'x-argus': 'XVN8HrfVF+m0utn7EzRB/0sjwdLj1sEVBc8SkwdB+1TIDwgZ5HLwisfWXea239MjwnsuvU3lSBw6VSsSt8jkvXyoADGC5asXlU/9n24R6NYQSEPmKoluQUDnLwRGwaAHt0P9CxDJBsON1TYrNwCZRU2dD5lsF1huw/AAUleQqpXOZeRrpq6LFPRoNEeZ3Fc4LTPyIS8rFhJqA8sP0qT/DM92rGTGSwgdayyzANYQJM7Ft6BnU0dfQZaQ/RwbLZLM6p4JmKLkgI13lb5hzU2DOhw/hvndWiE1aPUwl6Le8qKfacmq/RInJKyZGhdy3PTIDcz/PZqHnwXGfBnmHBgapSYvcvt+3yJrq/swctA1Srdg0Q==',
                            'x-bd-client-key': '#Eey4dFL4zZLneeBX+ah5tryRtnSH7Y0qKd5sQUeLaOpNMOBSTa7PW04PnG2urQxfdnyESBTo8W6eiHds',
                            'x-bd-kmsv': '0',
                            'x-gorgon': '040480d9400028d44c062c9621b35c24c076ad4145d0ae87b3eb',
                            'x-khronos': '1648901403',
                            'x-ladon': 'QDC4KOxG+usefDTgyhlYW/6bEwV0+ubIQJA+GclXoNRylYFn',
                            'x-ss-req-ticket': '1648901404143',
                            'x-ss-stub': '82A5715EB5652337319128944B2040F9',
                            'x-tt-cmpl-token': 'AgQQAPNSF-RPsLJ4qlYiKR0X-FiZvOWN_4QTYMDOrQ',
                            'x-tt-dm-status': 'login=1;ct=1;rt=1',
                            'x-tt-multi-sids': f'7059046590115234822%3A39a34a4a50d4f09d67d86a846840ce27%7C7081427588536042539%3A0ff6c00a6ce7d800061e52f8fb85de93%7C7081423268818437166%3A{ssid}',
                            'x-tt-store-idc': 'useast5',
                            'x-tt-store-region': 'us',
                            'x-tt-store-region-did': 'gb',
                            'x-tt-store-region-src': 'uid',
                            'x-tt-store-region-uid': 'us',
                            'x-tt-token': f'04{ssid}04f3d0c0d5372ac09299c2a55faf939b1eb568ded23be600ef4d391b35e31a1d2fe6f5ed28d689805335202bd7953086d8001e7e26321ccf735190ecb5003214d7cd673c0062a748b86876001a139be3800-1.0.1',
                            'x-vc-bdturing-sdk-version': '2.2.1.i18n',
                        }
                    r = requests.post(f'{rrl}', headers=heed, proxies=prox, data=f'login_name={user}&page_from=0').text
                    if 'success' in r:
                        disc =DiscordWebhook (url =huk )
                        embed = DiscordEmbed(title='Aims checker' , description=f'[{user}](https://tiktok.com/@{user}) is claimed', color='264dd9')

            
                        disc.add_embed(embed)

                        response = disc.execute()
                    else:
                        print(r)
                elif "10221" or "10223" in data:
                    print(f'{Fore.RED} {user} is banned{Fore.RESET}')
                else:
                    usernames.put(user)
                    print(f'Error on {user} | {data}')

        elif req.status_code == 403:

            print('Rate Limited')
            time.sleep(10)
        elif req.status_code == 400:
            usernames.put(user)
            print('Rate Limited')
           
            time.sleep(10)
        else:
            usernames.put(user)
            print(f'{Fore.RED}{user} taken{Fore.RESET}')
for i in range(5):
    time.sleep(.5)
    threading.Thread(target=checker).start()