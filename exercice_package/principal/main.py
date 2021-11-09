from slevel import add
from child_folder.child import divide
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from parent_file import multiply

print(round(divide(add(5,multiply(2,3)),3), 2))
print(round((5 + 2 * 3) / 3, 2))
