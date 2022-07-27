## constructing a dataframe
import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3, 4, 5],
                          'b': [3, 4, 5, 6, 7]})
df

## imports
import math
math.sqrt(36)

#importing a function
from math import sqrt
sqrt(36)

# show all functions in math model
print(dir(math))

## Data types
type(5)
type(5.0)
type('five')
type(False)

## check if an object is of a given type
isinstance(5.0, int)
isinstance(5.0, (int, float))
isinstance('Five', str)
isinstance('Five', int)
isinstance(False, bool)

## Convert an object to a given type
str(5.5)
