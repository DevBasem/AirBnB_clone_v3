# AirBnB Clone_v2 - Command Interpreter

## Project Description

This project serves as the foundational step in creating an AirBnB clone, featuring a command-line interpreter designed to manage AirBnB objects. The command interpreter empowers users to perform essential CRUD (Create, Read, Update, Delete) operations on objects, as well as execute various commands to manipulate and query the application's data.

## Command Interpreter

### How to Start

To launch the command interpreter, execute the console.py script from the terminal:

```bash
$ ./console.py
```
### How to Use
Once the command interpreter is running, you can use the following commands:

- `help`: Display a list of available commands with their descriptions.
- `quit` or `EOF`: Exit the command interpreter.
- `create`: Create a new instance of a specified class.
- `update`: Update the attributes of an existing object.
- `show`: Display information about a specific object.
- `destroy`: Remove a specified object.
- `all`: Display information about all objects or all objects of a specific class.

## Examples

- Interactive Mode

```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) quit
$
```
- Non-interactive Mode

```bash
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
```
## Console Commands

- Create
```bash
$(hbnb) create User
```

- Update
```bash
$(hbnb) update User 1234-5678-9012 first_name "John"
```

- Show
```bash
$(hbnb) show User 1234-5678-9012
```

- Destroy
```bash
$(hbnb) destroy User 1234-5678-9012
```

- All
```bash
$(hbnb) all
```

- All for a Specific Class
```bash
$(hbnb) all User
```

## Console Commands
- `Object Management`: Easily create, retrieve, update, and delete objects within the AirBnB application.

- `Interactive` and `Non-interactive` Modes: Use the command interpreter interactively or supply commands via scripts for automated workflows.
## Authors

- Basem Ahmed
- Nada Shaban

## Acknowledgments
- Special thanks to the ALX staff for their guidance and support throughout the development of this project.
