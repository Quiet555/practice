msg = """
cats are lovely and lazy animals.
Cats are lovely and lazy animals.
CAts are lovely and lazy animals.
Cats are lovely and lazy animals.
cAts are lovely and lazy animals.
cATs are lovely and lazy animals.
caTs are lovely and lazy animals.
CaTs are lovely and lazy animals."""

import re

items = re.sub("[Cc][Aa][Tt]s",'CAT', msg)
print(items)
