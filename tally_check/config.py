FILENAME = "DC228 - 9.875in Liner Tally - Rev0.xlsx"

# Row number for header (e.g. column names)
HEADER_ROW = 40

# Row number for shoe
SHOE_ROW = 41

# Row number for hanger
HANGER_ROW = 161

# Row number for cement head
CMT_HEAD_ROW = 316

# Excel columns for each variable
COLS = {
    # Joint length - threads off
    "jt_len": "E",
    # Total (cumulative) length
    "tot_len": "F",
    # Top of joint
    "jt_top": "H",
    # Whether joint is run or not (Y/N)
    "jt_in_out": "G",
}

# Open hole TD
OH_TD = 22788

# Top of rathole. If hole section not underreamed, use None.
RATHOLE = None

# Planned casing set depth
CSG_SET_DEP = 22768

# Depth of previous shoe
PREV_SHOE = 19052
