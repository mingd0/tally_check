from tally_check.tools import run_tally
import math


# Check sum of individual lengths is equal to total len
# Math.isclose() checks eqaulity to within 1e-9
def check_tot_len(df, jt_len="jt_len", total_len="tot_len"):
    # df_run = run_tally(df)
    return math.isclose(df[jt_len].sum(), df[total_len].iloc[-1])


# Check top of each joint is correct

# Check each row has correct total len
