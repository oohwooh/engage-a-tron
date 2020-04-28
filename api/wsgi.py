import os, sys, inspect

# Long story short, imports bad.
# This is needed to allow the cogs to import database, as python doesn't check in the parent directory otherwise.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from api.main_api import app

if __name__ == '__main__':
    app.run()
