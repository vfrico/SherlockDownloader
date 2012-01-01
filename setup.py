#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#
#       File: setup.py
#       This script allows install the guallet package with: "sudo python ./setup.py install"
#       
#       This file is part of Guallet.
#       Guallet Copyright 2011 Víctor Fernández Rico <vfrico@gmail.com>
#
#       Guallet is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       Guallet is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import os, shutil
from distutils.core import setup

setup(
    name = "sherlock-downloader",
    version = "0.1-prea",
    license='gpl3',
    author='Ví­ctor Fernández Rico',
    author_email='vfrico@gmail.com',
    description='Programa para llevar la cuenta de mi cartera',
    scripts=["bin/sherlock-downloader"],
    url = "http://www.cambiadeso.es",
    data_files=[("/usr/share/sherlock-downloader/",["src/sherlock.glade","src/sherlockdownloader.svg","src/sherlock-downloader.desktop"])],
    packages=["sherlockdownloader"]
    )
shutil.rmtree("/usr/share/sherlock-downloader/org/")
shutil.copytree("src/org/","/usr/share/sherlock-downloader/org/")
