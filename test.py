import os
import sys

# get env variables SECRET
SECRET = os.environ.get('SECRET')


def test():
    assert False, SECRET