#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, subprocess, os, shutil
import commands
import urllib

class interaction():
    def __init__(self):
        print "Interaction class"
    def GetUrl(self,url):
        salida = self.EjecutarComando1("--no-gui %s" % url)
        
        print "salida:",salida
        if salida == "No se ha encontrado el archivo :(":
            print "Qué lástima, hay un error"
            return [False,"",None]
        else:
            print "va todo bien"
            basename , extension = os.path.splitext(salida)
            return [True,salida,extension]
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
    def DescargarUrl(self,url,nombre = "",destino = "",rutafinal = ""):
        print "Descarga un archivo desde una URL especificada"
        if nombre == "" and destino == "" and rutafinal == "":
            print "Caso 1"
            descarga = urllib.urlretrieve(url)
        elif nombre != "" and destino != "" and rutafinal == "":
            print "caso 2"
            ruta = destino+"/"+nombre
            descarga = urllib.urlretrieve(url, filename = ruta)
        elif rutafinal != "":
            print "caso 3"
            descarga = urllib.urlretrieve(url, filename = rutafinal)
        else:
            print "caso 4"
            descarga = urllib.urlretrieve(url)
        print "Descarga: ",descarga
        basename , extension = os.path.splitext(descarga[0])
        print "Extensión: ",extension
        return [descarga[0],extension]

def separarext(self,ruta):
    base , ext = os.path.splitext(ruta)
    return ext
        
        
