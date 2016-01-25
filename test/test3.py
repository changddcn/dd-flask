#!/usr/bin/env python2.7
#coding:utf-8
#author:changddcn@qq.com
#get ip list http://ips.chacuo.net/
#please place the ip files in folder ip in current path

from sys import exit
import time
from multiprocessing.dummy import Pool as threadPool

import urllib2
pdf_id=736
time_start_float=time.mktime((2016, 1, 21, 10, 47, 39, 3, 21, 0))
time_end_float=time.mktime((2016, 1, 21, 13,00, 00, 3, 21, 0))
target_count=0


target_example='''
http://211.103.228.187/lms/attached/annexNotice/20160121/20160121104738_733.pdf
http://211.103.228.187/lms/attached/annexNotice/20160121/20160121115644_827.pdf
http://211.103.228.187/lms/attached/annexNotice/20160121/20160121130022_918.pdf
'''

#check port status，record the ip opening port 22,count opening and shutdown.
def check(target):
    global pdf_id
    global target_count
    target='http://211.103.228.187/lms/attached/annexNotice/20160121/%s_%s.pdf' %(target,pdf_id)
    try:
        result=urllib2.urlopen(url=target).read(600)
    except Exception as e:
        pass
    if result.find('Errorpage')==-1:
        print "\n\r"
        print "\n\r"
        print "#"*100
        print 'success:%s'%target
        print "#"*100
        print "\n\r"
        print "\n\r"
        with open('success.txt','a+') as hand:
            hand.write('\n\r')
            hand.writelines('success:%s\n\r'%target)
        exit(1)
    else:
        print '剩余：%s fail:%s' %(target_count,target)+'\r',
    target_count-=1
#threads controler
def getTargetList():
    timeList=[]
    global time_start_float
    global time_end_float
    while(time_start_float<=time_end_float):
        tmp_time=time.strftime('%Y%m%d%H%M%S',time.localtime(time_start_float))
        time_start_float+=1
        timeList.append(tmp_time)
    return timeList

def thControler(targetList):
    print 'starting checking threads.........'
    try:
        th=threadPool(8)
        th.map(check,targetList)
    except Exception as e:
        print e
    th.close()
    th.join()

def main():
    global target_count
    global pdf_id
    timeList=getTargetList()
    target_count=len(timeList)
    print '加载时间秒数:%s' %(target_count)
    for x in range(742,918):
        print '测试pdf:%s'%x
        print "\n\r"
        pdf_id=x
        thControler(timeList)

if __name__=='__main__':
    main()
