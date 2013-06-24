import unittest
from flask import Flask
from flask.ext.runner import Runner

class RunnerTestCase(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        self.runner = Runner(app)
        
    def test_defaults(self):
        args = self.runner.parse_args([])
        self.assertTrue(args['host'] == '127.0.0.1')
        self.assertTrue(args['port'] == 5000)
        self.assertTrue(args['use_debugger'] == False)
        self.assertTrue(args['use_evalex'] == True)
        self.assertTrue(args['use_reloader'] == False)
        self.assertTrue(args['extra_files'] == None)
        
    def test_host_port(self):
        args = self.runner.parse_args('--host 0.0.0.0 --port 8080'.split())
        self.assertTrue(args['host'] == '0.0.0.0')
        self.assertTrue(args['port'] == 8080)

    def test_debugger(self):
        args = self.runner.parse_args('--debug'.split())
        self.assertTrue(args['use_debugger'] == True)
        self.assertTrue(args['use_evalex'] == True)

    def test_evalex(self):
        args = self.runner.parse_args('--debug --noeval'.split())
        self.assertTrue(args['use_debugger'] == True)
        self.assertTrue(args['use_evalex'] == False)

    def test_reloader(self):
        args = self.runner.parse_args('--reload'.split())
        self.assertTrue(args['use_reloader'] == True)

    def test_reloader_extra(self):
        args = self.runner.parse_args('--reload --extra some_file.txt'.split())
        self.assertTrue(args['use_reloader'] == True)
        self.assertTrue(args['extra_files'] == ['some_file.txt'])

    def test_reloader_extra2(self):
        args = self.runner.parse_args('--reload --extra some_file.txt --extra another_file.txt'.split())
        self.assertTrue(args['use_reloader'] == True)
        self.assertTrue(args['extra_files'] == ['some_file.txt', 'another_file.txt'])

def suite():
    return unittest.makeSuite(RunnerTestCase)

if __name__ == '__main__':
    unittest.main(defaultTest = "suite")
