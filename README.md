# Web-Service-for-Architecture-IS
Parsing weather data at airports and checking for some conditions. The output of the result of the weather on the local server in the form of a html report

Folder app stores directly application

To run the program, you need to install it on the environment where you are going to launch the program (terminal, virtual environment, etc.), python 3 and library flask

The __init__.py file (in the 'app' folder) is an intermediate file between run.py and routs.py
The routs.py file contains the main code with comments, which includes decorators, a parser, and an HTML-report entry.
The file index.html (in the 'templates' folder) is the structure for the HTML-report.

To start the programm you need to be in directory Web-Service-for-Architecture-IS and write command in terminal (OS X, Linux) 'export FLASK_APP=run.py flask run' or (Windows) 'set' instead 'export'
Copy URL-address and open it in browser to get report
