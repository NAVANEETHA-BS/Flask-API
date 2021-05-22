from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
#from .start import app
from .customer.models import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()