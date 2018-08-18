from flask_main_module import FlaskMainModule
from main_module import MainModule

if __name__ == '__main__':
    FlaskMainModule
    application = MainModule.application_provider()
    application.run()
