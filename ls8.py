#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load('C:\\Users\\Zero\\Desktop\\Sprint-Challenge--Computer-Architecture\\sctest.ls8')
cpu.run()