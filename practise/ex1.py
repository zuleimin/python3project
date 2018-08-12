# CircleArea

#!/usr/bin/env python3
import math

while True:
    r = input("Enter the r: ")
    if str(r) == 'q':
        break
    else:
        r=float(r)
        print("{:.10f}".format(math.pi*r**2))