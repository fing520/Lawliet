# -*- coding: utf-8 -*-
import json
import re
import xml.etree.ElementTree as ET
class Request(object):

    """获取传递数据"""
    data = ''
    def __init__(self, environ):
        self.environ = environ
        self.data = self.get_data()

    def get_data(self):
        try:
            len_input = int(self.environ['CONTENT_LENGTH'])
            input_str = self.environ['wsgi.input'].read(len_input)
            if self.environ['CONTENT_TYPE'] == 'application/json':
                return json.loads(input_str)
            elif self.environ['CONTENT_TYPE'] == 'application/xml':
                return ET.fromstring(input_str)
            return input_str
        except:
            return None

    def headers(self, header):
        http_header = re.sub('-','_',header).upper()
        if http_header == 'CONTENT_TYPE':
            try:
                return self.environ[http_header]
            except:
                return None
        else:
            http_header = 'HTTP_' + http_header
            try:
                return self.environ[http_header]
            except:
                return None

    def params(self, param):
        query_string = self.environ['QUERY_STRING'].split('&')
        print query_string
        param_dict = dict()
        for i in query_string:
            param_one = i.split('=')
            param_dict[param_one[0]] = param_one[1]
        try:
            return param_dict[param]
        except:
            return None