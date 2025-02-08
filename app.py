import os
from flask import Flask
from controller import controller

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(controller)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)
