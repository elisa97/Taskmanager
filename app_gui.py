import tkinter as tk
from app import *
from projectmanager_gui import *

class App_GUI(tk.Frame):

    def __init__(self, root=tk.Tk()):
        super().__init__(root)

        self._root = root
    
    def _create_elements(self):
        
        #frames
        #self._fr_menu = tk.Frame(self)
        self.fr_projectmanager_gui = tk.Frame(self)

        #self._fr_menu.grid(row=0, column=0, rowspan=2)
        self.fr_projectmanager_gui.grid(row=3, column=0, rowspan=10)

        #elements app menu
        self._menu = tk.Menu(self._root)
        self._root.config(menu=self._menu)
        self._file_menu = tk.Menu(self._menu)
        self._menu.add_cascade(label='File', menu=self._file_menu)
        self._file_menu.add_command(label='save file', command=self._save_file)
        #self._file_menu.add_command(label='load file', command=self._open_file)
        self._user_menu = tk.Menu(self._file_menu)
        self._file_menu.add_command(label='User menu')

