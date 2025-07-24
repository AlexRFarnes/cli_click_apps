# setup.py

from setuptools import setup

setup(
    name="cli_tools",
    version="1.0",
    py_modules=["greeter", "calculator", "authenticate", "fileutils", "notes"],
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            "greetings=greeter:greet",
            "add=calculator:add",
            "subtract=calculator:subtract",
            "authenticate=authenticate:auth",
            "note=fileutils:note",
            "concat=fileutils:concat",
            "notes=notes:main",
        ]
    },
)
