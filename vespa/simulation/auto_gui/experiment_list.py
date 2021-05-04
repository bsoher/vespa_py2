# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 13:50:00 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((473, 300))
        self.ListExperiments = wx.ListBox(self, wx.ID_ANY, choices=[], style=0)
        self.ButtonCopy = wx.Button(self, wx.ID_ANY, "Copy List to Clipboard")
        self.ButtonClose = wx.Button(self, wx.ID_CLOSE, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_copy, self.ButtonCopy)
        self.Bind(wx.EVT_BUTTON, self.on_close, self.ButtonClose)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("dialog_1")
        self.SetSize((473, 300))
        self.ButtonClose.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.ListExperiments, 1, wx.ALL | wx.EXPAND, 10)
        sizer_2.Add(self.ButtonCopy, 0, 0, 0)
        sizer_2.Add((20, 20), 1, 0, 0)
        sizer_2.Add(self.ButtonClose, 0, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_copy(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_copy' not implemented!")
        event.Skip()

    def on_close(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_close' not implemented!")
        event.Skip()

# end of class MyDialog
