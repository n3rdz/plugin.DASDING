import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')

url = 'http://mp3-live.dasding.de/dasding_m.m3u'
li = xbmcgui.ListItem(label='Livestream Radio', iconImage='icon.png', thumbnailImage='thumbnail.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)
