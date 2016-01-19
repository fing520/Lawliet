#from lawliet.response import response
from lawliet import Response

xml_str = """
 <xml>
 <ToUserName><![CDATA[toUser]]></ToUserName>
 <FromUserName><![CDATA[fromUser]]></FromUserName>
 <CreateTime>1348831860</CreateTime>
 <MsgType><![CDATA[text]]></MsgType>
 <Content><![CDATA[this is a test]]></Content>
 <MsgId>1234567890123456</MsgId>
 </xml>
"""
def ping():
    return Response(status=403)

def res_json(request):
    return request.params('qqq')

def test_response():
    return Response(xml_str, headers={'Content-type': 'application/xml'})
