#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade HG on Wed Aug 15 15:07:16 2012

import wx

import vespa.common.wx_gravy.util
from wx.lib.agw.floatspin import FloatSpin, EVT_FLOATSPIN, FS_LEFT, FS_RIGHT, FS_CENTRE, FS_READONLY

# begin wxGlade: extracode
# end wxGlade


class WaterFirUI(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: WaterFirUI.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.SpinLength = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=100, style=wx.SP_ARROW_KEYS | wx.TE_AUTO_URL)
        self.SpinFirWidth = FloatSpin(self, wx.ID_ANY, style=wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER|wx.TE_AUTO_URL, agwStyle=FS_LEFT)
        self.SpinFirRipple = FloatSpin(self, wx.ID_ANY, style=wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER|wx.TE_AUTO_URL, agwStyle=FS_LEFT)
        self.ComboExtrap = wx.ComboBox(self, wx.ID_ANY, choices=["None", "Linear", "AR Model"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.SpinExtrap = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=100, style=wx.SP_ARROW_KEYS | wx.TE_AUTO_URL)

        self.__set_properties()
        self.__do_layout()

        self.Bind(EVT_FLOATSPIN, self.on_fir_width, self.SpinFirWidth)
        self.Bind(EVT_FLOATSPIN, self.on_fir_ripple, self.SpinFirRipple)
        self.Bind(wx.EVT_COMBOBOX, self.on_extrapolate_method, self.ComboExtrap)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: WaterFirUI.__set_properties
        self.SpinLength.SetMinSize((60, -1))
        self.SpinFirWidth.SetMinSize((80, -1))
        self.SpinFirRipple.SetMinSize((80, -1))
        self.ComboExtrap.SetSelection(1)
        self.SpinExtrap.SetMinSize((60, -1))
        self.SpinExtrap.SetSize((40,-1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: WaterFirUI.__do_layout
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        Length = wx.StaticText(self, wx.ID_ANY, "Filter Length:")
        sizer_3.Add(Length, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_3.Add(self.SpinLength, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_15.Add(sizer_3, 1, wx.ALIGN_RIGHT, 0)
        LabelFirWidth = wx.StaticText(self, wx.ID_ANY, "FIR 1/2 Width: ")
        sizer_4.Add(LabelFirWidth, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_4.Add(self.SpinFirWidth, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        LabelFirRipple = wx.StaticText(self, wx.ID_ANY, "FIR Ripple [dB]: ")
        sizer_4.Add(LabelFirRipple, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_4.Add(self.SpinFirRipple, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_15.Add(sizer_4, 1, wx.ALIGN_RIGHT, 0)
        LabelExtrapolation = wx.StaticText(self, wx.ID_ANY, "Extrapolation: ")
        sizer_5.Add(LabelExtrapolation, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_5.Add(self.ComboExtrap, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 3)
        LabelExtrap = wx.StaticText(self, wx.ID_ANY, "    Extrap Pts:")
        sizer_5.Add(LabelExtrap, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_5.Add(self.SpinExtrap, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_15.Add(sizer_5, 1, wx.ALIGN_RIGHT, 0)
        self.SetSizer(sizer_15)
        sizer_15.Fit(self)
        # end wxGlade

    def on_fir_width(self, event):  # wxGlade: WaterFirUI.<event_handler>
        print "Event handler `on_fir_width' not implemented!"
        event.Skip()

    def on_fir_ripple(self, event):  # wxGlade: WaterFirUI.<event_handler>
        print "Event handler `on_fir_ripple' not implemented!"
        event.Skip()

    def on_extrapolate_method(self, event):  # wxGlade: WaterFirUI.<event_handler>
        print "Event handler `on_extrapolate_method' not implemented!"
        event.Skip()

# end of class WaterFirUI

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.WaterFirUI = WaterFirUI(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.WaterFirUI, 0, wx.EXPAND | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
