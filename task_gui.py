import tkinter as tk
from task import *

class Task_GUI(tk.Frame):
    
    def __init__(self, task, root, super_project_gui):
        super().__init__(root)

        self.super_project_gui = super_project_gui
        self.task = task
        self._master = root
        self._check_var = tk.BooleanVar()
        self._check_var.set(False)

        self.configure(bd=1,relief='groove')

        #label
        self._lbl_task_name = tk.Label(self, text=self.task.name, width=20, anchor='w')

        self._lbl_task_notes = tk.Label(self.super_project_gui._fr_pro_task_notes, text=self.task.notes)

        #button
        self._check_task_done = tk.Checkbutton(self, variable=self.task.id)
        self._bttn_task_delete = tk.Button(self, text='delete', activebackground='red')
        self._bttn_task_edit = tk.Button(self, text='edit')
        self._check_task_show_notes = tk.Checkbutton(self, variable=self.task.id, text='show notes', var=self._check_var)
        
        #layout
        self._check_task_done.grid(row=0, column=0, sticky='w', padx=2)
        self._lbl_task_name.grid(row=0, column=1)
        self._check_task_show_notes.grid(row=0, column=4)
        self._bttn_task_edit.grid(row=0, column=5)
        self._bttn_task_delete.grid(row=0, column=6, sticky='e')

        self._lbl_task_notes.grid_forget()

        self._get_task_color()


        #eventhandler
        self._bttn_task_delete['command'] = self._delete_task_gui
        self._check_task_done['command'] = self._do_task_gui
        self._bttn_task_edit['command'] = self._edit_task_gui

        self._check_task_show_notes['command'] = self._show_task_notes

        #self._bttn_task_hide_notes['command'] = self._lbl_task_notes.grid_forget()

    def _show_task_notes(self):
        if self._check_var.get():
            self._lbl_task_notes.grid(row=1, column=0, sticky='w')
        else:
            self._lbl_task_notes.grid_forget()


    def _edit_task_gui(self):
        '''
        Generates a window where Task can be edited and saved
        Returns the edited or original Task 
        '''
        self._edit_window = tk.Toplevel(self._master)
        self._edit_window.title('Edit Task')

        
        #label
        self._lbl_set_task_name = tk.Label(self._edit_window, text='Task Name: ')
        self._lbl_set_task_notes = tk.Label(self._edit_window, text='Notes: ')
        self._lbl_set_task_priority = tk.Label(self._edit_window, text='Priority :')


        #button
        self._bttn_cancel_task = tk.Button(self._edit_window, 
                                            text='cancel',
                                            activebackground='red')
        self._bttn_save_task = tk.Button(self._edit_window, 
                                            text='save', 
                                            activebackground='green')

        #listbox
        self._lb_priority = tk.Listbox(self._edit_window, width=9, height=4)
        self._lb_priority.insert(0, 'none')
        self._lb_priority.insert(1, 'low')
        self._lb_priority.insert(2, 'medium')
        self._lb_priority.insert(3, 'high')

        #entry
        self._entry_task_name = tk.Entry(self._edit_window)
        self._entry_task_notes = tk.Text(self._edit_window, width=20, height=5)

        #configuration
        self._entry_task_name.insert(0, self.task.name)
        self._entry_task_notes.insert('1.0', self.task.notes)


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
        self._bttn_cancel_task['command'] = self._edit_window.destroy
        
    def _save_task(self):
        '''
        Returns the edited Task
        Writes the entry information from the Edit Task Window in the Task
        '''
        self.task.name = self._entry_task_name.get()
        self.task.notes = self._entry_task_notes.get('1.0', 'end-1c')
        self.task.priority = self._lb_priority.get('active')
        self.super_project_gui._lst_task_frames.append(self)
        self.super_project_gui._update_tasks()
        self._edit_window.destroy()

    def _get_task_color(self):
        '''
        Set the background color of 
        Task Gui, Label Task Name, Checkbutton Task Done
        to red if Task Priority is 'high',
        yellow if Task Priority is 'medium',
        green if Task Priority is 'low'
        '''
        if self.task.priority == 'high':
            self.configure(bg='red')
            self._lbl_task_name.configure(bg='red')
            self._check_task_done.configure(bg='red')
        elif self.task.priority == 'medium':
            self.configure(bg='yellow')
            self._lbl_task_name.configure(bg='yellow')
            self._check_task_done.configure(bg='yellow')
        elif self.task.priority == 'low':
            self.configure(bg='green')
            self._lbl_task_name.configure(bg='green')
            self._check_task_done.configure(bg='green')
    
    def _delete_task_gui(self):
        '''
        Deletes the Task and destroys the Task GUI
        '''
        self.task.project.delete_task(self.task)
        self.destroy()

    def _do_task_gui(self):
        '''
        Set Task State to Done and desrtoys Task GUI
        '''
        self.task.do_task()
        self.destroy()
