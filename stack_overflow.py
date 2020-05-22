import pandas as pd

"""
Copying and pasting dataframes from stackoverflow is something
that I do a lot, so I made something that makes it easy to convert
into a pandas dataframe.
"""


def from_stack(string):
    """Returns a pd.DataFrame object from string.
    
    string (string): String version of dataframe.
    """
    import re
    from io import StringIO

    pat = r'(?<!\\n)[^\S\n]+'

    dat = re.sub(pat, ',', string)
    df = pd.read_csv(StringIO(dat))
    
    return df

