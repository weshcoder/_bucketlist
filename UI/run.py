import os
from .app import APP


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    APP.run(port=port)