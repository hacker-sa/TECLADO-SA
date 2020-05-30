#!/usr/bin/env python2
#-*- coding:utf8 -*-
import os
import sys
import readline
from time import sleep
from tqdm import tqdm
from tqdm import trange
#=============================================================
#_______::::____::::____cores primárias____::::____::::_______
#=============================================================
c = "\033[90m"
r = "\033[91m"
g = "\033[0m\033[92m"
gi = "\033[3m\033[92m"
y = "\033[93m"
B = "\033[94m"
d = "\033[0m\033[97m"
b = "\033[0m\033[1;38;05;20m" #azul claro
#=============================================================
#___::___:::____cores secundárias e terçiárias____:::___::____
#=============================================================
gn = "\033[92m"
m = "\033[3m\033[1;38;05;129m"
v = "\033[3m\033[1;38;05;22m" #verde escuro
vn = "\033[0m\033[1;38;05;22m" #verde escuro
va = "\033[1;38;05;23m" #verde escuro com azul
ac = "\033[3m\033[1;38;05;20m" #azul claro
acn = "\033[0m\033[1;38;05;20m" #azul claro
ac2 = "\033[1;38;05;21;3m" #azulclaro2
ac3 = "\033[0m\033[1;38;05;21m" #azulclaro
a2 = "\033[0m\033[1;38;05;129m"
os.system("clear")
#=============================================================
#_____::::___::::_____modo e velocidade_____::::____::::______
#=============================================================
def text(s):
    for noobs in s + "\n":
            sys.stdout.write(noobs)
            sys.stdout.flush()
            sleep(5. / 2100)

#=============================================================
#_____::::___::::____definicao do banner____::::____::::______
#=============================================================
def banner():
    text (ac3+"""

▬▬▬▬▬▬▬▬▬▬▬▬
     █       █▀▀▀▀▀  █▀▀▀▀▀▀▀  █        █▀▀▀▀▀▀▀█  █▀▀▀▀▀▀▀⸜⸜  ╭▀▀▀▀▀▀╮    █▀▀▀▀▀▀  █▀▀▀▀▀▀█
     █       █       █         █        █       █  █        █  █      █    █        █      █
     █       █▬▬▬▬▬  █         █        █▬▬▬▬▬▬▬█  █        █  █      █ ▬▬ ╚═════╗  █▬▬▬▬▬▬█
     █       █       █         █        █       █  █        █  █      █          ║  █      █
     █       █       █         █        █       █  █        █  █      █          █  █      █
     █       ▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀  █       █  ▀▀▀▀▀▀▀▀⸍⸍  ╰▀▀▀▀▀▀╯    ▀▀▀▀▀▀▀  █      █
                                                    """+g+"ｃｒｅａｔｅｄ ｂｙ 👉 ｈａｃｋｅｒ-ｓａ"+g+"""
                                                                          ｖｅｒｓｉｏｎ:2.0
""")


#=============================================================
#"""_______::::___::::_____ menu 2 _____::::____::::_______"""
#=============================================================
def menu2():
    os.system('clear')
    print (acn+"\nescolha a opção 👇")
    print (g+"""

"""+b+"["+y+"1"+b+"]"+"""
   """+acn+"\_______________________________________"+g+"""
"""+acn+"""   ║                                      ║
"""+acn+"   ║"+v+"  ESC   /   -   HOME   UP   END  PGUP "+acn+"""║
   ║                                      ║
"""+acn+"   ║"+v+" TAB CTRL ALT  LEFT  DOWN  RIGHT PGDN "+acn+"""║
   ║"""+acn+"______________________________________║"+b+"""

"""+"["+y+"2"+b+"]"+"""
   """+acn+"\________________________________________"+g+"""
"""+acn+"""   ║                                       ║
"""+acn+"   ║"+v+"  {    }    [     ]     up    (    ) "+acn+"""  ║
   ║                                       ║
"""+acn+"   ║"+v+" ESC   /    -   HOME    +    END  PGUP "+acn+"""║
   ║                                       ║
"""+acn+"   ║"+v+" TAB CTRL  ALT  LEFT  DOWN  RIGHT PGDN "+acn+"""║
   ║"""+acn+"_______________________________________║"+b+"""

"""+"["+y+"3"+b+"]"+"""
   """+acn+"\_____________________________________________"+g+"""
"""+acn+"""   ║                                            ║
"""+acn+"   ║"+v+"   {    }    [    ]    *     up   (    ) "+acn+"""   ║
   ║                                            ║
"""+acn+"   ║"+v+" ESC   /    -   =    HOME    +    END  PGUP "+acn+"""║
   ║                                            ║
"""+acn+"   ║"+v+" TAB CTRL  ALT  ═    LEFT  DOWN  RIGHT PGDN "+acn+"""║
   ║"""+acn+"____________________________________________║"+b+"""

"""+"["+y+"4"+b+"]"+"""
   """+acn+"\________________________________________"+g+"""
"""+acn+"""   ║                                       ║
"""+acn+"   ║"+v+"  {}   []   ()    $     UP     #    _ "+acn+""" ║
   ║                                       ║
"""+acn+"   ║"+v+" ESC   /    -   HOME    +    END  PGUP "+acn+"""║
   ║                                       ║
"""+acn+"   ║"+v+" TAB CTRL  ALT  LEFT  DOWN  RIGHT PGDN "+acn+"""║
   ║"""+acn+"_______________________________________║"+b+"""

"""+"["+y+"5"+b+"]"+"""
   """+acn+"\____________________________________________"+g+"""
"""+acn+"""   ║                                           ║
"""+acn+"   ║"+v+"  {}   []   ()   *    $     UP     #    _ "+acn+""" ║
   ║                                           ║
"""+acn+"   ║"+v+" ESC   /    -   =   HOME    +    END  PGUP "+acn+"""║
   ║                                           ║
"""+acn+"   ║"+v+" TAB CTRL  ALT  ═   LEFT  DOWN  RIGHT PGDN "+acn+"""║
   ║"""+acn+"___________________________________________║"+b+"""

"""+"["+y+"6"+b+"]"+v+"                   ｐａｒａ ｄｅｓｅｎｈｏｓ"+acn+"""
   """+acn+"\____________________________________________________________________"+g+"""
"""+acn+"""   ║                                                                   ║
"""+acn+"   ║"+vn+"  ╔       ╗    ╦    ▒    ░    ╭     ╮     UP     ●     √   ✧   ▬  "+acn+""" ║
   ║                                                                   ║
"""+acn+"   ║"+vn+"  ╚       ╝    ╩    ▀    █    ╰     ╯     ¤      ¶     ▋   ☆  PGUP "+acn+"""║
   ║                                                                   ║
"""+acn+"   ║"+vn+" CTRL     ╠    ╣    ║    ═    ⸍   LEFT   DOWN  RIGHT   ⸜   ✺  PGDN "+acn+"""║
   ║"""+acn+"___________________________________________________________________║"+b+"""

"""+"["+y+"7"+b+"]"+v+"                   ｌｅｔｒａｓ ｇｒａｎｄｅｓ"+g+"""
   """+acn+"\_________________________________________________________________"+g+"""
"""+acn+"""   ║                                                                ║
"""+acn+"   ║"+vn+"  ｑ     ｗ    ｅ    ｒ    ｔ    ｙ    ｕ    UP    ｉ   ｏ   ｐ "+acn+"""║
   ║                                                                ║
"""+acn+"   ║"+vn+"  ESC    ａ    ｓ    ｄ    ｆ    ｇ    ｈ    ｊ    ｋ   ｌ   ！ "+acn+"""║
   ║                                                                ║
"""+acn+"   ║"+vn+" CTRL    ｚ    ｘ    ｃ    ｖ    ｂ   LEFT  DOWN  RIGHT ｎ   ｍ "+acn+"""║
   ║"""+acn+"________________________________________________________________║"+b+"""

"""+b+"["+y+"8"+b+"]"+v+" ｓｏｂｒｅ"+"""
"""+b+"["+y+"9"+b+"]"+v+" ｓａｉｒ"+"""
"""+b+"["+y+"10"+b+"]"+v+""" ｖｏｌｔａｒ ａｏ ｔｅｃｌａｄｏ ｏｒｉｇｉｎａｌ""")

    print (g)

#=============================================================
#"""______:::____●●●●●___☆_  update  _☆___●●●●●____:::_____"""
#=============================================================
def update():
    if os.path.exists("/data/data/com.termux/files/home/TECLADO-SA"):
      pass
    else:
       os.system("cd;git clone https://github.com/hacker-sa/TECLADO-SA")
       print ("updated")
       sys.exit()
    if os.path.exists("/data/data/com.termux/files/home/T-SA"):
         os.system("cd;cd T-SA;python2 config.py")
         sys.exit()
    else:
         print ("fazendo update...")
         os.system("cd /data/data/com.termux/files/home;mkdir T-SA")
         os.system("cd /data/data/com.termux/files/home;cd T-SA;git clone https://github.com/hacker-sa/TECLADO-SA")
         os.system("cd /data/data/com.termux/files/home;cd TECLADO-SA;mv -v config.py /data/data/com.termux/files/home/T-SA;cd;cd T-SA;python2 config.py")

#=============================================================
#"""______:::____::::___ teclado orgn ____::::____:::_____"""
#=============================================================
def mn():
    os.system("clear")
    print(ac+"\n\nｖｏｌｔａｎｄｏ ａｏ ｔｅｃｌａｄｏ ｏｒｉｇｉｎａｌ ｄｏ ｔｅｒｍｕｘ！")
    print ("")
    progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,15,16,17,18,20])

    for item in progressbar:
        sleep(0.2)
        progressbar.set_description("\033[0m\033[92m PROCESSANDO...{}".format(item))

    print(v+"═"*72)
    sleep(2)
    os.system("clear")

    t = 1
    while t <= 7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" Recuperando arquivo predeterminado do termux..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" Recuperando arquivo predeterminado do termux..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" Recuperando arquivo predeterminado do termux..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" Recuperando arquivo predeterminado do termux..."+y+"-")
      sleep(0.1)
      os.system('clear')

    try:

     os.mkdir("/data/data/com.termux/files/home/.termux")
    except:
        pass

    print(g+"["+y+"●"+g+"]"+g+" sucesso "+d+"["+gn+"√"+d+"]")
    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" adicionando botões no teclado predeterminado..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" adicionando botões no teclado predeterminado..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" adicionando botões no teclado predeterminado..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" adicionando botões no teclado predeterminado..."+y+"-")
      sleep(0.1)
      os.system('clear')

    with  open("/data/data/com.termux/files/home/.termux/termux.properties","w") as tp:
       tp.write("""extra-keys = [["ESC","TAB","CTRL","ALT","-","DOWN","UP"]]""")
       tp.close()

    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" terminando processo..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" terminando processo..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" terminando processo..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" terminando processo..."+y+"-")
      sleep(0.1)
      os.system('clear')

    sleep(1)
    os.system("termux-reload-settings")
    print (acn+"\n                              ｐｒｏｃｅｓｓｏ ｃｏｍｐｌｅｔｏ")
    print ("                                ｐｏｒ 👉 ｈａｃｋｅｒ-ｓａ")
    print ("")
    print(r+"╔"+"═"*85+"╗")
    print (r+"║"+g+"OBS: ｐｕｘｅ ｏ teclado da direita para a esquerda para entrar na área de  trabalho！"+r+"║")
    print("╚"+"═"*85+"╝")

#=============================================================
#"""______:::____::::_____ teclado 1 ______::::____:::_____"""
#=============================================================
def m1():
    os.system("clear")
    print(ac+"\n\nａｄｉｃｉｏｎａｎｄｏ ｔｅｃｌａｄｏ ｅｓｐｅｃｉａｌ ｎｏ ｔｅｒｍｕｘ！")
    print ("")
    progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,15,16,17,18,20])

    for item in progressbar:
        sleep(0.2)
        progressbar.set_description('\033[0m\033[92m PROCESSANDO...{}'.format(item))

    print(v+"═"*72)
    sleep(2)
    os.system("clear")

    t = 1
    while t <= 7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" Recuperando arquivo predeterminado do termux..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" Recuperando arquivo predeterminado do termux..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" Recuperando arquivo predeterminado do termux..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" Recuperando arquivo predeterminado do termux..."+y+"-")
      sleep(0.1)
      os.system('clear')

    try:

     os.mkdir("/data/data/com.termux/files/home/.termux")
    except:
        pass

    print(g+"["+y+"●"+g+"]"+g+" sucesso "+d+"["+gn+"√"+d+"]")
    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" adicionando botões no teclado predeterminado..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" adicionando botões no teclado predeterminado..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" adicionando botões no teclado predeterminado..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" adicionando botões no teclado predeterminado..."+y+"-")
      sleep(0.1)
      os.system('clear')

    with  open("/data/data/com.termux/files/home/.termux/termux.properties","w") as tp:
       tp.write("""extra-keys = [["ESC","/","-","HOME","UP","END","PGUP"],["TAB","CTRL","ALT","LEFT","DOWN","RIGHT","PGDN"]]""")
       tp.close()

    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" terminando processo..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" terminando processo..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" terminando processo..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" terminando processo..."+y+"-")
      sleep(0.1)
      os.system('clear')

    sleep(1)
    os.system("termux-reload-settings")
    print (acn+"\n                              ｐｒｏｃｅｓｓｏ ｃｏｍｐｌｅｔｏ")
    print ("                                ｐｏｒ 👉 ｈａｃｋｅｒ-ｓａ")
    print ("")
    print(r+"╔"+"═"*85+"╗")
    print (r+"║"+g+"OBS: ｐｕｘｅ ｏ teclado da direita para a esquerda para entrar na área de trabalho！"+r+"║")
    print("╚"+"═"*85+"╝")

#=============================================================
#"""____::::___::::_______teclado 2 _______::::____::::____"""
#=============================================================
def m2():
    os.system("clear")
    print(ac+"\n\nａｄｉｃｉｏｎａｎｄｏ ｔｅｃｌａｄｏ ｅｓｐｅｃｉａｌ ｎｏ ｔｅｒｍｕｘ！")
    print ("")
    progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,15,16,17,18,20])

    for item in progressbar:
        sleep(0.2)
        progressbar.set_description('\033[0m\033[92m PROCESSANDO...{}'.format(item))

    print(v+"═"*72)
    sleep(2)
    os.system("clear")

    t = 1
    while t <= 7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" Recuperando arquivo predeterminado do termux..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" Recuperando arquivo predeterminado do termux..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" Recuperando arquivo predeterminado do termux..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" Recuperando arquivo predeterminado do termux..."+y+"-")
      sleep(0.1)
      os.system('clear')

    try:
     os.mkdir("/data/data/com.termux/files/home/.termux")
    except:
        pass
    print(g+"["+y+"●"+g+"]"+g+" sucesso "+d+"["+gn+"√"+d+"]")
    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" adicionando botões no teclado predeterminado..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" adicionando botões no teclado predeterminado..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" adicionando botões no teclado predeterminado..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" adicionando botões no teclado predeterminado..."+y+"-")
      sleep(0.1)
      os.system('clear')

    with  open("/data/data/com.termux/files/home/.termux/termux.properties","w") as tp:
       tp.write("""extra-keys = [["{","}","[","]","UP","(",")"],["ESC","/","-","HOME","+","END","PGUP"],["TAB","CTRL","ALT","LEFT","DOWN","RIGHT","PGDN"]]""")
       tp.close()

    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" terminando processo..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" terminando processo..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" terminando processo..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" terminando processo..."+y+"-")
      sleep(0.1)
      os.system('clear')

    sleep(1)
    os.system("termux-reload-settings")
    print (acn+"\n                              ｐｒｏｃｅｓｓｏ ｃｏｍｐｌｅｔｏ")
    print ("                                ｐｏｒ 👉 ｈａｃｋｅｒ-ｓａ")
    print ("")
    print(r+"╔"+"═"*85+"╗")
    print (r+"║"+g+"OBS: ｐｕｘｅ ｏ teclado da direita para a esquerda para entrar na área de trabalho！"+r+"║")
    print("╚"+"═"*85+"╝")

#=============================================================
#"""______:::____::::_____ teclado 3 ______::::____:::_____"""
#=============================================================
def m3():
    os.system("clear")
    print(ac+"\n\nａｄｉｃｉｏｎａｎｄｏ ｔｅｃｌａｄｏ ｅｓｐｅｃｉａｌ ｎｏ ｔｅｒｍｕｘ！")
    print ("")
    progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,15,16,17,18,20])

    for item in progressbar:
        sleep(0.2)
        progressbar.set_description('\033[0m\033[92m PROCESSANDO...{}'.format(item))

    print(v+"═"*72)
    sleep(2)
    os.system("clear")

    t = 1
    while t <= 7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" Recuperando arquivo predeterminado do termux..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" Recuperando arquivo predeterminado do termux..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" Recuperando arquivo predeterminado do termux..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" Recuperando arquivo predeterminado do termux..."+y+"-")
      sleep(0.1)
      os.system('clear')

    try:
     os.mkdir("/data/data/com.termux/files/home/.termux")
    except:
        pass
    print(g+"["+y+"●"+g+"]"+g+" sucesso "+d+"["+gn+"√"+d+"]")
    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" adicionando botões no teclado predeterminado..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" adicionando botões no teclado predeterminado..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" adicionando botões no teclado predeterminado..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" adicionando botões no teclado predeterminado..."+y+"-")
      sleep(0.1)
      os.system('clear')

    with  open("/data/data/com.termux/files/home/.termux/termux.properties","w") as tp:
       tp.write("""extra-keys = [["{","}","[","]","*","UP","(",")"],["ESC","/","-","=","HOME","+","END","PGUP"],["TAB","CTRL","ALT","═","LEFT","DOWN","RIGHT","PGDN"]]""")
       tp.close()

    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" terminando processo..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" terminando processo..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" terminando processo..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" terminando processo..."+y+"-")
      sleep(0.1)
      os.system('clear')

    sleep(1)
    os.system("termux-reload-settings")
    print (acn+"\n                              ｐｒｏｃｅｓｓｏ ｃｏｍｐｌｅｔｏ")
    print ("                                ｐｏｒ 👉 ｈａｃｋｅｒ-ｓａ")
    print ("")
    print(r+"╔"+"═"*85+"╗")
    print (r+"║"+g+"OBS: ｐｕｘｅ ｏ teclado da direita para a esquerda para entrar na área de trabalho！"+r+"║")
    print("╚"+"═"*85+"╝")

#=============================================================
#"""______:::____::::_____ teclado 4 ______::::____:::_____"""
#=============================================================
def m4():
    os.system("clear")
    print(ac+"\n\nａｄｉｃｉｏｎａｎｄｏ ｔｅｃｌａｄｏ ｅｓｐｅｃｉａｌ ｎｏ ｔｅｒｍｕｘ！")
    print ("")
    progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,15,16,17,18,20])

    for item in progressbar:
        sleep(0.2)
        progressbar.set_description('\033[0m\033[92m PROCESSANDO...{}'.format(item))

    print(v+"═"*72)
    sleep(2)
    os.system("clear")

    t = 1
    while t <= 7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" Recuperando arquivo predeterminado do termux..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" Recuperando arquivo predeterminado do termux..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" Recuperando arquivo predeterminado do termux..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" Recuperando arquivo predeterminado do termux..."+y+"-")
      sleep(0.1)
      os.system('clear')

    try:

     os.mkdir("/data/data/com.termux/files/home/.termux")
    except:
         pass

    print(g+"["+y+"●"+g+"]"+g+" sucesso "+d+"["+gn+"√"+d+"]")
    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" adicionando botões no teclado predeterminado..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" adicionando botões no teclado predeterminado..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" adicionando botões no teclado predeterminado..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" adicionando botões no teclado predeterminado..."+y+"-")
      sleep(0.1)
      os.system('clear')

    with  open("/data/data/com.termux/files/home/.termux/termux.properties","w") as tp:
       tp.write("""extra-keys = [["{}","[]","()","$","UP","#","_"],["ESC","/","-","HOME","+","END","PGUP"],["TAB","CTRL","ALT","LEFT","DOWN","RIGHT","PGDN"]]""")
       tp.close()

    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" terminando processo..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" terminando processo..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" terminando processo..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" terminando processo..."+y+"-")
      sleep(0.1)
      os.system('clear')

    sleep(1)
    os.system("termux-reload-settings")
    print (acn+"\n                              ｐｒｏｃｅｓｓｏ ｃｏｍｐｌｅｔｏ")
    print ("                                ｐｏｒ 👉 ｈａｃｋｅｒ-ｓａ")
    print ("")
    print(r+"╔"+"═"*85+"╗")
    print (r+"║"+g+"OBS: ｐｕｘｅ ｏ teclado da direita para a esquerda para entrar na área de trabalho！"+r+"║")
    print("╚"+"═"*85+"╝")

#=============================================================
#"""_____:::___::::_______ teclado 5 _______::::___:::_____"""
#=============================================================
def m5():
    os.system("clear")
    print(ac+"\n\nａｄｉｃｉｏｎａｎｄｏ ｔｅｃｌａｄｏ ｅｓｐｅｃｉａｌ ｎｏ ｔｅｒｍｕｘ！")
    print ("")
    progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,15,16,17,18,20])

    for item in progressbar:
        sleep(0.2)
        progressbar.set_description('\033[0m\033[92m PROCESSANDO...{}'.format(item))

    print(v+"═"*72)
    sleep(2)
    os.system("clear")

    t = 1
    while t <= 7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" Recuperando arquivo predeterminado do termux..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" Recuperando arquivo predeterminado do termux..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" Recuperando arquivo predeterminado do termux..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" Recuperando arquivo predeterminado do termux..."+y+"-")
      sleep(0.1)
      os.system('clear')

    try:

     os.mkdir("/data/data/com.termux/files/home/.termux")
    except:
         pass

    print(g+"["+y+"●"+g+"]"+g+" sucesso "+d+"["+gn+"√"+d+"]")
    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" adicionando botões no teclado predeterminado..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" adicionando botões no teclado predeterminado..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" adicionando botões no teclado predeterminado..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" adicionando botões no teclado predeterminado..."+y+"-")
      sleep(0.1)
      os.system('clear')

    with  open("/data/data/com.termux/files/home/.termux/termux.properties","w") as tp:
       tp.write("""extra-keys = [["{}","[]","()","*","$","UP","#","_"],["ESC","/","-","=","HOME","+","END","PGUP"],["TAB","CTRL","ALT","═","LEFT","DOWN","RIGHT","PGDN"]]""")
       tp.close()

    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" terminando processo..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" terminando processo..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" terminando processo..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" terminando processo..."+y+"-")
      sleep(0.1)
      os.system('clear')

    sleep(1)
    os.system("termux-reload-settings")
    print (acn+"\n                              ｐｒｏｃｅｓｓｏ ｃｏｍｐｌｅｔｏ")
    print ("                                ｐｏｒ 👉 ｈａｃｋｅｒ-ｓａ")
    print ("")
    print(r+"╔"+"═"*85+"╗")
    print (r+"║"+g+"OBS: ｐｕｘｅ ｏ teclado da direita para a esquerda para entrar na área de trabalho！"+r+"║")
    print("╚"+"═"*85+"╝")

#=============================================================
#"""____::::___::::_______teclado 6 _______::::____::::____"""
#=============================================================
def m6():
    os.system("clear")
    print(ac+"\n\nａｄｉｃｉｏｎａｎｄｏ ｔｅｃｌａｄｏ ｅｓｐｅｃｉａｌ ｎｏ ｔｅｒｍｕｘ！")
    print ("")
    progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,15,16,17,18,20])

    for item in progressbar:
        sleep(0.2)
        progressbar.set_description('\033[0m\033[92m PROCESSANDO...{}'.format(item))

    print(v+"═"*72)
    sleep(2)
    os.system("clear")

    t = 1
    while t <= 7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" Recuperando arquivo predeterminado do termux..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" Recuperando arquivo predeterminado do termux..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" Recuperando arquivo predeterminado do termux..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" Recuperando arquivo predeterminado do termux..."+y+"-")
      sleep(0.1)
      os.system('clear')

    try:
     os.mkdir("/data/data/com.termux/files/home/.termux")
    except:
        pass
    print(g+"["+y+"●"+g+"]"+g+" sucesso "+d+"["+gn+"√"+d+"]")
    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" adicionando botões no teclado predeterminado..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" adicionando botões no teclado predeterminado..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" adicionando botões no teclado predeterminado..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" adicionando botões no teclado predeterminado..."+y+"-")
      sleep(0.1)
      os.system('clear')

    with  open("/data/data/com.termux/files/home/.termux/termux.properties","w") as tp:
       tp.write("""extra-keys = [["╔","╗","╦","▒","░","╭","╮","UP","●","√","✧","▬"],["╚","╝","╩","▀","█","╰","╯","°","¶","▋","☆","PGUP"],["CTRL","╠","╣","║","═","⸍","LEFT","DOWN","RIGHT","⸜","✺","PGDN"]]""")
       tp.close()

    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" terminando processo..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" terminando processo..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" terminando processo..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" terminando processo..."+y+"-")
      sleep(0.1)
      os.system('clear')

    sleep(1)
    os.system("termux-reload-settings")
    print (b+"\n                              ｐｒｏｃｅｓｓｏ ｃｏｍｐｌｅｔｏ")
    print ("                                ｐｏｒ 👉 ｈａｃｋｅｒ-ｓａ")
    print (gn+"""\neste teclado só pode ser usado em python se vc colocar o nome 👉 #-*- coding:utf8 -*-\nna primeira ou segunda linha do script""")
    print ("")
    print(r+"╔"+"═"*85+"╗")
    print (r+"║"+g+"OBS: ｐｕｘｅ ｏ teclado da direita para a esquerda para entrar na área de trabalho！"+r+"║")
    print("╚"+"═"*85+"╝")

#=============================================================
#"""____::::___::::_______teclado 7 _______::::____::::____"""
#=============================================================
def m7():
    os.system("clear")
    print(ac+"\n\nａｄｉｃｉｏｎａｎｄｏ ｔｅｃｌａｄｏ ｅｓｐｅｃｉａｌ ｎｏ ｔｅｒｍｕｘ！")
    print ("")
    progressbar = tqdm([1,2,3,4,5,6,7,8,9,10,11,12,13,13,14,15,16,17,18,20])

    for item in progressbar:
        sleep(0.2)
        progressbar.set_description('\033[0m\033[92m PROCESSANDO...{}'.format(item))

    print(v+"═"*72)
    sleep(2)
    os.system("clear")

    t = 1
    while t <= 7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" Recuperando arquivo predeterminado do termux..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" Recuperando arquivo predeterminado do termux..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" Recuperando arquivo predeterminado do termux..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" Recuperando arquivo predeterminado do termux..."+y+"-")
      sleep(0.1)
      os.system('clear')

    try:
     os.mkdir("/data/data/com.termux/files/home/.termux")
    except:
        pass
    print(g+"["+y+"●"+g+"]"+g+" sucesso "+d+"["+gn+"√"+d+"]")
    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" adicionando botões no teclado predeterminado..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" adicionando botões no teclado predeterminado..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" adicionando botões no teclado predeterminado..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" adicionando botões no teclado predeterminado..."+y+"-")
      sleep(0.1)
      os.system('clear')

    with  open("/data/data/com.termux/files/home/.termux/termux.properties","w") as tp:
       tp.write("""extra-keys = [["ｑ","ｗ","ｅ","ｒ","ｔ","ｙ","ｕ","UP","ｉ","ｏ","ｐ"],["ESC","ａ","ｓ","ｄ","ｆ","ｇ","ｈ","ｊ","ｋ","ｌ","！"],["CTRL","ｚ","ｘ","ｃ","ｖ","ｂ","LEFT","DOWN","RIGHT","ｎ","ｍ"]]""")
       tp.close()

    sleep(2)

    t = 1
    while t <=7:
      t = t+1
      print(g+"["+y+"●"+g+"]"+acn+" terminando processo..."+y+"\\")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+g+" terminando processo..."+y+"|")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+y+" terminando processo..."+y+"/")
      sleep(0.1)
      os.system('clear')
      print(g+"["+y+"●"+g+"]"+r+" terminando processo..."+y+"-")
      sleep(0.1)
      os.system('clear')

    sleep(1)
    os.system("termux-reload-settings")
    print (b+"\n                              ｐｒｏｃｅｓｓｏ ｃｏｍｐｌｅｔｏ")
    print ("                                ｐｏｒ 👉 ｈａｃｋｅｒ-ｓａ")
    print (gn+"""\neste teclado só pode ser usado em python se vc colocar o nome 👉 #-*- coding:utf8 -*-\nna primeira ou segunda linha do script""")
    print ("")
    print(r+"╔"+"═"*85+"╗")
    print (r+"║"+g+"OBS: ｐｕｘｅ ｏ teclado da direita para a esquerda para entrar na área de trabalho！"+r+"║")
    print("╚"+"═"*85+"╝")

#=============================================================
#"""_______::::___::::______ about ______::::___::::_______"""
#=============================================================
def m8():
    os.system("clear")
    print ("\n")
    print (v+"*" * 70)
    print (g+"\nｔｅｃｌａｄｏ-ｓａ "+y+"         "+ac+"               ｖｅｒｓａｏ:"+y+"1.0")
    print ("")
    print (ac+"ｃｒｉａｄｏ ｐｏｒ:"+y+" ｈａｃｋｅｒ-ｓａ  "+ac+"    ｄａｔａ:"+y+"03/04/2020")
    print ("")
    print (ac+"ｍｅｕ ｇｉｔｈｕｂ 👉"+y+" https://github.com/hacker-sa ")
    print ("")
    print (v+"*" * 70)
    print (g+"["+b+"1"+g+"]"+g+"voltar ao menu anterior")
    print (g+"["+b+"2"+g+"]"+g+"sair")
    opt2 = raw_input(" o quê deseja fazer? 👉 ")
    if opt2 in ["1"] or opt2 in ["01"]:
       restart()

    elif opt2 in ["2"] or opt2 in ["02"]:
       sair()

    else:
         os.system("clear")
         print (g+opt+B+" não é uma opção existente")
         print (B+"voltando ao menu principal...")
         sleep(3)
         restart()

#=============================================================
#"""___:::____::::____ modo e velocidade2 ____::::___:::___"""
#=============================================================
def txt(s):
    for noobs in s + "\n":
            sys.stdout.write(noobs)
            sys.stdout.flush()
            sleep(110. / 2100)


#=============================================================
#"""_______:::____::::___ menu de saída __::::____:::______"""
#=============================================================
def sair():
    print (g+"qual o seu nome?")
    nome = raw_input("nome 👉 ")
    os.system("clear")
    txt(g+"\nOlá "+nome+" muito obrigado por usar esta ferramenta!!! 👏 criei este \nteclado para facilitar a programação com relação  ao uso dos carácters\ne movimentação do cursor na hora de programar.")
    sleep(1)
    txt(g+"Espero tê-lo ajudado...Qualquer dúvida crítica ou sujestão por favor contate-me.\n\nEmail 👉"+b+" hacker-sa02@gmail.com")
    txt(g+"meu github 👉 "+b+"https://github.com/hacker-sa")
    sys.exit()

#=============================================================
#"""_______:::___::::___função restart __::::____:::_______"""
#=============================================================
def restart():
    r = sys.executable
    os.execl(r, r, * sys.argv)

def fn():
    print (y+"ｄｅｓｅｊａ ｔｅｓｔａｒ ｍａｉｓ ａｌｇｕｍ ｔｅｃｌａｄｏ ？")
    print (g+"["+y+"1"+g+"]"+acn+" testar")
    print (g+"["+y+"2"+g+"]"+acn+" sair")
    opt = raw_input(y+"opção 👉 ")
    if opt in ["1"] or opt in ["01"]:
       menu2()

    elif opt in ["2"] or opt in ["02"]:
       sair()

    else:
        os.system("clear")
        print (g+opt+B+" não é uma opção existente")
        print (B+"voltando ao menu principal...")
        sleep(3)
        restart()
