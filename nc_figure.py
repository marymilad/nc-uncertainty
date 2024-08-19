from nakamoto import compute_nakamoto_coefficient
from nakamoto_range import find_nc_range
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np
import datetime


def across_coins(dfs, labels):
    color = iter(cm.rainbow(np.linspace(0, 1, len(dfs))))
    fig, ax = plt.subplots()
    for i in range(len(dfs)):
        color2 = next(color)
        nc = compute_nakamoto_coefficient(dfs[i])
        thing = find_nc_range(dfs[i], nc)
        ax.plot(thing.index, thing['lower'],label=labels[i], color = color2)
        ax.plot(thing.index, thing['upper'], color = color2)
        plt.fill_between(thing.index, thing["upper"], thing["lower"], color = "pink")
    plt.xlim(datetime.date(2018, 9, 1), datetime.date(2018, 9, 8))
    plt.ylim(2, 6)
    plt.ylabel('Nakamoto Coefficient')
    plt.title('Range of the Nakamoto Coefficient Across Coins')
    plt.xticks(rotation=45)
    plt.legend()
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.tight_layout()
    plt.savefig('thing', bbox_inches='tight')
    plt.show()

def compare_gran(df):
    alphas = [0.001, 0.01, 0.025, 0.05, 0.1]
    colors = ["wheat", "pink", "lightsteelblue", "mediumseagreen", "darkslateblue" ]
    fig, ax = plt.subplots()
    for i in range(len(alphas)):
        alpha = alphas[i]
        color2 = colors[i]
        nc = compute_nakamoto_coefficient(df)
        thing = find_nc_range(df, nc, alpha)
        ax.plot(thing.index, thing['lower'],label=str(alpha), color = color2)
        ax.plot(thing.index, thing['upper'], color = color2)
        plt.fill_between(thing.index, thing["upper"], thing["lower"], color = color2)
    plt.xlim(datetime.date(2019, 1, 1), datetime.date(2019, 1, 14))
    plt.xticks(rotation=45)
    plt.ylim(1,7)
    plt.title("NC of Bitcoin with Varying Levels of Alpha")
    plt.ylabel('Nakamoto Coefficient')
    plt.legend()
    plt.gcf().subplots_adjust(bottom=0.20)
    plt.savefig('supper', bbox_inches='tight')
    plt.show()


