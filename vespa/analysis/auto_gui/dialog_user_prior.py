# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 12:14:55 2019
#

import wx
from wx.lib.agw.floatspin import FloatSpin, EVT_FLOATSPIN, FS_LEFT, FS_RIGHT, FS_CENTRE, FS_READONLY

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((1128, 557))
        self.WindowSplitter = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_NOBORDER)
        self.PanelPrior = wx.Panel(self.WindowSplitter, wx.ID_ANY)
        self.PanelLines = wx.Panel(self.PanelPrior, wx.ID_ANY)
        self.LabelPriorLinesPlaceholder = wx.StaticText(self.PanelLines, wx.ID_ANY, "Just a placeholder for prior lines")
        self.ButtonAutoAdd = wx.Button(self.PanelPrior, wx.ID_ANY, "Add Line")
        self.ButtonAutoDelete = wx.Button(self.PanelPrior, wx.ID_ANY, "Delete Selected")
        self.ButtonAutoRestoreDefaults = wx.Button(self.PanelPrior, wx.ID_ANY, "Restore Defaults")
        self.FloatAutoB0RangeStart = FloatSpin(self.PanelPrior, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatAutoB0RangeEnd = FloatSpin(self.PanelPrior, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatAutoPhase0RangeStart = FloatSpin(self.PanelPrior, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatAutoPhase0RangeEnd = FloatSpin(self.PanelPrior, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatAutoPhase1RangeStart = FloatSpin(self.PanelPrior, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatAutoPhase1RangeEnd = FloatSpin(self.PanelPrior, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatAutoPhase1Pivot = FloatSpin(self.PanelPrior, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.PanelPreview = wx.Panel(self.WindowSplitter, wx.ID_ANY)
        self.PanelView = wx.Panel(self.PanelPreview, wx.ID_ANY)
        self.LabelOKCancelPlaceholder = wx.StaticText(self, wx.ID_ANY, "LabelOKCancelPlaceholder")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_add_line, self.ButtonAutoAdd)
        self.Bind(wx.EVT_BUTTON, self.on_delete_line, self.ButtonAutoDelete)
        self.Bind(wx.EVT_BUTTON, self.on_restore_defaults, self.ButtonAutoRestoreDefaults)
        self.Bind( EVT_FLOATSPIN, self.on_auto_b0_range_start, self.FloatAutoB0RangeStart)
        self.Bind( EVT_FLOATSPIN, self.on_auto_b0_range_end, self.FloatAutoB0RangeEnd)
        self.Bind( EVT_FLOATSPIN, self.on_auto_phase0_range_start, self.FloatAutoPhase0RangeStart)
        self.Bind( EVT_FLOATSPIN, self.on_auto_phase0_range_end, self.FloatAutoPhase0RangeEnd)
        self.Bind( EVT_FLOATSPIN, self.on_auto_phase1_range_start, self.FloatAutoPhase1RangeStart)
        self.Bind( EVT_FLOATSPIN, self.on_auto_phase1_range_end, self.FloatAutoPhase1RangeEnd)
        self.Bind( EVT_FLOATSPIN, self.on_auto_phase1_pivot, self.FloatAutoPhase1Pivot)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("User-Defined Prior Spectrum for Automatic Phase/B0 Algorithms")
        self.SetSize((1128, 557))
        self.WindowSplitter.SetMinimumPaneSize(20)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17_copy = wx.StaticBoxSizer(wx.StaticBox(self.PanelPreview, wx.ID_ANY, "Preview"), wx.VERTICAL)
        sizer_70 = wx.BoxSizer(wx.VERTICAL)
        sizer_76 = wx.StaticBoxSizer(wx.StaticBox(self.PanelPrior, wx.ID_ANY, "Algorithm Parameters"), wx.VERTICAL)
        grid_sizer_3 = wx.FlexGridSizer(4, 4, 6, 2)
        sizer_12_copy = wx.StaticBoxSizer(wx.StaticBox(self.PanelPrior, wx.ID_ANY, "Model Lines"), wx.VERTICAL)
        sizer_48_copy = wx.BoxSizer(wx.HORIZONTAL)
        LinesGridSizer = wx.FlexGridSizer(1, 5, 5, 5)
        LinesGridSizer.Add(self.LabelPriorLinesPlaceholder, 0, 0, 0)
        LinesGridSizer.Add((0, 0), 0, 0, 0)
        LinesGridSizer.Add((0, 0), 0, 0, 0)
        LinesGridSizer.Add((0, 0), 0, 0, 0)
        LinesGridSizer.Add((0, 0), 0, 0, 0)
        self.PanelLines.SetSizer(LinesGridSizer)
        sizer_12_copy.Add(self.PanelLines, 0, wx.EXPAND, 0)
        sizer_48_copy.Add(self.ButtonAutoAdd, 0, wx.RIGHT, 4)
        sizer_48_copy.Add(self.ButtonAutoDelete, 0, wx.RIGHT, 4)
        sizer_48_copy.Add(self.ButtonAutoRestoreDefaults, 0, 0, 0)
        sizer_12_copy.Add(sizer_48_copy, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        sizer_70.Add(sizer_12_copy, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 8)
        label_27 = wx.StaticText(self.PanelPrior, wx.ID_ANY, "Auto B0 Range [ppm] - Start:")
        grid_sizer_3.Add(label_27, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_3.Add(self.FloatAutoB0RangeStart, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 8)
        label_28 = wx.StaticText(self.PanelPrior, wx.ID_ANY, "End:")
        grid_sizer_3.Add(label_28, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_3.Add(self.FloatAutoB0RangeEnd, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        label_29 = wx.StaticText(self.PanelPrior, wx.ID_ANY, "Auto Phase 0 Range [ppm] - Start:")
        grid_sizer_3.Add(label_29, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_3.Add(self.FloatAutoPhase0RangeStart, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 8)
        label_30 = wx.StaticText(self.PanelPrior, wx.ID_ANY, "End:")
        grid_sizer_3.Add(label_30, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_3.Add(self.FloatAutoPhase0RangeEnd, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        label_31 = wx.StaticText(self.PanelPrior, wx.ID_ANY, "Auto Phase 1 Range [ppm] - Start:")
        grid_sizer_3.Add(label_31, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_3.Add(self.FloatAutoPhase1RangeStart, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 8)
        label_32 = wx.StaticText(self.PanelPrior, wx.ID_ANY, "End:")
        grid_sizer_3.Add(label_32, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_3.Add(self.FloatAutoPhase1RangeEnd, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        label_33 = wx.StaticText(self.PanelPrior, wx.ID_ANY, "Phase 1 Pivot [ppm]:")
        grid_sizer_3.Add(label_33, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_3.Add(self.FloatAutoPhase1Pivot, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 8)
        grid_sizer_3.Add((20, 20), 0, wx.EXPAND, 0)
        grid_sizer_3.Add((20, 20), 0, wx.EXPAND, 0)
        sizer_76.Add(grid_sizer_3, 1, wx.BOTTOM | wx.EXPAND | wx.TOP, 2)
        sizer_70.Add(sizer_76, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 8)
        self.PanelPrior.SetSizer(sizer_70)
        sizer_17_copy.Add(self.PanelView, 1, wx.EXPAND, 0)
        self.PanelPreview.SetSizer(sizer_17_copy)
        self.WindowSplitter.SplitVertically(self.PanelPrior, self.PanelPreview)
        sizer_1.Add(self.WindowSplitter, 1, wx.ALL | wx.EXPAND, 5)
        sizer_2.Add(self.LabelOKCancelPlaceholder, 0, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_add_line(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_add_line' not implemented!")
        event.Skip()

    def on_delete_line(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_delete_line' not implemented!")
        event.Skip()

    def on_restore_defaults(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_restore_defaults' not implemented!")
        event.Skip()

    def on_auto_b0_range_start(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_auto_b0_range_start' not implemented!")
        event.Skip()

    def on_auto_b0_range_end(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_auto_b0_range_end' not implemented!")
        event.Skip()

    def on_auto_phase0_range_start(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_auto_phase0_range_start' not implemented!")
        event.Skip()

    def on_auto_phase0_range_end(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_auto_phase0_range_end' not implemented!")
        event.Skip()

    def on_auto_phase1_range_start(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_auto_phase1_range_start' not implemented!")
        event.Skip()

    def on_auto_phase1_range_end(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_auto_phase1_range_end' not implemented!")
        event.Skip()

    def on_auto_phase1_pivot(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_auto_phase1_pivot' not implemented!")
        event.Skip()

# end of class MyDialog
