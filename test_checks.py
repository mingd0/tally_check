from tally_check.checks import check_tot_len
import pandas as pd


def test_check_tot_len():
    # Equal lengths
    data = {"jt_len": [10, 10, 10], "tot_len": [10, 20, 30]}
    df = pd.DataFrame(data)

    result = check_tot_len(df)
    assert result is True
