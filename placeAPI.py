#coding=utf-8
import urllib2
import json
class placeApi:
    def place_api(self,query,city,index,num):
        try:
            #对百度地图api发送请求获取json,发送请求与解析json部分可以替换简洁写法，具体可参见readme.txt
            url = 'http://api.map.baidu.com/place/v2/search?query=%s&' \
                  'page_size=10&page_num=%d&scope=2&region=%s&output=json&ak=NYFRcc4A4UBQpq5qLdxhTcfx5DKn5C0H' \
                  %(query,int(num),city)
            req = urllib2.Request(url)
            request = urllib2.urlopen(req)
            jsons = request.read()
            #解析返回的json数据
            info = json.loads(jsons)
            #对json数据进行提取
            name = info['results'][index-1].get("name")
            address=info['results'][index-1].get("address")
            telephone = info['results'][index - 1].get('telephone')
            rating=info['results'][index-1].get('detail_info').get('overall_rating')
            if telephone==None:
                telephone='无'
            else:
                telephone=info['results'][index - 1].get('telephone')
            #返回所需信息
            return name,address,telephone,rating
        except Exception as e:
            print '发生异常:',e