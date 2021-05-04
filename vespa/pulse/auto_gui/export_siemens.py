# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 12:56:30 2019
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
        self.TextName = wx.TextCtrl(self, wx.ID_ANY, "")
        self.TextComment = wx.TextCtrl(self, wx.ID_ANY, "")
        self.TextAmpIntegral = wx.TextCtrl(self, wx.ID_ANY, "")
        self.TextCalcAmpIntegral = wx.TextCtrl(self, wx.ID_ANY, "")
        self.TextCalcAbsIntegral = wx.TextCtrl(self, wx.ID_ANY, "")
        self.TextCalcPowerIntegral = wx.TextCtrl(self, wx.ID_ANY, "")
        self.TextMinSliceThickness = wx.TextCtrl(self, wx.ID_ANY, "")
        self.TextMaxSliceThickness = wx.TextCtrl(self, wx.ID_ANY, "")
        self.TextReferenceGradient = wx.TextCtrl(self, wx.ID_ANY, "")
        self.ButtonResetIntegral = wx.Button(self, wx.ID_ANY, "Reset Integral")
        self.LabelOkCancelPlaceholder = wx.StaticText(self, wx.ID_ANY, "Placeholder for OK/Cancel")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("Export to Siemens")
        self.TextCalcAmpIntegral.Enable(False)
        self.TextCalcAbsIntegral.Enable(False)
        self.TextCalcPowerIntegral.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Pulse Characteristics"), wx.VERTICAL)
        grid_sizer_2 = wx.FlexGridSizer(7, 2, 2, 2)
        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Pulse Description"), wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 2, 2, 2)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Name:")
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        grid_sizer_1.Add(self.TextName, 0, wx.EXPAND, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Comment:")
        grid_sizer_1.Add(label_2, 0, wx.ALL, 4)
        grid_sizer_1.Add(self.TextComment, 1, wx.EXPAND, 0)
        grid_sizer_1.AddGrowableRow(1)
        grid_sizer_1.AddGrowableCol(1)
        sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Amplitude Integral [opt]:")
        grid_sizer_2.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        grid_sizer_2.Add(self.TextAmpIntegral, 0, wx.EXPAND, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, "Calcul. Amplitude Integral [opt]:")
        grid_sizer_2.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        grid_sizer_2.Add(self.TextCalcAmpIntegral, 0, wx.EXPAND, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Calcul. Absolute Integral [opt]:")
        grid_sizer_2.Add(label_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        grid_sizer_2.Add(self.TextCalcAbsIntegral, 0, wx.EXPAND, 0)
        label_6 = wx.StaticText(self, wx.ID_ANY, "Cacul. Power Integral [opt]:")
        grid_sizer_2.Add(label_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        grid_sizer_2.Add(self.TextCalcPowerIntegral, 0, wx.EXPAND, 0)
        label_7 = wx.StaticText(self, wx.ID_ANY, "MinSlice Thickness [mm]:")
        grid_sizer_2.Add(label_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        grid_sizer_2.Add(self.TextMinSliceThickness, 0, wx.EXPAND, 0)
        label_8 = wx.StaticText(self, wx.ID_ANY, "MaxSlice Thickness [mm]:")
        grid_sizer_2.Add(label_8, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        grid_sizer_2.Add(self.TextMaxSliceThickness, 0, wx.EXPAND, 0)
        label_9 = wx.StaticText(self, wx.ID_ANY, "Reference Gradient [mT/min]:")
        grid_sizer_2.Add(label_9, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)
        grid_sizer_2.Add(self.TextReferenceGradient, 0, wx.EXPAND, 0)
        grid_sizer_2.AddGrowableCol(1)
        sizer_3.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        sizer_4.Add(self.ButtonResetIntegral, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 12)
        sizer_4_copy.Add(self.LabelOkCancelPlaceholder, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(sizer_4_copy, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_4, 0, wx.ALL | wx.EXPAND, 4)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyDialog
