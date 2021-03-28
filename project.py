from task import *
import enum

class Color(enum.Enum):
    '''
    Enum for Project Color
    '''
    black = 'black'
    blue = 'blue'
    red = 'red'
    green = 'green'
    yellow = 'yellow'
    purple = 'purple'
    orange = 'orange'
    white = 'white'

def find_color(color_string):
    for col in Color:
        if col.value == color_string:
            return col

class Project():
    '''
    Project Object contains:
    name, projectmanager, color, notes, list of tasks

    can be constructed with 'Project(name, projectmanager)'
    '''


    def __init__(self, name, projectmanager, color=Color.black, tasks=[]):
        self.name = name
        self.projectmanager = projectmanager
        self.color = color
        self.notes = ''
        self._tasks = tasks

    
    def is_empty(self):
        '''
        Returns true, if list of Task is empty
        '''
        return len(self._tasks) == 0

    def create_task(self):
        '''
        Returns a new Task
        '''
        new_task = Task('Default Task', self)
        self._tasks.append(new_task)
        return new_task

    def delete_task(self, task):
        '''
        Deletes a task from list of Tasks

        task: task which should be deleted
        '''
        if task in self._tasks:
            self._tasks.remove(task)
    
    def delete_all_tasks(self):
        '''
        Deletes all Tasks of the Project
        '''
        if self.is_empty() == False:
            del self._tasks[:]
    
    def __str__(self):
        '''
        Returns a String with the Project Information
        '''
        printed_tasks = ''
        for task in self._tasks:
            printed_tasks += str(task)
            printed_tasks += '\n'
        return str( ' Name: ' + self.name + \
                    ' ProjectManager: ' + self.projectmanager.name +\
                    ' Color: ' + repr(self.color) + \
                    ' Notes: ' + self.notes + \
                    ' Tasks: \n' + printed_tasks)
