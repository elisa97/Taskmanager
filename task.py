import uuid
import enum

class State(enum.IntEnum):
    '''
    Enum for Task State
    '''
    unprocessed = 0
    done = 1
    
class Priority(enum.IntEnum):
    '''
    Enum for Task Priority
    '''
    none = 0
    low = 1
    medium = 2
    high = 3

class Task():
    '''
    Task Object contains members:
    name, id, project, state, priority, notes

    can be constructed with 'Task(name, project)'
    '''
    
    def __init__(self, name, project, state=State.unprocessed,
                 priority=Priority.none):
        self.name = name
        self.id = uuid.uuid4()
        self.project = project
        self.state = state
        self.priority = priority
        self.notes = ''

    def do_task(self):
        '''
        set Task State to 'done' 
        '''
        self.state = State.done

    def undo_task(self):
        '''
        set Task State to 'done' 
        '''
        self.state = State.unprocessed

    def __str__(self):
        '''
        Returns a String with the Task Information
        '''
        return str( 'Task Name' + self.name + \
                    ' Project:' + self.project.name + \
                    ' State:' + repr(self.state) + \
                    ' Piority' + repr(self.priority) + \
                    ' Notes: ' + self.notes)

