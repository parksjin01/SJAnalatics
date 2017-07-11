import cPickle
with open('dataset', 'rb') as f:
    data = cPickle.load(f)
print data[4]