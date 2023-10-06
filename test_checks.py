from tally_check.checks import check_tot_len, check_top_jt, check_tot_len_rows
import pandas as pd


def test_check_tot_len():
    # Equal lengths
    data = {"jt_len": [10, 10, 10], "tot_len": [10, 20, 30]}
    df = pd.DataFrame(data)

    result = check_tot_len(df)
    assert result is True

    # Unequal lengths
    data = {"jt_len": [10, 10, 10], "tot_len": [10, 20, 40]}
    df = pd.DataFrame(data)

    result = check_tot_len(df)
    assert result is False

    # Tolerance - verify small difference is accepted
    data = {"jt_len": [10, 10, 10], "tot_len": [10, 20, 30.0009]}
    df = pd.DataFrame(data)

    result = check_tot_len(df)
    assert result is True

def test_check_top_jt():
    btm_dep = 100

    # Correct
    data = {"tot_len": [10, 20, 30], "jt_top": [90, 80, 70]}
    df = pd.DataFrame(data)

    result = check_top_jt(df, btm_dep)
    assert result is True

    # Incorrect
    data = {"tot_len": [10, 20, 30], "jt_top": [90, 80, 60]}
    df = pd.DataFrame(data)

    result = check_top_jt(df, btm_dep)
    assert result is False

def test_check_tot_len_rows():
    # Correct
    data = {"jt_len": [10, 10, 10], "tot_len": [10, 20, 30]}
    df = pd.DataFrame(data)

    result = check_tot_len_rows(df)
    assert result is True

    # Incorrect
    data = {"jt_len": [10, 10, 10], "tot_len": [10, 25, 30]}
    df = pd.DataFrame(data)

    result = check_tot_len_rows(df)
    assert result is False