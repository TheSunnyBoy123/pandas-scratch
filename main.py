import time
import argparse
import os
import sys
import logging
import json
from output import *
from arrayClass import *


class Series():
    def __init__(self):
        self.values = []
    
    def __str__(self) -> str:
        return str(self.values)

class DataFrame():
    def __init__(self):
        pass


