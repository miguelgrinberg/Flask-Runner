Flask-Runner
============

A set of standard command line arguments for Flask applications.

Example code
------------

Here is how the `Runner` object is initialized and used:

    from flask import Flask
    from flask.ext.runner import Runner
    app = Flask(__name__)
    runner = Runner(app)
    
    @app.route('/')
    def hello_world():
        return 'Hello World!'
    
    if __name__ == '__main__':
        runner.run()

This application now has command line options that expose many of the configuration options that can be sent as arguments to `app.run()`:

    $ python hello.py --help
    usage: hello.py [-h] [--host HOST] [--port PORT] [--debug] [--noeval]
                    [--reload] [--extra FILE]
    
    optional arguments:
      -h, --help            show this help message and exit
      -H HOST, --host HOST  hostname or IP address to listen on (default is
                            "127.0.0.1")
      -P PORT, --port PORT  port of the web server (default is 5000)
      -d, --debug           enable the debugger
      --noeval              disable the exception evaluation feature in the
                            debugger
      -r, --reload          reload the Python process when any modules are changed
      --extra FILE          additional file for the reloader to watch for changes
      -p, --profile         run the profiler for each request
      -l, --lint            run the lint validation middleware

These are some example ways in which the application can be invoked:

    $ python hello.py

Start server with all defaults (listen on http://127.0.0.1:5000, no debugger, no reloader).

    $ python hello.py --host 0.0.0.0

Listen on all public IPs.

    $ python hello.py --port 8080

Listen on port 8080.

    $ python hello.py --debug

Enable the interactive debugger.

    $ python hello.py --debug --noeval

Enable the interactive debugger, but disable evaluation of expressions on the browser.

    $ python hello.py --debug --reload

Enable the interactive debugger and the reloader.

    $ python hello.py --reload --extra config.txt --extra babel.cfg

Enable the interactive reloader and make it watch config.txt and babel.cfg in addition to the application source files.

    $ python hello.py --profiler

Run the Werkzeug profiler on each request.

    $ python hello.py --link

Run the Werkzeug lint middleware.

