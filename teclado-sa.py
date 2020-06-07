#!/usr/bin/env python2
#-*- coding: utf-8 -*-
# TECLADO-SA v2.0
#=============================================================
#________::::____::::_____importacoes_____::::____::::________
#=============================================================
import os

try:
   import tqdm
except ImportError:
   os.system("pip2 install tqdm -y")

from tec import *

"""_____#_____+____ ꧁↠↠↠início↞↞↞꧂ ____+____#_____"""
"""                                                       """
os.system("rm -rf /data/data/com.termux/files/home/T-SA")
banner()

#=============================================================
#"""_______::::___::::______ menu ______::::____::::_______"""
#=============================================================
def menu():
    txt("ｅｓｃｏｌｈａ ａ ｏｐｃａｏ 👇")
    sleep(2)
    print (g+"""

"""+b+"["+y+"１"+b+"]"+"""
   """+acn+"\________________________________________"+g+"""
"""+acn+"""   ║                                       ║
"""+acn+"   ║"+v+"  ESC   /   -   HOME   UP   END   PvUP "+acn+"""║
   ║                                       ║
"""+acn+"   ║"+v+" TAB CTRL ALT  LEFT  DOWN  RIGHT PGDN "+acn+""" ║
   ║"""+acn+"_______________________________________║"+b+"""

"""+"["+y+"２"+b+"]"+"""
   """+acn+"\________________________________________"+g+"""
"""+acn+"""   ║                                       ║
"""+acn+"   ║"+v+"   {    }    [    ]     up     (    )  "+acn+"""║
   ║                                       ║
"""+acn+"   ║"+v+" ESC   /    -   HOME    +    END  PGUP "+acn+"""║
   ║                                       ║
"""+acn+"   ║"+v+" TAB CTRL  ALT  LEFT  DOWN  RIGHT PGDN "+acn+"""║
   ║"""+acn+"_______________________________________║"+b+"""

"""+"["+y+"３"+b+"]"+"""
   """+acn+"\_____________________________________________"+g+"""
"""+acn+"""   ║                                            ║
"""+acn+"   ║"+v+"   {    }    [    ]    *     up     (    )  "+acn+"""║
   ║                                            ║
"""+acn+"   ║"+v+" ESC   /    -   =    HOME    +    END  PGUP "+acn+"""║
   ║                                            ║
"""+acn+"   ║"+v+" TAB CTRL  ALT  ═    LEFT  DOWN  RIGHT PGDN "+acn+"""║
   ║"""+acn+"____________________________________________║"+b+"""

"""+"["+y+"４"+b+"]"+"""
   """+acn+"\________________________________________"+g+"""
"""+acn+"""   ║                                       ║
"""+acn+"   ║"+v+"  {}   []   ()    $     UP     #    _  "+acn+"""║
   ║                                       ║
"""+acn+"   ║"+v+" ESC   /    -   HOME    +    END  PGUP "+acn+"""║
   ║                                       ║
"""+acn+"   ║"+v+" TAB CTRL  ALT  LEFT  DOWN  RIGHT PGDN "+acn+"""║
   ║"""+acn+"_______________________________________║"+b+"""

"""+"["+y+"５"+b+"]"+"""
   """+acn+"\____________________________________________"+g+"""
"""+acn+"""   ║                                           ║
"""+acn+"   ║"+v+"  {}   []   ()   *    $     UP     #    _  "+acn+"""║
   ║                                           ║
"""+acn+"   ║"+v+" ESC   /    -   =   HOME    +    END  PGUP "+acn+"""║
   ║                                           ║
"""+acn+"   ║"+v+" TAB CTRL  ALT  ═   LEFT  DOWN  RIGHT PGDN "+acn+"""║
   ║"""+acn+"___________________________________________║"+b+"""

"""+"["+y+"６"+b+"]"+v+"                    ｐａｒａ ｄｅｓｅｎｈｏｓ"+acn+"""
   """+acn+"\____________________________________________________________________"+g+"""
"""+acn+"""   ║                                                                   ║
"""+acn+"   ║"+vn+"  ╔       ╗    ╦    ▒    ░    ╭     ╮     UP     ●     √   ✧   ▬  "+acn+""" ║
   ║                                                                   ║
"""+acn+"   ║"+vn+"  ╚       ╝    ╩    ▀    █    ╰     ╯     ¤      ¶     ▋   ☆  PGUP "+acn+"""║
   ║                                                                   ║
"""+acn+"   ║"+vn+" CTRL     ╠    ╣    ║    ═    ⸍   LEFT   DOWN  RIGHT   ⸜   ✺  PGDN "+acn+"""║
   ║"""+acn+"___________________________________________________________________║"+b+"""

"""+"["+y+"７"+b+"]"+v+"                   ｌｅｔｒａｓ ｇｒａｎｄｅｓ"+g+"""
   """+acn+"\_________________________________________________________________"+g+"""
"""+acn+"""   ║                                                                ║
"""+acn+"   ║"+vn+"  ｑ     ｗ    ｅ    ｒ    ｔ    ｙ    ｕ    UP    ｉ   ｏ   ｐ "+acn+"""║
   ║                                                                ║
"""+acn+"   ║"+vn+"  ESC    ａ    ｓ    ｄ    ｆ    ｇ    ｈ    ｊ    ｋ   ｌ   ！ "+acn+"""║
   ║                                                                ║
"""+acn+"   ║"+vn+" CTRL    ｚ    ｘ    ｃ    ｖ    ｂ   LEFT  DOWN  RIGHT ｎ   ｍ "+acn+"""║
   ║"""+acn+"________________________________________________________________║"+b+"""

"""+b+"["+y+"８"+b+"]"+v+" ｓｏｂｒｅ"+"""
"""+b+"["+y+"９"+b+"]"+v+" ｓａｉｒ"+"""
"""+b+"["+y+"１０"+b+"]"+v+" ｕｐｄａｔｅ"+"""
"""+b+"["+y+"００"+b+"]"+v+""" ｖｏｌｔａｒ ａｏ ｔｅｃｌａｄｏ ｏｒｉｇｉｎａｌ""")
menu()

print(g)

#=============================================================
#"""_______::::___::::______ input ______::::____::::______"""
#=============================================================
def input():
    while True:
        try:
            opt = raw_input("opção > ")

            if opt == "1" or opt == "01":
               m1()
               fn()
               input()

            elif opt == "2" or opt == "02":
               m2()
               fn()
               input()

            elif opt == "3" or opt == "03":
               m3()
               fn()
               input()

            elif opt == "4" or opt == "04":
               m4()
               fn()
               input()

            elif opt == "5" or opt == "05":
               m5()
               fn()
               input()

            elif opt == "6" or opt == "06":
               m6()
               fn()
               input()

            elif opt == "7" or opt == "07":
               m7()
               fn()
               input()

            elif opt == "8" or opt == "08":
               m8()
               fn()
               input()

            elif opt == "9" or opt == "09":
               sair()

            elif opt == "10":
               update()
            elif opt == "00":
               mn()
               fn()
               input()

            else:
               os.system("clear")
               print (g+opt+B+" não é uma opção existente")
               print (B+"voltando ao menu principal...")
               sleep(3)
               restart()

        except KeyboardInterrupt:
            print(g+"digite 9 para sair\nvoltando ao menu principal")
            sleep(2)
            restart()

input()
