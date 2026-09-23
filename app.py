from flask import Flask
from extensions import db, migrate, limiter
from config import Config
import front, admin


app = Flask(__name__)

# load config
app.config.from_object(Config)


# init extensions
db.init_app(app)
migrate.init_app(app, db)
limiter.init_app(app)


app.register_blueprint(front.front_bp, url_prefix='/')

app.register_blueprint(admin.admin_bp, url_prefix='/admin')

# load models
import models




if __name__ == '__main__':
    app.run()
