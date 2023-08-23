'''
Core curses.
'''

from math import pi,sin,cos

def Synth(
    voice:function = lambda x:0.0, # 音色
    freq:float = 1.0, # 频率(音高)
    vol:float = 1.0, # 音量
    length:int = 0,
    envelop:function = lambda x : 1.0, # 包络
    glide:function = lambda x : 1.0, # 滑音
    SampleRate = 64000 # ! Don't change it most of the time.
)->list[float]:
    w = []
    for i in range(length):
        s = i/SampleRate
        r = vol * envelop(s) * voice( glide(s) * freq * s ) 
        w.append(r)
    return w


