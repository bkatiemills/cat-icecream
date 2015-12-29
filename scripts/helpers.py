def getAges(color, flavor, data):
    ''' 
    given a dataframe <data> with columns 'color', 'age', and 'favorite-icecream',
    return a list of ages of cats who have 'color' == <color>, and 'favorite-icecream' == <flavor> 
    '''

    return data.loc[(data['color'] == color) & (data['favorite-icecream'] == flavor), 'age'].values.tolist()