class Seven:

    def __init__(self):
        self.d = {}

    def __setitem__(self, key, value):
        self.d[key] = value

    def __getitem__(self, key):
        return self.d[key]

    def __repr__(self):
        s = ''
        for k, v in self.d.items():
            s += str(k) + ": " + str(v) + "\n"
        return s


s1 = Seven()
s1["k1"] = "v1"  # Add key `k1` with value `v1`
s1[1] = 5  # Add key `1` with value `5`
s1[20] = 'foo'
print s1[1]  # Get value associated with key `1`
print s1["k1"]
print s1  # use __repr__ and print returning string
