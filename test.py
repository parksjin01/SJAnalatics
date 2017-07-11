# import threading
# import time
#
# def fun1(ret):
#     time.sleep(1)
#     ret.append(1+2)
#
# def fun2(ret):
#     print threading.current_thread()
#     time.sleep(3)
#     ret.append(1-2)
#
# res1 = []
# res2 = []
# thread1 = threading.Thread(target=fun1, name='thread1', args=[res1])
# thread2 = threading.Thread(target=fun2, name='thread2', args=[res2])
#
# start = time.time()
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print time.time()-start
#
# print res1, res2
# res1 = [[1], [2]]
# res2 = [[3], [4]]
# print res1+res2

print len('''Trial Version: http://goo.gl/i4onu Google Maps is now available for 8-bit Nintendo Entertainment Systems (NES). Availability in Google Store is TBD but you can try it on your browser by going to http://maps.google.com and clicking "Quest" in the upper right hand corner of the map. Also... Happy April Fools 2012!''')