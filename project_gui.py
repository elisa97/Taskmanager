import tkinter as tk
from task_gui import *


class Project_GUI(tk.Frame):
    """
    Project_GUI Object contains:
    project,
    super_projectmanager_gui,
    master,
    check_var_task (for showing/hiding checked Tasks),
    check_var_frame (for showing/hiding Tasks in general)

    can be constructed with
    'Project_GUI(project: Project, root: tkinter.Frame(),
                 super_projectmanager_gui: ProjectManager_GUI)'
    """

    def __init__(self, project, root, super_projectmanager_gui):
        super().__init__(root)

        self._project = project
        self._master = root
        self._super_projectmanager_gui = super_projectmanager_gui

        self._check_var_frame = tk.BooleanVar()
        self._check_var_frame.set(False)

        self._check_var_task = tk.BooleanVar()
        self._check_var_task.set(False)

        self.build_project_gui()
        self.update_tasks()
        self._disable_bttns()

    def build_project_gui(self):
        """
        Build a frame for a Project (Overview)

        contains
        a Checkbutton to show/hide Tasks in general,
        the name of the Project,
        a Checkbutton to show/hide the done Tasks,
        a Button to add a Task,
        a Button to delete all Tasks (also the done Tasks)
        """
        # outermost frames
        # elements
        self._fr_pro_overview = tk.Frame(
            self, height=20, width=20, bg=self._project.color.value
        )
        self._fr_pro_tasks = tk.Frame(self, height=20, width=20)

        # layout
        self._fr_pro_overview.grid(
            row=0, column=0, columnspan=3, rowspan=8, sticky="w"
        )
        self._fr_pro_tasks.grid(row=8, column=0, columnspan=3, rowspan=10)

        # fr_pro_overview
        # elemets
        self._fr_pro_notes = tk.Frame(
            self._fr_pro_overview,
            height=20,
            width=20,
            bg=self._project.color.value,
            bd=2,
            relief="groove",
        )
        self._lbl_pro_name = tk.Label(
            self._fr_pro_overview,
            text=self._project.name,
            width=20,
            font="28",
            bg=self._project.color.value,
        )
        self._bttn_pro_del_all_tasks = tk.Button(
            self._fr_pro_overview,
            text="delete all Tasks",
            activebackground="red",
        )
        self._bttn_pro_add_task = tk.Button(
            self._fr_pro_overview, text="+ add new Task", width=45
        )
        self._check_pro_fr_hide = tk.Checkbutton(
            self._fr_pro_overview,
            text="hide Tasks",
            var=self._check_var_frame,
        )
        self._check_show_done_tasks = tk.Checkbutton(
            self._fr_pro_overview,
            text="show done Tasks",
            var=self._check_var_task,
        )

        # layout
        self._fr_pro_notes.grid(row=0, column=5, rowspan=10)
        self._lbl_pro_name.grid(row=0, column=0, rowspan=2)
        self._check_pro_fr_hide.grid(row=4, column=0)
        self._check_show_done_tasks.grid(row=4, column=2)
        self._bttn_pro_del_all_tasks.grid(row=5, column=0)
        self._bttn_pro_add_task.grid(
            row=6, column=0, sticky="w", columnspan=3
        )

        # eventhandler
        self._bttn_pro_add_task["command"] = self._create_task_gui
        self._bttn_pro_del_all_tasks["command"] = self._delete_all_task_gui
        self._check_pro_fr_hide["command"] = self._hide_task
        self._check_show_done_tasks["command"] = self._show_done_tasks

        # fr_pro_notes
        # elements
        self._lbl_dscrb_pro_notes = tk.Label(
            self._fr_pro_notes, text="Notes: ", bg=self._project.color.value
        )
        self._lbl_pro_notes = tk.Label(
            self._fr_pro_notes,
            text=self._project.notes,
            height=5,
            width=10,
            anchor="nw",
            bg=self._project.color.value,
        )

        # layout
        self._lbl_dscrb_pro_notes.grid(row=0, column=0)
        self._lbl_pro_notes.grid(row=1, column=0, rowspan=5, pady=5)

        # fr_pro_tasks
        # elements
        self.fr_pro_task_notes = tk.Frame(
            self._fr_pro_tasks, height=20, width=20, bd=2, relief="groove"
        )
        self._fr_pro_task_list = tk.Frame(
            self._fr_pro_tasks, height=20, width=20
        )

        # layout
        self.fr_pro_task_notes.grid(row=0, column=10, sticky="n")
        self._fr_pro_task_list.grid(row=0, column=0, sticky="n")

        # fr_pro_task_notes
        self._lbl_dscrb_task_notes = tk.Label(
            self.fr_pro_task_notes, text="Task Notes: "
        )
        self._lbl_dscrb_task_notes.grid(row=0, column=0)

    def _create_task_gui(self):
        """
        Generates a window where a new Task can be created

        contains
        an Entry for the Task name,
        an Entry for the Task notes,
        an Listbox for the Task priority,
        a Button to save the new Task,
        a Button to cancel creating the Task

        Returns a new Task (if saved)
        Returns None (if canceled)
        """

        # window
        self.task_window = tk.Toplevel(self._master)
        self.task_window.title("Create Task")

        # elements
        self._lbl_set_task_name = tk.Label(
            self.task_window, text="Task Name: "
        )
        self._lbl_set_task_notes = tk.Label(self.task_window, text="Notes: ")
        self._lbl_set_task_priority = tk.Label(
            self.task_window, text="Priority :"
        )

        self._bttn_cancel_task = tk.Button(
            self.task_window, text="cancel", activebackground="red", width=5
        )
        self._bttn_save_task = tk.Button(
            self.task_window, text="save", activebackground="green", width=5
        )

        self._lb_priority = tk.Listbox(self.task_window, width=9, height=4)
        self._lb_priority.insert(0, "none")
        self._lb_priority.insert(1, "low")
        self._lb_priority.insert(2, "medium")
        self._lb_priority.insert(3, "high")

        self._entry_task_name = tk.Entry(self.task_window)
        self._entry_task_notes = tk.Text(self.task_window, width=20, height=5)

        # layout
        self._lbl_set_task_name.grid(row=0, column=0, rowspan=2)
        self._entry_task_name.grid(row=0, column=1, rowspan=2)
        self._lbl_set_task_notes.grid(row=2, column=0)
        self._lbl_set_task_priority.grid(row=2, column=4)
        self._entry_task_notes.grid(row=3, column=0, columnspan=3, rowspan=5)
        self._lb_priority.grid(row=3, column=4, rowspan=4)
        self._bttn_cancel_task.grid(row=8, column=5)
        self._bttn_save_task.grid(row=8, column=4)

        # eventhandler
        self._bttn_save_task["command"] = self._save_task
        self._bttn_cancel_task["command"] = self.task_window.destroy

        # configuration
        self._entry_task_name.insert(0, "Default Task")

    def _save_task(self):
        """
        Writes the entry information from the Create Task Window in a new Task

        Returns a new Task
        """
        self._new_task = self._project.create_task()
        self._new_task.name = self._entry_task_name.get()
        self._new_task.notes = self._entry_task_notes.get("1.0", "end-1c")
        self._new_task.priority = self._lb_priority.get("active")
        self.update_tasks()
        self._disable_bttns()
        self.task_window.destroy()

    def update_tasks(self):
        """
        Build a new list of Task_GUIs into a frame after destroying all Task_GUIs
        """
        self._lst_task_frames = []
        self._destroy_all_task_frames()

        for task in self._project.tasks:
            self._temp_task_gui = Task_GUI(task, self._fr_pro_task_list, self)
            self._temp_task_gui.grid()
            self._lst_task_frames.append(self._temp_task_gui)

        self._disable_bttns()
        self._show_done_tasks()

    def _delete_all_task_gui(self):
        """
        Deletes all Tasks and destroys all Task_GUIs
        """
        for task in self._lst_task_frames:
            task.delete_task_gui()
        self._disable_bttns()

    def _destroy_all_task_frames(self):
        """
        Clears the fr_pro_task frame
        """
        for widget in self._fr_pro_task_list.winfo_children():
            widget.destroy()

    def _hide_task(self):
        """
        Hides or shows Tasks,
        depending on check_var_frame
        """
        if self._check_var_frame.get():
            self._fr_pro_tasks.grid_forget()
            self._fr_pro_notes.grid_forget()
            self._check_show_done_tasks["state"] = "disabled"
        else:
            self._fr_pro_tasks.grid(row=8, column=0, columnspan=3, rowspan=10)
            self._fr_pro_notes.grid(row=0, column=5, rowspan=10)
            self._check_show_done_tasks["state"] = "normal"

    def _disable_bttns(self):
        """
        Disables 'delete all Tasks', 'show done Tasks', 'hide Tasks'
        if Project doesn't contain Tasks
        """
        if self._project.is_empty():
            self._bttn_pro_del_all_tasks["state"] = "disabled"
            self._check_show_done_tasks["state"] = "disabled"
            self._check_pro_fr_hide["state"] = "disabled"

        else:
            self._bttn_pro_del_all_tasks["state"] = "normal"
            self._check_show_done_tasks["state"] = "normal"
            self._check_pro_fr_hide["state"] = "normal"

    def _show_done_tasks(self):
        """
        Showes or hides done Tasks,
        depending on check_var_task
        """
        if self._check_var_task.get():
            for task in self._lst_task_frames:
                task.show_done()
        else:
            for task in self._lst_task_frames:
                task.show_unprocessed()
