'''
Write WaveTrack Into WAV File
Convention: The default sampling rate is 64000Hz.
And the wave track is of type list.

[Curse Locked]
'''

import ctypes
import wave

def output(file_name:str,w:list[int],SampleRate=64000):
    f =wave.open(file_name,'wb')# 打开文件
    f.setnchannels(1)# 声道数
    f.setsampwidth(2)# 采样位深
    f.setframerate(SampleRate)# 采样率
    # MAGIC 比struct快得多
    f.writeframes(\
        bytes((ctypes.c_int16 * len(w))(*w))\
    )
    f.close()