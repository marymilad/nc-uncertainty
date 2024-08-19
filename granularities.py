import pandas as pd

def granularity(df, num):
    '''
    :param df: dataframe of blocks mined, dates in rows & distinct entities in columns
    :param num: granularities of days to be combined
    :return:dataframe of combined blocks mined for granularity, dates in rows & distinct entities in columns
    '''
    daily = df.T.to_dict('list')
    result = []
    lister = []
    dates = []
    for k, v in sorted(daily.items()):
        lister.append(v)
        dates.append(k)
    i = 0
    indicies = dates
    step = num // 2
    while i <= len(lister)-1:
        thing = [sum(x) for x in zip(*lister[i-step:i+(num-step):])]
        result.append(thing)
        i += 1
    new = pd.DataFrame(data=result, index=indicies, columns=df.columns)
    return(new)

