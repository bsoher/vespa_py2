# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 12:37:09 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.LabelMessage = wx.StaticText(self, wx.ID_ANY, "Message text goes here")
        self.CopyDetails = wx.Button(self, wx.ID_ANY, "Copy Details to Clipboard")
        self.CheckboxOpenEmail = wx.CheckBox(self, wx.ID_ANY, "Open a new email on copy")
        self.TextDetails = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.HSCROLL | wx.TE_MULTILINE | wx.TE_READONLY)
        self.ButtonDone = wx.Button(self, wx.ID_CANCEL, "Done")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_copy, self.CopyDetails)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("dialog_1")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Details"), wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.LabelMessage, 0, wx.ALL | wx.EXPAND, 10)
        sizer_4.Add(self.CopyDetails, 0, wx.BOTTOM, 10)
        sizer_4.Add(self.CheckboxOpenEmail, 0, wx.LEFT, 10)
        sizer_5.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_5.Add(self.TextDetails, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_5, 1, wx.ALL | wx.EXPAND, 10)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_6.Add(self.ButtonDone, 0, wx.EXPAND, 0)
        sizer_6.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_6, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def on_copy(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_copy' not implemented!")
        event.Skip()

# end of class MyDialog
