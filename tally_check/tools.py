import string


# Converts excel column letter to 0-indexed number (e.g. col A = 0)
def col2num(col):
    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord("A")) + 1
    return num - 1


# Converts excel row number to 0-indexed DataFrame row, based on header row
# given by user (in config)
def row2dfindex(target_row, header_row):
    return target_row - header_row - 1


# Converts column dictionary (from config file) to another dictionary with
# 0-indexed numbers instead of letters
def coldict2num(coldict):
    new_coldict = {}
    for key in coldict.keys():
        new_coldict[key] = col2num(coldict[key])
    return new_coldict


# Rename columns in df according to dictionary "cols"
# Dictionary keys are new names, values are number indices (for DataFrame)
def rename_cols(df, cols):
    col_indices = list(cols.values())
    new_names = list(cols.keys())
    old_names = df.columns[col_indices]
    return df.rename(columns=dict(zip(old_names, new_names)))


# Returns "Run Tally" - only including the joints that are marked "in"
# Assumes we have already cleaned data (lowercase)
def run_tally(df):
    return df[df["jt_in_out"] == "y"]
