from project_manager import *
import pickle


class App:
    """
    Project App contains:
    list of Projectmanagers

    can be constructed with
    'App()'
    """

    def __init__(self):
        self.projectmanagers = []

    def is_empty(self):
        """
        Returns true, if list of Projectmanagers is empty
        """
        return len(self.projectmanagers) == 0

    def create_projectmanager(self):
        """
        Returns a new Projectmanager with the name 'Default User'
        """
        self.new_projectmanager = ProjectManager("Default User")
        self.projectmanagers.append(self.new_projectmanager)
        return self.new_projectmanager

    def delete_projectmanager(self, projectmanager):
        """
        Deletes a Projectmanager from list of Projectmanagers

        projectmanager: Projectmanager (which should be deleted)
        """
        if projectmanager in self.projectmanagers:
            self.projectmanagers.remove(projectmanager)

    def save_app(self):
        """
        Saves list of Projectmanagers to a pickle file

        Returns a pickle file named 'saved_app'
        """
        outfile = open("saved_app", "wb")
        pickle.dump(self.projectmanagers, outfile)
        outfile.close()

    def load_app(self):
        """
        Loads list of Projectmanagers from a pickle file

        Returns a list of Projectmanagers
        """
        infile = open("saved_app", "rb")
        self.projectmanagers = pickle.load(infile)
        infile.close()

    def __str__(self):
        """
        Returns a String with the App information
        """
        printed_projectmanagers = ""
        i = 0
        for projectmanager in self.projectmanagers:
            printed_projectmanagers += '[' + str(i) + "] "
            printed_projectmanagers += str(projectmanager)
            printed_projectmanagers += "\n"
        return str(" Users: \n" + printed_projectmanagers)
