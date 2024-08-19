from nakamoto import compute_nakamoto_coefficient
from scipy.stats import binomtest
import pandas as pd

def find_nc_range(df, nc, alpha = 0.05):
    '''

    :param df: dataframe of blocks mined, dates in rows & distinct entities in columns
    :param nc: dataframe of nakamoto coefficient, dates in rows & columns of nc and proportion owned by top #
    :return: result: dataframe of possible nakamoto coefficient values, dates in rows and columns of lower/upper nakamoto values
    '''
    lower = []
    upper = []
    for i in range(len(df.index)):
        total_blocks, coeff = int(df.iloc[i].sum(axis=0)), nc['nc'].iloc[i]
        coeffp, coeffq = coeff, coeff
        if total_blocks != 0:
            thing = df.iloc[i].sort_values(axis=0, ascending=False)
            successes = int(thing.nlargest(coeff).sum())
            p = binomtest(k=successes, n=total_blocks, p=0.5, alternative='greater').pvalue
            q = binomtest(k=successes, n=total_blocks, p=0.5, alternative='less').pvalue
            if p > alpha:
                while p > alpha: #upper
                    coeffp += 1
                    thing = df.iloc[i].sort_values(axis=0, ascending=False)
                    successes = int(thing.nlargest(coeffp).sum())
                    p = binomtest(k=successes, n=total_blocks, p=0.5, alternative='greater').pvalue
                coeffp -= 1
            if q > alpha:
                while q > alpha: #lower
                    coeffq -= 1
                    thing = df.iloc[i].sort_values(axis=0, ascending=False)
                    successes = int(thing.nlargest(coeffq).sum())
                    q = binomtest(k=successes, n=total_blocks, p=0.5, alternative='less').pvalue
                coeffq += 1
        lower.append(coeffq)
        upper.append(coeffp)
    result = pd.DataFrame({'lower': lower, 'upper': upper}, index=df.index)
    return(result)




