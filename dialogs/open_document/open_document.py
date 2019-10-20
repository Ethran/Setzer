#!/usr/bin/env python3
# coding: utf-8

# Copyright (C) 2017, 2018 Robert Griesel
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from dialogs.dialog import Dialog
import model.model_document as model_document

import os.path


class OpenDocumentDialog(Dialog):
    ''' File chooser for opening documents '''

    def __init__(self, main_window, workspace):
        self.main_window = main_window
        self.workspace = workspace

    def run(self):
        self.setup()
        response = self.view.run()
        if response == Gtk.ResponseType.OK:
            filename = self.view.get_filename()
            document_candidate = self.workspace.get_document_by_filename(filename)
            if document_candidate != None:
                self.workspace.set_active_document(document_candidate)
            else:
                document = model_document.Document(self.workspace.pathname, with_buffer=True)
                document.set_filename(filename)
                document.populate_from_filename()
                self.workspace.add_document(document)
                self.workspace.set_active_document(document)
        self.close()

    def setup(self):
        self.action = Gtk.FileChooserAction.OPEN
        self.buttons = ('_Cancel', Gtk.ResponseType.CANCEL, '_Open', Gtk.ResponseType.OK)
        self.view = Gtk.FileChooserDialog('Open', self.main_window, self.action, self.buttons)
        
        for widget in self.view.get_header_bar().get_children():
            if isinstance(widget, Gtk.Button) and widget.get_label() == '_Open':
                widget.get_style_context().add_class(Gtk.STYLE_CLASS_SUGGESTED_ACTION)
                widget.set_can_default(True)
                widget.grab_default()

        # file filtering
        file_filter1 = Gtk.FileFilter()
        file_filter1.add_pattern('*.tex')
        file_filter1.set_name('LaTeX files')
        self.view.add_filter(file_filter1)

        self.view.set_select_multiple(False)

        self.main_window.headerbar.document_chooser.popdown()

