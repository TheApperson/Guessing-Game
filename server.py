from flask_app import app
from flask_app.controllers import users
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

"""if __name__=="__main__":
    app.run(port=3308, debug=True)
    print('running')"""