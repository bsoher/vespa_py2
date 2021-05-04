# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 13:40:10 2019
#

import wx
from wx.lib.agw.floatspin import FloatSpin, EVT_FLOATSPIN, FS_LEFT, FS_RIGHT, FS_CENTRE, FS_READONLY

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class PanelRootReflect(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PanelRootReflect.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.ComboPlotSelection = wx.ComboBox(self, wx.ID_ANY, choices=["A Polynomial Roots", "A+B Polynomial Roots"], style=wx.CB_READONLY)
        self.ButtonResetRoots = wx.Button(self, wx.ID_ANY, "Reset Roots")
        self.FloatMaxRadius = FloatSpin(self, wx.ID_ANY, value=2.0, digits=2, min_val=0.0, max_val=100.0, increment=0.25, agwStyle=FS_LEFT, style=0)
        self.FloatGraphAngle = FloatSpin(self, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.PanelPlotSection = wx.Panel(self, wx.ID_ANY)
        self.CheckAutoUpdate = wx.CheckBox(self, wx.ID_ANY, "Automatic Update")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_plot_selection, self.ComboPlotSelection)
        self.Bind(wx.EVT_BUTTON, self.on_reset_roots, self.ButtonResetRoots)
        self.Bind( EVT_FLOATSPIN, self.on_max_radius, self.FloatMaxRadius)
        self.Bind( EVT_FLOATSPIN, self.on_graph_angle, self.FloatGraphAngle)
        self.Bind(wx.EVT_CHECKBOX, self.on_auto_update, self.CheckAutoUpdate)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PanelRootReflect.__set_properties
        self.ComboPlotSelection.SetSelection(0)
        self.CheckAutoUpdate.SetValue(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PanelRootReflect.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Root Reflection Tranformation (for B1 Pulses only)")
        sizer_4.Add(label_1, 0, wx.ALIGN_CENTER | wx.ALL, 8)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Plot Display")
        sizer_7.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        sizer_7.Add(self.ComboPlotSelection, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_7.Add(self.ButtonResetRoots, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        sizer_4.Add(sizer_7, 0, wx.ALL | wx.EXPAND, 3)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Max Radius")
        sizer_1.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 4)
        sizer_1.Add(self.FloatMaxRadius, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, "Graph Angle")
        sizer_1.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 9)
        sizer_1.Add(self.FloatGraphAngle, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT | wx.RIGHT, 4)
        sizer_4.Add(sizer_1, 0, wx.ALL | wx.EXPAND, 3)
        sizer_4.Add(self.PanelPlotSection, 1, wx.EXPAND, 0)
        sizer_5.Add(self.CheckAutoUpdate, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 6)
        sizer_4.Add(sizer_5, 0, wx.ALIGN_CENTER | wx.ALL, 9)
        self.SetSizer(sizer_4)
        sizer_4.Fit(self)
        self.Layout()
        # end wxGlade

    def on_plot_selection(self, event):  # wxGlade: PanelRootReflect.<event_handler>
        print("Event handler 'on_plot_selection' not implemented!")
        event.Skip()

    def on_reset_roots(self, event):  # wxGlade: PanelRootReflect.<event_handler>
        print("Event handler 'on_reset_roots' not implemented!")
        event.Skip()

    def on_max_radius(self, event):  # wxGlade: PanelRootReflect.<event_handler>
        print("Event handler 'on_max_radius' not implemented!")
        event.Skip()

    def on_graph_angle(self, event):  # wxGlade: PanelRootReflect.<event_handler>
        print("Event handler 'on_graph_angle' not implemented!")
        event.Skip()

    def on_auto_update(self, event):  # wxGlade: PanelRootReflect.<event_handler>
        print("Event handler 'on_auto_update' not implemented!")
        event.Skip()

# end of class PanelRootReflect

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.PanelRootReflect = PanelRootReflect(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.PanelRootReflect, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame
