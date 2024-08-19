import pandas as pd
from granularities import granularity


def compute_nakamoto_coefficient(df):
    """
    Calculates the Nakamoto coefficient of a distribution of blocks to entities
    :param df: dataframe of blocks mined, dates in rows & distinct entities in columns
    :returns: dataframe of nakamoto coefficient, dates in rows & columns of nc and proportion owned by top #
    """
    nclist = []
    powers = []
    for i in range(len(df.index)):
        total_blocks = df.iloc[i].sum(axis=0)
        nc, power_percentage = 0, 0
        if total_blocks == 0:
            nc, power_percentage = 0,0
        else:
            while power_percentage <= 0.50:
                for blocks in (df.iloc[i].sort_values(axis=0, ascending=False)):
                    nc += 1
                    power_percentage += (blocks/total_blocks)
                    if power_percentage > 0.50:
                        break
        nclist.append(nc)
        powers.append(power_percentage)
    result = pd.DataFrame( {'nc': nclist}, index=df.index)
    return result
