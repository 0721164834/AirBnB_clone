---

# AirBnB Clone Project

## Description
The AirBnB Clone project aims to develop a simplified version of the AirBnB platform. It includes the implementation of various classes such as User, State, City, and Place, along with a command-line interface (CLI) to manage AirBnB objects.

## Command Interpreter
The command interpreter allows users to interact with the AirBnB objects through textual commands. Below are the details on how to start and use the command interpreter:

### How to Start
To start the command interpreter, follow these steps:
1. Open a terminal window.
2. Navigate to the project directory.
3. Run the command `./console.py` to start the command interpreter.

### How to Use
Once the command interpreter is started, you can use the following commands:
- `create <class_name>`: Create a new object of the specified class.
- `show <class_name> <object_id>`: Show details of the specified object.
- `update <class_name> <object_id> <attribute_name> "<new_value>"`: Update the specified attribute of the object.
- `destroy <class_name> <object_id>`: Delete the specified object.
- `all <optional_class_name>`: Show details of all objects of the specified class, or all objects if no class is specified.
- `quit`: Exit the command interpreter.

### Examples
Here are some examples of how to use the command interpreter:
- To create a new User object: `create User`
- To show details of a User with ID "123": `show User 123`
- To update the name attribute of a User with ID "123": `update User 123 name "John Doe"`
- To delete a User with ID "123": `destroy User 123`
- To show details of all City objects: `all City`
