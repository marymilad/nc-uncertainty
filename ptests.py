import pandas as pd
from scipy.stats import binomtest


def binom_p(df, nc, alpha = 0.05):
    '''

    :param df: dataframe of blocks mined, dates in rows & distinct entities in columns
    :param nc: dataframe of nakamoto coefficient, dates in rows & column is nc
    :return: percentage of hyptohesis tests passed
    '''

    passes = 0
    total = 0
    for i in range(len(df.index)):
        num = int(df.iloc[i].sum(axis=0))
        if num != 0:
            coeff = nc['nc'].iloc[i]
            sorted_blocks = df.iloc[i].sort_values(axis=0, ascending=False)
            successes = int(sorted_blocks.nlargest(coeff).sum())
            p = binomtest(k=successes, n=num, p=0.5, alternative='greater')
            total += 1
            if p.pvalue < alpha:
                passes += 1
    result = (passes/total)*100
    return(result)
    #print(f'{result}% of p-tests passed')

