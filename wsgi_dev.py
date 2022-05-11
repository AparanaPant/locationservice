from core.constants.enviroment_constants import Environment
from run import create_app

app = create_app(Environment.development)

if __name__ == '__main__':
    app.run('127.0.0.9', port=4455)
