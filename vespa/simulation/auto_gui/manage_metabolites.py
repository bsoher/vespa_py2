# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 13:50:24 2019
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
        self.label_2 = wx.StaticText(self, wx.ID_ANY, "Isotope:")
        self.ComboIsotope = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.CheckboxShowDeactivated = wx.CheckBox(self, wx.ID_ANY, "Show deactivated")
        self.ButtonNew = wx.Button(self, wx.ID_NEW, "&New...")
        self.ButtonEdit = wx.Button(self, wx.ID_EDIT, "&Edit...")
        self.ButtonView = wx.Button(self, wx.ID_ANY, "&View...")
        self.ButtonClone = wx.Button(self, wx.ID_ANY, "C&lone")
        self.ButtonDeactivate = wx.Button(self, wx.ID_ANY, "(De)ac&tivate")
        self.ButtonDelete = wx.Button(self, wx.ID_DELETE, "")
        self.ListMetabolites = wx.ListCtrl(self, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_REPORT)
        self.ButtonImport = wx.Button(self, wx.ID_ANY, "&Import...")
        self.ButtonExport = wx.Button(self, wx.ID_ANY, "E&xport...")
        self.ButtonClose = wx.Button(self, wx.ID_CLOSE, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_isotope, self.ComboIsotope)
        self.Bind(wx.EVT_CHECKBOX, self.on_show_deactivated, self.CheckboxShowDeactivated)
        self.Bind(wx.EVT_BUTTON, self.on_new, self.ButtonNew)
        self.Bind(wx.EVT_BUTTON, self.on_edit, self.ButtonEdit)
        self.Bind(wx.EVT_BUTTON, self.on_view, self.ButtonView)
        self.Bind(wx.EVT_BUTTON, self.on_clone, self.ButtonClone)
        self.Bind(wx.EVT_BUTTON, self.on_deactivate, self.ButtonDeactivate)
        self.Bind(wx.EVT_BUTTON, self.on_delete, self.ButtonDelete)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_metabolite_activated, self.ListMetabolites)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.on_metabolite_selection_change, self.ListMetabolites)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_metabolite_selection_change, self.ListMetabolites)
        self.Bind(wx.EVT_BUTTON, self.on_import, self.ButtonImport)
        self.Bind(wx.EVT_BUTTON, self.on_export, self.ButtonExport)
        self.Bind(wx.EVT_BUTTON, self.on_close, self.ButtonClose)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("Manage Metabolites")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(3, 2, 10, 0)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2_copy = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        sizer_2_copy.Add(self.label_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
        sizer_2_copy.Add(self.ComboIsotope, 0, 0, 0)
        sizer_2.Add(sizer_2_copy, 1, wx.EXPAND, 0)
        sizer_2.Add(self.CheckboxShowDeactivated, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_5.Add(self.ButtonNew, 0, 0, 0)
        sizer_5.Add(self.ButtonEdit, 0, wx.TOP, 5)
        sizer_5.Add(self.ButtonView, 0, wx.TOP, 5)
        sizer_5.Add(self.ButtonClone, 0, wx.TOP, 5)
        sizer_5.Add(self.ButtonDeactivate, 0, wx.TOP, 5)
        sizer_5.Add(self.ButtonDelete, 0, wx.TOP, 30)
        grid_sizer_1.Add(sizer_5, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        grid_sizer_1.Add(self.ListMetabolites, 1, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        sizer_6.Add(self.ButtonImport, 0, 0, 0)
        sizer_6.Add(self.ButtonExport, 0, wx.LEFT, 10)
        sizer_6.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_6.Add(self.ButtonClose, 0, 0, 0)
        grid_sizer_1.Add(sizer_6, 1, wx.BOTTOM | wx.EXPAND, 10)
        grid_sizer_1.AddGrowableRow(1)
        grid_sizer_1.AddGrowableCol(1)
        sizer_4.Add(grid_sizer_1, 1, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer_4)
        sizer_4.Fit(self)
        self.Layout()
        # end wxGlade

    def on_isotope(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_isotope' not implemented!")
        event.Skip()

    def on_show_deactivated(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_show_deactivated' not implemented!")
        event.Skip()

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

    def on_deactivate(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_deactivate' not implemented!")
        event.Skip()

    def on_delete(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_delete' not implemented!")
        event.Skip()

    def on_metabolite_activated(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_metabolite_activated' not implemented!")
        event.Skip()

    def on_metabolite_selection_change(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_metabolite_selection_change' not implemented!")
        event.Skip()

    def on_import(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_import' not implemented!")
        event.Skip()

    def on_export(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_export' not implemented!")
        event.Skip()

    def on_close(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_close' not implemented!")
        event.Skip()

# end of class MyDialog
