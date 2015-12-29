import scripts.helpers
import pandas, numpy

def test_getAges():
    '''
    spot-check the nominal behavior of getAges
    '''

    data = {
        "color": ['calico', 'calico', 'black', 'tortoise', 'tabby'],
        "age": [12, 4, 13, 20, 8],
        "favorite-icecream": ['lemon', 'strawberry', 'strawberry', 'chocolate', 'vanilla']
    }

    df = pandas.DataFrame(data)

    assert numpy.array_equal(scripts.helpers.getAges('calico', 'lemon', df), [12])
