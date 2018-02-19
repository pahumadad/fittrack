from flask import Flask
from .controllers.utilities import utilities

app = Flask("fittracker")

app.register_blueprint(utilities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
