# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 13:51:38 2019
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
        self.LabelInstructions = wx.StaticText(self, wx.ID_ANY, "Select the experiment dimension (loop indices) you want to use.")
        self.panel_grid_loop = wx.Panel(self, wx.ID_ANY)
        self.LabelLoop1 = wx.StaticText(self.panel_grid_loop, wx.ID_ANY, "LabelLoop1")
        self.LabelLoop2 = wx.StaticText(self.panel_grid_loop, wx.ID_ANY, "LabelLoop2")
        self.LabelLoop3 = wx.StaticText(self.panel_grid_loop, wx.ID_ANY, "LabelLoop3")
        self.ListLoop1 = wx.ListCtrl(self.panel_grid_loop, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_REPORT | wx.LC_SINGLE_SEL)
        self.ListLoop2 = wx.ListCtrl(self.panel_grid_loop, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_REPORT | wx.LC_SINGLE_SEL)
        self.ListLoop3 = wx.ListCtrl(self.panel_grid_loop, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_REPORT | wx.LC_SINGLE_SEL)
        self.panel_output_location = wx.Panel(self, wx.ID_ANY)
        self.ButtonBrowse = wx.Button(self.panel_output_location, wx.ID_ANY, "&Browse...")
        self.LabelFilename = wx.StaticText(self.panel_output_location, wx.ID_ANY, "filename goes here...")
        self.label_1 = wx.StaticText(self, wx.ID_ANY, "Comment:")
        self.TextComment = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.panel_format_specific_parameters = wx.Panel(self, wx.ID_ANY)
        self.panel_parameters_lcmodel = wx.Panel(self.panel_format_specific_parameters, wx.ID_ANY)
        self.TextLcmFmtdat = wx.TextCtrl(self.panel_parameters_lcmodel, wx.ID_ANY, "(2E16.6)")
        self.label_13 = wx.StaticText(self.panel_parameters_lcmodel, wx.ID_ANY, "TRAMP:")
        self.FloatLcmTramp = FloatSpin(self.panel_parameters_lcmodel, wx.ID_ANY, value=1.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatLcmVolume = FloatSpin(self.panel_parameters_lcmodel, wx.ID_ANY, value=1.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatLcmSweepWidth = FloatSpin(self.panel_parameters_lcmodel, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.SpinLcmDataPoints = wx.SpinCtrl(self.panel_parameters_lcmodel, wx.ID_ANY, "", min=0, max=100, style=0)
        self.label_10 = wx.StaticText(self.panel_parameters_lcmodel, wx.ID_ANY, "Apodize [Hz]:")
        self.FloatLcmApodize = FloatSpin(self.panel_parameters_lcmodel, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.ChoiceLcmLineshape = wx.Choice(self.panel_parameters_lcmodel, wx.ID_ANY, choices=["Gaussian", "Lorentzian"])
        self.CheckLcmSinglet = wx.CheckBox(self.panel_parameters_lcmodel, wx.ID_ANY, "Add singlet at 0.0 PPM  ")
        self.panel_parameters_metabolitereport = wx.Panel(self.panel_format_specific_parameters, wx.ID_ANY)
        self.TextMetrepPulseq = wx.TextCtrl(self.panel_parameters_metabolitereport, wx.ID_ANY, "se")
        self.label_13_copy = wx.StaticText(self.panel_parameters_metabolitereport, wx.ID_ANY, "Echo String:")
        self.TextMetrepEcho = wx.TextCtrl(self.panel_parameters_metabolitereport, wx.ID_ANY, "030")
        self.FloatMetrepField = FloatSpin(self.panel_parameters_metabolitereport, wx.ID_ANY, value=3.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.SpinMetrepOffset = wx.SpinCtrl(self.panel_parameters_metabolitereport, wx.ID_ANY, "", min=0, max=100, style=0)
        self.FloatMetrepTime1 = FloatSpin(self.panel_parameters_metabolitereport, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatMetrepTime2 = FloatSpin(self.panel_parameters_metabolitereport, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatMetrepTime3 = FloatSpin(self.panel_parameters_metabolitereport, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatMetrepTimeMix = FloatSpin(self.panel_parameters_metabolitereport, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.FloatMetrepSweepWidth = FloatSpin(self.panel_parameters_metabolitereport, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.SpinMetrepDataPoints = wx.SpinCtrl(self.panel_parameters_metabolitereport, wx.ID_ANY, "", min=0, max=100, style=0)
        self.label_10_copy_1 = wx.StaticText(self.panel_parameters_metabolitereport, wx.ID_ANY, "Apodize [Hz]:")
        self.FloatMetrepApodize = FloatSpin(self.panel_parameters_metabolitereport, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.ChoiceMetrepLineshape = wx.Choice(self.panel_parameters_metabolitereport, wx.ID_ANY, choices=["Gaussian", "Lorentzian"])
        self.panel_parameters_jmruitext = wx.Panel(self.panel_format_specific_parameters, wx.ID_ANY)
        self.FloatJmruiSweepWidth = FloatSpin(self.panel_parameters_jmruitext, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.SpinJmruiDataPoints = wx.SpinCtrl(self.panel_parameters_jmruitext, wx.ID_ANY, "", min=0, max=100, style=0)
        self.label_10_copy_2 = wx.StaticText(self.panel_parameters_jmruitext, wx.ID_ANY, "Apodize [Hz]:")
        self.FloatJmruiApodize = FloatSpin(self.panel_parameters_jmruitext, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=0)
        self.ChoiceJmruiLineshape = wx.Choice(self.panel_parameters_jmruitext, wx.ID_ANY, choices=["Gaussian", "Lorentzian"])
        self.PanelMixedMetabolites = wx.Panel(self, wx.ID_ANY)
        self.ScrolledWindowDynamicList = wx.ScrolledWindow(self.PanelMixedMetabolites, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.LabelMetaboliteListGridSizerPlaceholder = wx.StaticText(self.ScrolledWindowDynamicList, wx.ID_ANY, "LabelMetaboliteListGridSizerPlaceholder")
        self.ButtonSelectAll = wx.Button(self.PanelMixedMetabolites, wx.ID_ANY, "Select All")
        self.ButtonDeselectAll = wx.Button(self.PanelMixedMetabolites, wx.ID_ANY, "De-Select All")
        self.ButtonAddMetabolite = wx.Button(self.PanelMixedMetabolites, wx.ID_ANY, "Add Metabolite")
        self.ButtonRemoveSelected = wx.Button(self.PanelMixedMetabolites, wx.ID_ANY, "Remove Selected")
        self.ButtonCreateMixture = wx.Button(self.PanelMixedMetabolites, wx.ID_ANY, "Add Metabolite Mixture ...")
        self.LabelStatus = wx.StaticText(self, wx.ID_ANY, "Welcome")
        self.LabelOkCancelPlaceholder = wx.StaticText(self, wx.ID_ANY, "LabelOkCancelPlaceholder", style=wx.ALIGN_RIGHT)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_list_select, self.ListLoop1)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_list_select, self.ListLoop2)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_list_select, self.ListLoop3)
        self.Bind(wx.EVT_BUTTON, self.on_browse, self.ButtonBrowse)
        self.Bind( EVT_FLOATSPIN, self.on_sweep_width, self.FloatLcmSweepWidth)
        self.Bind(wx.EVT_SPINCTRL, self.on_data_points, self.SpinLcmDataPoints)
        self.Bind( EVT_FLOATSPIN, self.on_apodize, self.FloatLcmApodize)
        self.Bind(wx.EVT_CHOICE, self.on_lineshape, self.ChoiceLcmLineshape)
        self.Bind( EVT_FLOATSPIN, self.on_sweep_width, self.FloatMetrepSweepWidth)
        self.Bind(wx.EVT_SPINCTRL, self.on_data_points, self.SpinMetrepDataPoints)
        self.Bind( EVT_FLOATSPIN, self.on_apodize, self.FloatMetrepApodize)
        self.Bind(wx.EVT_CHOICE, self.on_lineshape, self.ChoiceMetrepLineshape)
        self.Bind( EVT_FLOATSPIN, self.on_sweep_width, self.FloatJmruiSweepWidth)
        self.Bind(wx.EVT_SPINCTRL, self.on_data_points, self.SpinJmruiDataPoints)
        self.Bind( EVT_FLOATSPIN, self.on_apodize, self.FloatJmruiApodize)
        self.Bind(wx.EVT_CHOICE, self.on_lineshape, self.ChoiceJmruiLineshape)
        self.Bind(wx.EVT_BUTTON, self.on_select_all, self.ButtonSelectAll)
        self.Bind(wx.EVT_BUTTON, self.on_deselect_all, self.ButtonDeselectAll)
        self.Bind(wx.EVT_BUTTON, self.on_add_metabolite, self.ButtonAddMetabolite)
        self.Bind(wx.EVT_BUTTON, self.on_remove_selected, self.ButtonRemoveSelected)
        self.Bind(wx.EVT_BUTTON, self.on_add_mixture, self.ButtonCreateMixture)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("Mixed Metabolite Output")
        self.TextComment.SetMinSize((640, 45))
        self.TextLcmFmtdat.SetMinSize((70, -1))
        self.FloatLcmTramp.SetMinSize((70, -1))
        self.FloatLcmVolume.SetMinSize((70, -1))
        self.FloatLcmSweepWidth.SetMinSize((70, -1))
        self.SpinLcmDataPoints.SetMinSize((70, -1))
        self.FloatLcmApodize.SetMinSize((70, -1))
        self.ChoiceLcmLineshape.SetSelection(0)
        self.CheckLcmSinglet.SetValue(1)
        self.TextMetrepPulseq.SetMinSize((70, -1))
        self.TextMetrepEcho.SetMinSize((70, -1))
        self.FloatMetrepField.SetMinSize((70, -1))
        self.SpinMetrepOffset.SetMinSize((70, -1))
        self.FloatMetrepTime1.SetMinSize((70, -1))
        self.FloatMetrepTime2.SetMinSize((70, -1))
        self.FloatMetrepTime3.SetMinSize((70, -1))
        self.FloatMetrepTimeMix.SetMinSize((70, -1))
        self.FloatMetrepSweepWidth.SetMinSize((70, -1))
        self.SpinMetrepDataPoints.SetMinSize((70, -1))
        self.FloatMetrepApodize.SetMinSize((70, -1))
        self.ChoiceMetrepLineshape.SetSelection(0)
        self.panel_parameters_metabolitereport.Hide()
        self.FloatJmruiSweepWidth.SetMinSize((70, -1))
        self.SpinJmruiDataPoints.SetMinSize((70, -1))
        self.FloatJmruiApodize.SetMinSize((70, -1))
        self.ChoiceJmruiLineshape.SetSelection(0)
        self.ScrolledWindowDynamicList.SetScrollRate(10, 10)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.StaticBoxSizer(wx.StaticBox(self.PanelMixedMetabolites, wx.ID_ANY, "Metabolite and Mixed Metabolites Output List"), wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        MetaboliteListGridSizer = wx.FlexGridSizer(1, 7, 5, 5)
        sizer_6 = wx.StaticBoxSizer(wx.StaticBox(self.panel_format_specific_parameters, wx.ID_ANY, "Format Specific Parameters"), wx.VERTICAL)
        sizer_14_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_11_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_13_copy_1 = wx.StaticBoxSizer(wx.StaticBox(self.panel_parameters_jmruitext, wx.ID_ANY, "FID Creation"), wx.VERTICAL)
        sizer_15_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        sizer_13_copy = wx.StaticBoxSizer(wx.StaticBox(self.panel_parameters_metabolitereport, wx.ID_ANY, "FID Creation"), wx.VERTICAL)
        sizer_15_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18 = wx.StaticBoxSizer(wx.StaticBox(self.panel_parameters_metabolitereport, wx.ID_ANY, "Header Parameters"), wx.VERTICAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_19 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.StaticBoxSizer(wx.StaticBox(self.panel_parameters_lcmodel, wx.ID_ANY, "FID Creation"), wx.VERTICAL)
        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.StaticBoxSizer(wx.StaticBox(self.panel_parameters_lcmodel, wx.ID_ANY, "Header Paramters"), wx.HORIZONTAL)
        sizer_4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Experiment indices, Output location and Comment"), wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1_copy = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 3, 5, 15)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.LabelInstructions, 0, wx.EXPAND, 0)
        sizer_1_copy.Add(sizer_3, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 10)
        grid_sizer_1.Add(self.LabelLoop1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.LabelLoop2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.LabelLoop3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.ListLoop1, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.ListLoop2, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.ListLoop3, 0, wx.EXPAND, 0)
        self.panel_grid_loop.SetSizer(grid_sizer_1)
        grid_sizer_1.AddGrowableRow(1)
        sizer_1_copy.Add(self.panel_grid_loop, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_1_copy, 1, wx.EXPAND, 0)
        label_4 = wx.StaticText(self.panel_output_location, wx.ID_ANY, "Output Location:")
        sizer_9.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 4)
        sizer_9.Add(self.ButtonBrowse, 0, wx.RIGHT, 10)
        sizer_9.Add(self.LabelFilename, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_23.Add(sizer_9, 1, wx.BOTTOM | wx.EXPAND | wx.TOP, 10)
        self.panel_output_location.SetSizer(sizer_23)
        sizer_4.Add(self.panel_output_location, 0, wx.ALL | wx.EXPAND, 4)
        sizer_2.Add(self.label_1, 0, wx.BOTTOM | wx.TOP, 4)
        sizer_2.Add(self.TextComment, 0, wx.EXPAND, 0)
        sizer_4.Add(sizer_2, 0, wx.BOTTOM | wx.EXPAND, 5)
        sizer_1.Add(sizer_4, 0, wx.EXPAND | wx.TOP, 5)
        label_12 = wx.StaticText(self.panel_parameters_lcmodel, wx.ID_ANY, "FMTDAT:")
        sizer_12.Add(label_12, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_12.Add(self.TextLcmFmtdat, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_12.Add(self.label_13, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_12.Add(self.FloatLcmTramp, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_14 = wx.StaticText(self.panel_parameters_lcmodel, wx.ID_ANY, "VOLUME:")
        sizer_12.Add(label_14, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_12.Add(self.FloatLcmVolume, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_11.Add(sizer_12, 0, wx.EXPAND | wx.LEFT | wx.TOP, 4)
        label_8 = wx.StaticText(self.panel_parameters_lcmodel, wx.ID_ANY, "Sweep Width [Hz]:")
        sizer_15.Add(label_8, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_15.Add(self.FloatLcmSweepWidth, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_9 = wx.StaticText(self.panel_parameters_lcmodel, wx.ID_ANY, "Data Points:")
        sizer_15.Add(label_9, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_15.Add(self.SpinLcmDataPoints, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_15.Add(self.label_10, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_15.Add(self.FloatLcmApodize, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_11 = wx.StaticText(self.panel_parameters_lcmodel, wx.ID_ANY, "    Lineshape: ")
        sizer_15.Add(label_11, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_15.Add(self.ChoiceLcmLineshape, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_13.Add(sizer_15, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        sizer_16.Add(self.CheckLcmSinglet, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 8)
        sizer_13.Add(sizer_16, 0, wx.EXPAND, 0)
        sizer_11.Add(sizer_13, 0, wx.EXPAND | wx.LEFT, 4)
        sizer_14.Add(sizer_11, 0, wx.EXPAND, 0)
        self.panel_parameters_lcmodel.SetSizer(sizer_14)
        sizer_6.Add(self.panel_parameters_lcmodel, 0, wx.EXPAND, 0)
        label_12_copy = wx.StaticText(self.panel_parameters_metabolitereport, wx.ID_ANY, "PulSeq String:")
        sizer_19.Add(label_12_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_19.Add(self.TextMetrepPulseq, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_19.Add(self.label_13_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_19.Add(self.TextMetrepEcho, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_14_copy = wx.StaticText(self.panel_parameters_metabolitereport, wx.ID_ANY, "B0 Field [T]:")
        sizer_19.Add(label_14_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_19.Add(self.FloatMetrepField, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_14_copy_copy = wx.StaticText(self.panel_parameters_metabolitereport, wx.ID_ANY, "Offset [pts]:")
        sizer_19.Add(label_14_copy_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_19.Add(self.SpinMetrepOffset, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_18.Add(sizer_19, 1, wx.EXPAND, 0)
        label_8_copy_1_copy = wx.StaticText(self.panel_parameters_metabolitereport, wx.ID_ANY, "PulseTime1 [s]:")
        sizer_20.Add(label_8_copy_1_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_20.Add(self.FloatMetrepTime1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_8_copy_1_copy_1 = wx.StaticText(self.panel_parameters_metabolitereport, wx.ID_ANY, "PulseTime2 [s]:")
        sizer_20.Add(label_8_copy_1_copy_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_20.Add(self.FloatMetrepTime2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_8_copy_1_copy_3 = wx.StaticText(self.panel_parameters_metabolitereport, wx.ID_ANY, "PulseTime3 [s]:")
        sizer_20.Add(label_8_copy_1_copy_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_20.Add(self.FloatMetrepTime3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_8_copy_1_copy_2 = wx.StaticText(self.panel_parameters_metabolitereport, wx.ID_ANY, "MixTime [s]:")
        sizer_20.Add(label_8_copy_1_copy_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_20.Add(self.FloatMetrepTimeMix, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_18.Add(sizer_20, 1, wx.EXPAND, 0)
        sizer_10.Add(sizer_18, 1, wx.EXPAND | wx.LEFT | wx.TOP, 4)
        label_8_copy_1 = wx.StaticText(self.panel_parameters_metabolitereport, wx.ID_ANY, "Sweep Width [Hz]:")
        sizer_15_copy.Add(label_8_copy_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_15_copy.Add(self.FloatMetrepSweepWidth, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_9_copy_1 = wx.StaticText(self.panel_parameters_metabolitereport, wx.ID_ANY, "Data Points:")
        sizer_15_copy.Add(label_9_copy_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_15_copy.Add(self.SpinMetrepDataPoints, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_15_copy.Add(self.label_10_copy_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_15_copy.Add(self.FloatMetrepApodize, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_11_copy_1 = wx.StaticText(self.panel_parameters_metabolitereport, wx.ID_ANY, "    Lineshape: ")
        sizer_15_copy.Add(label_11_copy_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_15_copy.Add(self.ChoiceMetrepLineshape, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_13_copy.Add(sizer_15_copy, 0, wx.EXPAND, 0)
        sizer_10.Add(sizer_13_copy, 0, wx.EXPAND | wx.LEFT, 4)
        self.panel_parameters_metabolitereport.SetSizer(sizer_10)
        sizer_6.Add(self.panel_parameters_metabolitereport, 0, wx.EXPAND, 0)
        label_8_copy_2 = wx.StaticText(self.panel_parameters_jmruitext, wx.ID_ANY, "Sweep Width [Hz]:")
        sizer_15_copy_1.Add(label_8_copy_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_15_copy_1.Add(self.FloatJmruiSweepWidth, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_9_copy_2 = wx.StaticText(self.panel_parameters_jmruitext, wx.ID_ANY, "Data Points:")
        sizer_15_copy_1.Add(label_9_copy_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_15_copy_1.Add(self.SpinJmruiDataPoints, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_15_copy_1.Add(self.label_10_copy_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_15_copy_1.Add(self.FloatJmruiApodize, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_11_copy_2 = wx.StaticText(self.panel_parameters_jmruitext, wx.ID_ANY, "    Lineshape: ")
        sizer_15_copy_1.Add(label_11_copy_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.BOTTOM | wx.LEFT | wx.TOP, 6)
        sizer_15_copy_1.Add(self.ChoiceJmruiLineshape, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_13_copy_1.Add(sizer_15_copy_1, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        sizer_11_copy.Add(sizer_13_copy_1, 0, wx.EXPAND | wx.LEFT, 4)
        sizer_14_copy.Add(sizer_11_copy, 0, wx.EXPAND, 0)
        self.panel_parameters_jmruitext.SetSizer(sizer_14_copy)
        sizer_6.Add(self.panel_parameters_jmruitext, 0, wx.EXPAND, 0)
        self.panel_format_specific_parameters.SetSizer(sizer_6)
        sizer_1.Add(self.panel_format_specific_parameters, 0, wx.EXPAND, 0)
        MetaboliteListGridSizer.Add(self.LabelMetaboliteListGridSizerPlaceholder, 0, 0, 0)
        MetaboliteListGridSizer.Add((0, 0), 0, 0, 0)
        MetaboliteListGridSizer.Add((0, 0), 0, 0, 0)
        MetaboliteListGridSizer.Add((0, 0), 0, 0, 0)
        MetaboliteListGridSizer.Add((0, 0), 0, 0, 0)
        MetaboliteListGridSizer.Add((0, 0), 0, 0, 0)
        MetaboliteListGridSizer.Add((0, 0), 0, 0, 0)
        self.ScrolledWindowDynamicList.SetSizer(MetaboliteListGridSizer)
        sizer_7.Add(self.ScrolledWindowDynamicList, 1, wx.BOTTOM | wx.EXPAND, 5)
        sizer_8.Add(self.ButtonSelectAll, 0, wx.RIGHT, 5)
        sizer_8.Add(self.ButtonDeselectAll, 0, wx.RIGHT, 5)
        sizer_8.Add(self.ButtonAddMetabolite, 0, wx.RIGHT, 5)
        sizer_8.Add(self.ButtonRemoveSelected, 0, wx.RIGHT, 5)
        sizer_8.Add(self.ButtonCreateMixture, 0, wx.RIGHT, 5)
        sizer_7.Add(sizer_8, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 5)
        self.PanelMixedMetabolites.SetSizer(sizer_7)
        sizer_1.Add(self.PanelMixedMetabolites, 1, wx.EXPAND, 0)
        sizer_5.Add(self.LabelStatus, 1, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT | wx.TOP, 10)
        sizer_5.Add(self.LabelOkCancelPlaceholder, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(sizer_5, 0, wx.BOTTOM | wx.EXPAND | wx.RIGHT | wx.TOP, 10)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def on_list_select(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_list_select' not implemented!")
        event.Skip()

    def on_browse(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_browse' not implemented!")
        event.Skip()

    def on_sweep_width(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_sweep_width' not implemented!")
        event.Skip()

    def on_data_points(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_data_points' not implemented!")
        event.Skip()

    def on_apodize(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_apodize' not implemented!")
        event.Skip()

    def on_lineshape(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_lineshape' not implemented!")
        event.Skip()

    def on_select_all(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_select_all' not implemented!")
        event.Skip()

    def on_deselect_all(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_deselect_all' not implemented!")
        event.Skip()

    def on_add_metabolite(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_add_metabolite' not implemented!")
        event.Skip()

    def on_remove_selected(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_remove_selected' not implemented!")
        event.Skip()

    def on_add_mixture(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_add_mixture' not implemented!")
        event.Skip()

# end of class MyDialog
