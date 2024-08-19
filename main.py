import pandas as pd
import os
from nakamoto import compute_nakamoto_coefficient
from granularities import granularity
from ptests import binom_p
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from nakamoto_range import find_nc_range
from statistics import mean
from nc_figure import across_coins
from nc_figure import compare_gran
from statistics import mean
font = {'family' : 'serif',
         'size'   : 12,
         'serif':  'cmr10'}

matplotlib.rc('font', **font)
plt.rcParams['axes.facecolor']='whitesmoke'

bc_df = pd.read_csv('input/bitcoin_cash_daily.csv', header=0, index_col=0).T #df: blocks mined// dates in rows & distinct entities in columns#
b_df = pd.read_csv('input/bitcoin_daily.csv', header=0, index_col=0).T #df: blocks mined// dates in rows & distinct entities in columns
l_df = pd.read_csv('input/litecoin_daily.csv', header=0, index_col=0).T #df: blocks mined// dates in rows & distinct entities in columns
e_df = pd.read_csv('input/ethereum_daily.csv', header=0, index_col=0).T #df: blocks mined// dates in rows & distinct entities in columns
z_df = pd.read_csv('input/zcash_daily.csv', header=0, index_col=0).T #df: blocks mined// dates in rows & distinct entities in columns

bc_df.index = pd.to_datetime(bc_df.index)
b_df.index = pd.to_datetime(b_df.index)
l_df.index = pd.to_datetime(l_df.index)
e_df.index = pd.to_datetime(e_df.index)
z_df.index = pd.to_datetime(z_df.index)

e_df = e_df[:'2022-09-14']


'''
alphas = [0.001, 0.01, 0.025, 0.05, 0.1]


#dfs = [b_df, bc_df, l_df, e_df, z_df]
##for frame in dfs:
    #ya = frame['2019-01-01':'2019-01-14']
   # ncs = compute_nakamoto_coefficient(ya)
    #print(ncs)
    #for alpha in alphas:
        #thing = find_nc_range(ya, ncs, alpha)
        #plt.plot(ya.index, thing['upper'], color = 'pink')
        #plt.plot(ya.index, thing['lower'], color = 'blue')
        #plt.show()
        #print(alpha, find_nc_range(ya, ncs, alpha))

def export(to_export, output_folder, coin, word):
    to_export.to_csv(os.path.join(output_folder, f'{coin}_{word}.csv'))


def granularity_fix(df):
    things = [3, 7, 14, 30]
    result = []
    result.append(compute_nakamoto_coefficient(df)["nc"].tolist())
    for num in things:
        df2 = granularity(df, num)
        nc = compute_nakamoto_coefficient(df2)["nc"].tolist()
        result.append(nc)
    ender = np.array(result).T.tolist()
    output = pd.DataFrame(ender, columns = ['daily', '3-day', '7-day', '14-day', '30-day'], index=df.index)
    return output
    #export(output, 'output/bc',"bitcoin_cash_nc", num)


'''
'''
cols = ['1-day', '3-day', '7-day', '14-day', '30-day']
values = {}
things = [1, 3, 7, 14, 30]

def charter(df):
    values = []
    for num in things:
        df2 = granularity(df, num)
        nc = compute_nakamoto_coefficient(df2)
        answer = binom_p(df2, nc, 0.01)
        values.append(answer)
    return values

values['granularity'] = things
values['bitcoin_cash'] = (charter(bc_df))
values['bitcoin'] = (charter(b_df))
values['litecoin'] = (charter(l_df))
values['ethereum'] = (charter(e_df))
values['zcash'] = (charter(z_df))
df = pd.DataFrame(values)

plt.plot(df['granularity'], df['ethereum'],  label = 'Ethereum', marker = 'o', color = "mediumpurple")
plt.plot(df['granularity'], df['zcash'],  label = 'Zcash', marker = 'o', color = "yellowgreen")
plt.plot(df['granularity'], df['litecoin'], label = 'Litecoin', marker = 'o', color = "orange")
plt.plot(df['granularity'], df['bitcoin_cash'], label = 'Bitcoin Cash', marker = 'o', color = 'cadetblue')
plt.plot(df['granularity'], df['bitcoin'], label = 'Bitcoin', marker = 'o', color = "dimgrey")
plt.xticks([1, 3, 7, 14, 30], labels=["Daily", "3-day", "7-day", "14-day", "30-day"])
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], labels = ["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%","90%", "100%"])
plt.ylim(20, 100)
plt.legend(loc="lower right")
plt.grid(visible=True, color = "white", linewidth = 2)


plt.gca().margins(x=0.03)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.5# inch margin
s = maxsize/plt.gcf().dpi*20+2*m
margin = m/plt.gcf().get_size_inches()[0]

plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])


plt.savefig('gran1.eps', bbox_inches='tight', format = 'eps')
plt.show()
'''
'''
'''
'''
#print(nc.loc['2022-04-19'])
#new = z_df.T
#thing = new.loc[:, (new != 0).any(axis=0)]
#print(thing)
#print(thing.shape[1])

#update = nc['nc'].iloc[4000:4100]
#update.plot(type = scatter)
#plt.show()

df = granularity(c_df, 1)
nc = compute_nakamoto_coefficient(df)
thing = find_nc_range(df, nc, 0.01)
#nc.to_csv('nc.csv')

#check nc_range
from statsmodels.stats.proportion import proportion_confint
print("nc = ", nc["nc"].iloc[3041])
thing = b_df.iloc[3041].sort_values(axis=0, ascending=False)
successes = thing.nlargest(1).sum()
total = b_df.iloc[3041].sum(axis=0)
print(proportion_confint(successes, total, method='binom_test', alpha=0.05))
print(b_df.iloc[3041].name)
from scipy.stats import binomtest
p = binomtest(k=successes, n=total, p=0.5, alternative='less').pvalue
print(p)

'''
'''

df = b_df['2019-01-01':'2019-12-31']
nc = compute_nakamoto_coefficient(df)
thing = find_nc_range(df, nc, 0.05)
thing['upper'].plot(color = 'darkgoldenrod')
thing['lower'].plot(color = 'khaki')
plt.grid(visible=True, color = "white", linewidth = 2)
#plt.fill_between(thing.index, thing["upper"], thing["lower"], color = "yellow")
#plt.ylabel('Bitcoin')
#plt.xlabel('Date')
plt.xlim('2019-01-01', '2019-12-31')
plt.ylim(0, 5)
plt.tight_layout()
plt.legend()
plt.savefig('1 year nc range.eps', bbox_inches='tight', format = 'eps')
plt.show()
'''
'''
#df = bc_df
#compare_gran(df)
'''
'''
df1= granularity(bc_df, 7)
df2= granularity(z_df, 7)
dfs = [df1, df2]
labels = ["Zcash", "Bitcoin Cash"]
across_coins(dfs, labels)
#compare_gran(c_df)
'''
dfs = [b_df, bc_df, l_df, e_df, z_df]
for frame in dfs:
    thinger = []
    df = frame.loc[(frame != 0).any(axis=1)]
    for i in range(len(df)):
        thinger.append(df.iloc[i].sum(axis=0))
    print(mean(thinger))