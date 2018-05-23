import re

from scrapy import Selector



def list(l):
    l = '941028'.join(l)
    l = l.split()
    l = ''.join(l)
    l = l.split('941028')
    while '' in l:
        l.remove('')
    return l


def dealcontent(x):
    # 删掉作者
    while '\t' in x:
        x = x.split('\t')
        x = ''.join(x)
    while '\n' in x:
        x = x.split('\n')
        x = ''.join(x)
    while '\\n' in x:
        x = x.split('\\n')
        x = ''.join(x)
    while '\u200b' in x:
        x = x.split('\u200b')
        x = ''.join(x)
    while re.match(r'^ ', x):
        x = x.lstrip(' ')
    while '<br>' in x:
        x = x.split('<br>')
        x = ''.join(x)
    # 处理表情
    if Selector(text=x).xpath('//img[@title]'):
        face = Selector(text=x).xpath('//img/@title').extract()
        face_drop = re.findall(r'<img class=\"W_img_face\"[\s\S]*?>', x)
        lens = len(face)
        for i in range(0, lens):
            x = x.replace(face_drop[i], face[i])
    return x



def dealstr(s):

    # 处理表情
    while '\t' in s:
        s = s.split('\t')
        s = ''.join(s)
    while '\n' in s:
        s = s.split('\n')
        s = ''.join(s)
    while '\u200b' in s:
        s = s.split('\u200b')
        s = ''.join(s)
    while '\\n' in s:
        s = s.split('\\n')
        s = ''.join(s)
    while re.match(r'^ ', s):
        s = s.lstrip(' ')
    while re.match(r'[\s\S]*? $', s):
        s = s.rstrip(' ')
    while '<br>' in s:
        s = s.split('<br>')
        s = ''.join(s)
    if re.findall(r'<img[\s\S]*?>', s):
        imgs = re.findall(r'<img[\s\S]*?>', s)
        # 有表情处理表情
        if re.match(r'title=\"\[[\s\S]*?\]', s):
            for img in imgs:
                face = re.findall(r'title=\"\[[\s\S]*?\]', str(img))[0].strip('title=\"')
                s = s.split('{0}'.format(img))
                s = face.join(s)
        # 图片则删除
        else:
            for img in imgs:
                s = s.split('{0}'.format(img))
                s = ''.join(s)
    # 处理链接
    if re.findall(r'<a[\s\S]*?/a>', s):
        links = re.findall(r'<a[\s\S]*?/a>', s)
        for link in links:
            links_content = re.findall(r'>[\s\S]*?<', link)[0].strip('<').strip('>')
            s = s.split('{0}'.format(link))
            s = links_content.join(s)

    return s
