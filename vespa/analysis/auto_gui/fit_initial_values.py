# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 12:16:47 2019
#

import wx
from wx.lib.agw.floatspin import FloatSpin, EVT_FLOATSPIN, FS_LEFT, FS_RIGHT, FS_CENTRE, FS_READONLY

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class PanelInitialValues(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PanelInitialValues.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.ComboInitialB0ShiftMethod = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_READONLY)
        self.FloatB0ShiftValue = FloatSpin(self, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.ComboInitialBaselineMethod = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_READONLY)
        self.PanelBaselineInitLowess = wx.Panel(self, wx.ID_ANY)
        self.FloatBaselineInitIgnoreWidth = FloatSpin(self.PanelBaselineInitLowess, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatInitialBaselineLowessWidth = FloatSpin(self.PanelBaselineInitLowess, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.CheckInitialPeakSearchAbs = wx.CheckBox(self, wx.ID_ANY, " Area from abs(Real) data")
        self.ComboInitialSmallPeakAreas = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_READONLY)
        self.CheckInitialCrChoSeparation = wx.CheckBox(self, wx.ID_ANY, " Cho/Cr 0.2 PPM separation")
        self.ComboInitialSmallPeakFreqs = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_READONLY)
        self.ComboInitialLinewidthMethod = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_READONLY)
        self.FloatLinewidthValue = FloatSpin(self, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.PanelInitialLinewidth = wx.Panel(self, wx.ID_ANY)
        self.FloatInitialLinewidthStart = FloatSpin(self.PanelInitialLinewidth, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatInitialLinewidthEnd = FloatSpin(self.PanelInitialLinewidth, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatInitialLinewidthMultiplier = FloatSpin(self.PanelInitialLinewidth, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=0.1, agwStyle=FS_LEFT, style=0)
        self.ComboInitialPhaseMethod = wx.ComboBox(self, wx.ID_ANY, choices=["Manual", "Correlation - Phase0 only", "Correlation - Phase0+Phase1", "Integration - Phase0 only", "Integration - Phase0+Phase1"], style=wx.CB_READONLY)
        self.FloatInitialPhase0Value = FloatSpin(self, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatInitialPhase1Value = FloatSpin(self, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.PanelKOFilter = wx.Panel(self, wx.ID_ANY)
        self.CheckApplyKoFilter = wx.CheckBox(self.PanelKOFilter, wx.ID_ANY, " Apply Filter ")
        self.SpinInitialKOLinewidthMinimum = wx.SpinCtrl(self.PanelKOFilter, wx.ID_ANY, "", min=0, max=100)
        self.SpinInitialKOPoints = wx.SpinCtrl(self.PanelKOFilter, wx.ID_ANY, "", min=0, max=100)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_b0_shift_method, self.ComboInitialB0ShiftMethod)
        self.Bind( EVT_FLOATSPIN, self.on_b0_shift_value, self.FloatB0ShiftValue)
        self.Bind(wx.EVT_COMBOBOX, self.on_initial_baseline_method, self.ComboInitialBaselineMethod)
        self.Bind( EVT_FLOATSPIN, self.on_initial_baseline_ignore_width, self.FloatBaselineInitIgnoreWidth)
        self.Bind( EVT_FLOATSPIN, self.on_initial_baseline_lowess_width, self.FloatInitialBaselineLowessWidth)
        self.Bind(wx.EVT_CHECKBOX, self.on_initial_peak_search_abs, self.CheckInitialPeakSearchAbs)
        self.Bind(wx.EVT_COMBOBOX, self.on_initial_small_peak_areas, self.ComboInitialSmallPeakAreas)
        self.Bind(wx.EVT_CHECKBOX, self.on_initial_cr_cho_separation, self.CheckInitialCrChoSeparation)
        self.Bind(wx.EVT_COMBOBOX, self.on_initial_small_peak_freqs, self.ComboInitialSmallPeakFreqs)
        self.Bind(wx.EVT_COMBOBOX, self.on_initial_linewidth_method, self.ComboInitialLinewidthMethod)
        self.Bind( EVT_FLOATSPIN, self.on_linewidth_value, self.FloatLinewidthValue)
        self.Bind( EVT_FLOATSPIN, self.on_initial_linewidth_start, self.FloatInitialLinewidthStart)
        self.Bind( EVT_FLOATSPIN, self.on_initial_linewidth_end, self.FloatInitialLinewidthEnd)
        self.Bind( EVT_FLOATSPIN, self.on_initial_linewidth_multiplier, self.FloatInitialLinewidthMultiplier)
        self.Bind(wx.EVT_COMBOBOX, self.on_initial_phase_method, self.ComboInitialPhaseMethod)
        self.Bind( EVT_FLOATSPIN, self.on_initial_phase0_value, self.FloatInitialPhase0Value)
        self.Bind( EVT_FLOATSPIN, self.on_initial_phase1_value, self.FloatInitialPhase1Value)
        self.Bind(wx.EVT_CHECKBOX, self.on_apply_ko_filter, self.CheckApplyKoFilter)
        self.Bind(wx.EVT_SPINCTRL, self.on_initial_ko_linewidth_minimum, self.SpinInitialKOLinewidthMinimum)
        self.Bind(wx.EVT_SPINCTRL, self.on_initial_ko_points, self.SpinInitialKOPoints)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PanelInitialValues.__set_properties
        self.ComboInitialB0ShiftMethod.SetMinSize((180, -1))
        self.FloatB0ShiftValue.SetMinSize((90, -1))
        self.ComboInitialBaselineMethod.SetMinSize((180, -1))
        self.FloatBaselineInitIgnoreWidth.SetMinSize((90, -1))
        self.FloatInitialBaselineLowessWidth.SetMinSize((90, -1))
        self.CheckInitialCrChoSeparation.SetValue(1)
        self.ComboInitialLinewidthMethod.SetMinSize((180, -1))
        self.FloatLinewidthValue.SetMinSize((90,-1))
        self.FloatInitialLinewidthStart.SetMinSize((90, -1))
        self.FloatInitialLinewidthEnd.SetMinSize((90, -1))
        self.FloatInitialLinewidthMultiplier.SetMinSize((90, -1))
        self.ComboInitialPhaseMethod.SetMinSize((180, -1))
        self.ComboInitialPhaseMethod.SetSelection(0)
        self.FloatInitialPhase0Value.SetMinSize((90, -1))
        self.FloatInitialPhase1Value.SetMinSize((90, -1))
        self.SpinInitialKOLinewidthMinimum.SetMinSize((60, -1))
        self.SpinInitialKOPoints.SetMinSize((60, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PanelInitialValues.__do_layout
        sizer_44 = wx.BoxSizer(wx.VERTICAL)
        sizer_41 = wx.StaticBoxSizer(wx.StaticBox(self.PanelKOFilter, wx.ID_ANY, "Truncation Filter - Area Corrections"), wx.VERTICAL)
        sizer_37 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Phase 0/1"), wx.VERTICAL)
        sizer_66 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Linewidth"), wx.VERTICAL)
        grid_sizer_2 = wx.FlexGridSizer(2, 4, 4, 4)
        sizer_49 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_38_copy = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Area and PPM - By Peak Search"), wx.VERTICAL)
        grid_sizer_9 = wx.FlexGridSizer(2, 3, 2, 2)
        sizer_61 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Data Pre-processing "), wx.VERTICAL)
        sizer_63 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Baseline Estimate - Improves Peak Estimation"), wx.VERTICAL)
        grid_sizer_10 = wx.FlexGridSizer(2, 2, 2, 2)
        sizer_52 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_62 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "B0 Shift - Aligns Data With Model"), wx.VERTICAL)
        sizer_45 = wx.BoxSizer(wx.HORIZONTAL)
        label_7 = wx.StaticText(self, wx.ID_ANY, "Method:")
        sizer_45.Add(label_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 2)
        sizer_45.Add(self.ComboInitialB0ShiftMethod, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 8)
        label_11 = wx.StaticText(self, wx.ID_ANY, "B0 Value [Hz]:")
        sizer_45.Add(label_11, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 8)
        sizer_45.Add(self.FloatB0ShiftValue, 0, wx.EXPAND | wx.LEFT, 2)
        sizer_62.Add(sizer_45, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.TOP, 2)
        sizer_61.Add(sizer_62, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        label_13 = wx.StaticText(self, wx.ID_ANY, "Method:")
        sizer_52.Add(label_13, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 2)
        sizer_52.Add(self.ComboInitialBaselineMethod, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_63.Add(sizer_52, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        label_10_copy = wx.StaticText(self.PanelBaselineInitLowess, wx.ID_ANY, "Peak Ignore Region Width [Hz]:")
        grid_sizer_10.Add(label_10_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 2)
        grid_sizer_10.Add(self.FloatBaselineInitIgnoreWidth, 0, 0, 0)
        label_9_copy = wx.StaticText(self.PanelBaselineInitLowess, wx.ID_ANY, "Filter Window Size [Hz]:")
        grid_sizer_10.Add(label_9_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 2)
        grid_sizer_10.Add(self.FloatInitialBaselineLowessWidth, 0, 0, 6)
        self.PanelBaselineInitLowess.SetSizer(grid_sizer_10)
        sizer_63.Add(self.PanelBaselineInitLowess, 0, wx.BOTTOM | wx.TOP, 4)
        sizer_61.Add(sizer_63, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        sizer_44.Add(sizer_61, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 8)
        grid_sizer_9.Add(self.CheckInitialPeakSearchAbs, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 8)
        label_16 = wx.StaticText(self, wx.ID_ANY, "Small Peaks Area From:")
        grid_sizer_9.Add(label_16, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 8)
        grid_sizer_9.Add(self.ComboInitialSmallPeakAreas, 0, wx.LEFT, 4)
        grid_sizer_9.Add(self.CheckInitialCrChoSeparation, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 8)
        label_17 = wx.StaticText(self, wx.ID_ANY, "Small Peaks PPM From:")
        grid_sizer_9.Add(label_17, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 8)
        grid_sizer_9.Add(self.ComboInitialSmallPeakFreqs, 0, wx.LEFT, 4)
        sizer_38_copy.Add(grid_sizer_9, 0, 0, 0)
        sizer_44.Add(sizer_38_copy, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        label_12_copy = wx.StaticText(self, wx.ID_ANY, "Method:")
        sizer_49.Add(label_12_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 2)
        sizer_49.Add(self.ComboInitialLinewidthMethod, 0, wx.ALIGN_CENTER_VERTICAL, 6)
        label_6 = wx.StaticText(self, wx.ID_ANY, "Linewidth Value [Hz]:")
        sizer_49.Add(label_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        sizer_49.Add(self.FloatLinewidthValue, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.LEFT, 4)
        sizer_12.Add(sizer_49, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        label_23 = wx.StaticText(self.PanelInitialLinewidth, wx.ID_ANY, "Calculation Range [PPM] - Start:")
        grid_sizer_2.Add(label_23, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_2.Add(self.FloatInitialLinewidthStart, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.EXPAND, 4)
        label_24 = wx.StaticText(self.PanelInitialLinewidth, wx.ID_ANY, "End:")
        grid_sizer_2.Add(label_24, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_2.Add(self.FloatInitialLinewidthEnd, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        label_1 = wx.StaticText(self.PanelInitialLinewidth, wx.ID_ANY, "Initial Width Multiplier: ")
        grid_sizer_2.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_2.Add(self.FloatInitialLinewidthMultiplier, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        grid_sizer_2.Add((20, 20), 0, wx.EXPAND, 0)
        grid_sizer_2.Add((20, 20), 0, wx.EXPAND, 0)
        self.PanelInitialLinewidth.SetSizer(grid_sizer_2)
        sizer_12.Add(self.PanelInitialLinewidth, 0, wx.EXPAND, 0)
        sizer_44.Add(sizer_12, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        label_8 = wx.StaticText(self, wx.ID_ANY, "Method:")
        sizer_18.Add(label_8, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 2)
        sizer_18.Add(self.ComboInitialPhaseMethod, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_15.Add(sizer_18, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 2)
        label_25 = wx.StaticText(self, wx.ID_ANY, "Initial Value - Phase 0:")
        sizer_66.Add(label_25, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 4)
        sizer_66.Add(self.FloatInitialPhase0Value, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 4)
        label_26 = wx.StaticText(self, wx.ID_ANY, "Phase 1:")
        sizer_66.Add(label_26, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT | wx.RIGHT, 4)
        sizer_66.Add(self.FloatInitialPhase1Value, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_15.Add(sizer_66, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 2)
        sizer_44.Add(sizer_15, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        sizer_37.Add(self.CheckApplyKoFilter, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 4)
        labelLinewidthMinimum = wx.StaticText(self.PanelKOFilter, wx.ID_ANY, "Linewidth Min:")
        sizer_37.Add(labelLinewidthMinimum, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        sizer_37.Add(self.SpinInitialKOLinewidthMinimum, 0, wx.RIGHT, 4)
        labelKissOffPoints = wx.StaticText(self.PanelKOFilter, wx.ID_ANY, "Truncation [points]:")
        sizer_37.Add(labelKissOffPoints, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 4)
        sizer_37.Add(self.SpinInitialKOPoints, 0, 0, 0)
        sizer_41.Add(sizer_37, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 2)
        self.PanelKOFilter.SetSizer(sizer_41)
        sizer_44.Add(self.PanelKOFilter, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_44)
        sizer_44.Fit(self)
        self.Layout()
        # end wxGlade

    def on_b0_shift_method(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_b0_shift_method' not implemented!")
        event.Skip()

    def on_b0_shift_value(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_b0_shift_value' not implemented!")
        event.Skip()

    def on_initial_baseline_method(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_baseline_method' not implemented!")
        event.Skip()

    def on_initial_baseline_ignore_width(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_baseline_ignore_width' not implemented!")
        event.Skip()

    def on_initial_baseline_lowess_width(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_baseline_lowess_width' not implemented!")
        event.Skip()

    def on_initial_peak_search_abs(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_peak_search_abs' not implemented!")
        event.Skip()

    def on_initial_small_peak_areas(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_small_peak_areas' not implemented!")
        event.Skip()

    def on_initial_cr_cho_separation(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_cr_cho_separation' not implemented!")
        event.Skip()

    def on_initial_small_peak_freqs(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_small_peak_freqs' not implemented!")
        event.Skip()

    def on_initial_linewidth_method(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_linewidth_method' not implemented!")
        event.Skip()

    def on_linewidth_value(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_linewidth_value' not implemented!")
        event.Skip()

    def on_initial_linewidth_start(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_linewidth_start' not implemented!")
        event.Skip()

    def on_initial_linewidth_end(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_linewidth_end' not implemented!")
        event.Skip()

    def on_initial_linewidth_multiplier(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_linewidth_multiplier' not implemented!")
        event.Skip()

    def on_initial_phase_method(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_phase_method' not implemented!")
        event.Skip()

    def on_initial_phase0_value(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_phase0_value' not implemented!")
        event.Skip()

    def on_initial_phase1_value(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_phase1_value' not implemented!")
        event.Skip()

    def on_apply_ko_filter(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_apply_ko_filter' not implemented!")
        event.Skip()

    def on_initial_ko_linewidth_minimum(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_ko_linewidth_minimum' not implemented!")
        event.Skip()

    def on_initial_ko_points(self, event):  # wxGlade: PanelInitialValues.<event_handler>
        print("Event handler 'on_initial_ko_points' not implemented!")
        event.Skip()

# end of class PanelInitialValues

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1314, 1069))
        self.PanelInitialValues = PanelInitialValues(self, wx.ID_ANY)

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
        sizer_1.Add(self.PanelInitialValues, 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyFrame
