import os

from core.constants.enviroment_constants import Environment
from run import create_app

app = create_app(os.environ.get('CONFIG'))

if __name__ == '__main__':
    app.run()
