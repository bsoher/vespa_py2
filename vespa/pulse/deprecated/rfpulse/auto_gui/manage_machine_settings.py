# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 13:32:54 2019
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
        self.ButtonNew = wx.Button(self, wx.ID_ANY, "New...")
        self.ButtonEdit = wx.Button(self, wx.ID_ANY, "Edit...")
        self.ButtonView = wx.Button(self, wx.ID_ANY, "&View...")
        self.ButtonClone = wx.Button(self, wx.ID_ANY, "C&lone")
        self.ButtonDefault = wx.Button(self, wx.ID_ANY, "Default")
        self.ButtonDelete = wx.Button(self, wx.ID_DELETE, "")
        self.ListMachineSettings = wx.ListCtrl(self, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_REPORT)
        self.ButtonClose = wx.Button(self, wx.ID_CLOSE, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_new, self.ButtonNew)
        self.Bind(wx.EVT_BUTTON, self.on_edit, self.ButtonEdit)
        self.Bind(wx.EVT_BUTTON, self.on_view, self.ButtonView)
        self.Bind(wx.EVT_BUTTON, self.on_clone, self.ButtonClone)
        self.Bind(wx.EVT_BUTTON, self.on_default, self.ButtonDefault)
        self.Bind(wx.EVT_BUTTON, self.on_delete, self.ButtonDelete)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_template_activated, self.ListMachineSettings)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.on_selection_changed, self.ListMachineSettings)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_selection_changed, self.ListMachineSettings)
        self.Bind(wx.EVT_BUTTON, self.on_close, self.ButtonClose)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("Manage Machine Settings Templates")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 2, 10, 0)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(self.ButtonNew, 0, wx.TOP, 5)
        sizer_5.Add(self.ButtonEdit, 0, wx.TOP, 5)
        sizer_5.Add(self.ButtonView, 0, wx.TOP, 5)
        sizer_5.Add(self.ButtonClone, 0, wx.TOP, 5)
        sizer_5.Add(self.ButtonDefault, 0, wx.TOP, 5)
        sizer_5.Add(self.ButtonDelete, 0, wx.TOP, 30)
        grid_sizer_1.Add(sizer_5, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        grid_sizer_1.Add(self.ListMachineSettings, 1, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        sizer_6.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_6.Add(self.ButtonClose, 0, 0, 0)
        grid_sizer_1.Add(sizer_6, 0, wx.BOTTOM | wx.EXPAND, 10)
        grid_sizer_1.AddGrowableRow(0)
        grid_sizer_1.AddGrowableCol(1)
        sizer_4.Add(grid_sizer_1, 1, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer_4)
        sizer_4.Fit(self)
        self.Layout()
        # end wxGlade

    def on_new(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_new' not implemented!")
        event.Skip()

    def on_edit(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_edit' not implemented!")
        event.Skip()

    def on_view(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_view' not implemented!")
        event.Skip()

    def on_clone(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_clone' not implemented!")
        event.Skip()

    def on_default(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_default' not implemented!")
        event.Skip()

    def on_delete(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_delete' not implemented!")
        event.Skip()

    def on_template_activated(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_template_activated' not implemented!")
        event.Skip()

    def on_selection_changed(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_selection_changed' not implemented!")
        event.Skip()

    def on_close(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_close' not implemented!")
        event.Skip()

# end of class MyDialog
