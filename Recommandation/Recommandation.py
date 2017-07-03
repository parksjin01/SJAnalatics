import Recommand_Google
import Recommand_Google_V2

def Recommandation(url="google"):
    url = url.lower()
    if url == 'google':
        try:
            result = Recommand_Google_V2.Recommandation(100)
            # assert 1==2
        except Exception, e:
            print e
            result = Recommand_Google.Recommandation(100)
        for line in result:
            try:
                print '%-60s %-10s %-10s %10s %10s %10s %10s' %(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
            except:
                print line
    else:
        return -1

Recommandation()