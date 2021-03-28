import tkinter as tk
from project_manager import *
from project_gui import *

class GUI(tk.Frame):
    def __init__(self, projectmanger, root=tk.Tk()):
        super().__init__(root)

        self._root = root
        self._projectmanager = projectmanger

        self.pack()
        self._create_elements()

    def _create_elements(self):

        #frames
        self._fr_project = tk.Frame(self)
        self._fr_projectmanager = tk.Frame(self)

        #labels
        self._lbl_title = tk.Label(self._fr_project, text='Project Overview')

        #buttons
        self._bttn_create_project = tk.Button(self._fr_projectmanager, text='create Project')

        #listbox
        self._lb_projects = tk.Listbox(self._fr_projectmanager)

        #test
        '''self.test_projekt = self._projectmanager._create_project()
        self.test_projekt.name = 'test'
        self.test_projekt.notes = 'Hallo du da was machst du so?'
        self.test_projekt.color = Color.green
        self.progui = Project_GUI(self.test_projekt, self._fr_project)
        self.progui.grid(row=7, column=0, rowspan=10)
        self.progui.configure(bg=self.test_projekt.color.value)'''

        #projects
        #self._lst_project_frames = []

        self._update_listbox()

        #event handler
        self._bttn_create_project['command'] = self._create_project_gui

        #layout

        self._lbl_title.grid(row=0, column=0, columnspan=3)

        self._fr_project.grid(row=0, column=2, rowspan=5)
        self._fr_projectmanager.grid(row=0, column=0)


        self._bttn_create_project.grid(row=1, column=0)
        self._lb_projects.grid(row=3, column=0, rowspan=8)

        #self._create_project_overview()

        self._root.mainloop()



    def _create_project_gui(self):

        self.project_window = tk.Toplevel(self._root)
        self.project_window.title('Create a new Project')

        #label
        self._lbl_dscrb_project_name = tk.Label(self.project_window, text='Project Name: ')
        self._lbl_dscrb_project_notes = tk.Label(self.project_window, text='Notes: ')
        self._lbl_dscrb_project_color = tk.Label(self.project_window, text='Color: ')

        #button
        self._bttn_cancel_project = tk.Button(self.project_window, text='cancel')
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
        self._lbl_dscrb_project_name.grid(row=0, column=0, rowspan=2)
        self._entry_project_name.grid(row=0, column=1, rowspan=2, columnspan=2)
        self._lbl_dscrb_project_notes.grid(row=3, column=0)
        self._entry_project_notes.grid(row=3, column=1, columnspan=2, rowspan=3)
        self._lbl_dscrb_project_color.grid(row=1, column=4, columnspan=2)
        self._lb_color_project.grid(row=2, column=4, columnspan=2, rowspan=4)
        self._bttn_cancel_project.grid(row=7, column=5)
        self._bttn_save_project.grid(row=7, column=4)

        #eventhandler
        self._bttn_save_project['command'] = self.save_new_project
        self._bttn_cancel_project['command'] = self.project_window.destroy
        self._lb_projects.bind('<<ListboxSelect>>', self._update_project)
        #self._lb_projects['command'] = self._update_project

    def save_new_project(self):
        self._new_project = self._projectmanager._create_project()
        self._new_project.name = self._entry_project_name.get()
        self._new_project.notes = self._entry_project_notes.get('1.0', 'end-1c')
        self._new_project.color = self._lb_color_project.get('active')
        self._update_listbox()
        self.project_window.destroy()

    def build_listboxes(self):
        i = 0
        for pro in self._projectmanager._projects:
            self._lb_projects.insert(i, pro.name)
            i +=1

    def _update_listbox(self):
        self._lb_projects.delete(0, tk.END)
        self.build_listboxes()

    def _update_project(self, event):
        '''
        Build the new Project GUI Overview
        '''
        self._delete_project_overview()
        self._selected_pro_name = self._lb_projects.get('active')
        self.found_project = None
        for project in self._projectmanager._projects:
            if project.name == self._selected_pro_name:
                self.found_project = project
                break

        self._new_project_gui = Project_GUI(self.found_project, self._fr_project)
        self._new_project_gui.grid(row=7, column=0, rowspan=10)

    def _delete_project_overview(self):
        'to do'


