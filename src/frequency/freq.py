import sys, os
newdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(newdir)
sys.path.append(newdir)

from models import Model
