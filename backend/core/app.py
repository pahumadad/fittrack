from flask import Flask
from .controllers.utilities import utilities
from ..config.config import Config

app = Flask(Config.APP_NAME)
app.config.from_object(Config)

app.register_blueprint(utilities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
