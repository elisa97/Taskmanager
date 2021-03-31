from task import *
import enum


class Color(enum.Enum):
    """
    Enum for Project Color
    """

    white = "white"
    blue = "blue"
    red = "red"
    green = "green"
    yellow = "yellow"
    purple = "purple"
    orange = "orange"
    pink = "pink"


def find_color(color_string):
    """
    Finds Color for a given String

    Returns a Color

    color_string: str
    """
    for col in Color:
        if col.value == color_string:
            return col


class Project:
    """
    Project Object contains:
    name, projectmanager (corresponds to User),
    color (backgroundcolor in the tkinter GUI), notes, list of Tasks

    can be constructed with
    'Project(name: str, projectmanager: Projectmanager)'
    """

    def __init__(self, name, projectmanager, color=Color.white):
        self.name = name
        self._projectmanager = projectmanager
        self.color = color
        self.notes = ""
        self.tasks = []

    def is_empty(self):
        """
        Returns true, if list of Task is empty
        """
        return len(self.tasks) == 0

    def create_task(self):
        """
        Returns a new Task with the name 'Default Task'
        """
        self.new_task = Task("Default Task", self)
        self.tasks.append(self.new_task)
        return self.new_task

    def delete_task(self, task):
        """
        Deletes a task from list of Tasks

        task: Task (which should be deleted)
        """
        if task in self.tasks:
            self.tasks.remove(task)

    def delete_alltasks(self):
        """
        Deletes all Tasks of the Project
        """
        if self.is_empty() == False:
            del self.tasks[:]

    def __str__(self):
        """
        Returns a String with the Project information
        """
        printedtasks = ""
        i = 0
        for task in self.tasks:
            printedtasks += "[" + str(i) + "] "
            printedtasks += str(task)
            printedtasks += "\n"
            i += 1
        return str(
            " Name: "
            + self.name
            + " Notes: "
            + self.notes
            + " Tasks: \n"
            + printedtasks
        )
