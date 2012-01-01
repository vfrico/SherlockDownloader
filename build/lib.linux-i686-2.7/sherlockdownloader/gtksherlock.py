#!/usr/bin/python
# -*- coding: utf-8 -*-
from gi.repository import Gtk

class Sherlock():

    def __init__(self):
        self.window = Gtk.Window()
        self.window.connect("delete-event", Gtk.main_quit)
        self.window.set_size_request(400, 200)
        
        self.vbox = Gtk.VBox(homogeneous = True , spacing = 0)
        # Creates a new MenuBar, for display menus
        self.menubar = Gtk.MenuBar()

        # Creating File menu
        self.menufile = Gtk.Menu()
        self.menu_file = Gtk.MenuItem(label = "File")
        self.menu_file.set_submenu(self.menufile)
        
        # Creating Help menu 
        self.menuhelp = Gtk.Menu()
        self.menu_help = Gtk.MenuItem(label = "Help")
        self.menu_help.set_submenu(self.menuhelp)
        
        # Quit item on file menu
        self.quit_menuitem = Gtk.ImageMenuItem.new_with_label("Quit")
        self.quit_menuitem.set_image(Gtk.Image.new_from_stock(Gtk.STOCK_QUIT, Gtk.IconSize.MENU))
        self.quit_menuitem.set_always_show_image(True)
        self.quit_menuitem.show()
        self.quit_menuitem.connect("activate",self.quitprogram)
        # Append quit item to file menu
        self.menufile.append(self.quit_menuitem)
        
        # About item on Help menu
        self.about_menuitem = Gtk.ImageMenuItem.new_with_label("About")
        self.about_menuitem.set_image(Gtk.Image.new_from_stock(Gtk.STOCK_ABOUT, Gtk.IconSize.MENU))
        self.about_menuitem.set_always_show_image(True)
        self.about_menuitem.show()
        self.about_menuitem.connect("activate",self.aboutwindow)
        # Append about item to help menu
        self.menuhelp.append(self.about_menuitem)
        
        # Append menu file to menu bar
        self.menubar.append(self.menu_file)
        self.menubar.append(self.menu_help)
        
        
        
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.vbox.pack_start(self.menubar, expand=True , fill=True , padding = 0)
        self.vbox.pack_start(self.button, expand=True , fill=True , padding = 0)
        
        self.window.add(self.vbox)
        self.window.show_all()

    def on_button_clicked(self, widget):
        print "Hello World"
    
    def aboutwindow(self,widget):
        print "About window"
        
    def quitprogram(self,widget):
        print "Quit"
        Gtk.main_quit()
