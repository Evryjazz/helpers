# Handy matplotlib funtions to get thousands or percentage

def plt_thousand():
    # avoid scientific thousand notation + add comma between thousands for better readability
    ax = plt.gca()
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

def plt_percentage():
    # transform ylabel decimal in percentage
    ax = plt.gca()
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))


def graph(dataframe, **kwargs):
    '''
    Function to improve matplotlib graphs readability
    
    Prerequisites:
    → import matplotlib as mpl
    → import matplotlib.pyplot as plt
    → from matplotlib.ticker import FuncFormatter
    → import matplotlib.ticker as mtick
    → from cycler import cycler
    → functions plt_thousand() + plt_percentage()
    
    Optional informations:
    - kind: ['line', 'bar', 'barh', 'area', 'pie'...]
    - rot: handle xaxis text rotation
    - figsize: per default to (15,7)
    - title: optional title for the graph
    - stacked: True to be stacked
    - thousand: rely on the custom function plt_thousand()
    - percentage: rely on the custom function plt_percentage()
    
    todo:
    - legend: yes|no, location, custom values, understand why several column referenced
    - title position (put it a bit higher)
    
    '''
    
    # kwargs mapping
    kind = kwargs.get('kind', None) # type du graphique
    rot = kwargs.get('rot', 0) # rotation des x labels (0 = horizontal)
    figsize = kwargs.get('figsize', (15,7)) # taille du graphique
    title = kwargs.get('title', None) 
    stacked = kwargs.get('stacked', False)
    thousand = kwargs.get('thousand', False) # ajout d'une virgule pour séparer les milliers
    percentage = kwargs.get('percentage', False) # multiplié par 100 et ajout du % 
    legend = kwargs.get('legend', True)
    subplots = kwargs.get('subplots', False) # Doit être à True si kind='pie'
    xlabel = kwargs.get('xlabel', None) # Pas de titre pour l'axe des abscisses par défaut
    ylabel = kwargs.get('ylabel', None) # Pas de titre pour l'axe des abscisses par défaut
    ylim = kwargs.get('ylim', None) # Démarrage de l'axe des ordonnés
    xlim = kwargs.get('xlim', None) # Démarrage de l'axe des abscisses
    legend_loc =  kwargs.get('legend.loc', 'best')
    legend = kwargs.get('legend', None)
    color =  kwargs.get('color', 'set_1') # set_1 per default
    text =  kwargs.get('text', None)
    
    # Nuancier leboncoin : https://adevinta.frontify.com/document/2#/basics/couleurs/le-nuancier
    # remap colors to 'set_1' per default
    plt.rcParams['axes.prop_cycle'] = cycler('color', ['#FF6E14', '#3C78C8', '#FFBE00', '#55B950', '#DC002D', '#7346AA', '#BEBEBE', '#A8B4C0'])
    if color == 'set_1':
        set_1  = cycler('color', ['#FF6E14', '#3C78C8', '#FFBE00', '#55B950', '#DC002D', '#7346AA', '#BEBEBE', '#A8B4C0'])
        color =  kwargs.get('color', set_1) 
    if color == 'set_2': 
        set_2 = cycler('color', ['#FFD74B', '#87CD82', '#F05069', '#234678', '#870019', '#412864', '#3C3C3C', '#647382'])
        plt.rcParams['axes.prop_cycle'] = set_2
    if color == 'set_3':
        set_3  = cycler('color', ['#9B7DC3', '#D7E1F5', '#FFF0CD', '#DCF0DC', '#FACDD2', '#E6D7F0', '#E6EBEF', '#CAD1D9'])
        plt.rcParams['axes.prop_cycle'] = set_3
    
    # plotting main function
    (dataframe.plot(kind=kind
                  , rot=rot 
                  , figsize=figsize
                  , title=title
                  , stacked=stacked
                  , legend=legend
                  , subplots=subplots
                  , ylim=ylim
                  , xlim=xlim)
    )
    
    # legend
    plt.rcParams['legend.frameon'] = True
    
    if legend_loc != 'best':
        plt.rcParams['legend.loc'] = legend_loc
    
    # add an horizonal label for the y axis 
    # plt.text(-0.23, 0.96, 'Transaction Type', fontsize=15, fontweight='black', color = '#333F4B')

    # set the spines position
    #ax.spines['bottom'].set_position(('axes', -0.04))
    #ax.spines['left'].set_position(('axes', 0.015))

    # style
    
    # font
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.serif'] = 'Arial'
    plt.rcParams['font.size'] = 12

    # axis style
    plt.rcParams['axes.edgecolor'] = '#E6EBEF'
    plt.rcParams['axes.linewidth'] = 0.8
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['axes.titleweight'] = 'heavy'
    
    # change the style of the axis spines
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.labelcolor'] = '#3C3C3C'
    
    plt.rcParams['xtick.top'] = False
    plt.rcParams['ytick.right'] = False
    #ax.spines['right'].set_color('none')
    #ax.spines['left'].set_smart_bounds(True)
    #ax.spines['bottom'].set_smart_bounds(True)
    
    # line style
    plt.rcParams['lines.linewidth'] = 1.5
    
    # label
    #ax.set_xlabel(xlabel, fontsize=15, fontweight='black', color = '#333F4B')
    plt.xlabel(xlabel, fontsize=15, fontweight='black', color='#333F4B')
    plt.ylabel(ylabel, fontsize=15, fontweight='black', color='#333F4B')
    plt.ylim(ylim)
    plt.xlim(xlim)
    
    # handle Thousand notation on y-axis
    if thousand == True:
        plt_thousand()
        
    # handle Percentage notation on y-axis
    if percentage == True:
        plt_percentage()

    # custom legend    
    if legend != None:
        plt.legend(legend)
