import os
import wx

class MpdAmpMain(wx.Frame):
    """"""
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)

        panel = wx.Panel(self, size=(275,116))

        main = wx.Image(os.path.join('base-2.91/main.bmp'), wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        sbmp = wx.StaticBitmap(panel, wx.ID_ANY, main, size=(275,116))

        self.windowpos = None

        sbmp.Bind(wx.EVT_LEFT_DOWN, self.mouse_down)
        sbmp.Bind(wx.EVT_LEFT_UP, self.mouse_up)
        sbmp.Bind(wx.EVT_MOTION, self.mouse_motion)
    
    def mouse_down(self, event: wx.MouseEvent) -> None:
        print(event)

        print(event.Position)
        print(self.Position)
        
        self.windowpos = event.Position
        event.Skip()

    def mouse_up(self, event: wx.MouseEvent) -> None:
        print(event)
        self.windowpos = None
        event.Skip()
        
    def mouse_motion(self, event: wx.MouseEvent) -> None:
        if event.Dragging():
            print(event.Position)
            #self.SetPosition()
        event.Skip()

def main():
    """The main function for MPDCMD"""
    app = wx.App()
    frame = MpdAmpMain(None, title='MpdAmp', size=(275,116), style=wx.NO_BORDER)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()