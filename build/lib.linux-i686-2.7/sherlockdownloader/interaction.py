#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, subprocess, os, shutil
import commands

class interaction():
    def __init__(self):
        print "Interaction class"
    def GetUrl(self,url):
        salida = self.EjecutarComando1("--no-gui %s" % url)
        print "salida:",salida
        if salida == "No se ha encontrado el archivo :(":
            print "Qué lástima, hay un error"
            return [False,""]
        else:
            print "va todo bien"
            return [True,salida]
    def EjecutarComando1(self,args):
        comando = "cd /usr/share/sherlock-downloader/ && java org.carballude.sherlock.Starter %s" % args
        salida = commands.getoutput(comando)
        return salida
    def EjecutarComando(self,args):
        comando = "cd /usr/share/sherlock-downloader/ && java org.carballude.sherlock.Starter %s" % args
        proceso = subprocess.Popen(comando, shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        lista = []
        while True:
            next_line = proceso.stdout.readline()
            lista.append(next_line)
            print "hola", next_line,"lista:",lista
            sys.stdout.write(next_line)    
            sys.stdout.flush()
            if next_line == '' and proceso.poll() != None:
                break
            return lista
        
