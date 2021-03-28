import tkinter as tk
from task_gui import *

class Project_GUI(tk.Frame):
    '''
    Project GUI Object contains:
    project, super_projectmanager_gui, master, check_var

    can be constructed with 'Project_GUI(project, root, super_projectmanager_gui)'
    '''

    def __init__(self, project, root, super_projectmanager_gui):
        super().__init__(root)

        self.project = project
        self._master = root
        self.super_projectmanager_gui = super_projectmanager_gui

        self._check_var = tk.BooleanVar()
        self._check_var.set(False)

        #frame
        
        self._fr_pro_overview = tk.Frame(self, height=20, width=20, bg=self.project.color)
        
        self._update_tasks()        

    def _design_project_gui(self):
        '''
        Creates the Project GUI labels, buttons, ...
        '''

        self._fr_pro_tasks = tk.Frame(self, height=20, width=20)
        self._fr_pro_notes = tk.Frame(self, height=20, width=20, bg=self.project.color, bd=2, relief='groove')
        self._fr_pro_task_notes = tk.Frame(self._fr_pro_notes, height=20, width=20, bd=2, relief='groove')

        #label
        self._lbl_pro_name = tk.Label(self._fr_pro_overview, text=self.project.name)
        self._lbl_dscrb_pro_notes = tk.Label(self._fr_pro_notes, text='Notes: ')
        self._lbl_pro_notes = tk.Label(self._fr_pro_notes, text=self.project.notes, height=5, anchor='nw')
        #self._lbl_pro_no_tasks = tk.Label(self, text='All Tasks done! :-)')
        self._lbl_dscrb_task_notes = tk.Label(self._fr_pro_task_notes, text='Task Notes: ')

        #button
        self._bttn_pro_delete = tk.Button(self._fr_pro_overview, text='delete')
        self._bttn_pro_edit = tk.Button(self._fr_pro_overview, text='edit')
        self._bttn_pro_del_all_tasks = tk.Button(self._fr_pro_overview, text='delete all Tasks')
        self._bttn_pro_add_task = tk.Button(self._fr_pro_overview, text='+ add new Task', width=49)
        self._check_pro_fr_hide = tk.Checkbutton(self._fr_pro_overview, text='hide Tasks', var=self._check_var)

        #layout
        self._lbl_pro_name.grid(row=0, column=0, rowspan=2)
        self._bttn_pro_delete.grid(row=2, column=1)
        self._check_pro_fr_hide.grid(row=4, column=0)
        self._bttn_pro_del_all_tasks.grid(row=5, column=0)
        self._bttn_pro_add_task.grid(row=6, column=0,sticky='w', columnspan=3)

        self._lbl_dscrb_pro_notes.grid(row=0, column=0)

        self._lbl_pro_notes.grid(row=1, column=0, rowspan=5, pady=5)
        self._lbl_dscrb_task_notes.grid(row=0, column=0)


        self._fr_pro_overview.grid(row=0, column=0, columnspan=3, rowspan=8)
        self._fr_pro_tasks.grid(row=8, column=0, columnspan=3, rowspan=10)
        self._fr_pro_notes.grid(row=0, column=5, rowspan=10, sticky='n')
        self._fr_pro_task_notes.grid(row=10, column=0)


        #eventhandler
        self._bttn_pro_add_task['command'] = self._create_task_gui
        self._bttn_pro_del_all_tasks['command'] = self._delete_all_task_gui
        self._check_pro_fr_hide['command'] = self._hide_task

    def _hide_task(self):
        if self._check_var.get():
            self._fr_pro_tasks.grid_forget()
        else:
            self._fr_pro_tasks.grid(row=8, column=0, columnspan=3, rowspan=10)
       
    def _create_task_gui(self):
        '''
        Generates a window where a new Task can be generated
        Returns the new Task or nothing
        '''

        self.task_window = tk.Toplevel(self._master)
        self.task_window.title('Create Task')

        #label
        self._lbl_set_task_name = tk.Label(self.task_window, text='Task Name: ')
        self._lbl_set_task_notes = tk.Label(self.task_window, text='Notes: ')
        self._lbl_set_task_priority = tk.Label(self.task_window, text='Priority :')

        #button
        self._bttn_cancel_task = tk.Button(self.task_window, 
                                            text='cancel',
                                            activebackground='red')
        self._bttn_save_task = tk.Button(self.task_window, 
                                            text='save', 
                                            activebackground='green')

        #listbox
        self._lb_priority = tk.Listbox(self.task_window, width=9, height=4)
        self._lb_priority.insert(0, 'none')
        self._lb_priority.insert(1, 'low')
        self._lb_priority.insert(2, 'medium')
        self._lb_priority.insert(3, 'high')

        #entry
        self._entry_task_name = tk.Entry(self.task_window)
        self._entry_task_notes = tk.Text(self.task_window, width=20, height=5)

        #configuration
        self._entry_task_name.insert(0, 'Default Name')

        #layout
        self._lbl_set_task_name.grid(row=0, column=0, rowspan=2)
        self._entry_task_name.grid(row=0, column=1, rowspan=2)
        self._lbl_set_task_notes.grid(row=2, column=0)
        self._lbl_set_task_priority.grid(row=2, column=4)
        self._entry_task_notes.grid(row=3, column=0, columnspan=3, rowspan=5)
        self._lb_priority.grid(row=3, column=4, rowspan=4)
        self._bttn_cancel_task.grid(row=8, column=5)
        self._bttn_save_task.grid(row=8, column=4)

        #eventhandler
        self._bttn_save_task['command'] = self._save_task
        self._bttn_cancel_task['command'] = self.task_window.destroy
        
    def _save_task(self):
        '''
        Returns the saved Task
        Writes the entry information from the Create Task Window in a new Task
        '''
        self._new_task = self.project.create_task()
        self._new_task.name = self._entry_task_name.get()
        self._new_task.notes = self._entry_task_notes.get('1.0', 'end-1c')
        self._new_task.priority = self._lb_priority.get('active')

        #self._new_task_gui = Task_GUI(self._new_task, self._fr_pro_tasks, self)
        #self._new_task_gui.grid()
        #self._lst_task_frames.append(self._new_task_gui)
        self._update_tasks()
        self.task_window.destroy()

    def _update_tasks(self):
        '''

        '''
        self._design_project_gui()
        self._destroy_all_task_gui()

        self._lst_task_frames = []
        for task in self.project._tasks:
            self._temp_task_gui = Task_GUI(task, self._fr_pro_tasks, self)
            self._temp_task_gui.grid()
            self._lst_task_frames.append(self._temp_task_gui)

    def _destroy_all_task_gui(self):
        '''
        ????
        '''
        for old in self._fr_pro_tasks.winfo_children():
            old.destroy()

    def _delete_all_task_gui(self):
        '''
        Deletes all Tasks and destroys all Task GUIs
        '''
        for task in self._lst_task_frames:
            task._delete_task_gui()
        self._update_tasks()