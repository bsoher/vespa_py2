#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade HG on Thu Dec 15 09:09:11 2011

import wx

import vespa.common.wx_gravy.util
from wx.lib.agw.floatspin import FloatSpin, EVT_FLOATSPIN, FS_LEFT, FS_RIGHT, FS_CENTRE, FS_READONLY

# begin wxGlade: extracode
# end wxGlade



class PanelOptimalControlNonselect(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PanelOptimalControlNonselect.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.ComboOptimizePulseType = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.ComboPhaseType = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.FloatTipAngle = FloatSpin(self, -1, value=0.0, increment=0.5, agwStyle=FS_LEFT)
        self.FloatLinearFactor = FloatSpin(self, -1, increment=0.001, agwStyle=FS_LEFT)
        self.SpinExciteBandPoints = wx.SpinCtrl(self, -1, "", min=1, max=100000)
        self.FloatBandwidth = FloatSpin(self, -1, increment=0.1, agwStyle=FS_LEFT)
        self.FloatB1ImmunityRange = FloatSpin(self, -1, increment=0.5, agwStyle=FS_LEFT)
        self.SpinRangeSteps = wx.SpinCtrl(self, -1, "", min=1, max=10000)
        self.ComboStepSizeModification = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.FloatStepSizeMultiplier = FloatSpin(self, -1, increment=0.01, agwStyle=FS_LEFT)
        self.FloatLimitB1Max = FloatSpin(self, -1, increment=0.5, agwStyle=FS_LEFT)
        self.FloatErrorIncreaseTolerance = FloatSpin(self, -1, increment=1e-06, agwStyle=FS_LEFT)
        self.CheckLimitSar = wx.CheckBox(self, -1, "SAR...  Factor:")
        self.FloatLimitSarFactor = FloatSpin(self, -1, increment=0.1, agwStyle=FS_LEFT)
        self.CheckSymmetrize = wx.CheckBox(self, -1, "Symmetrize")
        self.label_15 = wx.StaticText(self, -1, "Optimization is suspended when any criterion is met.")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.label_13 = wx.StaticText(self, -1, "Your Limit")
        self.label_14 = wx.StaticText(self, -1, "Actual Value")
        self.CheckMaxIterations = wx.CheckBox(self, -1, "Iterations:")
        self.SpinMaxIterationNumber = wx.SpinCtrl(self, -1, "", min=1, max=1000000)
        self.LabelActualIterations = wx.StaticText(self, -1, "LabelActualIterations")
        self.CheckLimitByTime = wx.CheckBox(self, -1, "Time [minutes]:")
        self.SpinCtrlTimeLimit = wx.SpinCtrl(self, -1, "", min=0, max=100)
        self.LabelActualTimeElapsed = wx.StaticText(self, -1, "LabelActualTimeElapsed")
        self.CheckResidualError = wx.CheckBox(self, -1, "Residual error [%]:")
        self.FloatResidualError = FloatSpin(self, -1, increment=0.01, agwStyle=FS_LEFT)
        self.LabelActualResidualError = wx.StaticText(self, -1, "LabelActualResidualError")
        self.CheckDifferentialError = wx.CheckBox(self, -1, "Differential error [%%]:")
        self.FloatDifferentialError = FloatSpin(self, -1, increment=1e-06, agwStyle=FS_LEFT)
        self.LabelActualDifferentialError = wx.StaticText(self, -1, "LabelActualDifferentialError")
        self.CheckHaltErrorIncreasing = wx.CheckBox(self, -1, "Increasing error")
        self.ButtonContinue = wx.Button(self, -1, "Continue in New Tab")
        self.sizer_3_staticbox = wx.StaticBox(self, -1, "Optimization Suspension Criteria")
        self.sizer_2_staticbox = wx.StaticBox(self, -1, "Broadband B1-Immune Optimal Control Parameters")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_selchange_pulse_type, self.ComboOptimizePulseType)
        self.Bind(wx.EVT_COMBOBOX, self.on_selchange_phase_type, self.ComboPhaseType)
        self.Bind(wx.EVT_SPINCTRL, self.on_range_steps_changed, self.SpinRangeSteps)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_sar, self.CheckLimitSar)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_max_iterations, self.CheckMaxIterations)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_limit_time, self.CheckLimitByTime)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_residual_error, self.CheckResidualError)
        self.Bind(wx.EVT_CHECKBOX, self.on_check_differential_error, self.CheckDifferentialError)
        self.Bind(wx.EVT_BUTTON, self.on_continue_run, self.ButtonContinue)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PanelOptimalControlNonselect.__set_properties
        self.ComboOptimizePulseType.SetMinSize((80, -1))
        self.ComboPhaseType.SetMinSize((80,-1))
        self.FloatTipAngle.SetMinSize((80,-1))
        self.FloatLinearFactor.SetMinSize((80, -1))
        self.FloatLinearFactor.Enable(False)
        self.SpinExciteBandPoints.SetMinSize((80, -1))
        self.FloatBandwidth.SetMinSize((80, -1))
        self.FloatB1ImmunityRange.SetMinSize((80, -1))
        self.SpinRangeSteps.SetMinSize((80, -1))
        self.ComboStepSizeModification.SetMinSize((80, -1))
        self.FloatStepSizeMultiplier.SetMinSize((80, -1))
        self.FloatLimitB1Max.SetMinSize((80, -1))
        self.FloatErrorIncreaseTolerance.SetMinSize((80, -1))
        self.FloatLimitSarFactor.SetMinSize((80, -1))
        self.CheckSymmetrize.SetMinSize((-1, -1))
        self.CheckSymmetrize.SetValue(1)
        self.SpinMaxIterationNumber.SetMinSize((100, -1))
        self.SpinCtrlTimeLimit.SetMinSize((100, -1))
        self.FloatResidualError.SetMinSize((100, -1))
        self.FloatDifferentialError.SetMinSize((100, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PanelOptimalControlNonselect.__do_layout
        self.sizer_2_staticbox.Lower()
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.VERTICAL)
        self.sizer_3_staticbox.Lower()
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.VERTICAL)
        grid_sizer_3 = wx.FlexGridSizer(1, 3, 0, 0)
        grid_sizer_2 = wx.FlexGridSizer(7, 3, 5, 5)
        grid_sizer_1 = wx.FlexGridSizer(12, 4, 8, 4)
        label_1 = wx.StaticText(self, -1, "Pulse Usage:")
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.ComboOptimizePulseType, 0, wx.EXPAND, 0)
        label_2 = wx.StaticText(self, -1, "Phase Type:")
        grid_sizer_1.Add(label_2, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.ComboPhaseType, 0, wx.EXPAND, 0)
        label_3 = wx.StaticText(self, -1, "Tip Angle:")
        grid_sizer_1.Add(label_3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.FloatTipAngle, 0, wx.EXPAND, 0)
        label_linear = wx.StaticText(self, -1, "Linear Factor:")
        grid_sizer_1.Add(label_linear, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.FloatLinearFactor, 0, wx.EXPAND, 0)
        label_5 = wx.StaticText(self, -1, "Excite Band Pts:")
        grid_sizer_1.Add(label_5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.SpinExciteBandPoints, 0, wx.EXPAND, 0)
        label_6 = wx.StaticText(self, -1, "Bandwidth [kHz]:")
        grid_sizer_1.Add(label_6, 0, wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 8)
        grid_sizer_1.Add(self.FloatBandwidth, 0, wx.EXPAND, 0)
        label_7 = wx.StaticText(self, -1, "B1 Immunity [%]:")
        grid_sizer_1.Add(label_7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.FloatB1ImmunityRange, 0, wx.EXPAND, 0)
        label_8 = wx.StaticText(self, -1, "Range Steps:")
        grid_sizer_1.Add(label_8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.SpinRangeSteps, 0, wx.EXPAND, 0)
        label_9 = wx.StaticText(self, -1, "Step Size Mods:")
        grid_sizer_1.Add(label_9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.ComboStepSizeModification, 0, wx.EXPAND, 0)
        label_10 = wx.StaticText(self, -1, "Step Size Mult.:")
        grid_sizer_1.Add(label_10, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.FloatStepSizeMultiplier, 0, wx.EXPAND, 0)
        label_11 = wx.StaticText(self, -1, "Max B1 Limit:")
        grid_sizer_1.Add(label_11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.FloatLimitB1Max, 0, wx.EXPAND, 0)
        label_12 = wx.StaticText(self, -1, "Error Tolerance:")
        grid_sizer_1.Add(label_12, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.FloatErrorIncreaseTolerance, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.CheckLimitSar, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.FloatLimitSarFactor, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.CheckSymmetrize, 0, 0, 0)
        grid_sizer_1.AddGrowableCol(1)
        grid_sizer_1.AddGrowableCol(3)
        sizer_2.Add(grid_sizer_1, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_15, 0, wx.BOTTOM, 5)
        sizer_3.Add(self.static_line_1, 0, wx.BOTTOM|wx.EXPAND, 5)
        grid_sizer_2.Add((20, 20), 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.label_13, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.label_14, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.CheckMaxIterations, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.SpinMaxIterationNumber, 0, 0, 0)
        grid_sizer_2.Add(self.LabelActualIterations, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.CheckLimitByTime, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.SpinCtrlTimeLimit, 0, 0, 0)
        grid_sizer_2.Add(self.LabelActualTimeElapsed, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.CheckResidualError, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.FloatResidualError, 0, 0, 0)
        grid_sizer_2.Add(self.LabelActualResidualError, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.CheckDifferentialError, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.FloatDifferentialError, 0, 0, 0)
        grid_sizer_2.Add(self.LabelActualDifferentialError, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.CheckHaltErrorIncreasing, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add((20, 20), 0, wx.EXPAND, 0)
        grid_sizer_2.Add((20, 20), 0, wx.EXPAND, 0)
        grid_sizer_2.AddGrowableCol(2)
        sizer_3.Add(grid_sizer_2, 0, wx.EXPAND, 0)
        grid_sizer_3.Add((20, 20), 0, wx.EXPAND, 0)
        grid_sizer_3.Add(self.ButtonContinue, 0, 0, 0)
        grid_sizer_3.Add((20, 20), 0, wx.EXPAND, 0)
        grid_sizer_3.AddGrowableCol(0)
        grid_sizer_3.AddGrowableCol(2)
        sizer_3.Add(grid_sizer_3, 0, wx.TOP|wx.EXPAND, 15)
        sizer_2.Add(sizer_3, 1, wx.TOP|wx.EXPAND, 5)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        # end wxGlade

    def on_selchange_pulse_type(self, event): # wxGlade: PanelOptimalControlNonselect.<event_handler>
        print "Event handler `on_selchange_pulse_type' not implemented!"
        event.Skip()

    def on_selchange_phase_type(self, event): # wxGlade: PanelOptimalControlNonselect.<event_handler>
        print "Event handler `on_selchange_phase_type' not implemented!"
        event.Skip()

    def on_range_steps_changed(self, event): # wxGlade: PanelOptimalControlNonselect.<event_handler>
        print "Event handler `on_range_steps_changed' not implemented!"
        event.Skip()

    def on_check_sar(self, event): # wxGlade: PanelOptimalControlNonselect.<event_handler>
        print "Event handler `on_check_sar' not implemented!"
        event.Skip()

    def on_check_max_iterations(self, event): # wxGlade: PanelOptimalControlNonselect.<event_handler>
        print "Event handler `on_check_max_iterations' not implemented!"
        event.Skip()

    def on_check_limit_time(self, event): # wxGlade: PanelOptimalControlNonselect.<event_handler>
        print "Event handler `on_check_limit_time' not implemented!"
        event.Skip()

    def on_check_residual_error(self, event): # wxGlade: PanelOptimalControlNonselect.<event_handler>
        print "Event handler `on_check_residual_error' not implemented!"
        event.Skip()

    def on_check_differential_error(self, event): # wxGlade: PanelOptimalControlNonselect.<event_handler>
        print "Event handler `on_check_differential_error' not implemented!"
        event.Skip()

    def on_continue_run(self, event): # wxGlade: PanelOptimalControlNonselect.<event_handler>
        print "Event handler `on_continue_run' not implemented!"
        event.Skip()

# end of class PanelOptimalControlNonselect


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.PanelOptimalControlNonselect = PanelOptimalControlNonselect(self, -1)

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
        sizer_1.Add(self.PanelOptimalControlNonselect, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    MyFrame = MyFrame(None, -1, "")
    app.SetTopWindow(MyFrame)
    MyFrame.Show()
    app.MainLoop()
