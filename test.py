#!/usr/bin/env python
# coding: utf-8

from wxbot import *


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.send_msg_by_uid(u'hi', msg['user']['id'])
            #self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])
'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''


def main():
    bot = WXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()
    return bot
def send(MyWXBot,p_list,dialog):
    print p_list
    print dialog
    MyWXBot.list_send(p_list,dialog)



if __name__ == '__main__':
    main()
