import logging
import os
import wx

logging.basicConfig(level=logging.DEBUG)

class Skin():
    """"""
    def __init__(self, path, name):
        self.main = wx.Image(os.path.join(path, name, 'MAIN.BMP'), wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.main_titlebar = wx.Image(os.path.join(path, name, 'TITLEBAR.BMP'), wx.BITMAP_TYPE_BMP).ConvertToBitmap()
    def get_main(self):
        return self.main.GetSubBitmap(wx.Rect(0, 0, 275, 116))
    def get_main_titlebar_active(self):
        return self.main_titlebar.GetSubBitmap(wx.Rect(27, 0, 275, 14))

class MpdAmpMain(wx.Frame):
    """"""
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)

        self.logger = logging.getLogger(type(self).__name__)
        self.logger.debug('__init__()')

        panel = wx.Panel(self, size=(275,116))

        self.skin = Skin(os.curdir, 'base-2.91')


        s_main = wx.StaticBitmap(panel, wx.ID_ANY, self.skin.get_main(), size=(275,116), pos=(0,0))
        s_titlebar = wx.StaticBitmap(panel, wx.ID_ANY, self.skin.get_main_titlebar_active(), size=(275,14), pos=(0,0))

        self.rel_position = None

        s_main.Bind(wx.EVT_LEFT_DOWN, self.mouse_down)
        s_main.Bind(wx.EVT_LEFT_UP, self.mouse_up)
        s_main.Bind(wx.EVT_MOTION, self.mouse_motion)
    
    def mouse_down(self, event: wx.MouseEvent) -> None:
        self.logger.debug('Event position %s' % event.Position)
        self.logger.debug('Frame position %s' % self.Position)
        self.rel_position = event.Position
        event.Skip()

    def mouse_up(self, event: wx.MouseEvent) -> None:
        event.Skip()
        
    def mouse_motion(self, event: wx.MouseEvent) -> None:
        if event.Dragging():
            self.logger.debug('Drag position %s' % event.Position)
            self.SetPosition(self.Position+event.Position-self.rel_position)
        event.Skip()

def main():
    """The main function for MPDCMD"""
    app = wx.App()
    frame = MpdAmpMain(None, title='MpdAmp', size=(275,116), style=wx.NO_BORDER)
    frame.SetPosition((100,100))
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()