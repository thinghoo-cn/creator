import os
from unittest import TestCase

from creator import app


class FunctionalTest(TestCase):

    def test_create_package(self):
        package_name = ''
        
        res = app.create_package(package_name=package_name)
        self.assertTrue(os.path.exists(res))
        self.assertTrue(os.path.exists(f'{res}/__init__.py'))
