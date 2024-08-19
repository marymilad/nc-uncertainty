import pandas as pd
from scipy.stats import binomtest

def binom_p(coin):
    p_values = {}
    cols = ['nc', 'p-value', 'confidence interval']
    columncountplus = []
    columncountminus = []
    for i, coeff in nc.iterrows():
        num = coin[str(i)].sum()
        if num == 0:
        else:
        successes = coin[str(i)].nlargest(coeff.values[0]).sum()
        p = binomtest(k=successes, n=num, p=0.5, alternative='greater')
        p_values[str(i)] = [coeff.values[0], p.pvalue, p.proportion_ci(confidence_level=0.95)]
        thing = p.pvalue
        ncplus = 0
        while thing >= 0.05:
            ncplus += 1
            successes = coin[str(i)].nlargest(coeff.values[0]+ncplus).sum()
            pplus = binomtest(k=successes, n=num, p=0.5, alternative='greater')
            p_values[str(i)].extend([coeff.values[0]+ncplus, pplus.pvalue, pplus.proportion_ci(confidence_level=0.95)])
            thing = pplus.pvalue
            columncountplus.append(ncplus)
    for x in range(1, max(columncountplus) + 1):
        cols.extend([f'ncplus {x}', f'pplus {x}', f'pplus {x} confidence interval'])
    for i, coeff in nc.iterrows():
        num = coin[str(i)].sum()
        successes = coin[str(i)].nlargest(coeff.values[0]).sum()
        p = binomtest(k=successes, n=num, p=0.5, alternative='greater')
        thing2 = p.pvalue
        ncminus = 0
        while thing2 <= 0.05 and coeff.values[0]-ncminus > 0:
            ncminus += 1
            successes = coin[str(i)].nlargest(coeff.values[0]-ncplus).sum()
            pminus = binomtest(k=successes, n=num, p=0.5, alternative='greater')
            p_values[str(i)].extend((coeff.values[0]-ncplus, pminus.pvalue, pminus.proportion_ci(confidence_level=0.95)))
            thing2 = pminus.pvalue
            columncountminus.append(ncminus)
    for x in range(1, max(columncountminus) + 1):
        cols.extend([f'ncminus {x}', f'pminus {x}', f'pminus {x} confidence interval'])
    pdf = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in p_values.items()])).T
    pdf.columns = cols
    return(pdf)