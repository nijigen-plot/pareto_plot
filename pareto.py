from typing import TypeVar
PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')
import matplotlib.pyplot as plt
import seaborn as sns

def plot(df : PandasDataFrame, bar_x : str, bar_y : str, title : str, figsize = (10, 6)):
    df['cumsum'] = df[bar_y].cumsum()
    df['accumulation'] = df['cumsum'] / df[bar_y].sum()
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.bar(df[bar_x], df[bar_y], color='darkorange')
    ax2 = ax.twinx()
    ax2.plot(df[bar_x], df['accumulation'], color='royalblue')
    ax2.scatter(df[bar_x], df['accumulation'], color='royalblue')
    sns.despine(ax=ax2, left=True, right=False)
    plt.title(title)
    plt.show()