# part-manager

### Description

A desktop app using sqlite3 to store item data 

## Stack Components

- [tkinter]
- [sqlite3]
- [pyinstaller]


## Development
### Sandbox setup
1. Clone this repository and navigate to it
2. Install pipenv
    ```
    pip3 install pipenv
    ```
3. Activate pipenv
    ```
    pipenv shell
    ```
4. Install dependencies
    ```
    pipenv install pyinstaller


### Create desktop app (create .exe file from .py)
Run below command in Terminal:
pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Versions/8.5/Resources/Documentation/Reference/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Versions/8.5/Resources/Documentation/Reference/Tcl':'tcl' part_manager.py
