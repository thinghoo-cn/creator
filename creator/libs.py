import os
import pathlib


def create_package(package_name: str) -> pathlib.Path:
    path = pathlib.Path(package_name)
    if path.exists():
        raise Exception('not work')

    path = path.absolute()
    os.mkdir(path)
    initpy = path / '__init__.py'
    initpy.touch()

    return path
    