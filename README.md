# Pur'N'Kleen

Version: 1.2.1 - 23 September 2018.

## Description

Django site for [Pur'N'Kleen](https://purnkleen.com).  

## Project setup

1. Install [Homebrew](https://brew.sh/).
2. This project uses Python 3. Make sure you have installed Python 3. One way to install it is: `brew install python3`. 
3. You can verify which version of Python is installed by: `python3 --version`, and run it with `python3`.
4. Create a new Python virtual environment, for example `python3.7 -m venv purnkleen`.
5. To activate the new virtual environment, `source purnkleen/bin/activate`.
6. And you can start Python by typing: `python`.
7. Next, install `virtualenvwrapper` by first running `pip install virtualenv --user` and then 
`pip install virtualenvwrapper --user`.
8. Create a folder that will contain all your virtual environments: `mkdir ~/.virtualenvs`.
9. Open your .bashrc file and add: `export WORKON_HOME=~/.virtualenvs` and 
`source /Users/rommel/Library/Python/2.7/bin/virtualenvwrapper.sh`
10. You can activate these changes by typing `source .bashrc`.
11. We are ready to create a new virtual environment using Python 3 with 
`mkvirtualenv --python=/usr/local/bin/python3 purnkleen`.
12. This creates a folder `purnkleen` inside the environments folder ~/.virtualenvs.The new environment will be active 
after running the previous command. 
13. To deactivate it, just type `deactivate`.
14. And to activate it again: `workon purnkleen`.
15. While being in your python3 virtual environment, if you type `python` you activate python 3! Moreover, you can use 
`pip` to call `pip3` and install python3 packages. For example, you can install Django 1.7 using 
`pip install Django==1.7`. 

Now, you’re ready to code!

## PostgreSQL Setup

1. Download from here: https://www.postgresql.org/download/macosx/
2. Make sure the port matches what is in your `config/settings_local.ini` folder.
3. Click initialize.
4. Install pgAdmin: https://www.pgadmin.org/
5. Create a new server using the settings in the `config/settings_local.ini`.
6. Set up the database using the default `postgres` user.
7. Create the `pnk_admin` user with full access.
8. Create `purnkleen` database.
9. `python manage.py migrate`

That's it. Run the server! (http://127.0.0.1:52046/browser/#)

## Contributing

If you wish to contribute to this repo, please read the [Contributing document](.github/CONTRIBUTING.md).

## Support

If you need help with this project, please read the [Support document](.github/SUPPORT.md).

## License

[MIT License](LICENSE)

