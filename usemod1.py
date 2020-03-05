#!/usr/bin/env python
import os

print(os.getenv("PYTHONPATH"))

from hughes.tech import hugheslib

hugheslib.spam()
hugheslib.ham()
hugheslib._toast()  # NAUGHTY NAUGHTY


