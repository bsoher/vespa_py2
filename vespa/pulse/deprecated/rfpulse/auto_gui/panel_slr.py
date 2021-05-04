# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 13:40:47 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class PanelSlr(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PanelSlr.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.TextTipAngle = wx.TextCtrl(self, wx.ID_ANY, "")
        self.TextTimeSteps = wx.TextCtrl(self, wx.ID_ANY, "")
        self.TextDuration = wx.TextCtrl(self, wx.ID_ANY, "")
        self.TextBandwidth = wx.TextCtrl(self, wx.ID_ANY, "")
        self.LabelSeparation = wx.StaticText(self, wx.ID_ANY, "Separation: ", style=wx.ALIGN_RIGHT)
        self.TextSeparation = wx.TextCtrl(self, wx.ID_ANY, "")
        self.LabelSeparationKhz = wx.StaticText(self, wx.ID_ANY, "kilohertz")
        self.RadioBandType = wx.RadioBox(self, wx.ID_ANY, "Single or Dual Band", choices=["Single Band", "Dual Band"], majorDimension=2, style=wx.RA_SPECIFY_COLS)
        self.ComboNonCoalesced = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.CB_READONLY | wx.CB_SIMPLE)
        self.RadioFilter = wx.RadioBox(self, wx.ID_ANY, "Filter", choices=["SLR (Remez)", "Least-Squares"], majorDimension=2, style=wx.RA_SPECIFY_COLS)
        self.label_7 = wx.StaticText(self, wx.ID_ANY, "Passband Ripple: ")
        self.TextPassbandRipple = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_8 = wx.StaticText(self, wx.ID_ANY, " Percent")
        self.label_9 = wx.StaticText(self, wx.ID_ANY, "Reject Ripple: ", style=wx.ALIGN_CENTER)
        self.TextRejectRipple = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_8_copy = wx.StaticText(self, wx.ID_ANY, " Percent")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT_ENTER, self.on_tip_angle, self.TextTipAngle)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_duration, self.TextDuration)
        self.Bind(wx.EVT_RADIOBOX, self.on_radio_band, self.RadioBandType)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_passband_changed, self.TextPassbandRipple)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_reject_changed, self.TextRejectRipple)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PanelSlr.__set_properties
        self.TextTipAngle.SetMinSize((175, -1))
        self.TextTimeSteps.SetMinSize((175, -1))
        self.TextDuration.SetMinSize((175, -1))
        self.TextBandwidth.SetMinSize((175, -1))
        self.TextSeparation.SetMinSize((175, -1))
        self.RadioBandType.SetMinSize((234, -1))
        self.RadioBandType.SetSelection(0)
        self.ComboNonCoalesced.SetMinSize((-1, -1))
        self.RadioFilter.SetSelection(0)
        self.TextPassbandRipple.SetMinSize((154, -1))
        self.TextRejectRipple.SetMinSize((154, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PanelSlr.__do_layout
        sizer_params_slr = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Pulse Params"), wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 3, 4, 0)
        sizer_5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Non-Coalesced Phase Type"), wx.HORIZONTAL)
        grid_sizer_pulse_params = wx.FlexGridSizer(6, 3, 3, 5)
        label_2_copy = wx.StaticText(self, wx.ID_ANY, "Tip Angle: ", style=wx.ALIGN_RIGHT)
        grid_sizer_pulse_params.Add(label_2_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_pulse_params.Add(self.TextTipAngle, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "degrees")
        grid_sizer_pulse_params.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_2_copy_1 = wx.StaticText(self, wx.ID_ANY, "Time Steps: ", style=wx.ALIGN_RIGHT)
        grid_sizer_pulse_params.Add(label_2_copy_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_pulse_params.Add(self.TextTimeSteps, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, "increments")
        grid_sizer_pulse_params.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_2_copy_2 = wx.StaticText(self, wx.ID_ANY, "Duration: ", style=wx.ALIGN_RIGHT)
        grid_sizer_pulse_params.Add(label_2_copy_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_pulse_params.Add(self.TextDuration, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, "milliseconds")
        grid_sizer_pulse_params.Add(label_5, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_2_copy_3 = wx.StaticText(self, wx.ID_ANY, "Bandwidth: ", style=wx.ALIGN_RIGHT)
        grid_sizer_pulse_params.Add(label_2_copy_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_pulse_params.Add(self.TextBandwidth, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_5_copy = wx.StaticText(self, wx.ID_ANY, "kilohertz")
        grid_sizer_pulse_params.Add(label_5_copy, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_pulse_params.Add(self.LabelSeparation, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_pulse_params.Add(self.TextSeparation, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_pulse_params.Add(self.LabelSeparationKhz, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_pulse_params.Add((75, 2), 0, 0, 0)
        grid_sizer_pulse_params.Add((154, 2), 0, 0, 0)
        grid_sizer_pulse_params.Add((20, 2), 0, 0, 0)
        sizer_params_slr.Add(grid_sizer_pulse_params, 0, wx.EXPAND, 0)
        sizer_params_slr.Add(self.RadioBandType, 0, wx.BOTTOM, 4)
        sizer_5.Add(self.ComboNonCoalesced, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        sizer_params_slr.Add(sizer_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        sizer_3.Add(self.RadioFilter, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 2)
        grid_sizer_1.Add(self.TextPassbandRipple, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        grid_sizer_1.Add(self.label_8, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        grid_sizer_1.Add(self.label_9, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 2)
        grid_sizer_1.Add(self.TextRejectRipple, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        grid_sizer_1.Add(self.label_8_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_3.Add(grid_sizer_1, 0, wx.ALL | wx.EXPAND, 5)
        sizer_3.Add((20, 2), 0, wx.EXPAND, 0)
        sizer_params_slr.Add(sizer_3, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_params_slr)
        sizer_params_slr.Fit(self)
        self.Layout()
        # end wxGlade

    def on_tip_angle(self, event):  # wxGlade: PanelSlr.<event_handler>
        print("Event handler 'on_tip_angle' not implemented!")
        event.Skip()

    def on_duration(self, event):  # wxGlade: PanelSlr.<event_handler>
        print("Event handler 'on_duration' not implemented!")
        event.Skip()

    def on_radio_band(self, event):  # wxGlade: PanelSlr.<event_handler>
        print("Event handler 'on_radio_band' not implemented!")
        event.Skip()

    def on_text_passband_changed(self, event):  # wxGlade: PanelSlr.<event_handler>
        print("Event handler 'on_text_passband_changed' not implemented!")
        event.Skip()

    def on_text_reject_changed(self, event):  # wxGlade: PanelSlr.<event_handler>
        print("Event handler 'on_text_reject_changed' not implemented!")
        event.Skip()

# end of class PanelSlr

class FrameSlr(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: FrameSlr.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.PanelSlr = PanelSlr(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: FrameSlr.__set_properties
        self.SetTitle("frame_create_pulse")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: FrameSlr.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.PanelSlr, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class FrameSlr
