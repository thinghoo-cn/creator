from setuptools import setup

requires = [
]

dev_requires = [
]

setup(
    name='creator',
    install_requires=requires,
    extra_requires={
        'dev': dev_requires,
    },
    entry_points={
        'creator.main': [
            'main = creator.__main__'
        ]
    }
)