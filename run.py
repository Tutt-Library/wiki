__author__ = "Jeremy Nelson"
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from app import app

app.config['DEBUG'] = True

application = DispatcherMiddleware(
    app,
    {"/wiki": app}
)

if __name__ == '__main__':
    run_simple('0.0.0.0', 8085, application, use_reloader=True, use_debugger=True)

