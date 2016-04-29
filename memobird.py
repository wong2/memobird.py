#-*-coding:utf-8-*-

import requests
from base64 import b64encode
from cStringIO import StringIO
from datetime import datetime
from PIL import Image, ImageOps


class ApiError(Exception):
    pass


class Paper(object):

    def __init__(self):
        self.contents = []

    @staticmethod
    def _ensure_gbk(text):
        try:
            text = text.decode('utf-8')
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass
        return text.encode('gbk')

    def add_text(self, text):
        text = self._ensure_gbk(text)
        content = 'T:%s' % b64encode(text)
        self.contents.append(content)

    def add_image(self, image):
        output = StringIO()
        im = Image.open(image)
        im.thumbnail((384, 384), Image.ANTIALIAS)
        ImageOps.flip(im).convert('1').save(output, 'BMP')
        content = 'P:%s' % b64encode(output.getvalue())
        self.contents.append(content)

    def encode(self):
        return '|'.join(self.contents)


class Memobird(object):

    API_BASE_URL = 'http://open.memobird.cn/home'

    def __init__(self, ak):
        self.ak = ak
        self.user_id = None
        self.device_id = None

    def _request(self, url, data):
        url = self.API_BASE_URL + url
        data.update({
            'ak': self.ak,
            'timestamp': str(datetime.now().replace(microsecond=0))
        })
        r = requests.post(url, data=data)
        r.raise_for_status()
        resp = r.json()
        if resp['showapi_res_code'] != 1:
            raise ApiError(resp['showapi_res_error'])
        return resp

    def setup_device(self, device_id):
        resp = self._request('/setuserbind', {
            'memobirdID': device_id,
            'useridentifying': device_id
        })
        self.user_id = resp['showapi_userid']
        self.device_id = device_id

    def print_paper(self, paper):
        data = {
            'printcontent': paper.encode(),
            'memobirdID': self.device_id,
            'userID': self.user_id,
        }
        resp = self._request('/printpaper', data=data)
        return resp['printcontentid']

    def print_text(self, text):
        paper = Paper()
        paper.add_text(text)
        return self.print_paper(paper)

    def print_image(self, image):
        paper = Paper()
        paper.add_image(image)
        return self.print_paper(paper)

    def is_paper_printed(self, paper_id):
        resp = self._request('/getprintstat', data={
            'printcontentID': paper_id
        })
        return resp['printflag'] == 1
