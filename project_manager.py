from project import *
import pickle


class ProjectManager:
    """
    ProjectManager Object contains:
    name, 
    list of projects

    can be constructed with 'ProjectManager(name: str)'
    """

    def __init__(self, name):
        self.name = name
        self.projects = []

    def is_empty(self):
        """
        Returns true, if list of Projects is empty
        """
        return len(self.projects) == 0

    def create_project(self):
        """
        Returns a new Project with the name 'Default Project'
        """
        self.new_project = Project("Default Project", self)
        self.projects.append(self.new_project)
        return self.new_project

    def delete_project(self, project):
        """
        Deletes a Project from list of Projects

        project: Project (which should be deleted)
        """
        if project in self.projects:
            self.projects.remove(project)

    def __str__(self):
        """
        Returns a String with the ProjectManager information
        """
        printed_projects = ""
        for project in self.projects:
            printed_projects += str(project)
            printed_projects += "\n"
        return str("Name: " + self.name + " Projects: \n" + printed_projects)
