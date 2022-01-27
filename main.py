import os
from dotenv import load_dotenv

load_dotenv()

from flask_migrate import Migrate
from app import create_app, db,sk
create_app = create_app(os.environ.get("DATABASE_URL"))
create_app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
migrate = Migrate(create_app, db)



if __name__ == "__main__":
    sk.run(create_app, debug=True)
