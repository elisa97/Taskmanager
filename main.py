from app_gui import *

if __name__ == '__main__':


    #Tests

    '''new_projectmanager = ProjectManager('test')
    new_project = new_projectmanager._create_project()
    new_project.name = 'Hallo'

    new_task = new_project.create_task()
    task_2 = new_project.create_task()

    task_3 = new_project.create_task()
    task_3.name = 'task 3'

    print(new_projectmanager)

    new_projectmanager._save_projects()

    del new_projectmanager'''

    #projectmanager_2 = ProjectManager('test2')

    #projectmanager_2._load_projects()

    #print(projectmanager_2)

    app = App()

    user = app.create_projectmanager()
    user.name = 'heinz'
    print(app)
    app.save_app()
    app.delete_projectmanager(user)
    app.save_app()
    del app

    new_app = App()
    new_app.load_app()
    print(new_app)

    new_app.save_app()
    print(new_app)


    App_GUI()