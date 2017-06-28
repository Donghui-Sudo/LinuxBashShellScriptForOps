#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:apiTestForWeChatWithItChat.py
User:               Guodong
Create Date:        2017/3/8
Create Time:        10:37

https://github.com/littlecodersh/ItChat
https://zhuanlan.zhihu.com/p/25581913

Please do NOT edit this file directly unless you know what does it mean

 """
import re
import time
import itchat
from itchat.content import *


@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def text_reply(msg):
    if msg['Type'] == 'Text':
        reply_content = msg['Text']
    elif msg['Type'] == 'Picture':
        reply_content = u"图片: " + msg['FileName']
    elif msg['Type'] == 'Card':
        reply_content = u" " + msg['RecommendInfo']['NickName'] + u" 的名片"
    elif msg['Type'] == 'Map':
        x, y, location = re.search("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1,
                                                                                                                    2,
                                                                                                                    3)
        if location is None:
            reply_content = u"位置: 纬度->" + x.__str__() + " 经度->" + y.__str__()
        else:
            reply_content = u"位置: " + location
    elif msg['Type'] == 'Note':
        reply_content = u"通知"
    elif msg['Type'] == 'Sharing':
        reply_content = u"分享"
    elif msg['Type'] == 'Recording':
        reply_content = u"语音"
    elif msg['Type'] == 'Attachment':
        reply_content = u"文件: " + msg['FileName']
    elif msg['Type'] == 'Video':
        reply_content = u"视频: " + msg['FileName']
    else:
        reply_content = u"消息"

    friend = itchat.search_friends(userName=msg['FromUserName'])
    itchat.send(u"Friend:%s -- %s    "
                u"Time:%s    "
                u" Message:%s" % (friend['NickName'], friend['RemarkName'], time.ctime(), reply_content),
                toUserName='filehelper')

    itchat.send(u"我已经收到你在【%s】发送的消息【%s】稍后回复。--微信助手(Python版)" % (time.ctime(), reply_content),
                toUserName=msg['FromUserName'])


itchat.auto_login()
itchat.run()