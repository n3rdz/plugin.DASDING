import sys
import xbmcgui
import xbmcplugin
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')
url = 'http://swrdasding-lh.akamaihd.net/i/dasdingvisual_live@6416/master.m3u8'
li = xbmcgui.ListItem(label='HLS Stream Visual Radio', iconImage='icon.png', thumbnailImage='visualradio.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)
