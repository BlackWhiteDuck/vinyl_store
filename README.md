# vinyl_store

## How to run the application with the virtual environment:
1. Please ensure that you have the Python 3.x prerequisite.
2. First create a new folder on your Desktop, with a name of your choice and add the project (vinyls) within the folder.
3. Next enter your command prompt, and go into the folder directory, by typing "cd Desktop" then enter, followed by "cd 'Name_of_your_folder'" and then enter.
4. Now download pip by typing: "python -m pip install pip" in your command prompt.
5. Now download virtual environments by typing: "pip install virtualenv" in your command prompt.
6. Now create a virtual environment by typing: "python -m virtualenv venv"... making your virtual enviornment's name "venv" in your command prompt.
7. Now enter "venv" by typing: "cd venv" in your command prompt.
8. Now enter "Scripts" by typing: "cd Scripts" in your command prompt.
9. Next activate Scripts by simply typing: "activate" in your command prompt.
10. Then go back to your folder by typing "cd.." twice to ensure your're back in your folder in your command prompt.
11. Next cd into the project (vinyls) by typing: "cd vinyls" in your command prompt.
12. Now download the requirements.txt file by typing: "pip install -r requirements.txt" in your command prompt.
13. Now run the application by typing: "python manage.py runserver" in your command prompt.

## How to run the application with Docker:
1. Please ensure that you have the Docker 3.x prerequisite.
2. Enter your command prompt and type: "docker build -t vinyl_store ./" in your command prompt.
3. Now run it by typing: "docker run -p 8000:8000 vinyl_store" in your command prompt.
