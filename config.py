#!usr
#-*- coding:utf8 -*-
os.system("rm -rf /data/data/com.termux/files/home/TECLADO-SA")
os.system("cd;cd T-SA;mv -v TECLADO-SA /data/data/com.termux/files/home;cd;cd TECLADO-SA;toilet --g -f slant updated;python2 teclado-sa3.py")
os.system("cd;rm -rf T-SA")
