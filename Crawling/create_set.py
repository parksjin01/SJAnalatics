import cPickle

with open('dataset', 'rb') as f:
    result, content = cPickle.load(f)
print len(result), len(content)

print 0x41c