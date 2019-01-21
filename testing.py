import platform
import sys

def identity():
    return sys.platform()

print(identity())
