import tkinter as tk
from project_manager import *
from project_gui import *


class ProjectManager_GUI(tk.Frame):
    """
    ProjectManager_GUI Object contains:
    projectmanager,
    app_gui,
    root,

    can be constructed with
    'ProjectManager_GUI(projectmanager: ProjectManager,
                        app_gui: App_GUI, root: tkinter.Frame())'
    """

    def __init__(self, projectmanger, app_gui, root):
        super().__init__(root)

        self._root = root
        self._projectmanager = projectmanger

        self.build_projectmanager_gui()

    def build_projectmanager_gui(self):
        """
        Build a frame for a ProjectManager

        contains
        a Frame with the Project Overview
        containing a Project_GUI,
        a Frame with the Projectmanager Overview containing
        a Button to add a Project,
        a Listbox containing all existing Projects,
        a Button to show a Project,
        a Button to edit a Project,
        a Button to delete a Project
        """

        # outermost frames
        # elements
        self._fr_project = tk.Frame(self)
        self._fr_projectmanager = tk.Frame(self)

        # layout
        self._fr_project.grid(row=0, column=2, rowspan=5)
        self._fr_projectmanager.grid(row=0, column=0)

        # projectmanager frame
        # elements
        self._bttn_create_project = tk.Button(
            self._fr_projectmanager, text="+ add a new Project", width=15
        )
        self._bttn_show_project = tk.Button(
            self._fr_projectmanager,
            text="show Project",
            state="normal",
            activebackground="green",
            width=15,
        )
        self._bttn_edit_project = tk.Button(
            self._fr_projectmanager,
            text="edit Project",
            state="normal",
            width=15,
        )
        self._bttn_delete_project = tk.Button(
            self._fr_projectmanager,
            text="delete Project",
            state="normal",
            activebackground="red",
            width=15,
        )
        self._lb_projects = tk.Listbox(self._fr_projectmanager)

        # layout
        self._lb_projects.grid(row=3, column=0, rowspan=8)
        self._bttn_create_project.grid(row=0, column=0)
        self._bttn_show_project.grid(row=12, column=0)
        self._bttn_edit_project.grid(row=13, column=0)
        self._bttn_delete_project.grid(row=14, column=0)

        # eventhandler
        self._bttn_create_project["command"] = self._create_project_gui
        self._bttn_show_project["command"] = self._update_project
        self._bttn_edit_project["command"] = self._edit_project_gui
        self._bttn_delete_project["command"] = self._delete_project_gui

        # configurations
        self._disable_bttns()
        self._build_listboxes_pro()

    def _create_project_gui(self):
        """
        Generates a window where a new Project can be created

        contains
        an Entry for the Project name,
        an Entry for the Project notes,
        an Listbox for the Project color,
        a Button to save the new Project,
        a Button to cancel creating the Project

        Returns a new Project (if saved)
        Returns None (if canceled)
        """

        # window
        self.project_window = tk.Toplevel(self._root)
        self.project_window.title("Create a new Project")

        # elements
        self._lbl_dscrb_project_name = tk.Label(
            self.project_window, text="Project Name: "
        )
        self._lbl_dscrb_project_notes = tk.Label(
            self.project_window, text="Notes: "
        )
        self._lbl_dscrb_project_color = tk.Label(
            self.project_window, text="Color: "
        )

        self._bttn_cancel_project = tk.Button(
            self.project_window,
            text="cancel",
            activebackground="red",
            width=5,
        )
        self._bttn_save_project = tk.Button(
            self.project_window,
            text="save",
            activebackground="green",
            width=5,
        )

        self._lb_color_project = tk.Listbox(
            self.project_window, width=7, height=8
        )
        self._lb_color_project.insert(0, "white")
        self._lb_color_project.insert(1, "blue")
        self._lb_color_project.insert(2, "red")
        self._lb_color_project.insert(3, "green")
        self._lb_color_project.insert(4, "yellow")
        self._lb_color_project.insert(5, "purple")
        self._lb_color_project.insert(6, "orange")
        self._lb_color_project.insert(7, "pink")

        self._entry_project_name = tk.Entry(self.project_window)
        self._entry_project_notes = tk.Text(
            self.project_window, width=20, height=5
        )

        # layout
        self._lbl_dscrb_project_name.grid(row=0, column=0, rowspan=2)
        self._entry_project_name.grid(
            row=0, column=1, rowspan=2, columnspan=2
        )
        self._lbl_dscrb_project_notes.grid(row=3, column=0)
        self._entry_project_notes.grid(
            row=3, column=1, columnspan=2, rowspan=3
        )
        self._lbl_dscrb_project_color.grid(row=1, column=4, columnspan=2)
        self._lb_color_project.grid(row=2, column=4, columnspan=2, rowspan=4)
        self._bttn_cancel_project.grid(row=7, column=5)
        self._bttn_save_project.grid(row=7, column=4)

        # eventhandler
        self._bttn_save_project["command"] = self.save_new_project
        self._bttn_cancel_project["command"] = self.project_window.destroy

        # configuration
        self._entry_project_name.insert(0, "Default Project")

    def save_new_project(self):
        """
        Writes the entry information from the Create Project Window
        into a new Project

        Returns a new Project
        """
        self._new_project = self._projectmanager.create_project()
        self._new_project.name = self._entry_project_name.get()
        self._new_project.notes = self._entry_project_notes.get(
            "1.0", "end-1c"
        )
        self._new_project.color = find_color(
            self._lb_color_project.get("active")
        )
        self._build_listboxes_pro()
        self._disable_bttns()
        self.project_window.destroy()

    def _edit_project_gui(self):
        """
        Generates a Window where a Project can be edited and saved

        contains
        an Entry for the Project name,
        an Entry for the Project notes,
        an Listbox for the Project color,
        a button to save the edited Project,
        a Button to cancel editing the Project

        Returns the edited Project (if saved)
        Returns the original Project (if canceled)
        """

        # find Project to edit
        self._find_active_project()
        self._project_to_edit = self.found_project

        # window
        self._edit_window = tk.Toplevel(self._root)
        self._edit_window.title("Edit Project")

        # elements
        self._lbl_dscrb_edit_name = tk.Label(
            self._edit_window, text="Project Name: "
        )
        self._lbl_dscrb_edit_notes = tk.Label(
            self._edit_window, text="Notes: "
        )
        self._lbl_dscrb_edit_color = tk.Label(
            self._edit_window, text="Color: "
        )

        self._bttn_cancel_edit = tk.Button(
            self._edit_window, text="cancel", activebackground="red", width=5
        )
        self._bttn_save_edit = tk.Button(
            self._edit_window, text="save", activebackground="green", width=5
        )

        self._lb_color_edit = tk.Listbox(self._edit_window, width=7, height=8)
        self._lb_color_edit.insert(0, "white")
        self._lb_color_edit.insert(1, "blue")
        self._lb_color_edit.insert(2, "red")
        self._lb_color_edit.insert(3, "green")
        self._lb_color_edit.insert(4, "yellow")
        self._lb_color_edit.insert(5, "purple")
        self._lb_color_edit.insert(6, "orange")
        self._lb_color_edit.insert(7, "pink")

        self._entry_edit_name = tk.Entry(self._edit_window)
        self._entry_edit_notes = tk.Text(
            self._edit_window, width=20, height=5
        )

        # layout
        self._lbl_dscrb_edit_name.grid(row=0, column=0, rowspan=2)
        self._entry_edit_name.grid(row=0, column=1, rowspan=2, columnspan=2)
        self._lbl_dscrb_edit_notes.grid(row=3, column=0)
        self._entry_edit_notes.grid(row=3, column=1, columnspan=2, rowspan=3)
        self._lbl_dscrb_edit_color.grid(row=1, column=4, columnspan=2)
        self._lb_color_edit.grid(row=2, column=4, columnspan=2, rowspan=4)
        self._bttn_cancel_edit.grid(row=7, column=5)
        self._bttn_save_edit.grid(row=7, column=4)

        # eventhandler
        self._bttn_save_edit["command"] = self.save_edited_project
        self._bttn_cancel_edit["command"] = self._edit_window.destroy

        # configuration
        self._entry_edit_name.insert(0, self._project_to_edit.name)
        self._entry_edit_notes.insert("1.0", self._project_to_edit.notes)

    def save_edited_project(self):
        """
        Writes the entry information from the Edit Project Window
        into the Project

        Returns the edited Project
        """
        self._project_to_edit.name = self._entry_edit_name.get()
        self._project_to_edit.notes = self._entry_edit_notes.get(
            "1.0", "end-1c"
        )
        self._project_to_edit.color = find_color(
            self._lb_color_edit.get("active")
        )
        self._delete_project_overview()
        self._build_listboxes_pro()
        self._edit_window.destroy()

    def _build_listboxes_pro(self):
        """
        Inserts the names of the Projects into the Listbox

        Returns Listbox elements
        """
        self._lb_projects.delete(0, tk.END)
        i = 0
        for pro in self._projectmanager.projects:
            self._lb_projects.insert(i, pro.name)
            i += 1

    def _update_project(self):
        """
        Build a new Project_GUI after destroying the existing frame,
        if present
        """
        try:
            self._delete_project_overview()
            self._find_active_project()
            self._new_project_gui = Project_GUI(
                self.found_project, self._fr_project, self
            )
            self._new_project_gui.grid()
        except AttributeError:
            pass

        self._build_listboxes_pro()
        self._disable_bttns()

    def _find_active_project(self):
        """
        Searches for the selected Project in the Listbox

        Returns the selected Project
        """
        self._selected_pro_name = self._lb_projects.get("active")
        self.found_project = None
        for project in self._projectmanager.projects:
            if project.name == self._selected_pro_name:
                self.found_project = project
                break

    def _delete_project_overview(self):
        """
        Clears the Project Overview frame
        """
        for widget in self._fr_project.winfo_children():
            widget.destroy()

    def _delete_project_gui(self):
        """
        Deletes a in the Listbox selected Project
        and updates the Listbox
        """
        self._find_active_project()
        self._project_to_delete = self.found_project
        self._projectmanager.delete_project(self._project_to_delete)
        self._build_listboxes_pro()
        self._disable_bttns()
        self._update_project()

    def _disable_bttns(self):
        """
        Disables 'delete Project', 'show Project', 'edit Project'
        if ProjectManager doesn't contain Projects
        """
        if self._projectmanager.is_empty():
            self._bttn_edit_project["state"] = "disabled"
            self._bttn_delete_project["state"] = "disabled"
            self._bttn_show_project["state"] = "disabled"
        else:
            self._bttn_edit_project["state"] = "normal"
            self._bttn_delete_project["state"] = "normal"
            self._bttn_show_project["state"] = "normal"
