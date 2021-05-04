# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 12:27:30 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class PanelRawUI(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PanelRawUI.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.WindowSplitter = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
        self.PanelRaw = wx.Panel(self.WindowSplitter, wx.ID_ANY)
        self.ListDataSources = wx.ListBox(self.PanelRaw, wx.ID_ANY, choices=[], style=wx.LB_HSCROLL | wx.LB_NEEDED_SB | wx.LB_SINGLE)
        self.window_1_pane_2 = wx.Panel(self.WindowSplitter, wx.ID_ANY)
        self.TextHeaderInformationDisplay = wx.TextCtrl(self.window_1_pane_2, wx.ID_ANY, "", style=wx.HSCROLL | wx.TE_MULTILINE | wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LISTBOX, self.on_list_item_select, self.ListDataSources)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.on_list_double_click, self.ListDataSources)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PanelRawUI.__set_properties
        self.WindowSplitter.SetMinimumPaneSize(20)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PanelRawUI.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.StaticBoxSizer(wx.StaticBox(self.window_1_pane_2, wx.ID_ANY, "Header Information"), wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.StaticBoxSizer(wx.StaticBox(self.PanelRaw, wx.ID_ANY, "Data Sources"), wx.VERTICAL)
        sizer_1.Add(self.ListDataSources, 1, wx.EXPAND, 0)
        sizer_6.Add(sizer_1, 1, wx.EXPAND, 0)
        self.PanelRaw.SetSizer(sizer_6)
        sizer_4.Add(self.TextHeaderInformationDisplay, 1, wx.EXPAND, 0)
        self.window_1_pane_2.SetSizer(sizer_4)
        self.WindowSplitter.SplitVertically(self.PanelRaw, self.window_1_pane_2)
        sizer_3.Add(self.WindowSplitter, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

    def on_list_item_select(self, event):  # wxGlade: PanelRawUI.<event_handler>
        print("Event handler 'on_list_item_select' not implemented!")
        event.Skip()

    def on_list_double_click(self, event):  # wxGlade: PanelRawUI.<event_handler>
        print("Event handler 'on_list_double_click' not implemented!")
        event.Skip()

# end of class PanelRawUI

class MyFrame1(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.PanelRawUI = PanelRawUI(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame1.__set_properties
        self.SetTitle("frame_2")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame1.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.PanelRawUI, 1, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame1