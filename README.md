# Lonzo and Kyle Hbnb Console
## Description

Recreation of the AirBnb console. Takes input from user and stores data in JSON file. Takes various commands pertaining to and Airbnb listing.

## Requirements

* Must follow Pep8 style guidelines
* Allowed code editors are: vi, vim, and emacs
* Must  have `README.md`file
* Must have **#!/usr/bin/python3** as shebang
* All files must be executable
* All classes, modules, and functions should have documentation

## Unit Test Requirements
* All test files should end with a new line
* All test files should be inside a folder **tests**
* All test files should be python files
* All tests files and folder names should start with **test_**
* All classes, modules, and functions should have documentation

## Files, Folders, and Functions
 
### Unit Tests
* test_models - Directory for testing Amenity, BaseModel, City, Place, Review, State, and User classes
  * test_amenity.py - tests amenity class
  * test_base_model.py - tests BaseModel class
  * test_city.py - tests City class
  * test_place.py - tests Place class
  * test_review.py - tests Review class
  * test_state.py - tests State class
  * test_user.py - tests User class
* test_engine - Directory for testing FileStorage
  * test_file_storage.py - Tests FileStorage class

###  Models
* models - Directory for Amenity, BaseModel, City, Place, Review, State, and User classes
  * amenity.py - amenity class
  * base_model.py - BaseModel class
  * city.py - City class
  * place.py - Place class
  * review.py - Review class
  * state.py - State class
  * user.py - User class
* engine - Directory for FileStorage
  * file_storage.py - FileStorage class
	  * Deals with saving, reloading, and new objects.

### console.py
This is sort of like a shell from a previous project. There is a prompt and it takes input from the keyboard. Help functions were created to display help text if a command was used incorrectly.

* do_all(self, arg) - Prints all str representations of all instances based on class name. If no class name, prints all instances of all objects
* do_update(self, arg) - Update an instance based on class name and id
* do_show(self, arg) - Prints str representation of an instance
* do_create(self, arg) - Creates new BaseModel objects
* do_destroy(self, arg) - Destroys an instance based on class name and id
* do_quit(self, arg) - Executes the quit command to exit console.
* do_EOF(self, line) - Executes EOF
* emptyline(self) - deals with empty line given in console
* default(self, line) - deals with the command class name.all()
## Compilation

```c
./console.py
```
## Sample Output
### Interactive Mode

```c
~/user$ ./console.py
(hbnb)create User
1e756283-81d8-4061-b4d3-65c86335b4ca
(hbnb)

```

### Non-Interactive Mode

```c
~/user$ echo "create City" | ./console.py
(hbnb)2cc29369-fc0d-462f-abfd-c73b0093a5cb
~/user$
```

## Bugs

None at this time


## Authors

Lonzo Rust | [GitHub](https://github.com/lonzor)
Kyle Gross | [GitHub](https://github.com/kyle-gross)
