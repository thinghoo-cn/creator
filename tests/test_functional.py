import os
import shutil
from unittest import TestCase

from creator import app


class FunctionalTest(TestCase):

    def tearDown(self):
        folder = 'tmp'
        if os.path.exists(folder):
            shutil.rmtree(folder)

        return super().tearDown()

    def test_create_package(self):
        package_name = 'tmp'
        
        res = app.create_package(package_name=package_name)
        self.assertTrue(os.path.exists(res))
        self.assertTrue(os.path.exists(f'{res}/__init__.py'))
