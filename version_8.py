import sys
import enum
import pickle
import uuid
import tkinter as tk

class State(enum.IntEnum):
    unprocessed = 0
    done = 1

class Priority(enum.IntEnum):
    none = 0
    low = 1
    medium = 2
    high = 3

class Color(enum.IntEnum):
    black = 0
    blue = 1
    red = 2
    green = 3
    yellow = 4
    purple = 5
    orange = 6
    white = 7

class Task():
    
    def __init__(self, name, project, state=State.unprocessed, priority=Priority.none):
        self.name = name
        self.id = uuid.uuid4()
        self.project = project
        self.state = state
        self.priority = priority
        self.notes = ''

    def do_task(self):
        self.state = State.done


    def __str__(self):
        return str('Task Name' + self.name + ' Project:' + self.project.name + ' State:' + repr(self.state) + ' Piority' + repr(self.priority) + ' Notes: ' + self.notes)


class Project():

    def __init__(self, name, color=Color.black, tasks=[]):
        self.name = name
        self.color = color
        self.notes = ''
        self._tasks = tasks

    
    def is_empty(self):
        return len(self._tasks) == 0

    def create_task(self):
        new_task = Task('Default Task', self)
        self._tasks.append(new_task)
        return new_task

    def delete_task(self, task):
        if task in self._tasks:
            self._tasks.remove(task)
    
    def delete_all_tasks(self):
        if self.is_empty() == False:
            del self._tasks[:]
    
    def __str__(self):
        printed_tasks = ''
        for task in self._tasks:
            printed_tasks += str(task)
            printed_tasks += '\n'
        return str(' Name: ' + self.name + ' Color: ' + repr(self.color) + ' Notes: ' + self.notes + ' Tasks: \n' + printed_tasks)

class ProjectManager():

    def __init__(self):
        self._projects = []

    def _create_project(self):
        new_project = Project('Default Project')
        self._projects.append(new_project)
        return new_project

    def _delete_project(self, project):
        if project in self._projects:
            self._projects.remove(project)

    def _save_projects(self):
        outfile = open('saved_projects', 'wb')
        pickle.dump(self._projects, outfile)
        outfile.close()

    def _load_projects(self):
        infile = open('saved_projects','rb')
        self._projects = pickle.load(infile)
        infile.close()
    
    def __str__(self):
        printed_projects = ''
        for project in self._projects:
            printed_projects += str(project)
            printed_projects += '\n'
        return str('Projects: \n' + printed_projects)


class Project_GUI(tk.Frame):

    def __init__(self, project, root):
        super().__init__(root)

        self.project = project
        self._master = root

        #frame
        self._fr_pro_tasks = tk.Frame(self, height=20 , width=20)

        #canvas
        self._can_pro_tasks = tk.Canvas(self._fr_pro_tasks)

        #label
        self._lbl_pro_name = tk.Label(self, text=project.name)
        self._lbl_pro_notes = tk.Label(self, text=project.notes)
        self._lbl_pro_no_tasks = tk.Label(self, text='All Tasks done! :-)')

        #button
        self._bttn_pro_delete = tk.Button(self, text='delete')
        self._bttn_pro_edit = tk.Button(self, text='edit')
        self._bttn_pro_del_all_tasks = tk.Button(self, text='delete all Tasks')
        self._bttn_pro_add_task = tk.Button(self, text='+ add new Task')

        self._bttn_pro_fr_hide = tk.Button(self, 
                          text = 'hide Tasks',
                          command=lambda: self._fr_pro_tasks.grid_forget())

        self._bttn_pro_fr_show = tk.Button(self,
                          text = 'show Tasks',
                          command=lambda: 
                          self._fr_pro_tasks.grid(row=8, column=0, columnspan=2, rowspan=10))   


        #tasks
        self._lst_task_frames = []
        for task in project._tasks:
            self._temp_task_gui = Task_GUI(task, self._can_pro_tasks)
            self._temp_task_gui.grid(sticky='w')
            self._lst_task_frames.append(self._temp_task_gui)


        #test
        self.testtask = self.project.create_task()
        self.testtask.name = 'hello word'
        self.testtask_gui = Task_GUI(self.testtask, self._can_pro_tasks)
        self.testtask_gui.grid(sticky='w')
        self._lst_task_frames.append(self.testtask_gui)


        #layout
        self._lbl_pro_name.grid(row=0, column=0, rowspan=2)
        self._lbl_pro_notes.grid(row=1, column=0, rowspan=3)
        self._bttn_pro_delete.grid(row=2, column=1)
        self._bttn_pro_fr_hide.grid(row=4, column=0)
        self._bttn_pro_fr_show.grid(row=4, column=1)
        self._bttn_pro_del_all_tasks.grid(row=5, column=0)

        self._bttn_pro_add_task.grid(row=6, column=0, columnspan=3)

        self._can_pro_tasks.grid(row=0, column=0, columnspan=3, rowspan=9)
        self._fr_pro_tasks.grid(row=8, column=0, columnspan=3, rowspan=10)


        #eventhandler
        self._bttn_pro_add_task['command'] = self._create_task_gui

    def _create_task_gui(self):
        self.new_task = self.project.create_task()
        self.new_task_window = tk.Toplevel(self._master)
        self.new_task_window.title('Create/Edit Task')
        self.new_task_window = TaskWindow(self.new_task, self.new_task_window)
        self.new_task_window._create_task_gui()



class TaskWindow():
    def __init__(self, task, window):
        self._task = task
        self.task_window = window

    def _create_task_gui(self):
        
        #label
        self._lbl_set_task_name = tk.Label(self.task_window, text='Task Name: ')
        self._lbl_set_task_notes = tk.Label(self.task_window, text='Notes: ')
        self._lbl_set_task_priority = tk.Label(self.task_window, text='Priority :')


        #button
        self._bttn_cancel_task = tk.Button(self.task_window, text='cancel', activebackground='red')
        self._bttn_save_task = tk.Button(self.task_window, text='save', activebackground='green')

        #listbox
        self._lb_priority = tk.Listbox(self.task_window, width=9, height=4)
        self._lb_priority.insert(0, 'none')
        self._lb_priority.insert(1, 'low')
        self._lb_priority.insert(2, 'medium')
        self._lb_priority.insert(1, 'high')

        #entry
        self._entry_task_name = tk.Entry(self.task_window)
        self._entry_task_notes = tk.Text(self.task_window, width=20, height=5)

        #configuration
        self._entry_task_name.insert(0, self._task.name)
        self._entry_task_notes.insert(0, self._task.notes)


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
        self._new_task = self._task
        self._new_task.name = self._entry_task_name.get()
        self._new_task.notes = self._entry_task_notes.get('1.0', 'end-1c')
        self._new_task.priority = self._lb_priority.get('active')
        self._new_task_gui = Task_GUI(self._new_task, self._can_pro_tasks)
        self._new_task_gui.grid(column=1)
        self._lst_task_frames.append(self._new_task_gui)
        self.task_window.destroy()
        
        

class Task_GUI(tk.Frame):
    
    def __init__(self, task, root):
        super().__init__(root)

        self.task = task
        self._master = root

        #label
        self._lbl_task_name = tk.Label(self, text=self.task.name)
        self._lbl_task_priority = tk.Label(self, text=self.task.priority)
        self._lbl_task_notes = tk.Label(self, text=self.task.notes)

        #button
        self._check_task_done = tk.Checkbutton(self, variable=self.task.id)
        self._bttn_task_delete = tk.Button(self, text='delete', activebackground='red')
        self._bttn_task_edit = tk.Button(self, text='edit')
        self._bttn_task_show_notes = tk.Button(self, text='show notes')
        
        #layout
        self._check_task_done.grid(row=0, column=0)
        self._lbl_task_name.grid(row=0, column=1, columnspan=2)
        self._lbl_task_priority.grid(row=0, column=3)
        self._bttn_task_show_notes.grid(row=0, column=4)
        self._bttn_task_edit.grid(row=0, column=5)
        self._bttn_task_delete.grid(row=0, column=6)

        #eventhandler
        self._bttn_task_delete['command'] = self._delete_task_gui
        self._check_task_done['command'] = self._do_task_gui
        #self._edit_task_gui['command'] = self._edit_task_gui
    
    def _delete_task_gui(self):
        self.task.project.delete_task(self.task)
        self.destroy()
    
    def _do_task_gui(self):
        self.task.do_task()
        self.destroy()

    def _edit_task_gui(self):
        self._edit_window = TaskWindow(self.task, tk.Toplevel(self._master))
        



class GUI(tk.Frame):
    def __init__(self, root=tk.Tk()):
        super().__init__(root)

        self._root = root
        self._projectmanager = ProjectManager()
        self.progui = Project_GUI(Project('test'), self)

        self.pack()
        self._create_elements()

        
    def _create_project_gui(self):
        project_window = tk.Toplevel(self._root)
        project_window.title('Create a new Project')

        #label
        self._lbl_set_project_name = tk.Label(project_window, text='Project Name: ')
        self._lbl_set_project_notes = tk.Label(project_window, text='Notes: ')

        #button
        self._bttn_del_project = tk.Button(project_window, text='delete')
        self._bttn_save_project = tk.Button(project_window, text='save')

        #entry
        self._entry_project_name = tk.Entry(project_window)
        self._entry_project_notes = tk.Text(project_window, width=20, height=5)

        #layout
        self._lbl_set_project_name.grid(row=0, column=0, rowspan=2)
        self._entry_project_name.grid(row=0, column=1, rowspan=2, columnspan=3)
        self._lbl_set_project_notes.grid(row=2, column=1)
        self._entry_project_notes.grid(row=3, column=1, columnspan=3)
        self._bttn_del_project.grid(row=5, column=3)
        self._bttn_save_project.grid(row=5, column=4)

   

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


       



if __name__ == '__main__':


    #Tests

    new_projectmanager = ProjectManager()
    new_project = new_projectmanager._create_project()

    new_task = new_project.create_task()
    task_2 = new_project.create_task()

    task_3 = new_project.create_task()
    task_3.name = 'task 3'

    print(new_projectmanager)

    new_projectmanager._save_projects()

    del new_projectmanager

    projectmanager_2 = ProjectManager()

    projectmanager_2._load_projects()

    print(projectmanager_2)


    GUI()