#!/usr/bin/env python

# Python modules
from __future__ import division
import os
import struct
import webbrowser

# 3rd party modules
import wx
#import wx.aui as aui
import wx.adv as wx_adv
import wx.lib.agw.aui as aui        # NB. wx.aui version throws odd wxWidgets exception on Close/Exit, ?? Not anymore in wxPython 4.0.6 ??

# Our modules
import vespa.priorset.images as images
import vespa.priorset.mrs_priorset as mrs_priorset
import vespa.priorset.notebook_priorset as notebook_priorset
import vespa.priorset.util_menu as util_menu
import vespa.priorset.util_import as util_import
import vespa.priorset.util_priorset_config as util_priorset_config

import vespa.common.util.init as util_init
import vespa.common.util.export as util_export
import vespa.common.util.misc as util_misc
import vespa.common.wx_gravy.util as wx_util
import vespa.common.wx_gravy.common_dialogs as common_dialogs
import vespa.common.dialog_export as dialog_export
import vespa.common.dialog_experiment_browser as dialog_experiment_browser
import vespa.common.util.db as common_util_db


class Main(wx.Frame):    
    def __init__(self, db, position, size):
        # Create a frame using values from our INI file.
        self._left,  self._top    = position
        self._width, self._height = size
    
        style = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX |  \
                wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.RESIZE_BORDER |       \
                wx.CLIP_CHILDREN

        wx.Frame.__init__(self, None, wx.ID_ANY, "Priorset",
                          (self._left, self._top),
                          (self._width, self._height), style)

        self.db = db
        
        # GUI Creation ----------------------------------------------

        self._mgr = aui.AuiManager()
        self._mgr.SetManagedWindow(self)

        self.SetIcon(images.Mondrian.GetIcon())

        self.statusbar = self.CreateStatusBar(4, 0)
        self.statusbar.SetStatusText("Ready")

        bar = util_menu.PriorsetMenuBar(self)
        self.SetMenuBar(bar)
        util_menu.bar = bar

        self.build_panes()
        self.bind_events()


        
    def build_panes(self):
        
        self.notebook_priorsets = notebook_priorset.NotebookPriorset(self)

        # create center pane
        self._mgr.AddPane(self.notebook_priorsets, 
                          aui.AuiPaneInfo().
                          Name("notebook_priorsets").
                          CenterPane().
                          PaneBorder(False))
                          
        # "commit" all changes made to AuiManager
        self._mgr.Update()                          
                          


    def bind_events(self):
        self.Bind(wx.EVT_CLOSE, self.on_self_close)
        self.Bind(wx.EVT_SIZE, self.on_self_coordinate_change)
        self.Bind(wx.EVT_MOVE, self.on_self_coordinate_change)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.on_erase_background)


    def on_erase_background(self, event):
        event.Skip()


    ##############                                    ############
    ##############       Menu handlers are below      ############
    ##############       in the order they appear     ############
    ##############             on the menu            ############
    ##############                                    ############

    ############    Priorset menu

    def on_new(self, event):
        dialog = dialog_experiment_browser.DialogExperimentBrowser(self, self.db)
        dialog.ShowModal()

        if dialog.selected_experiment_id:
            wx.BeginBusyCursor()
            experiment = self.db.fetch_experiment(dialog.selected_experiment_id)
            priorset = mrs_priorset.Priorset()
            priorset.get_prior_from_experiment(experiment)
            self.notebook_priorsets.Freeze()
            self.notebook_priorsets.add_priorset_tab(priorset=priorset)
            self.notebook_priorsets.Thaw()
            self.notebook_priorsets.Layout()
            wx.EndBusyCursor()
            self.update_title()

    
    def on_open(self, event):
        wx.BeginBusyCursor()

        ini_name = "save_viff"
        default_path = util_priorset_config.get_path(ini_name)

        filetype_filter="Spectra (*.xml,*.xml.gz,*.viff,*.vif)|*.xml;*.xml.gz;*.viff;*.vif"
        filename = common_dialogs.pickfile(filetype_filter=filetype_filter,
                                            multiple=False,
                                            default_path=default_path)
        if filename:
            msg = ""
            try:
                importer = util_import.PriorsetImporter(filename)
            except IOError:
                msg = """I can't read the file "%s".""" % filename
            except SyntaxError:
                msg = """The file "%s" isn't valid Vespa Interchange File Format.""" % filename

            if msg:
                common_dialogs.message(msg, "Priorset - Open File", 
                                       common_dialogs.E_OK)
            else:
                # Time to rock and roll!
                wx.BeginBusyCursor()
                priorsets = importer.go()
                wx.EndBusyCursor()    

                if priorsets:
                    priorset = priorsets[0]
    
                    self.notebook_priorsets.Freeze()
                    self.notebook_priorsets.add_priorset_tab(priorset=priorset)
                    self.notebook_priorsets.Thaw()
                    self.notebook_priorsets.Layout()
                    self.update_title()
                    
                    path, _ = os.path.split(filename)
                    util_priorset_config.set_path(ini_name, path)
                else:
                    msg = """The file "%s" didn't contain any priorsets.""" % filename
                    common_dialogs.message(msg)
                
        wx.EndBusyCursor()                


    def on_save_viff(self, event, save_as=False):
        # This event is also called programmaticallyby on_save_as_viff().
        priorset = self.notebook_priorsets.active_tab.priorset

        filename = priorset.priorset_filename
        if filename and (not save_as):
            # This dataset already has a filename which means it's already
            # associated with a VIFF file. We don't bug the user for a 
            # filename, we just save it.
            pass
        else:
            if not filename:
                filename = priorset.experiment.name
            path, filename = os.path.split(filename)
            # The default filename is the current filename with the extension
            # changed to ".xml".
            filename = os.path.splitext(filename)[0] + ".xml"

            filename = common_dialogs.save_as("Save As XML/VIFF (Vespa Interchange Format File)",
                                              "VIFF/XML files (*.xml)|*.xml",
                                              path, filename)

        if filename:
            priorset.priorset_filename = filename
        
            self._save_viff(priorset)
        
        
    def on_save_as_viff(self, event):
        self.on_save_viff(event, True)        
        
        
    def on_close_priorset(self, event):
        self.notebook_priorsets.close_priorset()


    def on_export_spectrum_viff(self, event):
        if self.notebook_priorsets.active_tab:
            self.notebook_priorsets.active_tab.export_spectrum_to_viff()
    

    def on_export_monte_carlo_viff(self, event):
        if self.notebook_priorsets.active_tab:
            self.notebook_priorsets.active_tab.export_monte_carlo_to_viff()


    def on_export_spectrum_vasf(self, event):
        if self.notebook_priorsets.active_tab:
            self.notebook_priorsets.active_tab.export_spectrum_to_vasf()


    def on_export_spectrum_vasf_sid(self, event):
        if self.notebook_priorsets.active_tab:
            self.notebook_priorsets.active_tab.export_spectrum_to_vasf_sid()
    

    def on_export_monte_carlo_vasf(self, event):
        if self.notebook_priorsets.active_tab:
            self.notebook_priorsets.active_tab.export_monte_carlo_to_vasf()

    def on_export_spectrum_siemens_rda(self, event):
        if self.notebook_priorsets.active_tab:
            self.notebook_priorsets.active_tab.export_spectrum_to_siemens_rda()

    ############    View  menu
    
    # View options affect only the dataset and so it's up to the
    # experiment notebook to react to them.

    def on_menu_view_option(self, event):
        self.notebook_priorsets.on_menu_view_option(event)
        
    def on_menu_view_output(self, event):
        self.notebook_priorsets.on_menu_view_output(event)


    ############    Help menu

    def on_user_manual(self, event):
        path = util_misc.get_vespa_install_directory()
        path = os.path.join(path, "docs", "priorset_user_manual.pdf")
        wx_util.display_file(path)


    def on_vespa_help_online(self, event):
        webbrowser.open("http://scion.duhs.duke.edu/vespa", 1)


    def on_about(self, event):
        bit = str(8 * struct.calcsize('P')) + '-bit Python'
        info = wx_adv.AboutDialogInfo()
        info.SetVersion(util_misc.get_vespa_version())
        info.SetCopyright("Copyright 2012, Duke University. All rights reserved.")
        info.SetDescription("Priorset creates simulated data sets from the output of the Simulation application. Running on "+bit)
        info.SetWebSite("http://scion.duhs.duke.edu/vespa/")
        wx_adv.AboutBox(info)


    def on_show_inspection_tool(self, event):
        wx_util.show_wx_inspector(self)



    ############    Global Events
    
    def on_self_close(self, event):
        # I trap this so I can save my coordinates
        config = util_priorset_config.Config()

        config.set_window_coordinates("main", self._left, self._top, 
                                      self._width, self._height)

        config.write()
        
        self._mgr.UnInit()      # needed to avoid wx._core.wxAssertionError: C++ assertion "GetEventHandler() == this" failed at ..\..\src\common\wincmn.cpp 
        self.Destroy()


    def on_self_coordinate_change(self, event):
        # This is invoked for move & size events
        if self.IsMaximized() or self.IsIconized():
            # Bah, forget about this. Recording coordinates doesn't make sense
            # when the window is maximized or minimized. This is only a
            # concern on Windows; GTK and OS X don't produce move or size
            # events when a window is minimized or maximized.
            pass
        else:
            if event.GetEventType() == wx.wxEVT_MOVE:
                self._left, self._top = self.GetPosition()
            else:
                # This is a size event
                self._width, self._height = self.GetSize()


    
    ##############
    ##############   Public  functions  alphabetized  below
    ##############

    def update_title(self):
        """Updates the main window title to reflect the current dataset."""
        name = ""
        
        # Create an appropriate name for whatever is selected.
        tab = self.notebook_priorsets.active_tab
        if tab:
            filename = tab.priorset.priorset_filename
            if not filename:
                filename = tab.priorset.experiment.name
            name = " - " + os.path.split(filename)[1] 

        self.SetTitle("Prior" + name)
        
        
    ##############
    ##############   Private  functions  alphabetized  below
    ##############

    def _save_viff(self, priorset):    
        msg = ""
        filename = priorset.priorset_filename
        try:
            util_export.export(filename, [priorset], None, None, False)
            path, _ = os.path.split(filename)
            util_priorset_config.set_path("save_viff", path)
        except IOError:
            msg = """I can't write the file "%s".""" % filename

        if msg:
            common_dialogs.message(msg, style=common_dialogs.E_OK)
        else:
            # dataset.filename is an attribute set only at run-time to maintain
            # the name of the VIFF file that was read in rather than deriving 
            # a filename from the raw data filenames with *.xml appended. We 
            # set it here to indicate the current name that the dataset has 
            # been saved to VIFF file as.
            priorset.priorset_filename = filename
                    
        self.update_title()



#------------------------------------------------------------------------------

def main():

    # This function is for profiling with cProfile

    app = wx.PySimpleApp(0)
    
    # The app name must be set before the call to GetUserDataDir() below.
    app.SetAppName("Priorset")
    
    # Installation will probably create a per-user data directory for us, but
    # if it doesn't exist (the user may have deleted it, or we may be running
    # in development mode) then I (re)create it here.
    path = wx.StandardPaths.Get().GetUserDataDir()
    if not os.path.exists(path):
        os.mkdir(path)
    
    wx.InitAllImageHandlers()
    frame = Main()
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()    



if __name__ == "__main__":
    app, db_path = util_init.init_app("Priorset")
    
    db = common_util_db.Database(db_path, True)

    # My settings are in prior.ini
    config = util_priorset_config.Config()

    position, size = config.get_window_coordinates("main")
    frame = Main(db, position, size)
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()    
    
