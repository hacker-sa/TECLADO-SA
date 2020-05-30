#!usr
#-*- coding:utf8 -*-
import os
import sys

os.system("rm -rf /data/data/com.termux/files/home/TECLADO-SA")
os.system("cd;cd T-SA;cp -rf TECLADO-SA /data/data/com.termux/files/home;cd;cd TECLADO-SA;toilet --g -f slant updated;python2 teclado-sa.py")
sys.exit()
