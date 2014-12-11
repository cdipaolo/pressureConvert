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

        ## Conversion Factors using "From_To" as key to multiply by
        self.conversionFactors = {"psi_psi":1,"bar_psi":14.504,"atm_psi":14.7,"Pa_psi":.000145,"mmHg_psi":.01934,
                                "psi_bar":.0689,"bar_bar":1,"atm_bar":1.01325,"Pa_bar":.00001,"mmHg_bar":.001333,
                                "psi_atm":.0681,"bar_atm":.987,"atm_atm":1,"Pa_atm":.00001,"mmHg_atm":.001316,
                                "psi_Pa":6895,"bar_Pa":100000,"atm_Pa":101325,"Pa_Pa":1,"mmHg_Pa":133.3,
                                "psi_mmHg":51.715,"bar_mmHg":750.1,"atm_mmHg":760,"Pa_mmHg":.0075,"mmHg_mmHg":1}

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