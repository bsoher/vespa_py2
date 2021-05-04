# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Wed Sep 11 12:19:22 2019
#

import wx
from wx.lib.agw.floatspin import FloatSpin, EVT_FLOATSPIN, FS_LEFT, FS_RIGHT, FS_CENTRE, FS_READONLY

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1314, 1069))
        self.PanelMetabolite = wx.Panel(self, wx.ID_ANY)
        self.ButtonPriorInformationFromDatabase = wx.Button(self.PanelMetabolite, wx.ID_ANY, "Prior Information From Database...")
        self.ButtonPriorInformationFromFile = wx.Button(self.PanelMetabolite, wx.ID_ANY, "Prior Information from File...")
        self.TextPriorInformationSource = wx.TextCtrl(self.PanelMetabolite, wx.ID_ANY, "", style=wx.TE_READONLY)
        self.FloatPriorPpmStart = FloatSpin(self.PanelMetabolite, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=wx.SP_ARROW_KEYS | wx.TE_PROCESS_ENTER)
        self.FloatPriorPpmEnd = FloatSpin(self.PanelMetabolite, wx.ID_ANY, value=0.0, digits=3, min_val=0.0, max_val=100.0, increment=1.0, agwStyle=FS_LEFT, style=wx.SP_ARROW_KEYS | wx.TE_PROCESS_ENTER)
        self.PanelMetaboliteLines = wx.ScrolledWindow(self.PanelMetabolite, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.LabelMetabolites = wx.StaticText(self.PanelMetaboliteLines, wx.ID_ANY, "placeholder")
        self.ComboLineshapeModel = wx.ComboBox(self.PanelMetabolite, wx.ID_ANY, choices=["Voigt", "Gaussian", "Lorentzian"], style=wx.CB_READONLY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_prior_information_from_database, self.ButtonPriorInformationFromDatabase)
        self.Bind(wx.EVT_BUTTON, self.on_prior_information_from_file, self.ButtonPriorInformationFromFile)
        self.Bind( EVT_FLOATSPIN, self.on_prior_ppm_start, self.FloatPriorPpmStart)
        self.Bind( EVT_FLOATSPIN, self.on_prior_ppm_end, self.FloatPriorPpmEnd)
        self.Bind(wx.EVT_COMBOBOX, self.on_lineshape_model, self.ComboLineshapeModel)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        self.PanelMetaboliteLines.SetScrollRate(10, 10)
        self.ComboLineshapeModel.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.StaticBoxSizer(wx.StaticBox(self.PanelMetabolite, wx.ID_ANY, "Metabolites In Model"), wx.VERTICAL)
        MetaboliteGridSizer = wx.FlexGridSizer(1, 7, 5, 5)
        sizer_53 = wx.StaticBoxSizer(wx.StaticBox(self.PanelMetabolite, wx.ID_ANY, "Metabolite Prior Information"), wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17.Add(self.ButtonPriorInformationFromDatabase, 0, wx.RIGHT, 4)
        sizer_17.Add(self.ButtonPriorInformationFromFile, 0, 0, 0)
        sizer_53.Add(sizer_17, 1, wx.ALL | wx.EXPAND, 4)
        label_3 = wx.StaticText(self.PanelMetabolite, wx.ID_ANY, "Source:")
        sizer_7.Add(label_3, 0, wx.ALL, 4)
        sizer_7.Add(self.TextPriorInformationSource, 1, 0, 0)
        sizer_53.Add(sizer_7, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        labelPeakRange = wx.StaticText(self.PanelMetabolite, wx.ID_ANY, "Peak Include Range [ppm]  -")
        sizer_8.Add(labelPeakRange, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 3)
        labelStart = wx.StaticText(self.PanelMetabolite, wx.ID_ANY, "Start: ")
        sizer_8.Add(labelStart, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 2)
        sizer_8.Add(self.FloatPriorPpmStart, 0, 0, 0)
        labelEnd = wx.StaticText(self.PanelMetabolite, wx.ID_ANY, "End: ")
        sizer_8.Add(labelEnd, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 10)
        sizer_8.Add(self.FloatPriorPpmEnd, 0, wx.LEFT, 0)
        sizer_53.Add(sizer_8, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        sizer_11.Add(sizer_53, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 8)
        MetaboliteGridSizer.Add(self.LabelMetabolites, 0, wx.ALL, 2)
        MetaboliteGridSizer.Add((0, 0), 0, 0, 0)
        MetaboliteGridSizer.Add((0, 0), 0, 0, 0)
        MetaboliteGridSizer.Add((0, 0), 0, 0, 0)
        self.PanelMetaboliteLines.SetSizer(MetaboliteGridSizer)
        sizer_16.Add(self.PanelMetaboliteLines, 1, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        sizer_11.Add(sizer_16, 1, wx.EXPAND, 0)
        label_2 = wx.StaticText(self.PanelMetabolite, wx.ID_ANY, "Lineshape Model:")
        sizer_14.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 4)
        sizer_14.Add(self.ComboLineshapeModel, 0, wx.RIGHT, 4)
        sizer_11.Add(sizer_14, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 4)
        self.PanelMetabolite.SetSizer(sizer_11)
        sizer_1.Add(self.PanelMetabolite, 0, 0, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_prior_information_from_database(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_prior_information_from_database' not implemented!")
        event.Skip()

    def on_prior_information_from_file(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_prior_information_from_file' not implemented!")
        event.Skip()

    def on_prior_ppm_start(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_prior_ppm_start' not implemented!")
        event.Skip()

    def on_prior_ppm_end(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_prior_ppm_end' not implemented!")
        event.Skip()

    def on_lineshape_model(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Event handler 'on_lineshape_model' not implemented!")
        event.Skip()

# end of class MyFrame