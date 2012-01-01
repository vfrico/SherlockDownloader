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
        
        signals = {"download_clicked": self.download,
                "descifrar_clicked" : self.descifrar,
                "about_activate" : self.showabout,
                "main_close" : self.cerrarapp}

        self.builder.connect_signals(signals)
        if(self.window1):
            self.window1.connect("destroy", self.cerrarapp)
    def cerrarapp(self,widget):
        print "Closing program"
        Gtk.main_quit()

    def descifrar(self,widget):
        print "Descifrando"
        self.geturl = self.builder.get_object("entryurl")
        self.seturl = self.builder.get_object("exiturl")
        url = self.geturl.get_text()
        descifrado = interaction.interaction().GetUrl(url)
        if descifrado[0]:
            self.seturl.set_text(descifrado[1])
        else:
            self.seturl.set_text("Ha habido un error")

    def download(self,widget):
        print "Descargar"
        
    def showabout(self,widget):
        print "Acerca de"
        self.aboutwindow = self.builder.get_object("aboutdialog")
        self.aboutwindow.set_version(info.version)
        self.aboutwindow.run()
        self.aboutwindow.hide()
        
    def closeabout(self,widget):
        print "Cerrar about dialog"
        self.aboutwindow.hide()
        
#Ejecucion del programa
if __name__ == '__main__':
    sherlock = Sherlock()
    Gtk.main()   
