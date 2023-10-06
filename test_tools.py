from tally_check.tools import col2num, row2dfindex, coldict2num, rename_cols
import pandas as pd


def test_col2num():
    # Given
    col1 = "B"
    col2 = "AE"

    # When
    num1 = col2num(col1)
    num2 = col2num(col2)

    # Then
    assert num1 == 1
    assert num2 == 30


def test_row2dfindex():
    # Given
    header_row = 3
    target_row = 4

    # When
    index = row2dfindex(target_row, header_row)

    # Then
    assert index == 0


def test_coldict2num():
    # Given
    cols = {"jt_len": "E", "tot_len": "F"}

    # When
    df_cols = coldict2num(cols)

    # Then
    assert df_cols == {"jt_len": 4, "tot_len": 5}


def test_rename_cols():
    # Given
    df_cols = {"jt_len": 0, "tot_len": 1}
    df = pd.DataFrame(columns=["Joint Length Threads Off", "Total Length"])

    # When
    new_df = rename_cols(df, df_cols)

    # Then
    assert list(new_df.columns) == ["jt_len", "tot_len"]
