#!/usr/bin/env python3

import sebastian

if __name__ == '__main__':
    try:
        sebastian.run()
    except KeyboardInterrupt:
        print('Stopping...')
