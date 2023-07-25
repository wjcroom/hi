import requests,time
from requests.auth import HTTPDigestAuth
import cambot
auth=HTTPDigestAuth('admin','password')
#时间格式2023-05-13T23:59:59Z
fmtbody='<?xml version="1.0" encoding="UTF-8"?>\r\n<CMSearchDescription>\r\n '\
     ' <searchID>1</searchID>\r\n<languageID>1</languageID>\r\n    <channelID>0</channelID>\r\n    <LogTypeList>\r\n   '\
     '<logType>{type}</logType>\r\n    </LogTypeList>\r\n    <timeSpan>\r\n        <startTime>{}</startTime>\r\n    '\
     '<endTime>{}</endTime>\r\n    </timeSpan>\r\n    <searchResultPostion>1</searchResultPostion>\r\n    '\
     '<maxResults>{}</maxResults>\r\n</CMSearchDescription>'
def getinits():
    s=requests.Session()
    s.auth=auth
    s.headers["content-type"]="application/xml; charset=UTF-8"
    return s 

#5分钟内的消息
#type报警信息All是全部，Alam是报警

def getevent(sesionA,long,much,host="192.168.1.1:8080",type="Alarm"):
    
    bg=time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(time.time()-long*60))
    ed=time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime(time.time()))
    num=5
    body=fmtbody.format(bg,ed,much,type=type)

    
    return sesionA.post("http://{}/ISAPI/ContentMgmt/logSearch".format(host),data=body).content.decode()

def parseevent(respones):
    if respones.find('报警发生')>=1:
        print('移动发生报警：'+respones)
        print(requests.get('http://192.168.1.2:8080').status_code)
        cambot.sendmsg(1,"发生报警")
        
    
def looprun(intver=3):

    s=getinits()
    pre=""
    while True :
        try:

            r=getevent(s,1,2)
            if r!=pre:
                 parseevent(r)
                 pre =r
            else :
                print ("一样")
        except (requests.exceptions.ChunkedEncodingError,ConnectionResetError ):
        
               s=getinits()
               print("conn, session restart")
        time.sleep(3)
if __name__=="__main__":
    looprun()
        
