import pandas
import matplotlib.pyplot

def getAges(color, flavor, data):
    ''' 
    given a dataframe <data> with columns 'color', 'age', and 'favorite-icecream',
    return a list of ages of cats who have 'color' == <color>, and 'favorite-icecream' == <flavor> 
    '''

    return data.loc[(data['color'] == color) & (data['favorite-icecream'] == flavor), 'age'].values.tolist()


data = pandas.read_csv('data/cat-data.csv')
color = data['color'].unique()
icecream = data['favorite-icecream'].unique()

matplotlib.pyplot.figure().set_tight_layout(True)

for i, flave in enumerate(icecream):
    for col in color:
        matplotlib.pyplot.subplot(221 + i)
        matplotlib.pyplot.hist(getAges(col, flave, data), 20, normed=1, histtype='step')
        matplotlib.pyplot.xlim(0,20)
        
        matplotlib.pyplot.title(flave)
        matplotlib.pyplot.xlabel('Age')
        matplotlib.pyplot.ylabel('Popularity')



matplotlib.pyplot.show()
 

