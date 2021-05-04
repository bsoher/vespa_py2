# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 12:16:30 2019
#

import wx
from wx.lib.agw.floatspin import FloatSpin, EVT_FLOATSPIN, FS_LEFT, FS_RIGHT, FS_CENTRE, FS_READONLY

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class PanelBaselineUI(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PanelBaselineUI.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.PanelBaseline = wx.Panel(self, wx.ID_ANY)
        self.ComboBaselineMethod = wx.ComboBox(self.PanelBaseline, wx.ID_ANY, choices=[], style=wx.CB_READONLY)
        self.CheckBaselineSmoothingFlag = wx.CheckBox(self.PanelBaseline, wx.ID_ANY, " Smooth whole metabolite region")
        self.CheckBaselineSkipLastSmooth = wx.CheckBox(self.PanelBaseline, wx.ID_ANY, " Smoothing OFF for last iteration")
        self.FloatBaselineSmoothingWidth = FloatSpin(self.PanelBaseline, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=wx.SP_ARROW_KEYS | wx.TE_PROCESS_ENTER)
        self.FloatBaselineUnderestimate = FloatSpin(self.PanelBaseline, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=wx.SP_ARROW_KEYS | wx.TE_PROCESS_ENTER)
        self.PanelBaselineParameters = wx.Panel(self.PanelBaseline, wx.ID_ANY)
        self.PanelBsplineParameters = wx.Panel(self.PanelBaselineParameters, wx.ID_ANY)
        self.SpinBaselineSplineNknots = wx.SpinCtrl(self.PanelBsplineParameters, wx.ID_ANY, "", min=0, max=100)
        self.FloatBaselineSplineSpacing = FloatSpin(self.PanelBsplineParameters, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=wx.SP_ARROW_KEYS | wx.TE_PROCESS_ENTER)
        self.StaticHzSpacing = wx.StaticText(self.PanelBsplineParameters, wx.ID_ANY, "xx.yyyy")
        self.labelOrder = wx.StaticText(self.PanelBsplineParameters, wx.ID_ANY, "Order of B-splines:")
        self.SpinBaselineSplineOrder = wx.SpinCtrl(self.PanelBsplineParameters, wx.ID_ANY, "", min=0, max=100)
        self.PanelWaveletParameters = wx.Panel(self.PanelBaselineParameters, wx.ID_ANY)
        self.ComboBaselineWaveletScale = wx.ComboBox(self.PanelWaveletParameters, wx.ID_ANY, choices=[], style=wx.CB_READONLY)
        self.FloatBaselineWaveletMinDyad = FloatSpin(self.PanelWaveletParameters, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_baseline_method, self.ComboBaselineMethod)
        self.Bind(wx.EVT_CHECKBOX, self.on_baseline_smoothing_flag, self.CheckBaselineSmoothingFlag)
        self.Bind(wx.EVT_CHECKBOX, self.on_baseline_skip_last_smooth, self.CheckBaselineSkipLastSmooth)
        self.Bind( EVT_FLOATSPIN, self.on_baseline_smoothing_width, self.FloatBaselineSmoothingWidth)
        self.Bind( EVT_FLOATSPIN, self.on_baseline_underestimate, self.FloatBaselineUnderestimate)
        self.Bind(wx.EVT_SPINCTRL, self.on_baseline_spline_nknots, self.SpinBaselineSplineNknots)
        self.Bind( EVT_FLOATSPIN, self.on_baseline_spline_spacing, self.FloatBaselineSplineSpacing)
        self.Bind(wx.EVT_SPINCTRL, self.on_baseline_spline_order, self.SpinBaselineSplineOrder)
        self.Bind(wx.EVT_COMBOBOX, self.on_baseline_wavelet_scale, self.ComboBaselineWaveletScale)
        self.Bind( EVT_FLOATSPIN, self.on_baseline_wavelet_min_dyad, self.FloatBaselineWaveletMinDyad)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PanelBaselineUI.__set_properties
        self.CheckBaselineSkipLastSmooth.SetValue(1)
        self.SpinBaselineSplineNknots.SetMinSize((60, -1))
        self.FloatBaselineSplineSpacing.SetMinSize((60, -1))
        self.SpinBaselineSplineOrder.SetMinSize((60, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PanelBaselineUI.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_20 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_19 = wx.StaticBoxSizer(wx.StaticBox(self.PanelWaveletParameters, wx.ID_ANY, "Wavelet Filter Parameters"), wx.VERTICAL)
        grid_sizer_6 = wx.FlexGridSizer(2, 2, 2, 2)
        sizer_22 = wx.StaticBoxSizer(wx.StaticBox(self.PanelBsplineParameters, wx.ID_ANY, "B-spline Parameters"), wx.VERTICAL)
        grid_sizer_5 = wx.FlexGridSizer(3, 4, 2, 2)
        sizer_21 = wx.StaticBoxSizer(wx.StaticBox(self.PanelBaseline, wx.ID_ANY, "Smoothing Parameters"), wx.VERTICAL)
        grid_sizer_4 = wx.FlexGridSizer(2, 2, 2, 2)
        sizer_30 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_24 = wx.BoxSizer(wx.HORIZONTAL)
        label_1_copy = wx.StaticText(self.PanelBaseline, wx.ID_ANY, "Baseline Method:")
        sizer_24.Add(label_1_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        sizer_24.Add(self.ComboBaselineMethod, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_20.Add(sizer_24, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 8)
        sizer_30.Add(self.CheckBaselineSmoothingFlag, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 8)
        sizer_30.Add(self.CheckBaselineSkipLastSmooth, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 4)
        sizer_21.Add(sizer_30, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 8)
        labelMetab = wx.StaticText(self.PanelBaseline, wx.ID_ANY, "Metab Region Lowess - Window Size [Hz]:")
        grid_sizer_4.Add(labelMetab, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 4)
        grid_sizer_4.Add(self.FloatBaselineSmoothingWidth, 0, 0, 0)
        labelFirstPass = wx.StaticText(self.PanelBaseline, wx.ID_ANY, "First Pass Underestimation [%]:")
        grid_sizer_4.Add(labelFirstPass, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 4)
        grid_sizer_4.Add(self.FloatBaselineUnderestimate, 0, 0, 0)
        sizer_21.Add(grid_sizer_4, 1, 0, 0)
        sizer_20.Add(sizer_21, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 8)
        labelSplineNumber = wx.StaticText(self.PanelBsplineParameters, wx.ID_ANY, "Variable Smoothing Factor:")
        grid_sizer_5.Add(labelSplineNumber, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 4)
        grid_sizer_5.Add(self.SpinBaselineSplineNknots, 0, 0, 0)
        grid_sizer_5.Add((20, 20), 0, wx.EXPAND, 0)
        grid_sizer_5.Add((20, 20), 0, wx.EXPAND, 0)
        labelSplineSpacing = wx.StaticText(self.PanelBsplineParameters, wx.ID_ANY, "Fixed knot spacing [pts] of")
        grid_sizer_5.Add(labelSplineSpacing, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 4)
        grid_sizer_5.Add(self.FloatBaselineSplineSpacing, 0, wx.RIGHT, 4)
        label_111 = wx.StaticText(self.PanelBsplineParameters, wx.ID_ANY, "gives [Hz] spacing of ")
        grid_sizer_5.Add(label_111, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 2)
        grid_sizer_5.Add(self.StaticHzSpacing, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 2)
        grid_sizer_5.Add(self.labelOrder, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.RIGHT, 4)
        grid_sizer_5.Add(self.SpinBaselineSplineOrder, 0, 0, 0)
        grid_sizer_5.Add((20, 20), 0, wx.EXPAND, 0)
        grid_sizer_5.Add((20, 20), 0, wx.EXPAND, 0)
        sizer_22.Add(grid_sizer_5, 1, wx.EXPAND, 0)
        self.PanelBsplineParameters.SetSizer(sizer_22)
        sizer_3.Add(self.PanelBsplineParameters, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 8)
        labelWaveletScale = wx.StaticText(self.PanelWaveletParameters, wx.ID_ANY, "Wavelet Scale Multiplier [x Linewidth]:")
        grid_sizer_6.Add(labelWaveletScale, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 4)
        grid_sizer_6.Add(self.ComboBaselineWaveletScale, 0, 0, 0)
        labelWaveletDyad = wx.StaticText(self.PanelWaveletParameters, wx.ID_ANY, "Wavelet Dyad Min Scale [Hz]:")
        grid_sizer_6.Add(labelWaveletDyad, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 4)
        grid_sizer_6.Add(self.FloatBaselineWaveletMinDyad, 1, wx.EXPAND, 0)
        sizer_19.Add(grid_sizer_6, 1, 0, 0)
        self.PanelWaveletParameters.SetSizer(sizer_19)
        sizer_3.Add(self.PanelWaveletParameters, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 8)
        self.PanelBaselineParameters.SetSizer(sizer_3)
        sizer_20.Add(self.PanelBaselineParameters, 0, wx.EXPAND, 0)
        self.PanelBaseline.SetSizer(sizer_20)
        sizer_2.Add(self.PanelBaseline, 1, 0, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

    def on_baseline_method(self, event):  # wxGlade: PanelBaselineUI.<event_handler>
        print("Event handler 'on_baseline_method' not implemented!")
        event.Skip()

    def on_baseline_smoothing_flag(self, event):  # wxGlade: PanelBaselineUI.<event_handler>
        print("Event handler 'on_baseline_smoothing_flag' not implemented!")
        event.Skip()

    def on_baseline_skip_last_smooth(self, event):  # wxGlade: PanelBaselineUI.<event_handler>
        print("Event handler 'on_baseline_skip_last_smooth' not implemented!")
        event.Skip()

    def on_baseline_smoothing_width(self, event):  # wxGlade: PanelBaselineUI.<event_handler>
        print("Event handler 'on_baseline_smoothing_width' not implemented!")
        event.Skip()

    def on_baseline_underestimate(self, event):  # wxGlade: PanelBaselineUI.<event_handler>
        print("Event handler 'on_baseline_underestimate' not implemented!")
        event.Skip()

    def on_baseline_spline_nknots(self, event):  # wxGlade: PanelBaselineUI.<event_handler>
        print("Event handler 'on_baseline_spline_nknots' not implemented!")
        event.Skip()

    def on_baseline_spline_spacing(self, event):  # wxGlade: PanelBaselineUI.<event_handler>
        print("Event handler 'on_baseline_spline_spacing' not implemented!")
        event.Skip()

    def on_baseline_spline_order(self, event):  # wxGlade: PanelBaselineUI.<event_handler>
        print("Event handler 'on_baseline_spline_order' not implemented!")
        event.Skip()

    def on_baseline_wavelet_scale(self, event):  # wxGlade: PanelBaselineUI.<event_handler>
        print("Event handler 'on_baseline_wavelet_scale' not implemented!")
        event.Skip()

    def on_baseline_wavelet_min_dyad(self, event):  # wxGlade: PanelBaselineUI.<event_handler>
        print("Event handler 'on_baseline_wavelet_min_dyad' not implemented!")
        event.Skip()

# end of class PanelBaselineUI

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1314, 1069))
        self.PanelBaselineUI = PanelBaselineUI(self, wx.ID_ANY)

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
        sizer_1.Add(self.PanelBaselineUI, 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyFrame