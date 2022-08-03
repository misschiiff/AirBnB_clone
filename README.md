# AirBnB clone - The console

![AirBnB](https://drive.google.com/file/d/1qd7wmuI_P2X2UiomHDCK00PlUsbTI24k/view?usp=drivesdk)


The console is a Command interpreter to manage your AirBnB objects

## Description

This project put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

*Whats a AirBnB command interpreter?*

A command be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc
Do operations on objects (count, compute stats, etc)
Update attributes of an object
Destroy an object

### Execution

To use in a *interactive mode*, compile `$ ./console.py` 

Usage: *(hbnb)* [commands]

Example:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$


To use in a *in non-interactive mode*

Example:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$



*Architecture Diagram*
![console](https://semanticadigital.com/wp-content/uploads/2017/01/815046647d23428a14ca.png)


## Authors

* Bryan Somtochukwu <[bryansomto](github.com/bryansomto)>
* BRIDGET IZBA <[misschiiff](Www.GitHub.com/misschiiff)>


