import tkinter as tk
from app import *
from projectmanager_gui import *

class App_GUI(tk.Frame):

    def __init__(self, root=tk.Tk()):
        super().__init__(root)

        self._root = root
        self._app = App()

        try:
            self._app.load_app()
        except FileNotFoundError:
            pass

        self._create_elements()
    
    def _create_elements(self):
        '''
        Build the main window of the App with the menu
        and the frame for the projectmanager_gui
        '''
        
        #frames
        self.fr_projectmanager_gui = tk.Frame(self)

        self.fr_projectmanager_gui.grid(row=3, column=0, rowspan=10)

        #elements app menu
        self._menu = tk.Menu(self._root)
        self._root.config(menu=self._menu)
        self._file_menu = tk.Menu(self._menu)
        self._menu.add_cascade(label='File', menu=self._file_menu)
        self._file_menu.add_command(label='save file', command=self._app.save_app)
        #self._file_menu.add_command(label='load file', command=self._app.load_app)
        self._user_menu = tk.Menu(self._menu)
        self._menu.add_cascade(label='Users', menu=self._user_menu)
        self._user_menu.add_command(label='User Overview', command=self._create_user_window)

        self._root.mainloop()


    def _create_user_window(self):
        '''
        Generates a window with the User Overview
        existing Users can be selected, edited or deleted
        new Users can be created
        '''
        
        #hide projectmanager if opened
        try:
            self._shown_projectmanager_gui.grid_forget()
        except AttributeError:
            pass

        #window
        self._user_window = tk.Toplevel(self._root)
        self._user_window.title('User Overview')

        #elements
        self._lbl_user_name = tk.Label(self._user_window, text='Users: ')
        self._lb_users = tk.Listbox(self._user_window)
        self._bttn_add_user = tk.Button(self._user_window, text='+ add a new User')
        self._bttn_edit_user = tk.Button(self._user_window, text='edit User')
        self._bttn_delete_user = tk.Button(self._user_window, text='delete User', activebackground='red')
        self._bttn_select_user = tk.Button(self._user_window, text='select User', activebackground='green')

        #layout
        self._lbl_user_name.grid(row=0, column=0)
        self._bttn_add_user.grid(row=1, column=0)
        self._lb_users.grid(row=2, column=0, rowspan=10, sticky='n')
        self._bttn_edit_user.grid(row=14, column=0)
        self._bttn_delete_user.grid(row=15, column=0)
        self._bttn_select_user.grid(row=13, column=0)

        #eventhandler
        self._bttn_add_user['command'] = self._create_new_user_gui
        self._bttn_delete_user['command'] = self._delete_user_gui
        self._bttn_edit_user['command'] = self._edit_user_gui
        self._bttn_select_user['command'] = self._select_projectmanager

        self._disable_bttns()
        self._build_listboxes_gui()


    def _create_new_user_gui(self):
        '''
        Generates a window where a new User 
        can be created and saved

        Returns the new User or nothing
        '''
        self._new_user_window = tk.Toplevel(self._root)
        self._new_user_window.title('Create a new User')

        #elements
        self._lbl_dscrb_user_name = tk.Label(self._new_user_window, text='User Name:')
        self._entry_user_name = tk.Entry(self._new_user_window)
        self._bttn_save_new_user = tk.Button(self._new_user_window, text='save', activebackground='green')
        self._bttn_cancel_new_user = tk.Button(self._new_user_window, text='cancel', activebackground='red')

        #layout
        self._lbl_dscrb_user_name.grid(row=0, column=0)
        self._entry_user_name.grid(row=0, column=1, columnspan=2)
        self._bttn_save_new_user.grid(row=2, column=1)
        self._bttn_cancel_new_user.grid(row=2, column=2)

        #eventhandler
        self._bttn_save_new_user['command'] = self._save_new_user
        self._bttn_cancel_new_user['command'] = self._new_user_window.destroy

    def _save_new_user(self):
        '''
        
        '''
        self._new_user = self._app.create_projectmanager()
        self._new_user.name = self._entry_user_name.get()

        self._build_listboxes_gui()
        self._disable_bttns()
        self._new_user_window.destroy()


    def _edit_user_gui(self):
        '''
        '''

        self._find_active_user()
        self._user_to_edit = self._found_user

        self._edit_user_window = tk.Toplevel(self._root)
        self._edit_user_window.title('Edit User')

        #elements
        self._lbl_dscrb_edit_user_name = tk.Label(self._edit_user_window, text='User Name:')
        self._entry_edit_user_name = tk.Entry(self._edit_user_window)
        self._entry_edit_user_name.insert(0, self._user_to_edit.name)
        self._bttn_save_edit_user = tk.Button(self._edit_user_window, text='save', activebackground='green')
        self._bttn_cancel_edit_user = tk.Button(self._edit_user_window, text='cancel', activebackground='red')


        #layout
        self._lbl_dscrb_edit_user_name.grid(row=0, column=0)
        self._entry_edit_user_name.grid(row=0, column=1, columnspan=2)
        self._bttn_save_edit_user.grid(row=2, column=1)
        self._bttn_cancel_edit_user.grid(row=2, column=2)

        #eventhandler
        self._bttn_save_edit_user['command'] = self._save_edited_user
        self._bttn_cancel_edit_user['command'] = self._edit_user_window.destroy

    def _save_edited_user(self):
        '''
        '''
        self._user_to_edit.name = self._entry_edit_user_name.get()
        self._build_listboxes_gui()
        self._disable_bttns()
        self._edit_user_window.destroy()

    def _build_listboxes_gui(self):
        self._lb_users.delete(0, tk.END)
        i = 0
        for user in self._app.projectmanagers:
            self._lb_users.insert(i, user.name)
            i +=1

    def _find_active_user(self):
        '''
        '''
        self._selected_user_name = self._lb_users.get('active')
        self._found_user = None
        for user in self._app.projectmanagers:
            if user.name == self._selected_user_name:
                self._found_user = user
                break

    def _select_projectmanager(self):
        '''
        '''   
        for widget in self.fr_projectmanager_gui.winfo_children():
            widget.destroy()

        self._find_active_user()
        self._shown_projectmanager_gui = ProjectManager_GUI(self._found_user, self.fr_projectmanager_gui, self._root)
        self._shown_projectmanager_gui.grid()
        self._build_listboxes_gui()
        self._user_window.destroy()

    def _delete_user_gui(self):
        '''
        '''
        self._find_active_user()
        self._user_to_delete = self._found_user
        self._app.delete_projectmanager(self._user_to_delete)
        self._disable_bttns()
        self._build_listboxes_gui()
    
    def _disable_bttns(self):
        '''
        '''
        if self._app.is_empty():
            self._bttn_delete_user['state'] = 'disabled'
            self._bttn_edit_user['state'] = 'disabled'
            self._bttn_select_user['state'] = 'disabled'
        else:
            self._bttn_edit_user['state'] = 'normal'
            self._bttn_delete_user['state'] = 'normal'
            self._bttn_select_user['state'] = 'normal'
