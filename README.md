# **DeadBox**

## *Third year software development Python-Flask SPA*

## Virtual Clipboard to store your links, texts. For easier multiplatform sharing.


## Instalation guide:
Download and install Python 3.5.2 or later:

> https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe

Download and install PostreSQL database:

> https://www.postgresql.org/download/

Take note of password you used. You will need to change it in app.py file

> app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresql:**password**@localhost/postgres'

Clone repo. In Git bash: 

> git clone https://github.com/MartinRep/deadBox.git

Install virtualenv via pip:

> $ pip install virtualenv

Create a virtual environment for a project:

> $ cd deadbox
> $ virtualenv venv

To begin using the virtual environment, it needs to be activated:

> $  /venv/Scripts/activate

Install requirements from root directory of an app:

> $ pip install -r requirements.txt

And finally run the app:

> python app.py

The app should run on local host port 5000:

> http://127.0.0.1:5000/

You need to register to start using DeadBox. Simply enter your Email and confirm password.
You will receive welcoming email. I am using Flask security project for logging in. You can config content
of confirmation mail. Also I didn't change css for login and registration templates, which can be changed to fit more with
current bootstrap template used.
Now you can add, delete, copy your clipboads across platforms.

CLipboard list is unique for each user.

*This is just a simple single page application to demonstate flask ability to make comunication easier betwen fron and back end.*



