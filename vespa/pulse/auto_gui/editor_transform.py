# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 12:55:20 2019
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
        self.NotebookTools = wx.Notebook(self, wx.ID_ANY, style=0)
        self.PanelDesign = wx.Panel(self.NotebookTools, wx.ID_ANY)
        self.SplitDesign = wx.SplitterWindow(self.PanelDesign, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
        self.PanelDesignControls = wx.Panel(self.SplitDesign, wx.ID_ANY)
        self.TextName = wx.TextCtrl(self.PanelDesignControls, wx.ID_ANY, "")
        self.TextMenuLabel = wx.TextCtrl(self.PanelDesignControls, wx.ID_ANY, "")
        self.TextCreator = wx.TextCtrl(self.PanelDesignControls, wx.ID_ANY, "")
        self.ChoiceType = wx.Choice(self.PanelDesignControls, wx.ID_ANY, choices=["Create Transform", "Modify Transform"])
        self.LabelUuid = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "xxxxxxxx-yyyy-zzzz-1111-222222222222")
        self.LabelCreated = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "timestamp goes here")
        self.CheckFile1 = wx.CheckBox(self.PanelDesignControls, wx.ID_ANY, " Hide")
        self.TextFile1Label = wx.TextCtrl(self.PanelDesignControls, wx.ID_ANY, "")
        self.CheckFile2 = wx.CheckBox(self.PanelDesignControls, wx.ID_ANY, " Hide")
        self.TextFile2Label = wx.TextCtrl(self.PanelDesignControls, wx.ID_ANY, "")
        self.CheckTimeSteps = wx.CheckBox(self.PanelDesignControls, wx.ID_ANY, " Hide")
        self.TextTimeSteps = wx.TextCtrl(self.PanelDesignControls, wx.ID_ANY, "")
        self.CheckDuration = wx.CheckBox(self.PanelDesignControls, wx.ID_ANY, " Hide")
        self.TextDuration = wx.TextCtrl(self.PanelDesignControls, wx.ID_ANY, "")
        self.CheckTipAngle = wx.CheckBox(self.PanelDesignControls, wx.ID_ANY, " Hide")
        self.TextTipAngle = wx.TextCtrl(self.PanelDesignControls, wx.ID_ANY, "")
        self.CheckBandwidth = wx.CheckBox(self.PanelDesignControls, wx.ID_ANY, " Hide")
        self.TextBandwidth = wx.TextCtrl(self.PanelDesignControls, wx.ID_ANY, "")
        self.ButtonAddUserParameter = wx.Button(self.PanelDesignControls, wx.ID_ANY, "Add")
        self.ButtonRemoveUserParameter = wx.Button(self.PanelDesignControls, wx.ID_ANY, "Remove Selected")
        self.LabelPlaceholder1 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "LabelPlaceholder1")
        self.TextComment = wx.TextCtrl(self.PanelDesignControls, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.PanelDesignAlgorithm = wx.Panel(self.SplitDesign, wx.ID_ANY)
        self.PanelTest = wx.Panel(self.NotebookTools, wx.ID_ANY)
        self.SplitTest = wx.SplitterWindow(self.PanelTest, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
        self.PanelTransformBase = wx.Panel(self.SplitTest, wx.ID_ANY)
        self.PanelConsole = wx.Panel(self.SplitTest, wx.ID_ANY)
        self.TextConsole = wx.TextCtrl(self.PanelConsole, wx.ID_ANY, "\n", style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_WORDWRAP)
        self.LabelStatus0 = wx.StaticText(self, wx.ID_ANY, "box0")
        self.LabelStatus1 = wx.StaticText(self, wx.ID_ANY, "box1")
        self.LabelStatus2 = wx.StaticText(self, wx.ID_ANY, "box2")
        self.LabelStatus3 = wx.StaticText(self, wx.ID_ANY, "box3")
        self.LabelOkCancelPlaceholder = wx.StaticText(self, wx.ID_ANY, "   OK and Cancel Placeholder")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_add_user_parameter, self.ButtonAddUserParameter)
        self.Bind(wx.EVT_BUTTON, self.on_remove_user_parameter, self.ButtonRemoveUserParameter)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_page_changed, self.NotebookTools)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("dialog_1")
        self.ChoiceType.SetSelection(0)
        self.CheckFile1.SetValue(1)
        self.CheckFile2.SetValue(1)
        self.ButtonAddUserParameter.SetToolTip("A new parameter will be added to bottom of list")
        self.ButtonRemoveUserParameter.SetToolTip("Selected parameter rows will be deleted")
        self.SplitDesign.SetMinimumPaneSize(20)
        self.SplitTest.SetMinimumPaneSize(20)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        SizerTest = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.StaticBoxSizer(wx.StaticBox(self.PanelConsole, wx.ID_ANY, "Console"), wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_31 = wx.BoxSizer(wx.VERTICAL)
        sizer_33 = wx.StaticBoxSizer(wx.StaticBox(self.PanelDesignControls, wx.ID_ANY, "Comments"), wx.HORIZONTAL)
        sizer_user_parameters = wx.StaticBoxSizer(wx.StaticBox(self.PanelDesignControls, wx.ID_ANY, "User Defined Parameters (optional)"), wx.VERTICAL)
        grid_sizer_2 = wx.FlexGridSizer(1, 8, 5, 0)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_global_parameters = wx.StaticBoxSizer(wx.StaticBox(self.PanelDesignControls, wx.ID_ANY, "Global Parameters (required and optional)"), wx.VERTICAL)
        grid_sizer_8 = wx.FlexGridSizer(6, 4, 4, 4)
        sizer_transform_info = wx.StaticBoxSizer(wx.StaticBox(self.PanelDesignControls, wx.ID_ANY, "Identifying Information"), wx.HORIZONTAL)
        grid_sizer_1 = wx.FlexGridSizer(3, 4, 4, 4)
        label_1 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "Name:")
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.TextName, 0, wx.EXPAND, 0)
        label_14 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "Menu Label:")
        grid_sizer_1.Add(label_14, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.TextMenuLabel, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        label_12 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "Creator:")
        grid_sizer_1.Add(label_12, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.TextCreator, 0, wx.EXPAND, 0)
        label_2 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "Type:")
        grid_sizer_1.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.ChoiceType, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_11 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "UUID:")
        grid_sizer_1.Add(label_11, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.LabelUuid, 0, wx.EXPAND, 0)
        label_13 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "Created:")
        grid_sizer_1.Add(label_13, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.LabelCreated, 0, 0, 0)
        grid_sizer_1.AddGrowableCol(1)
        grid_sizer_1.AddGrowableCol(3)
        sizer_transform_info.Add(grid_sizer_1, 1, wx.BOTTOM | wx.EXPAND | wx.RIGHT, 4)
        sizer_31.Add(sizer_transform_info, 0, wx.ALL | wx.EXPAND, 4)
        grid_sizer_8.Add(self.CheckFile1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_1_copy = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, " File1     Top Label: ", style=wx.ALIGN_RIGHT)
        label_1_copy.SetMinSize((-1, -1))
        grid_sizer_8.Add(label_1_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_8.Add(self.TextFile1Label, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        grid_sizer_8.Add((20, 20), 0, 0, 0)
        grid_sizer_8.Add(self.CheckFile2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_6 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, " File2     Top Label: ", style=wx.ALIGN_RIGHT)
        label_6.SetMinSize((-1, -1))
        grid_sizer_8.Add(label_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_8.Add(self.TextFile2Label, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        grid_sizer_8.Add((20, 20), 0, 0, 0)
        grid_sizer_8.Add(self.CheckTimeSteps, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_9 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "Time Steps [increments]: ", style=wx.ALIGN_RIGHT)
        label_9.SetMinSize((123, -1))
        grid_sizer_8.Add(label_9, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_8.Add(self.TextTimeSteps, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        label_4 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "default")
        grid_sizer_8.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_8.Add(self.CheckDuration, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_10 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "Duration [milliseconds]: ", style=wx.ALIGN_RIGHT)
        label_10.SetMinSize((115, -1))
        grid_sizer_8.Add(label_10, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_8.Add(self.TextDuration, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        label_5 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "default")
        grid_sizer_8.Add(label_5, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_8.Add(self.CheckTipAngle, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_8 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "Tip Angle [degrees]: ", style=wx.ALIGN_RIGHT)
        label_8.SetMinSize((102, -1))
        grid_sizer_8.Add(label_8, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_8.Add(self.TextTipAngle, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        label_3 = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "default")
        grid_sizer_8.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_8.Add(self.CheckBandwidth, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_11_copy = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "Bandwidth [kilohertz]: ", style=wx.ALIGN_RIGHT)
        label_11_copy.SetMinSize((109, -1))
        grid_sizer_8.Add(label_11_copy, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 0)
        grid_sizer_8.Add(self.TextBandwidth, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
        label_12_copy = wx.StaticText(self.PanelDesignControls, wx.ID_ANY, "default")
        grid_sizer_8.Add(label_12_copy, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_8.AddGrowableCol(2)
        sizer_global_parameters.Add(grid_sizer_8, 1, wx.EXPAND, 0)
        sizer_31.Add(sizer_global_parameters, 0, wx.ALL | wx.EXPAND, 6)
        sizer_6.Add(self.ButtonAddUserParameter, 0, wx.RIGHT, 5)
        sizer_6.Add(self.ButtonRemoveUserParameter, 0, wx.LEFT, 5)
        sizer_user_parameters.Add(sizer_6, 0, wx.BOTTOM | wx.EXPAND, 10)
        grid_sizer_2.Add(self.LabelPlaceholder1, 0, 0, 0)
        grid_sizer_2.AddGrowableCol(3)
        grid_sizer_2.AddGrowableCol(5)
        grid_sizer_2.AddGrowableCol(7)
        sizer_user_parameters.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        sizer_31.Add(sizer_user_parameters, 0, wx.ALL | wx.EXPAND, 4)
        sizer_33.Add(self.TextComment, 1, wx.EXPAND, 0)
        sizer_31.Add(sizer_33, 1, wx.EXPAND, 0)
        self.PanelDesignControls.SetSizer(sizer_31)
        self.SplitDesign.SplitVertically(self.PanelDesignControls, self.PanelDesignAlgorithm)
        sizer_7.Add(self.SplitDesign, 1, wx.EXPAND, 0)
        self.PanelDesign.SetSizer(sizer_7)
        sizer_5.Add(self.TextConsole, 1, wx.EXPAND, 0)
        self.PanelConsole.SetSizer(sizer_5)
        self.SplitTest.SplitHorizontally(self.PanelTransformBase, self.PanelConsole)
        SizerTest.Add(self.SplitTest, 1, wx.EXPAND, 0)
        self.PanelTest.SetSizer(SizerTest)
        self.NotebookTools.AddPage(self.PanelDesign, "Design")
        self.NotebookTools.AddPage(self.PanelTest, "Test")
        sizer_1.Add(self.NotebookTools, 1, wx.EXPAND, 0)
        sizer_2.Add(self.LabelStatus0, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.LabelStatus1, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.LabelStatus2, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.LabelStatus3, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.LabelOkCancelPlaceholder, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(sizer_2, 0, wx.ALL | wx.EXPAND, 6)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def on_add_user_parameter(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_add_user_parameter' not implemented!")
        event.Skip()

    def on_remove_user_parameter(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_remove_user_parameter' not implemented!")
        event.Skip()

    def on_page_changed(self, event):  # wxGlade: MyDialog.<event_handler>
        print("Event handler 'on_page_changed' not implemented!")
        event.Skip()

# end of class MyDialog
