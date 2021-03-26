import tkinter as tk
from project_manager import *
from project_gui import *

class GUI(tk.Frame):
    def __init__(self, root=tk.Tk()):
        super().__init__(root)

        self._root = root
        self._projectmanager = ProjectManager()
        self.progui = Project_GUI(Project('test'), self)

        self.pack()
        self._create_elements()

        
    def _create_project_gui(self):
        self.project_window = tk.Toplevel(self._root)
        self.project_window.title('Create a new Project')
        

        #label
        self._lbl_set_project_name = tk.Label(self.project_window, text='Project Name: ')
        self._lbl_set_project_notes = tk.Label(self.project_window, text='Notes: ')
        self._lbl_set_project_color = tk.Label(self.project_window, text='Color: ')

        #button
        self._bttn_del_project = tk.Button(self.project_window, text='delete')
        self._bttn_save_project = tk.Button(self.project_window, text='save')

        self._lb_color_project = tk.Listbox(self.project_window, width=7, height=8)
        self._lb_color_project.insert(0, 'black')
        self._lb_color_project.insert(1, 'blue')
        self._lb_color_project.insert(2, 'red')
        self._lb_color_project.insert(3, 'green')
        self._lb_color_project.insert(4, 'yellow')
        self._lb_color_project.insert(5, 'purple')
        self._lb_color_project.insert(6, 'orange')
        self._lb_color_project.insert(7, 'white')

        #entry
        self._entry_project_name = tk.Entry(self.project_window)
        self._entry_project_notes = tk.Text(self.project_window, width=20, height=5)

        #layout
        self._lbl_set_project_name.grid(row=0, column=0, rowspan=2)
        self._entry_project_name.grid(row=0, column=1, rowspan=2, columnspan=2)
        self._lbl_set_project_notes.grid(row=3, column=0)
        self._entry_project_notes.grid(row=3, column=1, columnspan=2, rowspan=3)
        self._lbl_set_project_color.grid(row=1, column=4, columnspan=2)
        self._lb_color_project.grid(row=2, column=4, columnspan=2, rowspan=4)
        self._bttn_del_project.grid(row=7, column=4)
        self._bttn_save_project.grid(row=7, column=5)

   

    def _create_elements(self):

        #frames
        self._fr_project = tk.Frame(self)

        self._can_projects = tk.Canvas(self._fr_project)

        #labels
        self._lbl_title = tk.Label(self, text='Project Overview')

        #buttons
        self._bttn_create_project = tk.Button(self._fr_project, text='create Project')

        #projects
        self._lst_project_frames = []
        for pro in self._projectmanager._projects:
            self._lst_project_frames.append(Project_GUI(pro, self._can_projects))

    
        #event handler
        self._bttn_create_project['command'] = self._create_project_gui

        #layout

        self._lbl_title.grid(row=0, column=0, columnspan=3)
        self._fr_project.grid(row=1, column=0, columnspan=3, rowspan=5)


        self._bttn_create_project.grid(row=1, column=0)

        self.progui.grid(row=7, column=0, rowspan=10)

        #configuration
        self.progui.configure(bg='white')


        self._root.mainloop()
