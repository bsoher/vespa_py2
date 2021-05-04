# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 12:30:01 2019
#

import wx
from wx.lib.agw.floatspin import FloatSpin, EVT_FLOATSPIN, FS_LEFT, FS_RIGHT, FS_CENTRE, FS_READONLY

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class PanelPrepTimeseriesUI(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PanelPrepTimeseriesUI.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.SplitterWindow = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
        self.PanelPrepFidsum = wx.Panel(self.SplitterWindow, wx.ID_ANY)
        self.PanelCoilCombination = wx.Panel(self.PanelPrepFidsum, wx.ID_ANY)
        self.label_7 = wx.StaticText(self.PanelCoilCombination, wx.ID_ANY, "Combination Method: ")
        self.ComboCoilCombineMethod = wx.ComboBox(self.PanelCoilCombination, wx.ID_ANY, choices=["None", "Siemens (Brown)", "CMRR"], style=wx.CB_READONLY)
        self.PanelFidAveraging = wx.Panel(self.PanelPrepFidsum, wx.ID_ANY)
        self.SpinFidsToAverage = wx.SpinCtrl(self.PanelFidAveraging, wx.ID_ANY, "1", min=1, max=100, style=0)
        self.PanelFidCorrectionsAndAveraging = wx.Panel(self.PanelPrepFidsum, wx.ID_ANY)
        self.SpinFidIndex = wx.SpinCtrl(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "", min=0, max=100, style=0)
        self.FloatGaussianApodization = FloatSpin(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatPeakShiftValue = FloatSpin(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.SpinFidLeftShift = wx.SpinCtrl(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "", min=-100, max=100, style=0)
        self.FloatPhase0 = FloatSpin(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.label_4 = wx.StaticText(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Global Phase 1 [deg]:")
        self.FloatGlobalPhase1 = FloatSpin(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.label_12 = wx.StaticText(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Global Phase 0 [deg:")
        self.FloatGlobalPhase0 = FloatSpin(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, value=0.0, digits=1, min_val=0.0, max_val=360.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.CheckApplyPeakShift = wx.CheckBox(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, " Apply Peak Shift")
        self.ButtonResetPeakShift = wx.Button(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Reset Peak Shifts")
        self.FloatReferencePeakCenter = FloatSpin(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatPeakSearchWidth = FloatSpin(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.CheckApplyPhase0 = wx.CheckBox(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, " Apply Phase0")
        self.ButtonResetPhase0 = wx.Button(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Reset Phase0 Values")
        self.FloatPhase0RangeStart = FloatSpin(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatPhase0RangeEnd = FloatSpin(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.ButtonCalculateCorrections = wx.Button(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Calculate Corrections")
        self.ButtonPushResults = wx.Button(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Push Results to Associated Datasets")
        self.window_1_pane_2 = wx.Panel(self.SplitterWindow, wx.ID_ANY)
        self.PanelViewPrepFidsum = wx.Panel(self.window_1_pane_2, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_coil_combine_method, self.ComboCoilCombineMethod)
        self.Bind(wx.EVT_SPINCTRL, self.on_fids_to_average, self.SpinFidsToAverage)
        self.Bind(wx.EVT_SPINCTRL, self.on_fid_index, self.SpinFidIndex)
        self.Bind( EVT_FLOATSPIN, self.on_gaussian_apodization, self.FloatGaussianApodization)
        self.Bind( EVT_FLOATSPIN, self.on_peak_shift_value, self.FloatPeakShiftValue)
        self.Bind(wx.EVT_SPINCTRL, self.on_fid_left_shift, self.SpinFidLeftShift)
        self.Bind( EVT_FLOATSPIN, self.on_phase0, self.FloatPhase0)
        self.Bind( EVT_FLOATSPIN, self.on_global_phase1, self.FloatGlobalPhase1)
        self.Bind( EVT_FLOATSPIN, self.on_global_phase0, self.FloatGlobalPhase0)
        self.Bind(wx.EVT_CHECKBOX, self.on_apply_peak_shift, self.CheckApplyPeakShift)
        self.Bind(wx.EVT_BUTTON, self.on_reset_peak_shift, self.ButtonResetPeakShift)
        self.Bind( EVT_FLOATSPIN, self.on_reference_peak_center, self.FloatReferencePeakCenter)
        self.Bind( EVT_FLOATSPIN, self.on_peak_search_width, self.FloatPeakSearchWidth)
        self.Bind(wx.EVT_CHECKBOX, self.on_apply_phase0, self.CheckApplyPhase0)
        self.Bind(wx.EVT_BUTTON, self.on_reset_phase0, self.ButtonResetPhase0)
        self.Bind( EVT_FLOATSPIN, self.on_phase0_range_start, self.FloatPhase0RangeStart)
        self.Bind( EVT_FLOATSPIN, self.on_phase0_range_end, self.FloatPhase0RangeEnd)
        self.Bind(wx.EVT_BUTTON, self.on_calculate_corrections, self.ButtonCalculateCorrections)
        self.Bind(wx.EVT_BUTTON, self.on_push_results, self.ButtonPushResults)
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, self.on_splitter, self.SplitterWindow)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PanelPrepTimeseriesUI.__set_properties
        self.CheckApplyPeakShift.SetValue(1)
        self.CheckApplyPhase0.SetValue(1)
        self.SplitterWindow.SetMinimumPaneSize(20)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PanelPrepTimeseriesUI.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.StaticBoxSizer(wx.StaticBox(self.window_1_pane_2, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.StaticBoxSizer(wx.StaticBox(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "FID Corrections and Averaging"), wx.VERTICAL)
        sizer_9 = wx.StaticBoxSizer(wx.StaticBox(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Automated Data Corrections"), wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_7 = wx.FlexGridSizer(6, 2, 4, 4)
        sizer_7 = wx.StaticBoxSizer(wx.StaticBox(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Display Processing and Manual Corrections"), wx.VERTICAL)
        grid_sizer_6 = wx.FlexGridSizer(3, 4, 4, 4)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.StaticBoxSizer(wx.StaticBox(self.PanelFidAveraging, wx.ID_ANY, "FID Averaging"), wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.StaticBoxSizer(wx.StaticBox(self.PanelCoilCombination, wx.ID_ANY, "Coil Combination"), wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12.Add(self.label_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 8)
        sizer_12.Add(self.ComboCoilCombineMethod, 0, 0, 0)
        sizer_8.Add(sizer_12, 1, 0, 0)
        self.PanelCoilCombination.SetSizer(sizer_8)
        sizer_1.Add(self.PanelCoilCombination, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 8)
        label_13 = wx.StaticText(self.PanelFidAveraging, wx.ID_ANY, "Number of raw FIDs to average together:")
        sizer_14.Add(label_13, 0, wx.ALL, 8)
        sizer_14.Add(self.SpinFidsToAverage, 0, wx.ALL, 8)
        sizer_13.Add(sizer_14, 1, 0, 0)
        self.PanelFidAveraging.SetSizer(sizer_13)
        sizer_1.Add(self.PanelFidAveraging, 0, wx.ALL, 8)
        label_1 = wx.StaticText(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "FID index : ")
        sizer_6.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 3)
        sizer_6.Add(self.SpinFidIndex, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(sizer_6, 0, wx.ALL | wx.EXPAND, 8)
        label_9 = wx.StaticText(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Gauss apodize [Hz]:")
        grid_sizer_6.Add(label_9, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 12)
        grid_sizer_6.Add(self.FloatGaussianApodization, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        label_11 = wx.StaticText(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Peak shift [Hz]:")
        grid_sizer_6.Add(label_11, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 12)
        grid_sizer_6.Add(self.FloatPeakShiftValue, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        label_2 = wx.StaticText(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "FID left shift [pts]:")
        grid_sizer_6.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 8)
        grid_sizer_6.Add(self.SpinFidLeftShift, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        label_3 = wx.StaticText(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Indiv Phase 0 [deg]:")
        grid_sizer_6.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 8)
        grid_sizer_6.Add(self.FloatPhase0, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        grid_sizer_6.Add(self.label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 8)
        grid_sizer_6.Add(self.FloatGlobalPhase1, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        grid_sizer_6.Add(self.label_12, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 8)
        grid_sizer_6.Add(self.FloatGlobalPhase0, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        sizer_7.Add(grid_sizer_6, 0, wx.ALL | wx.EXPAND, 4)
        sizer_5.Add(sizer_7, 0, wx.EXPAND | wx.TOP, 10)
        grid_sizer_7.Add(self.CheckApplyPeakShift, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_7.Add(self.ButtonResetPeakShift, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        label_8 = wx.StaticText(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Reference peak center [ppm]:")
        grid_sizer_7.Add(label_8, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_7.Add(self.FloatReferencePeakCenter, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        label_10 = wx.StaticText(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Peak search width [+/- ppm]:")
        grid_sizer_7.Add(label_10, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_7.Add(self.FloatPeakSearchWidth, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        grid_sizer_7.Add(self.CheckApplyPhase0, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_7.Add(self.ButtonResetPhase0, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        label_5 = wx.StaticText(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Optimization Range Start [ppm]:")
        grid_sizer_7.Add(label_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_7.Add(self.FloatPhase0RangeStart, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        label_6 = wx.StaticText(self.PanelFidCorrectionsAndAveraging, wx.ID_ANY, "Optimization Range End [ppm]:")
        grid_sizer_7.Add(label_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_7.Add(self.FloatPhase0RangeEnd, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        sizer_9.Add(grid_sizer_7, 0, wx.BOTTOM | wx.EXPAND, 30)
        sizer_11.Add(self.ButtonCalculateCorrections, 0, wx.EXPAND, 0)
        sizer_11.Add(self.ButtonPushResults, 0, wx.LEFT, 10)
        sizer_9.Add(sizer_11, 0, wx.EXPAND, 0)
        sizer_5.Add(sizer_9, 0, wx.ALL | wx.EXPAND, 4)
        self.PanelFidCorrectionsAndAveraging.SetSizer(sizer_5)
        sizer_1.Add(self.PanelFidCorrectionsAndAveraging, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 8)
        sizer_1.Add(sizer_10, 0, wx.ALL | wx.EXPAND, 4)
        self.PanelPrepFidsum.SetSizer(sizer_1)
        sizer_4.Add(self.PanelViewPrepFidsum, 1, wx.EXPAND, 0)
        self.window_1_pane_2.SetSizer(sizer_4)
        self.SplitterWindow.SplitVertically(self.PanelPrepFidsum, self.window_1_pane_2)
        sizer_3.Add(self.SplitterWindow, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

    def on_coil_combine_method(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_coil_combine_method' not implemented!")
        event.Skip()

    def on_fids_to_average(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_fids_to_average' not implemented!")
        event.Skip()

    def on_fid_index(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_fid_index' not implemented!")
        event.Skip()

    def on_gaussian_apodization(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_gaussian_apodization' not implemented!")
        event.Skip()

    def on_peak_shift_value(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_peak_shift_value' not implemented!")
        event.Skip()

    def on_fid_left_shift(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_fid_left_shift' not implemented!")
        event.Skip()

    def on_phase0(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_phase0' not implemented!")
        event.Skip()

    def on_global_phase1(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_global_phase1' not implemented!")
        event.Skip()

    def on_global_phase0(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_global_phase0' not implemented!")
        event.Skip()

    def on_apply_peak_shift(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_apply_peak_shift' not implemented!")
        event.Skip()

    def on_reset_peak_shift(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_reset_peak_shift' not implemented!")
        event.Skip()

    def on_reference_peak_center(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_reference_peak_center' not implemented!")
        event.Skip()

    def on_peak_search_width(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_peak_search_width' not implemented!")
        event.Skip()

    def on_apply_phase0(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_apply_phase0' not implemented!")
        event.Skip()

    def on_reset_phase0(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_reset_phase0' not implemented!")
        event.Skip()

    def on_phase0_range_start(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_phase0_range_start' not implemented!")
        event.Skip()

    def on_phase0_range_end(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_phase0_range_end' not implemented!")
        event.Skip()

    def on_calculate_corrections(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_calculate_corrections' not implemented!")
        event.Skip()

    def on_push_results(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_push_results' not implemented!")
        event.Skip()

    def on_splitter(self, event):  # wxGlade: PanelPrepTimeseriesUI.<event_handler>
        print("Event handler 'on_splitter' not implemented!")
        event.Skip()

# end of class PanelPrepTimeseriesUI

class MyFrame1(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((730, 940))
        self.PanelPrepTimeseriesUI = PanelPrepTimeseriesUI(self, wx.ID_ANY)

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
        sizer_2.Add(self.PanelPrepTimeseriesUI, 1, wx.ALL | wx.EXPAND, 4)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

# end of class MyFrame1
