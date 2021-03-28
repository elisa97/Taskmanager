from project import *
import pickle

class ProjectManager():
    '''
    ProjectManager Object contains:
    name, list of projects

    can be constructed with 'ProjectManager(name)'
    '''

    def __init__(self, name, projects=[]):
        self.name = name
        self._projects = projects

    def _create_project(self):
        '''
        Returns a new Project
        '''
        new_project = Project('Default Project')
        self._projects.append(new_project)
        return new_project

    def _delete_project(self, project):
        '''
        Deletes a Project from list of Projects

        project: Project which should be deleted
        '''
        if project in self._projects:
            self._projects.remove(project)

    def _save_projects(self):
        '''
        Saves list of Projects to a file
        Returns a pickle file
        '''
        outfile = open('saved_projects', 'wb')
        pickle.dump(self._projects, outfile)
        outfile.close()

    def _load_projects(self):
        '''
        Loads list of Projects to a file
        Returns a list of Projects
        '''
        infile = open('saved_projects','rb')
        self._projects = pickle.load(infile)
        infile.close()
    
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
