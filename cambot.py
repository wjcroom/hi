import requests
bot6camapikey="""ee766919b07a836babf799d5336fdac5c2e8241cef02644986607f315c6104cb7b22756964223a362c226e6f6e6365223a222b4b474d447843707657514141414141336e61693135557a6a4a34344f72344e227d"""
##来自不同的bot
bot6camapikey="e6436097fd63ebeefc1262397c5406cede6c42132d65a2a8ae1e5742d5c219a27b22756964223a31312c226e6f6e6365223a226c625a6d4b70374a766d514141414141626e533032685a31334e567639305053227d"
##发给不同的人
toid=1
apiurl = f"https://chat.ezdial.cn:8000/api/bot/send_to_user/%s"

def sendmsg(toid,msg):
    msgurl = apiurl%toid
    payload=f'摄像头消息:{msg}'.encode()
    headers = {
      'Content-Type': 'text/markdown',
      'Accept': 'aplication/json; charset=utf-8',
      "x-api-key":bot6camapikey,
      'X-Properties':""
    }
    response = requests.request("POST", msgurl, headers=headers, data=payload)
    #返回200就是发送成功了
    print(response.status_code,response.text)

sendmsg(toid,"hello")
