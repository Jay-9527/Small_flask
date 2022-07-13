import os

from flask_script import Manager, Shell
from flask_migrate import Migrate
from __init__ import create_app, db

app = create_app(os.environ.get('flask_config') or 'defaults')
manager = Manager(app)
migrate = Migrate(app, db)


# @app.make_shell_context
def make_shell_context():
    return dict(db=db, app=app)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", Migrate)

if __name__ == "__main__":
    manager.run()
