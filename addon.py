import sys
import xbmcgui
import xbmcplugin
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://swrdasding-lh.akamaihd.net/i/dasdingvisual_live@6416/master.m3u8'
li = xbmcgui.ListItem(label='DASDING Visual Radio Stream')
li.setIconImage('DefaultVideo.png')
li.setThumbnailImage('icon.png')
li.setProperty('fanart_image', 'visualradio.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)
