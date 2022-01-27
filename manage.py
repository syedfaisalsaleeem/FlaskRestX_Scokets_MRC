import os
from dotenv import load_dotenv

load_dotenv()

from main import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app_env = os.environ.get("APP_SETTINGS")

migrate = Migrate(create_app, db)

manager = Manager(create_app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
