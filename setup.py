from setuptools import setup

setup(
    name='yatzy',
    version='0.1.0',
    description='Yatzy game',
    author='Marcus Veibäck',
    author_email='sirmar@gmail.com',
    url='https://github.com/sirmar/yatzy',
    packages=['yatzy'],
    install_requires=[],
    extras_require={
        'test': [
            'coverage',
            'black',
            'mypy',
            'pylint'
        ],
    },
    entry_points={
        'console_scripts': [
            'yatzy=yatzy.main:yatzy',
            'maxi_yatzy=yatzy.main:maxi_yatzy',
        ]
    },
)
