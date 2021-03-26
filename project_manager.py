from project import *
import pickle

class ProjectManager():

    def __init__(self):
        self._projects = []

    def _create_project(self):
        new_project = Project('Default Project')
        self._projects.append(new_project)
        return new_project

    def _delete_project(self, project):
        if project in self._projects:
            self._projects.remove(project)

    def _save_projects(self):
        outfile = open('saved_projects', 'wb')
        pickle.dump(self._projects, outfile)
        outfile.close()

    def _load_projects(self):
        infile = open('saved_projects','rb')
        self._projects = pickle.load(infile)
        infile.close()
    
    def __str__(self):
        printed_projects = ''
        for project in self._projects:
            printed_projects += str(project)
            printed_projects += '\n'
        return str('Projects: \n' + printed_projects)
