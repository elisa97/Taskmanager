import uuid
import enum

class State(enum.IntEnum):
    unprocessed = 0
    done = 1
    
class Priority(enum.IntEnum):
    none = 0
    low = 1
    medium = 2
    high = 3

class Task():
    
    def __init__(self, name, project, state=State.unprocessed,
                 priority=Priority.none):
        self.name = name
        self.id = uuid.uuid4()
        self.project = project
        self.state = state
        self.priority = priority
        self.notes = ''

    def do_task(self):
        self.state = State.done


    def __str__(self):
        return str( 'Task Name' + self.name + \
                    ' Project:' + self.project.name + \
                    ' State:' + repr(self.state) + \
                    ' Piority' + repr(self.priority) + \
                    ' Notes: ' + self.notes)

