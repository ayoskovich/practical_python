"""
Quickly reordering the columns of a dataframe.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'a':np.random.randint(1, 4, 5),
    'cost_two':np.random.randint(1, 4, 5),
    'b':np.random.randint(1, 4, 5),
    'test_price':np.random.randint(1, 4, 5),
    'test_thing':np.random.randint(1, 4, 5),
    'cost_one':np.random.randint(1, 4, 5)
})
