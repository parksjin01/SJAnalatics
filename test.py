# from Util.Make_trainset import *
# import cPickle
#
# # code = get_code(100)
# with open('test_case', 'rb') as f:
#     code = cPickle.load(f)
# print len(code)
#
# idx = 0
# company = []
# done_list = []
# res = []
#
# for one in code:
#     print idx, one
#     idx+=1
#     if one in done_list:
#         continue
#     try:
#         tmp = Search(one)
#     except Exception, e:
#         print e
#         print '[-] Error occured',one
#         continue
#     company.append(tmp[0])
#     done_list.append(tmp[0])
#
# crawling_with_google(company, 60, res)
# # print res[0][:30]
# print res[1]
#

assert 1 not in [1, 2, 3]