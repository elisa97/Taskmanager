from app import *
import sys
import string


class CLI:
    def __init__(self):
        self._app = App()

    def start_programm(self):
        print(
            """Hello, welcome to the TaskManager CLI! \n 
            -------------------------------------------------------------\n 
            To interact with this CLI,
            please enter the character in the brackets,\n 
            e.g. [s] save: press 's' if you want to save"""
        )
        self._user_overview()

    def _user_overview(self):
        while True:
            if self._app.is_empty:
                entry = input(
                    """There are no Users yet.
                    Please insert [1] to add a new User
                    or [s] to save the programm."""
                )
                try:
                    entry == 1 or entry == "s"
                except ValueError:
                    print(
                        """Please insert a valid command. \n
                        [1] create a new user \
                        [s] save programm"""
                    )
                    continue
                if entry == "s":
                    App.save_app()
                    continue
                elif entry == "1":
                    self._create_user()
                    continue
                else:
                    continue
            else:
                print(
                    """Here is an User overview. \n 
                    Select a User by entering its number.\n 
                    If you want to create a new User, please insert [n]. \n 
                    If you want to save the programm, please insert [s]."""
                )
                print(self._app)
                user = input()
                if user == "n":
                    self._create_user()
                    continue
                elif user == "s":
                    self._app.save_app()
                try:
                    self._get_selected_user(user)
                except ValueError:
                    print("{} is no valid entry.".format(user))
                    continue
                selection = input(
                    """Your selected User is: {}.\n 
                    Options:    [1] select the User  \
                                [2] edit the User  \
                                [3] delete the User""".format(
                        self._selected_user.name
                    )
                )
                if selection == 1:
                    self.select_user()
                elif selection == 2:
                    self._edit_user()
                elif selection == 3:
                    self._delete_user()
                else:
                    continue

    def _get_selected_user(self, number):
        self._selected_user = self._app.projectmanagers[number]

    def _create_user(self):
        while True:
            user_name = input("Please insert the User name: ")
            print(
                """User name: {}. \n 
                If you want to save the User name, please insert [s]\n
                If you want to change the User name, 
                please insert any character EXCEPT [s] and [c] \n 
                If you want to cancel, please insert [c].""".format(
                    user_name
                )
            )
            entry = input()
            if entry == "s":
                self.new_user = self._app.create_projectmanager()
                self.new_user.name = user_name
                break
            elif entry == "c":
                break
            else:
                continue

    def _edit_user(self):
        while True:
            print("Current User name: {}".format(self._selected_user))
            user_name = input("Please insert a new User name")
            print(
                """User name: {}. \n 
                If you want to save the User name, please insert [s]\n \
                If you want to change the User name, 
                please insert any character EXCEPT [s] and [c] \n 
                If you want to cancel, please insert [c].""".format(
                    user_name
                )
            )
            entry = input()
            if entry == "s":
                self._selected_user.name = user_name
                break
            elif entry == "c":
                break
            else:
                continue

    def _delete_user(self):
        self._app.delete_projectmanager(self._selected_user)

    def _select_user(self):
        while True:
            if self._selected_user.is_empty():
                print(
                    """There are no Projects yet. \n
                    Please insert [1] to add a new Project."""
                )
                entry = input()
                try:
                    entry == 1 or entry == "s"
                except ValueError:
                    print(
                        """Please insert a valid command. \n 
                        [1] create a new project \
                        [s] save programm"""
                    )
                    continue
                if entry == "s":
                    App.save_app()
                elif entry == "1":
                    self._create_project()
                    continue
                else:
                    continue
            else:
                print(
                    """Here is a Project overview. \n 
                    Select a Project by entering its number.\n 
                    If you want to create a new Project, 
                    please insert [n]. \n 
                    If you want to go back to User Overview,
                    please insert [u]. \n 
                    If you want to save the programm, please insert [s]."""
                )
                print(self._app)
                pro = input()
                if pro == "n":
                    self._create_project()
                    continue
                elif pro == "u":
                    break
                elif pro == "s":
                    self._app.save_app()
                try:
                    self._get_selected_project(pro)
                except ValueError:
                    print("{} is no valid entry.".format(pro))
                    continue
                selection = input(
                    """Your selected Project is: {}.\n 
                    Options:    [1] select the Project  \
                                [2] edit the Project  \
                                [3] delete the Project""".format(
                        self._select_project.name
                    )
                )
                if selection == 1:
                    self.select_project()
                elif selection == 2:
                    self._edit_project()
                elif selection == 3:
                    self._delete_project()
                else:
                    continue

    def _get_selected_project(self, number):
        self._selected_project = self._selected_user.projects[number]

    def _create_project(self):
        while True:
            pro_name = input("Please insert the Project name: ")
            pro_notes = input("Please insert Project notes: ")
            print(
                """Project name: {}. \n 
                Project notes: {} \n 
                If you want to save the User name, please insert [s]\n 
                If you want to change the User name, 
                please insert any character EXCEPT [s] and [c] \n 
                If you want to cancel, please insert [c].""".format(
                    pro_name, pro_notes
                )
            )
            entry = input()
            if entry == "s":
                self.new_pro = self._selected_user.create_project()
                self.new_pro.name = pro_name
                self.new_pro.notes = pro_notes
                break
            elif entry == "c":
                break
            else:
                continue

    def _edit_project(self):
        while True:
            print(
                "Current Project name: {} \n \
                Current Project notes: {} \
                ".format(
                    self._selected_project.name, self._selected_project.notes
                )
            )
            pro_name = input(
                """Please insert a new Project name.\n 
                If you do not want to change the name, insert [x]."""
            )
            pro_notes = input(
                """Please insert Project notes:  \n 
                If you do not want to change the notes, insert [x]."""
            )
            if pro_name == "x":
                pro_name = self._selected_project.name
            if pro_notes == "x":
                pro_notes = self._selected_project.notes
            print(
                """Project name: {}. \n 
                Project notes: {} \n 
                If you want to save the changes, please insert [s]\n 
                If you want to change again, 
                please insert any character EXCEPT [s] and [c] \n 
                If you want to cancel, please insert [c].""".format(
                    self._selected_project.name, self._selected_project.notes
                )
            )
            entry = input()
            if entry == "s":
                self._selected_project.name = pro_name
                self._selected_project.notes = pro_notes
                break
            elif entry == "c":
                break
            else:
                continue

    def _delete_project(self):
        self._selected_user.delete_project(self._selected_project)

    def _select_project(self):
        while True:
            if self._selected_project.is_empty():
                print(
                    """There are no Tasks yet. \n
                        Please insert [1] to add a new Task."""
                )
                entry = input()
                try:
                    entry == 1 or entry == "s"
                except ValueError:
                    print(
                        """Please insert a valid command. \n 
                            [1] create a new project  \
                            [s] save programm"""
                    )
                    continue
                if entry == "s":
                    App.save_app()
                elif entry == "1":
                    self._create_task()
                    continue
                else:
                    continue
            else:
                print(
                    """Here is a Task overview. \n 
                        Select a Task by entering its number.\n 
                        If you want to create a new Task, please insert [n]. \n 
                        If you want to save the programm, please insert [s]. \n 
                        If you want to go back to the Project Overview, 
                        please insert [p]."""
                )
                print(self._app)
                task = input()
                if task == "n":
                    self._create_project()
                    continue
                elif task == "p":
                    break
                elif task == "s":
                    self._app.save_app()
                try:
                    self._get_selected_task(task)
                except ValueError:
                    print("{} is no valid entry.".format(task))
                    continue
                print(
                    """Your selected Task is: {}.\n 
                        Options:    [1] change Task state  \
                                    [2] edit the Task  \
                                    [3] delete the Task""".format(
                        self._selected_task.name
                    )
                )
            selection = input()
            if selection == 1:
                self._change_state()
                continue
            elif selection == 2:
                self._edit_task()
                continue
            elif selection == 3:
                self._delete_task()
                continue
            else:
                continue

    def _get_selected_task(self, number):
        self._selected_task = self._selected_project.tasks[number]

    def _change_state(self):
        if self._selected_task.state == 0:
            self._selected_task.do_task()
        elif self._selected_task.state == 1:
            self._selected_task.undo_task()

    def _create_task(self):
        while True:
            task_name = input("Please insert the Task name: ")
            task_notes = input("Please insert Task notes: ")
            task_prio = input(
                """Please insert Task Priority:\n 
                                [0] none  \
                                [1] low  \
                                [2] medium  \
                                [3] high"""
            )
            task_priority = find_priority(task_prio)
            print(
                """Task name: {}. \n 
                Task notes: {} \n 
                Task priority: {} \n 
                If you want to save the Task name, please insert [s]\n 
                If you want to change the Task name, 
                please insert any character EXCEPT [s] and [c] \n 
                If you want to cancel, please insert [c].""".format(
                    task_name, task_notes, task_priority
                )
            )
            entry = input()
            if entry == "s":
                self.new_task = self._selected_user.create_project()
                self.new_task.name = task_name
                self.new_task.notes = task_notes
                self.new_task.priority = task_priority
                break
            elif entry == "c":
                break
            else:
                continue

    def _edit_task(self):
        while True:
            print(
                """Current Task name: {} \n 
                Current Task notes: {} \n 
                Current Task priority: {} \n 
                """.format(
                    self._selected_task.name,
                    self._selected_task.notes,
                    self._selected_task.priority,
                )
            )
            task_name = input(
                """Please insert a new Task name.\n 
                If you do not want to change the name, insert [x]."""
            )
            task_notes = input(
                """Please insert new Task notes:  \n 
                If you do not want to change the notes, insert [x]."""
            )
            task_priority = input(
                """Please insert a new Task priority:  \n 
                                [0] none  \
                                [1] low  \
                                [2] medium  \
                                [3] high \n 
                If you do not want to change the priority, insert [x]."""
            )
            if task_name == "x":
                task_name = self._selected_task.name
            if task_notes == "x":
                task_notes = self._selected_task.notes
            if task_priority == "x":
                task_priority = self._selected_task.priority
            print(
                """Task name: {}. \n 
                Task notes: {} \n 
                Task priority: {} \n 
                If you want to save the changes, please insert [s]\n 
                If you want to change again, 
                please insert any character EXCEPT [s] and [c] \n 
                If you want to cancel, please insert [c].""".format(
                    self._selected_task.name,
                    self._selected_task.notes,
                    self._selected_task.priority,
                )
            )
            entry = input()
            if entry == "s":
                self._selected_task.name = task_name
                self._selected_task.notes = task_notes
                self._selected_task.priority = task_priority
                break
            elif entry == "c":
                break
            else:
                continue

    def _delete_task(self):
        self._selected_project.delete_task(self._selected_task)

if __name__ == '__main__':
    cli = CLI()
    cli.start_programm()