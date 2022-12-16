#!/usr/bin/env python3

# Blinks every LED to the same color
#
# Usage:
# python blink.py [color hex string] [blink interval in seconds]

import sys
import time

from backend.ceiling import Ceiling
from backend.util import hex_to_rgb

if len(sys.argv) != 2:
    print("Usage: python blink.py [color hex string] [blink interval in seconds]")

color_input = sys.argv[1]
interval = float(sys.argv[2])

on_rgb = hex_to_rgb(color_input)
off_rgb = [0] * len(on_rgb)

ceil = Ceiling()
ceil.clear()

on = True

while True:
    ceil.fill(on_rgb if on else off_rgb)
    ceil.show()
    on = not on
    time.sleep(interval)