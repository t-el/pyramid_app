# pyramid_app

pyramid_app_v1
==============

Getting Started
---------------

- Change directory into your newly created project if not already there. Your
  current directory should be the same as this README.txt file and setup.py.

    `cd pyramid_app_v1`

- Create a Python virtual environment, if not already created.

    `python3 -m venv env`

- Upgrade packaging tools, if necessary.

    `env/bin/pip install --upgrade pip setuptools`

- Install the project in editable mode with its testing requirements.

    `env/bin/pip install -e .`

- Run your project.

    `env/bin/pserve development.ini`

env file ,required section
---------------

    env file must be in root project (the root folder)
    NOTE : you have to name variable like this
    SUPABASE_URL=https://hsuiydedkodizodzitudz.supabase.co 
    SUPABASE_KEY=eyolkoikcdlpdpopodicYmFzZSIsInJlZiI6ImRveWdoc3B1bHNrZ2RhdGZ1bnpsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2NjYzNTgxMSwiZXhwIjoxOTgyMjExODExfQ.XkjQuYwARmv51JmnW6pB8eWQVBikPHAX2nOsU1jQ_8U
    
    
Outh authentication (Google,Github,Discord) , required section
---------------
in supabase go to authentication > Settings > Auth Providers 

Enable Github,Google,Discord

Github  : https://supabase.com/docs/guides/auth/auth-github
Google  : https://supabase.com/docs/guides/auth/auth-google
Discord : https://supabase.com/docs/guides/auth/auth-discord
