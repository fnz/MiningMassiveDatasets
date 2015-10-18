class MapReduceBase:
    data = {}

    def __init__(self):
        print 'init'

    def emit(self, k, v):
        if k not in self.data.keys():
            self.data[k] = []
        self.data[k].append(v)

    def map_function(self, x):
        self.emit(x, 1)

    def reduce_function(self, v):
        add = lambda x, y: x + y
        return reduce(add, self.data[v])

    def run(self, input_list):
        map(self.map_function, input_list)
        ret = {}
        for k in self.data.keys():
            ret[k] = self.reduce_function(k)
        return ret




