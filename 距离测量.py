import json
import requests as rs
def geturl():
    print ("请输入起点所在的城市：")
    origin_region = input(">>>")
    print ("请输入起点位置：")
    origin = input(">>>")
    print ("请输入终点点所在的城市：")
    destination_region = input(">>>")
    print ("请输入终点位置：")
    destination = input(">>>")
    ak="GVbSTEgzFooVjLVqfmzTrGRO1fGhWPVG"
    url = "http://api.map.baidu.com/direction/v1?mode=transit&origin=%s&destination=%s&origin_region=%s&&destination_region=%s&output=json&ak=%s" % (origin,destination,origin_region,destination_region,ak)
    return (url,origin_region,origin,destination_region,destination)

def getres(url):
    res = rs.get(url)
    js = json.loads(res.text)
    if js["status"] == 0:
        try:
            if js["result"]["error"] == 0:
                return js["result"]["taxi"]
        except:
            return 0
    return 0

print ('''
************************************************
     Welcome to Location Searching System!       
************************************************
''')

url = geturl()
result = getres(url[0])
if result == 0:
    print ("Error: Cannot find the place!")
else:
    print ("起点： %s  %s" % (url[1],url[2]))
    print ("终点： %s  %s" % (url[3],url[4]))
    print ("距离： %.1f  公里，开车大约需要%d分钟 " % (result["distance"]/1000,result["duration"]/60+1))    
