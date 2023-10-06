import math
import pandas as pd
import numpy as np


# Ref top of jt for row
PTS_OF_INTEREST = {
    "btm_chrome": {"row": 54, "reqs": "todo"},
    "top_chrome": {"row": 67, "reqs": "todo"},
}

outputs = {
    "total_len_total": False,
    "total_len_rows": False,
    "top_jt_rows": False,
    "count_is_consecutive": False,
    "shoe_from_td": False,
    "shoe_from_rathole": False,
    "hgr_from_prev_shoe": False,
}


# Check each row in Total Length column is correct
def check_cum_len_rows(df, jt_len="jt_len", total_len="total_len"):
    df = df.loc[:, [jt_len, total_len]]
    df["check"] = (df[total_len] - df[jt_len]).shift(-1)
    df = df.dropna()
    return (df["check"].round(4) == df[total_len].round(4)).all()


def check_jt_top_rows(df, jt_top="jt_top", total_len="total_len"):
    df = df.loc[:, [jt_top, total_len]]
    df["check"] = CSG_SET_DEP - df[total_len]
    return (df["check"].round(4) == df[jt_top].round(4)).all()


def check_depth_offset(df, excel_row, depth):
    df_index = convert_excel_row_to_df_index(excel_row, HEADER_ROW)
    return (depth - df.loc[df_index, "jt_top"] + df.loc[df_index, "jt_len"]).round(2)


def display_outputs(outputs):
    print(
        f"""
          Sum of lengths is equal to total length:\t{outputs['total_len_total']}
          Total length formulas OK:\t{outputs['total_len_rows']}
          Top of joint formulas OK:\t{outputs['top_jt_rows']}
          Shoe distance from TD:\t{outputs['shoe_from_td']}
          Shoe distance from rathole:\t{outputs['shoe_from_rathole']}
          Hanger distance from previous shoe:\t{outputs['hgr_from_prev_shoe']}
          """
    )


def main():
    outputs["total_len_total"] = check_tot_len_tot(df_run)
    outputs["total_len_rows"] = check_tot_len(df_run)
    outputs["top_jt_rows"] = check_jt_top(df_run)
    outputs["shoe_from_td"] = check_depth_offset(df_run, SHOE_ROW, OH_TD)
    outputs["shoe_from_rathole"] = check_depth_offset(df_run, SHOE_ROW, RATHOLE)
    outputs["hgr_from_prev_shoe"] = check_depth_offset(df_run, HANGER_ROW, PREV_SHOE)

    display_outputs(outputs)


if __name__ == "__main__":
    main()
