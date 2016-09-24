import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "version.txt")) as f:
    version = f.read().rstrip()

setup(
    name="beetmoverscript",
    version=version,
    description="TaskCluster Beetmover Script",
    author="Mozilla Release Engineering",
    author_email="release+python@mozilla.com",
    url="https://github.com/lundjordan/beetmoverscript",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "beetmoverscript = beetmoverscript.script:main",
        ],
    },
    license="MPL2",
    install_requires=[
        "arrow",
        "scriptworker",
        "taskcluster",
        "boto",
        "PyYAML",
        "Jinja2",
    ],
)