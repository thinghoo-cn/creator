from setuptools import setup

requires = [
    'click'
]

dev_requires = [
    'invoke',
    'pytest',
    'pytest-sugar',
]

setup(
    name='creator',
    install_requires=requires,
    extra_requires={
        'dev': dev_requires,
    },
    entry_points={
        'console_scripts': ['hellopy=creator.hello:main'],
        'creator.main': [
            'main = creator.__main__'
        ]
    },

    # pytest config
    setup_requires=['pytest-runner'],
    test_requires=['pytest'],
)