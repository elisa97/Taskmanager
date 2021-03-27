from gui import *

if __name__ == '__main__':


    #Tests

    new_projectmanager = ProjectManager()
    new_project = new_projectmanager._create_project()
    new_project.name = 'Hallo'

    new_task = new_project.create_task()
    task_2 = new_project.create_task()

    task_3 = new_project.create_task()
    task_3.name = 'task 3'

    print(new_projectmanager)

    new_projectmanager._save_projects()

    del new_projectmanager

    projectmanager_2 = ProjectManager()

    projectmanager_2._load_projects()

    print(projectmanager_2)


    GUI()