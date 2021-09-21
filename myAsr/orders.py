import os,win32api
import re
class Orders:
    orderlist=['网易云',"记事本"]
    exelist=['Y:\Z\CloudMusic\cloudmusic.exe','E:\\song.txt']

    def bind_olist(self,olist):
        self.orderlist=olist

    def bind_oaddlist(self,oaddlist):
        self.exelist=oaddlist
    def play_music(self):
        win32api.ShellExecute(0, 'open', 'Y:\Z\CloudMusic\cloudmusic.exe', '','',1)
    

    def open_notepad(self):
        win32api.ShellExecute(0, 'open', 'E:\\song.txt', '','',1)
    
    def run_exe(self,index):
        win32api.ShellExecute(0, 'open', self.exelist[index], '','',1)


    def re_And_Execute(self,result):
        for i  in range(len(self.orderlist)):
            for res in result['result']:
               # self.run_exe(i)
                if(re.match(".*"+self.orderlist[i]+".*",res)):
                    self.run_exe(i)