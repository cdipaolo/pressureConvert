#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

try:
    import wx
except ImportError:
    raise ImportError,"The wxPython module is required to run this program"


class simpleapp_wx(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.initialize()

    def initialize(self):
        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(3, 3, 9, 25)

        fromText = wx.StaticText(panel, label="From")
        toText = wx.StaticText(panel, label="To")

        fromEnter = wx.TextCtrl(panel)
        toEnter = wx.TextCtrl(panel)
        


        fgs.AddMany([(fromText), (wx.StaticText(panel),1,wx.EXPAND), (toText), 
            (fromEnter, 1, wx.EXPAND), (wx.StaticText(panel, label="=")), (toEnter, 1, wx.EXPAND),
            (wx.StaticText(panel),1,wx.EXPAND),(wx.StaticText(panel),1,wx.EXPAND),(wx.StaticText(panel),1,wx.EXPAND)])

        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)
        self.Show(True)

    '''def OnButtonClick(self,event):
        self.label.SetLabel( self.entry.GetValue() + " (You clicked the button)" )
        self.entry.SetFocus()
        self.entry.SetSelection(-1,-1)

    def OnPressEnter(self,event):
        self.label.SetLabel( self.entry.GetValue() + " (You pressed ENTER)" )
        self.entry.SetFocus()
        self.entry.SetSelection(-1,-1)'''

if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'Pressure Convert')
    app.MainLoop()