from app import *
import sys
import string


class CLI:
    def __init__(self):
        self._app = App()

    def _start_programm(self):
        print(
            "Hello, welcome to the TaskManager CLI! \n \
            -------------------------------------------------------------\n \
            To interact with this CLI,\
            please enter the character in the brackets,\n \
            e.g. [s] save: ipress 's' if you want to save"
        )

    def _user_overview(self):
        while True:
            if self._app.is_empty:
                print('There are no Users yet. \
                    Please insert [1] to add a new User.')
                entry = sys.argv[1]
                try:
                    entry == 1 or entry == 's'
                except ValueError:
                    print('Please insert a valid command. \n \
                        [1] create a new user \n \
                        [s] save programm')
                    continue
                if entry == 's':
                    App.save_app()
                elif entry == '1':
                    self._create_user()
                    continue
                else:
                    continue
            else:
                print('Here is an User overview. \n \
                    Select a User by entering its number.')
                print(self._app)
                entry = sys.argv[1]
                try:
                    selected_user = self._app.projectmanagers[entry]
                except ValueError:
                    print('{} is no valid entry.'.format(entry))
                    continue
                print('Your selected User is: {}.\n \
                    Options:    [1] select the User  \
                                [2] edit the User  \
                                [3] delete the User ')
                
                


    def _create_user(self):
        while True:
            print('Please insert the User name: ')
            user_name = sys.argv[1]
            print('User name: {}. \n \
                If you want to save the User name, please insert [s]\n \
                If you want to change the User name, \
                please insert any character EXCEPT [s] and [c] \n \
                If you want to cancel, please insert [c].'.format(user_name))
            entry = sys.argv[1]
            if entry == 's':
                self.new_user = self._app.create_projectmanager()
                self.new_user.name = user_name
                break
            elif entry == 'c':
                break
            else:
                continue

    def _edit_user(self, self._user_to_edit):
        while True:
            print('Current User name: {}. \n \
                Please insert a new User name.'.format(self._user_to_edit))