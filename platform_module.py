# functions from platform module

from platform import platform, machine, processor, system, version

print(platform(aliased = False, terse = False))

print(machine())
 
print(processor())

print(system())

print(version())