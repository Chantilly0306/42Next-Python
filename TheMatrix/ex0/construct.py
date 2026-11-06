#!/usr/bin/env python3
import sys
import site


print("Python executable:", sys.executable)
print("Python prefix:", sys.prefix)
print("Python base prefix:", sys.base_prefix)

print("Site packages:", site.getsitepackages())
