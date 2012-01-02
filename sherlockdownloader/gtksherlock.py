#!/usr/bin/python
# -*- coding:UTF-8 -*-
#
#       File: gtksherlock.py
#       This script is the main file of the program
#       
#       This file is part of Sherlock Downloader
#       Sherlock Downloader Copyright 2012 Víctor Fernández Rico <vfrico@gmail.com>
#
#       Sherlock Downloader is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       Sherlock Downloader is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from gi.repository import Gtk
from sherlockdownloader import info
from sherlockdownloader import interaction
class Sherlock:
    def __init__(self):
        # Crea la ventana de trabajo Principal y obtiene los objetos en Glade
        self.builder = Gtk.Builder()
        self.builder.add_from_file("/usr/share/sherlock-downloader/sherlock.glade")

        self.window1 = self.builder.get_object("window1")
        self.window1.show()
        self.geturl = self.builder.get_object("entryurl")
        self.seturl = self.builder.get_object("exiturl")
        self.alignement = self.builder.get_object("alignment2")
        self.alignement12 = self.builder.get_object("alignment12")
        self.seturl.hide()
        self.alignement.hide()
        self.alignement12.hide()
        self.newdestination = self.builder.get_object("filechooserbutton1")
        self.dialogdownload = self.builder.get_object("dialogdownload")
        self.downdest = self.builder.get_object("filechooserbutton2")
        
        
        signals = {"download_clicked": self.download,
                "descifrar_clicked" : self.descifrar,
                "about_activate" : self.showabout,
                "main_close" : self.cerrarapp,
                "closedown" : self.descargarvideo,
                "canceldown" : self.cerrarventanadescarga,
                "toggle_descifrar_clicked" : self.togglemostrar,
                "toggle_descargar" : self.toggledownload}

        self.builder.connect_signals(signals)
        if(self.window1):
            self.window1.connect("destroy", self.cerrarapp)
    def cerrarapp(self,widget):
        print "Closing program"
        Gtk.main_quit()
    def togglemostrar(self,widget):
        print "toggle"
        self.toggbut = self.builder.get_object("togglebutton1")
        if self.toggbut.get_active():
            algo = self.descifrar(None)
            print "descifrar" 
            self.seturl.show()
            self.alignement.show()
        elif self.toggbut.get_active() == False:
            self.seturl.hide()
            self.alignement.hide()
        else:
            print "Hay un error"
    def descifrar(self,widget):
        print "Descifrando"
        url = self.geturl.get_text()
        #~ self.seturl.show()
        #~ self.alignement.show()
        descifrado = interaction.interaction().GetUrl(url)
        if descifrado[0]:
            self.seturl.set_text(descifrado[1])
        else:
            self.seturl.set_text("Ha habido un error")
    def toggledownload(self,widget):
        print "toggle download"
        self.toggbut2 = self.builder.get_object("togglebutton2")
        if self.toggbut2.get_active():
            print "descifrar" 
            self.alignement12.show()
            self.download1()
        elif self.toggbut2.get_active() == False:
            self.alignement12.hide()
        else:
            print "Hay un error"
    def download1(self):
        url = interaction.interaction().GetUrl(self.geturl.get_text())
        extension = url[2] #obtiene la extensión, 3ªposicion  de la lista
    def download(self,widget):
        print "Descargar"
        url = interaction.interaction().GetUrl(self.geturl.get_text())
        extension = url[2] #obtiene la extensión, 3ªposicion  de la lista
        self.newnameentry = self.builder.get_object("entry1")
        # Muestra al usuario un ejemplo de descarga con la extensión
        self.newnameentry.set_placeholder_text("mivideo"+str(extension))
        self.dowindow = self.builder.get_object("downwindow")
        self.dowindow.show()
        
        
    def showabout(self,widget):
        print "Acerca de"
        self.aboutwindow = self.builder.get_object("aboutdialog")
        self.aboutwindow.set_version(info.version)
        self.aboutwindow.run()
        self.aboutwindow.hide()
        
    def closeabout(self,widget):
        print "Cerrar about dialog"
        self.aboutwindow.hide()
    def cerrarventanadescarga(self,widget):
        print "Cerrar ventana de descarga"
        self.dowindow.hide()
    
    def descargarvideo(self,widget):
        nombre = self.newnameentry.get_text()
        destino = self.newdestination.get_filename()
        url = interaction.interaction().GetUrl(self.geturl.get_text())
        self.dialogdownload.run()
        self.dialogdownload.hide()
        salida = interaction.interaction().DescargarUrl(url[1],nombre = nombre, destino = destino)
        self.lblfinaldown = self.builder.get_object("lblfinaldown")
        self.lblfinaldown.set_text(salida[0])
        #~ self.dialogdownload.format_secondary_text("El vídeo está siendo descargado en: "+str(salida[0]))
        
        
#Ejecucion del programa
if __name__ == '__main__':
    sherlock = Sherlock()
    Gtk.main()   
