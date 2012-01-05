#!/usr/bin/python
# -*- coding: utf-8 -*-
from sherlockdownloader import interaction
download = interaction.interaction().DescargarUrl("http://localhost/index-1.html")
print "la extensión es:",download[1]
