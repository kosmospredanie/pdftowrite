__version__ = '2021.03.22'

import sys
from pdftowrite.pdftowrite import run

def main():
    run(sys.argv[1:])
