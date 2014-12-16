try:
    from collections import OrderedDict
except:
    from ordereddict import OrderedDict

from .output import Output
from .graphviz import GraphvizOutput
from .gephi import GephiOutput
from .ubigraph import UbigraphOutput
from .pickle import PickleOutput


outputters = OrderedDict([
    ('graphviz', GraphvizOutput),
    ('gephi', GephiOutput),
    # ('ubigraph', UbigraphOutput),
])
