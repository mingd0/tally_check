import pandas as pd
import config
from tally_check.tools import coldict2num, rename_cols
from tally_check.checks import check_tot_len

# from condition import ConditionCheck



def main():
    # Read in excel tally and load to DataFrame
    df = pd.read_excel(config.FILENAME, header=(config.HEADER_ROW - 1))

    # DATA CLEANING

    # Rename required columns based on excel column letters given in config
    # file
    df = rename_cols(df, coldict2num(config.COLS))
    # Filter dataframe columns for the ones given in config file
    df = df.loc[:, list(config.COLS.keys())]
    # Clean joint in/out column by making all lowercase
    df["jt_in_out"] = df["jt_in_out"].str.casefold()

    # DATA CHECKS
    tot_len_check = check_tot_len(df)

    # GENERATE REPORT

    print()


if __name__ == "__main__":
    main()
