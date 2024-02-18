# CRUD Todo List

## Description
Flask Todo List created following a YouTube tutorial by Python Engineer.
One of the changes I made was not allowing an empty task to be added.
I will continue to make this app more my own by adding to it.

### Frontend/Backend
The backend uses Flask, SQLite with SQLAlchemy, and Python. 
The front end uses HTML and the SemanticUI Componenet Framework.

### Usage
- You can create one or many task to add to your list
- Pressing update changes the status label from incomplete to complete with a green label background
- You can undo the status by pressing update again
- You can delete the task regardless if you have completed it or not.

<img src="img\todo-list.png" width="400" height="400">

# Installation using Poetry:
1. You should have Poetry and Python(3.10) installed  
2. Clone the repo
3. In the project directory open the terminal
4. Run the command:
``` poetry install ```

5. Activate the virtual enviorment:
``` .venv\Scripts\activate ```

6. Run the app in the development environment
``` python app.py ```