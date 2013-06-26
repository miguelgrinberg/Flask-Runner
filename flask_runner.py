import argparse

class Runner():
    def __init__(self, app):
        self.app = app

    def parse_args(self, args = None):
        parser = argparse.ArgumentParser()
        parser.add_argument('-H', '--host', metavar = 'HOST', type = str,
            default = '127.0.0.1',
            help = 'hostname or IP address to listen on (default is "127.0.0.1")')
        parser.add_argument('-P', '--port', metavar = 'PORT', type = int,
            default = 5000,
            help = 'port of the web server (default is 5000)')
        parser.add_argument('-d', '--debug', dest = 'debug', action = 'store_true',
            help = 'enable the debugger')
        parser.add_argument('--noeval', dest = 'use_evalex', action = 'store_false',
            help = 'disable the exception evaluation feature in the debugger')
        parser.add_argument('-r', '--reload', dest = 'use_reloader', action = 'store_true',
            help = 'reload the Python process when any modules are changed')
        parser.add_argument('--extra', metavar = 'FILE', type = str, dest = 'extra_files', action = 'append', 
            help = 'additional file for the reloader to watch for changes')
        return parser.parse_args(args).__dict__

    def run(self, **kwargs):
        args = self.parse_args()
        args.update(kwargs)
        self.app.run(**args)

