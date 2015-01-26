import sys
import xbmcgui
import xbmcplugin
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://swrdasding-lh.akamaihd.net/i/dasdingvisual_live@6416/master.m3u8'
li = xbmcgui.ListItem(label='DASDING Visual Radio HLS Stream m3u8')
li.setIconImage('DefaultVideo.png')
li.setThumbnailImage('icon.png')
li.setProperty('fanart_image', 'visualradio.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://swrdasding-lh.akamaihd.net/z/dasdingvisual_live@6416/manifest.f4m'
li = xbmcgui.ListItem(label='DASDING Visual Radio HDS Stream f4m')
li.setProperty('fanart_image', 'visualradio.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://mp3-live.dasding.de/dasding_m.m3u'
li = xbmcgui.ListItem(label='DASDING Radio Livestream 128kbit m3u')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://swr.ic.llnwd.net:80/stream/swr_mps_m_dasdinga'
li = xbmcgui.ListItem(label='DASDING Radio 5.1 Surround Livestream')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://mp3-live.dasding.de/dasdingraka01_m.m3u'
li = xbmcgui.ListItem(label='Lautstark nachhören 128kbit m3u')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://mp3-live.dasding.de/dasdingraka02_m.m3u'
li = xbmcgui.ListItem(label='Sprechstunde nachhören 128kbit m3u')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://mp3-live.dasding.de/dasdingraka03_m.m3u'
li = xbmcgui.ListItem(label='Plattenleger nachhören 128kbit m3u')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)
