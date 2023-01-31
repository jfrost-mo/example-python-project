"""
Example package to demonstrate pytest and CI tooling.

This __init__.py file is needed for making this into a valid package.
"""
from .example import hello_world

def main():
    hello_world()
    return 0
