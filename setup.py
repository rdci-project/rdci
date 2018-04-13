from setuptools import setup, find_packages
from hfs2018 import __version__

setup(
    name='hfs2018',
    version=__version__,
    description="Hack the planet.",
    long_description="Hack the planet in a more verbose way...",
    keywords=[],
    author='None',
    author_email='None',
    url="https://gitlab.com/hackingforsweden/hfs2018",
    install_requires=["click", "requests"],
    packages=find_packages(exclude=["tests*"]),
    test_suite="tests",
    license='MIT',
    entry_points={
        'console_scripts': ['hfs2018 = hfs2018.cli:main']
    },
)
