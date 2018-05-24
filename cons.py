
import numpy as np
import pandas as pd 
import time
import random
import sys
import matplotlib.pyplot as plt
import os

w = 50
h = 30
title = 'folder'
strs = []


def printkrasivo(s):
	s = printwithotstup(s)
	s = s + '\n'
	strtoprint = ''
	for i in s:
		strtoprint = strtoprint + str(i)
		sys.stdout.write('\r\r' + (strtoprint) + '')
		#time.sleep(0.01)
		if i != ' ':
			time.sleep(0.005)
		else:
			pass


def printwithotstup(s):
	otstup = (w - len(s)) // 2
	return(otstup * ' ' + s)


def gengran():
	strs[0] = '╔' + ('═' * (w - 2)) + '╗'
	strs[h - 1] = '╚' + ('═' * (w - 2)) + '╝'
	for i in range(1, h - 1):
		strs[i] = '║' + (' ' * (w - 2)) + '║'
	strs[2] = '╠' + ('═' * (w - 2)) + '╣'
	strs[1] = '║' + '  ' + title + (' ' * (w - (len(title) + 4))) +'║'


def genstr(s):
	strr = '║' + '  ' + s + (' ' * (w - (len(s) + 4))) +'║'
	return strr


def initlist():
	s = []
	for i in range(0, h):
		s.append('')
	return s


def info():
	printkrasivo('     _             _ _ ')
	printkrasivo('  __| | __ _ _ __ (_) |')
	printkrasivo(' / _` |/ _` | "_ \| | |')
	printkrasivo('| (_| | (_| | | | | | |')
	printkrasivo(' \__,_|\__,_|_| |_|_|_|')
	printkrasivo('                                _   ')
	printkrasivo(' _ __  _ __ ___  ___  ___ _ __ | |_ ')
	printkrasivo('| "_ \| "__/ _ \/ __|/ _ \ "_ \| __|')
	printkrasivo('| |_) | | |  __/\__ \  __/ | | | |_ ')
	printkrasivo('| .__/|_|  \___||___/\___|_| |_|\__|')
	printkrasivo('|_|                                 ')
	input()


def main():
	global strs
	strs = initlist()
	while True:
		os.system('cls')
		printkrasivo('          ')
		printkrasivo('DESKTOP')
		printkrasivo('          ')
		printkrasivo('╔════════╗')
		printkrasivo('║        ║')
		printkrasivo('║ folder ║')
		printkrasivo('║   №1   ║')
		printkrasivo('║        ║')
		printkrasivo('║        ║')
		printkrasivo('╚════════╝')
		printkrasivo('          ')
		printkrasivo('          ')
		printkrasivo('comands:folder number')
		starter1 = input(printwithotstup('Input your folder: '))
		if starter1 == 'folder 1':
			os.system('cls')
			f1 = open('name.txt', 'r')
			l1 = []       
			for i in f1:
				l1.append(i)
			l1 = [line.rstrip() for line in l1]
			title = 'folder№1'
			os.system('cls')
			gengran()
			strs[3] = genstr(l1[0])
			for i in strs:
				printkrasivo(i)	
		vibor1 = str(input('comands:info,exit,open file name >>'))	
		if vibor1 == 'exit':
			os.system('cls')
			pass
		if vibor1 == 'open file t.txt':
			os.system('cls')
			f = open('t.txt', 'r')
			l = []
			for i in f:
				l.append(i)
			l = [line.rstrip() for line in l]
			os.system('cls')
			title = 'folder№1'
			gengran()
			strs[3] = genstr(l[0])
			for i in strs:
				printkrasivo(i)
			vibor2 = str(input('comands:exit >>'))
			if vibor2 == 'exit':
				pass
		if vibor1 == 'info':
			os.system('cls')
			info()
			os.system('cls')


if __name__ == '__main__':
	main()