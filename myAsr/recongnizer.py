import speech_recognition as sr
from orders import Orders
import wave
import pyaudio
from aip import AipSpeech







class Recongnizer:
    APP_ID = '24165137'
    API_KEY = 't4Y9q9sco1e6TNpy0lEYGcl9'
    SECRET_KEY = 'Ft6XVEVl56ATtb1OrwadfQ8xoQOS3Mpl'
    def __init__(self) -> None:
        self.rate=16000
        self.channels=1
        self.format=pyaudio.paInt16
        self.CHUNK=1024
        self.orders=Orders()
        self.mircophone=sr.Microphone()
        self.recognizer=sr.Recognizer()
        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)



    def recorder_and_rec(self,language):
        frames_data=self.record(5,"./temp.wav")
        return self.get_result(frames_data,'wav',self.rate,language)

    def record(self,time_sec, save_file=None, **kwarg):
    
        mypyaudio=pyaudio.PyAudio()
        frames = []
        stream = mypyaudio.open(rate=self.rate,
                              channels=self.channels,
                              format=self.format,
                              input=True,
                              frames_per_buffer=self.CHUNK,
                              **kwarg)

        print('"*"*10, "开始录音：请在'+str(time_sec)+"秒内输入语音")
        for i in range(self.rate * time_sec // self.CHUNK):
            data = stream.read(self.CHUNK)
            frames.append(data)
        print("*"*10, "录音结束\n")

        stream.stop_stream()
        stream.close()
        mypyaudio.terminate()

        frames_data = b''.join(frames)

        if save_file != None:
            with wave.open(save_file, 'wb') as wf:
                wf.setnchannels(self.channels)
                wf.setsampwidth(mypyaudio.get_sample_size(self.format))
                wf.setframerate(self.rate)
                wf.writeframes(frames_data)

        return frames_data


    
    def get_result(self,wave,format,rate,language):
        return self.client.asr(wave,format,rate,{
            'dev_pid': language, # 默认1537(普通话 输入法模型)  1737（英语）
        })