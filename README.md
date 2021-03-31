# TaskManager
## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Usage](#usage)

### General Info
***
This is a tool to simply organize your tasks and projects.
You can add, edit, delete and check tasks which you can arrange in projects. It gives you the opportunity to create multiple users who can create their own projects. 


## Technologies
***
A list of technologies used within the project:
* [Python3](https://www.python.org/): Version 3.8.5
* [TkInter](https://wiki.python.org/moin/TkInter): Version 8.6
* [Pickle](https://wiki.python.org/moin/UsingPickle): Version 4.0

## Installation
***
To execute this programm, these programms are required:
* Python3
* TkInter


### Installation of *Python3*
***
To install *Python3*, download the programm [here](https://www.python.org/downloads/)
or use the following command line (for Linux-Users):  
`$ sudo apt-get install python3 `


### Installation of *TkInter*
***
To install *TkInter*, check out [here](https://tkdocs.com/tutorial/install.html)
or use the following command line (for Linux-Users):  
`$ sudo apt-get install python3-tk `



## Usage
***

### How to start the programm
***
If you **have installed the required programms**, you can use the following command lines to start this programm:
* if you have the zip file  *TaskManager_119599.zip* on your computer
    ```
    $ cd ../path/to/the/zip-file/location
    $ unzip TaskManager_119599.zip
    $ cd /TaskManager_119599
    $ python3 main.py
    ```
* from [github](https://github.com/elisa97/Taskmanager):
    ```
    $ git clone https://github.com/elisa97/Taskmanager
    $ cd ../path/to/the/file
    $ python3 main.py
    ```
* if you want to start the CLI of the programm, please use the following command line:  
    `$ python3 cli.py`

### First steps
***
When you **start the *TaskManager* for the first time**, there won't be any Users, Projects or Tasks. 
So please don't wonder, if there's just a small window with a slim menu. Follow these few steps, to generate your first tasks:

* **create your first user**:
    * select *Users* in the Menu
    * select *User Overview* in the submenu and a new window with the *User Overview* will open
    * press the button *add a new User* and another new window *create a new User* will open
    * insert a User name into the entry and press the button *save*
    * the window *create a new User* will close automatically and you'll see your new User in a listbox in the *User Overview*

* **create your first project**
    * click onto your new User in the listbox and press the button *select User* afterwards
    * the *User Overview* window will close and you'll see a new pressable button *create Project* in the main window, which you should take
    * after clicking onto the button, a new window will appear where you can insert your Project name and Project notes and pick a color for the background of your *Project Overview*. Please take a look if the color is still selected before you're pressing the button *save*
    * after that, the window *create a new Project* will be closed and your new Project will appear in a listbox

* **create your first Task**
    * select your new Project in the listbox and then click to the button *show project*
    * there will appear a *Project Overview* with the backgroundcolor you picked for your Project
    * you now choose *add a new Task* and similar to the User and Project before, a new window will pop up
    * there you can enter the Task name, Task notes and before saving, select a Task priority
    * after you saved the Task, it will show up below your *Project Overview*

* **save the programm**
    before closing the programm, please be sure you've saved your new Users, Projects and Tasks:
    * select *file* in the menu of the main window
    * click *save file*, then all changes will be saved
    * you can close the main window afterwards and when you'll start the programm the next time, your changes will be there

### How to go on using the programm
***
After **finishing the first steps**, you may have seen that the GUI of the *TaskManager* is simple and hopefully understandable.
E.g. if you haven't created any Users, the buttons *edit User*, *select User* and *delete User* will be disabled. Same with Projects and Tasks.
Now to the further usage and features of this programm:

* ***Users*** 
    Only 1 User can be selected at a time.
    Users can handle arbitrary Projects and a Project can include arbitrary Tasks. But they are connected to the User:  
    **Projects are User specific and can't be shared with other Users!**
    * create *Users*
        as described in the [First Steps](###first-steps)
    * edit *Users*
        a window will appear, where you can change the User name and save it
    * delete *Users*
        once deleted, a User can't be restored. 
        **Attention: If you delete a User, you also delete all Projects and Tasks of this User!**
    * select *User*
        is like a sign in with this User, it will show an overview of the Projects of the User

* ***Projects***
    Only 1 *Project Overview* of a Project can be shown at a time.
    Projects can organize arbitrary Tasks. But they are connected to the Project:
    **Tasks are Project specific and can't be shared with other Projects or other Users!**  
    * create *Project*
        like described in the [First Steps](###first-steps)
    * edit *Project*
        a window will pop up, where you can modify your Project name, notes and backgroundcolor and save it
    * delete *Project*
        once deleted, a Project can't be restored.
        **Attention: If you delete a Project, you also delete all Tasks of this Project!**
    * show *Project*
        will show an overview of your listbox-selected Project and the Tasks of this Project

* ***Project Overview***
    Here you see name, notes and Tasks of a Project and have further options:
    * add a new *Task*
        like described in the [First Steps](###first-steps)
    * hide *Tasks*
        will just hide all Tasks, but won't delete them
        can be checked and un-checked
    * show done *Tasks*
        will just show Tasks, you already marked as done
        can be checked and un-checked 
    * delete all *Tasks*
        **will delete all Tasks, also the Tasks you checked as *done***

* ***Tasks***
    Tasks will appear in a list below the *Project Overview*
    Every Task:
    * has a checkbutton on the left, which marks the Task as *done*, or *unprocessed* if un-checked again
    * the name of the task
    * a checkbutton to show the notes of the Task
        **Please just check this button on 1 Task at the same time!**
    * a button *edit*, which makes appear a new window, where the Task name, notes and priority can be edited and saved
    * a button *delete*, which unrecoverably deletes the Task 
    * a color, if the *priority* isn't *none*:
        * red, if the priority is high
        * yellow, if the priority is medium
        * green, if the priority is low 
