# using modules from regular directory (extra)

from sys import path
path.append('..\\package_poc')
 
import extra.iota
print(extra.iota.funI())

import extra.good.best.sigma 
print(extra.good.best.sigma.funS())

print("From now, I invoke functions from modules from package in a zip file.")

# using modules from extra.zip file

from sys import path
path.append('..\\package_poc\extra.zip')
 
import extra.bad.omega as OMEGA
print(OMEGA.funO())

import extra.good.best.tau as TAU
print(TAU.funT())
