# -*- coding: utf-8 -*-
from q27 import get_rid_of_inner_link_markup
from q20 import picup_eng_txt
import re
from pprint import pprint


def get_rid_of_markup(txt):
    txt = get_rid_of_inner_link_markup(txt)
    txt = re.sub(r'\[\[ファイル:[^|]*\|[^|]*\|([^\]]*)\]\]', r'\1', txt)
    txt = re.sub(r'\[https?://[\w/:%#\$&\?\(\)~\.=\+\-]+ ?([^\]]*)\]', r'\1', txt)
    txt = re.sub(r'\[\[Category[\]]*\]\]', '', txt)
    txt = re.sub(r'#REDIRECT \[\[([^\]]*)\]\]', r'\1', txt)
    txt = re.sub(r'<!--[^-]*-->', '', txt)
    txt = re.sub(r'(=+)(.+)\1', r'\2', txt)
    txt = re.sub(r'<[^>]*>', '', txt)
    # 疲れたのでやめます
    return txt


if __name__ == '__main__':
    txt = picup_eng_txt()
    txt = txt[txt.find('{{基礎情報 国'):]
    txt = txt.split('\n')[1:]
    pattern = re.compile(r'\|(\w+) = ([^{]+)')
    pattern2 = re.compile(r'\|(\w+) = {{(\w+)')
    line = txt.pop(0)
    m = re.match(pattern, line)
    infomation_list = {}
    while m:
        infomation_list[m.group(1)] = get_rid_of_markup(m.group(2))
        line = txt.pop(0)
        m = re.match(pattern, line)
        if not m:
            m2 = re.match(pattern2, line)
            if m2:
                v = ''
                line = txt.pop(0)
                m = re.match(pattern, line)
                while not m:
                    v += get_rid_of_markup(line)
                    line = txt.pop(0)
                    m = re.match(pattern, line)
                infomation_list[m2.group(1)] = v
    pprint(infomation_list)
