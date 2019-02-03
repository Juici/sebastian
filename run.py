#!/usr/bin/env python3

import sebastian
import sys

if __name__ == '__main__':
    try:
        sebastian.run()
    except KeyboardInterrupt:
        print('')
        sys.exit(0)
