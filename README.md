Flask-Runner
============

A set of standard command line arguments for Flask applications built on top of Flask-Script.

Example code
------------

In its simplest usage, an application can create and initialize a `Runner` object as follows:

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
    usage: hello.py [-h] [-t HOST] [-p PORT] [--threaded] [--processes PROCESSES]
                    [--passthrough-errors] [-d] [-r] [--noeval] [--extra FILE]
                    [--profile] [--profile-count COUNT]
                    [--profile-percent PERCENT] [--profile-regex REGEX]
                    [--profile-dir DIR] [--lint]
    
    Runs the Flask development server i.e. app.run()
    
    optional arguments:
      -h, --help            show this help message and exit
      -t HOST, --host HOST
      -p PORT, --port PORT
      --threaded
      --processes PROCESSES
      --passthrough-errors
      -d, --no-debug
      -r, --no-reload
      --noeval              disable exception evaluation in the debugger
      --reload-extra FILE   additional file for the reloader to watch for changes
      --profile             run the profiler for each request
      --profile-count COUNT
                            restrict profiler output to the top COUNT lines
      --profile-percent PERCENT
                            restrict profiler output to the top PERCENT lines
      --profile-regex REGEX
                            filter profiler output with REGEX
      --profile-dir DIR     write profiler results one file per request in folder
                            DIR
      --lint                run the lint validation middleware
    
Resources
---------

- [Documentation](http://pythonhosted.org/Flask-Runner)
- [pypi](https://pypi.python.org/pypi/Flask-Runner) 

