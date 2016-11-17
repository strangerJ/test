# -*- coding: utf-8 -*- 

import wx
import wx.xrc
from test import *
from wxbot import *
from threading import Thread

 

class TestThread(Thread):
    """Test Worker Thread Class."""
  
    #----------------------------------------------------------------------
    def __init__(self, wxObject):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.wxObject = wxObject
        self.setDaemon(True)
        self.start()    # start the thread
  
    #----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        self.wxObject.proc_msg()
        # This is the code executing in the new thread.


class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u'助手', pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.panel = wx.Panel(self, -1)
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText1 = wx.StaticText( self.panel, wx.ID_ANY, u"请登录", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        self.m_button1 = wx.Button( self.panel, wx.ID_ANY, u"登录微信", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.panel.SetSizer(bSizer1)

        self.Layout()
        self.Centre( wx.BOTH )
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.login )
        self.list = []
        self.index = []

    def login( self, event ):
        self.dd = main()
        TestThread(self.dd)
        self.panel.Destroy()
        name=[]
        self.panel2 = wx.Panel(self,-1)
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        for contact in self.dd.contact_list:
            if contact['RemarkName']=='':
                name.append(contact['NickName'])
            else:
                name.append(contact['RemarkName'])
        self.checklist = wx.CheckListBox( self.panel2,-1,(20,20),(200,100),name, wx.LB_MULTIPLE)
        bSizer2.Add( self.checklist, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )
        self.m_button3 = wx.Button( self.panel2, wx.ID_ANY, u"选择所有人员", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.m_button1 = wx.Button( self.panel2, wx.ID_ANY, u"确认发送", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.m_button4 = wx.Button( self.panel2, wx.ID_ANY, u"重置选择人员", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl1 = wx.TextCtrl( self.panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(350,50), style=wx.TE_MULTILINE|wx.TE_RICH2 )
        bSizer3.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        bSizer2.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        bSizer2.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

        self.checklist.Bind(wx.EVT_CHECKLISTBOX,self.getvalue)
        self.m_button1.Bind( wx.EVT_BUTTON, self.FindSquare )
        self.m_button3.Bind( wx.EVT_BUTTON, self.get_all )
        self.m_button4.Bind( wx.EVT_BUTTON, self.del_all )
        self.panel2.SetSizer(bSizer2)
    def get_all(self,event):
        leng = len(self.dd.contact_list)
        for i in range(leng):
            self.checklist.SetSelection(i)
            self.checklist.Check(i)
            label = self.checklist.GetString(i)
            self.list.append(label)
            self.index.append(i)
    def del_all(self,event):
        self.list = []
        for s in self.index:
            self.checklist.Check(s,False)
            self.checklist.Deselect(s)
        self.index = []
    def getvalue(self,event):
        index = event.GetSelection()
        label = self.checklist.GetString(index)
        self.checklist.SetSelection(index)
        if label not in self.list:
            self.list.append(label)
            self.index.append(index)
        else:
            self.list.remove(label)
            self.index.remove(index)
    def FindSquare( self, event ):
        if len(self.list)==0:
            self.dialogBox=wx.MessageBox(u'请选择人员',u'操作错误')
        elif self.m_textCtrl1.GetValue()=='':
            self.dialogBox=wx.MessageBox(u'请输入消息',u'操作错误')
        else:
            sendlist = []
            for i in self.list:
                for per in self.dd.contact_list:
                    if per['RemarkName']==i or per['NickName'] ==i:
                        sendlist.append(per['UserName'])
            dialog = self.m_textCtrl1.GetValue()
            send(self.dd,sendlist,u'%s'%dialog)
            self.m_textCtrl1.SetValue('')


        
if __name__=='__main__':
    app = wx.PySimpleApp()
    MyFrame1(None).Show()
    app.MainLoop()
