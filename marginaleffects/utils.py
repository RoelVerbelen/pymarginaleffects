import polars as pl
import numpy as np

def sort_columns(df, by = None):
    cols = ["rowid", "group", "term", "contrast", "estimate", "std_error", "statistic", "p_value", "s_value", "conf_low", "conf_high"] + df.columns
    if by is not None:
        if isinstance(by, list):
            cols = by + cols
        else:
            cols = [by] + cols
    cols = [x for x in cols if x in df.columns]
    cols_unique = []
    for item in cols:
        if item not in cols_unique:
            cols_unique.append(item)
    out = df.select(cols_unique)
    return out


def pad_array(arr, n):
    if len(arr) == 1:
        out = np.repeat(arr[0], n)
    elif len(arr) < n:
        out = np.concatenate([np.repeat(arr[0], n - len(arr)), arr])
    else:
        out = arr
    return pl.Series(out)

def get_pad(df, colname, uniqs):
    if uniqs is None:
        return(None)
    first = [df.slice(0, 1)] * len(uniqs)
    first = pl.concat(first)
    first = first.with_columns(uniqs.alias(colname))
    return first
