from orders import Orders
from recongnizer import Recongnizer
import threading

class LAEThread(threading.Thread):
    def __init__(self) :
        threading.Thread.__init__(self)
        self.orders=Orders()
        self.recognizer=Recongnizer()

    def bind_window(self,window):
        self.mywindow=window

    def bind_orderlist(self,olist):
        self.orders.bind_olist(olist)
    def bind_orderaddlist(self,oaddlist):
        self.orders.bind_oaddlist(oaddlist)

    def run(self):
        self.listenAndHandler()

    
    def listenAndHandler(self,*args): 
        
        while(True):
            self.mywindow._signal.emit('------开始录音：请在5秒内输入语音------')
            result = self.recognizer.recorder_and_rec(1537)   #1537中文   1737 英文
            print(result)
            if result['err_msg'] == 'success.':
                self.mywindow._signal.emit(' '.join(result['result']))
                self.orders.re_And_Execute(result)

            else:
                self.mywindow._signal.emit(str({'err_no':result['err_no'], 'err_msg': result['err_msg']}))             
                           
            self.mywindow._signal.emit('--------------录音结束---------------\n')

# if __name__=='__main__':
#     listenAndHandler=threading.Thread(group=None,target=LAEThread.listenAndHandler,args=(application,))
#     listenAndHandler.start()