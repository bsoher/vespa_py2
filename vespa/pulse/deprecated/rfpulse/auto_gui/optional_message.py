# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 13:34:33 2019
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
        self.LabelMessage = wx.StaticText(self, wx.ID_ANY, "Message goes here...")
        self.CheckDontShowAgain = wx.CheckBox(self, wx.ID_ANY, "Don't show this message again")
        self.LabelOkCancelPlaceholder = wx.StaticText(self, wx.ID_ANY, "OK and Cancel go here at runtime")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("dialog_1")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.LabelMessage, 0, wx.EXPAND, 0)
        sizer_2.Add(self.CheckDontShowAgain, 0, wx.BOTTOM | wx.TOP, 10)
        sizer_2.Add(self.LabelOkCancelPlaceholder, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyDialog
