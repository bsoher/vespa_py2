# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 13:38:14 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class PanelKernelGlobals(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PanelKernelGlobals.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.LabelTransformName = wx.StaticText(self, wx.ID_ANY, "Transform Name")
        self.PanelFile1 = wx.Panel(self, wx.ID_ANY)
        self.LabelFile1 = wx.StaticText(self.PanelFile1, wx.ID_ANY, "Label File1")
        self.ButtonBrowseFile1 = wx.Button(self.PanelFile1, wx.ID_ANY, "Browse")
        self.TextFile1 = wx.TextCtrl(self.PanelFile1, wx.ID_ANY, "", style=wx.TE_READONLY)
        self.PanelFile2 = wx.Panel(self, wx.ID_ANY)
        self.LabelFile2 = wx.StaticText(self.PanelFile2, wx.ID_ANY, "Label File2")
        self.ButtonBrowseFile2 = wx.Button(self.PanelFile2, wx.ID_ANY, "Browse")
        self.TextFile2 = wx.TextCtrl(self.PanelFile2, wx.ID_ANY, "", style=wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PanelKernelGlobals.__set_properties
        self.TextFile1.SetMinSize((175, -1))
        self.TextFile2.SetMinSize((175, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PanelKernelGlobals.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.StaticBoxSizer(wx.StaticBox(self.PanelFile2, wx.ID_ANY, "File2 Selection"), wx.VERTICAL)
        grid_sizer_7 = wx.FlexGridSizer(1, 4, 4, 4)
        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self.PanelFile1, wx.ID_ANY, "File1 Selection"), wx.VERTICAL)
        grid_sizer_6 = wx.FlexGridSizer(1, 4, 4, 4)
        sizer_4_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_4_copy.Add(self.LabelTransformName, 0, wx.EXPAND, 0)
        sizer_4.Add(sizer_4_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 6)
        sizer_2.Add(self.LabelFile1, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        grid_sizer_6.Add(self.ButtonBrowseFile1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_6.Add(self.TextFile1, 0, wx.EXPAND, 0)
        grid_sizer_6.AddGrowableCol(1)
        sizer_2.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        self.PanelFile1.SetSizer(sizer_2)
        sizer_4.Add(self.PanelFile1, 0, wx.ALL | wx.EXPAND, 4)
        sizer_3.Add(self.LabelFile2, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.TOP, 4)
        grid_sizer_7.Add(self.ButtonBrowseFile2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_7.Add(self.TextFile2, 0, wx.EXPAND, 0)
        grid_sizer_7.AddGrowableCol(1)
        sizer_3.Add(grid_sizer_7, 1, wx.EXPAND, 0)
        self.PanelFile2.SetSizer(sizer_3)
        sizer_4.Add(self.PanelFile2, 0, wx.ALL | wx.EXPAND, 4)
        self.SetSizer(sizer_4)
        sizer_4.Fit(self)
        self.Layout()
        # end wxGlade

# end of class PanelKernelGlobals

class FrameKernelGlobals(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: FrameKernelGlobals.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.PanelKernelGlobals = PanelKernelGlobals(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: FrameKernelGlobals.__set_properties
        self.SetTitle("frame_transform_core")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: FrameKernelGlobals.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.PanelKernelGlobals, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class FrameKernelGlobals
