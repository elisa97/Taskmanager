from task import *
import enum

class Color(enum.IntEnum):
    black = 0
    blue = 1
    red = 2
    green = 3
    yellow = 4
    purple = 5
    orange = 6
    white = 7

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
        return str( ' Name: ' + self.name + \
                    ' Color: ' + repr(self.color) + \
                    ' Notes: ' + self.notes + \
                    ' Tasks: \n' + printed_tasks)
