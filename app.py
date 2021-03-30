from project_manager import *
import pickle

class App():

    def __init__(self):
        self._projectmanagers = []

    def is_empty(self):
        '''
        Returns true, if list of Projectmanagers is empty
        '''
        return len(self._projectmanagers) == 0


    def create_projectmanager(self):
        '''
        Returns a new Projectmanager
        '''
        self.new_projectmanager = ProjectManager('Default User')
        self._projectmanagers.append(self.new_projectmanager)
        return self.new_projectmanager

    def delete_projectmanager(self, projectmanager):
        '''
        Deletes a Projectmanager from list of Projectmanagers

        project: Projectmanager which should be deleted
        '''
        if projectmanager in self._projectmanagers:
            self._projectmanagers.remove(projectmanager)

    def save_app(self):
        '''
        Saves list of Projectmanagers to a file
        Returns a pickle file
        '''
        outfile = open('saved_app', 'wb')
        pickle.dump(self._projectmanagers, outfile)
        outfile.close()

    def load_app(self):
        '''
        Loads list of Projectmanagers to a file
        Returns a list of Projectmanagers
        '''
        infile = open('saved_app','rb')
        self._projectmanagers = pickle.load(infile)
        infile.close()

    def __str__(self):
        '''
        Returns a String with the App Information
        '''
        printed_projectmanagers = ''
        for projectmanager in self._projectmanagers:
            printed_projectmanagers += str(projectmanager)
            printed_projectmanagers += '\n'
        return str(' Projects: \n' + printed_projectmanagers)

