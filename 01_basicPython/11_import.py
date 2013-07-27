## import

# import existing modules, functions, classes in to a script

# Importing modules 
import robofab
print robofab

# Importing all objects from a module
from robofab import *
print version            # a number 

# Importing a specific sub module
from robofab.pens.filterPen import halftoneGlyph
print halftoneGlyph      # a function