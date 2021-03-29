from project import *
import pickle

class ProjectManager():
    '''
    ProjectManager Object contains:
    name, list of projects

    can be constructed with 'ProjectManager(name)'
    '''

    def __init__(self, name):
        self.name = name
        self._projects = []

    def _create_project(self):
        '''
        Returns a new Project
        '''
        self.new_project = Project('Default Project', self)
        self._projects.append(self.new_project)
        return self.new_project

    def _delete_project(self, project):
        '''
        Deletes a Project from list of Projects

        project: Project which should be deleted
        '''
        if project in self._projects:
            self._projects.remove(project)

    
    def __str__(self):
        '''
        Returns a String with the ProjectManager Information
        '''
        printed_projects = ''
        for project in self._projects:
            printed_projects += str(project)
            printed_projects += '\n'
        return str( 'Name: ' + self.name + \
                    ' Projects: \n' + printed_projects)
