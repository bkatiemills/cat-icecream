import pandas
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import scripts.helpers


data = pandas.read_csv('data/cat-data.csv')
color = data['color'].unique()
icecream = data['favorite-icecream'].unique()

matplotlib.pyplot.figure().set_tight_layout(True)

for i, flave in enumerate(icecream):
    for col in color:
        matplotlib.pyplot.subplot(221 + i)
        matplotlib.pyplot.hist(scripts.helpers.getAges(col, flave, data), 20, normed=1, histtype='step')
        matplotlib.pyplot.xlim(0,20)
        
        matplotlib.pyplot.title(flave)
        matplotlib.pyplot.xlabel('Age')
        matplotlib.pyplot.ylabel('Popularity')

matplotlib.pyplot.savefig('img/cat-icecream.png')
 

