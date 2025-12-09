from setuptools import setup, find_packages

requires = [
    'pyramid',
    'sqlalchemy',
    'alembic',
    'waitress',
]

setup(
    name='matakuliah_app',
    version='1.0',
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = matakuliah_app:main',
        ],
    },
)