from flask import Flask
from extensions import db, migrate
from config import Config
import front


app = Flask(__name__)

# load config
app.config.from_object(Config)


# init extensions
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(front.front_bp, url_prefix='/')

# load models
import models


if __name__ == '__main__':
    app.run()
