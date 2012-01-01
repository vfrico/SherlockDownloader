#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, subprocess, os, shutil

class interaction():
	def __init__(self):
		print "Interaction class"
	def geturl(self,url):
		None
	def EjecutarComando(self,comando):
        proceso = subprocess.Popen(comando, shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        while True:
            next_line = proceso.stdout.readline()
            sys.stdout.write(next_line)    
            sys.stdout.flush()
            if next_line == '' and proceso.poll() != None:
                break	
            return next_line
