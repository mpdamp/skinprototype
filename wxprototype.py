import os
import wx

class MpdAmpMain(wx.Frame):
    """"""
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)

        panel = wx.Panel(self, size=(275,116))

        sizer = wx.BoxSizer(wx.VERTICAL)

        panel.SetSizer(sizer)

        main = wx.Image(os.path.join('base-2.91/main.bmp'), wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        #sbmp = wx.StaticBitmap(panel, wx.ID_ANY, main, size=(275,116))
        #sizer.Add(sbmp, 0, wx.EXPAND|wx.ALL, 1)

        self.Bind(wx.EVT_LEFT_DOWN, self.mouse_left_down, self)
    
    def mouse_left_down(self, event: wx.MouseEvent) -> None:
        print('test')
        print(event)

def main():
    """The main function for MPDCMD"""
    app = wx.App()
    frame = MpdAmpMain(None, title='MpdAmp', size=(275,116), style=wx.NO_BORDER)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()