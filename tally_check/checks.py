from tally_check.tools import run_tally
import math


# Check sum of individual lengths is equal to total len
# Math.isclose() checks eqaulity to within 1e-9
def check_tot_len(df, jt_len="jt_len", tot_len="tot_len"):
    return math.isclose(df[jt_len].sum(), df[tot_len].iloc[-1], abs_tol=1e-3)


# Check top of each joint is correct
# TODO - add comment
def check_top_jt(df, btm_dep, tot_len="tot_len", jt_top="jt_top"):
    return (btm_dep - df[tot_len]).equals(df[jt_top])


# Check each row has correct total len
# TODO - add comment
def check_tot_len_rows(df, jt_len="jt_len", tot_len="tot_len"):
    return (df[jt_len].cumsum()).equals(df[tot_len])