#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmcaddon,base64
pluginhandle = int(sys.argv[1])
xbox = xbmc.getCondVisibility("System.Platform.xbox")
settings = xbmcaddon.Addon(id='plugin.DASDING')
translation = settings.getLocalizedString
forceViewMode=settings.getSetting("forceViewMode")
if forceViewMode=="true":
forceViewMode=True
else:
forceViewMode=False
viewMode=str(settings.getSetting("viewMode"))
def index():
addDir("Visual Radio","http://mp3-live.dasding.de/dasding_m.m3u',"")
elif mode == 'playAudio':
playAudio(url)
else:
 index()
 
