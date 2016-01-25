#coding:utf-8
#!/usr/bin/python
#20160121130022_918--20160121180000_???
import requests
import time,sys

target_example='''
http://211.103.228.187/lms/attached/annexNotice/20160121/20160121104738_733.pdf
http://211.103.228.187/lms/attached/annexNotice/20160121/20160121115644_827.pdf
http://211.103.228.187/lms/attached/annexNotice/20160121/20160121130022_918.pdf
'''

def check():
    time_start=20160121115644
    time_start_float=time.mktime((2016, 1, 21, 13, 00, 22, 3, 21, 0))
    id_start=922
    id_end=990
    time_end=20160121140000
    time_end_float=time.mktime((2016, 1, 21, 18, 00, 00, 3, 21, 0))

    while(time_start_float<=time_end_float):
        #累加时间秒，测试id号，知道时间值等于结束时间值

        test_time=time.strftime('%Y%m%d%H%M%S',time.localtime(time_start_float))
        target='http://211.103.228.187/lms/attached/annexNotice/20160121/%s_%s.pdf'%(test_time,id_start)
        result=requests.get(url=target).content
        if result.find('showError')==-1:
            print 'success:%s'%target
            print "\n\r"
            print "\n\r"
            id_start+=1
            with open('success.txt','a+') as hand:
                hand.writelines('success:%s'%target)
        else:
            print 'fail:%s'%target
            with open('fail.txt','a+') as handfail:
                handfail.writelines('fail:%s'%target)
        time_start_float=time_start_float+1

if __name__ == '__main__':
    check()