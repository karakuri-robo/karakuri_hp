import sys
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *

Kp = Ki = Kd = 0
def create_plt(event):
    global Kp,Ki,Kd
    M = 1.00
    M1 =  0.00

    e = 0.00
    e1 = 0.00
    e2 = 0.00
    
    #ゲイン
    #Kp = Ki = Kd = 0.1
    """
    Kp = Kp
    Ki = Ki
    Kd = kd
    """    
    t = 100
    
    #目標値
    goal = 50.00

    x_list = []
    y_list = []

    x_list.append(0)
    y_list.append(0.00)

    for i in range(1,t):
        rand = randint(10) #0~9の中からランダムに１つの数を抽出

        M1 = M
        e2 = e1
        e1 = e

        if rand == 5 or rand == 7 or rand == 3:
            noize = randint(-30, 30) / 10
            e = goal - y_list[i-1] + noize

        elif rand == 9:
            noize = randint(-100, 100) / 10
            e = goal - y_list[i-1] + noize

        else:
            e = goal - y_list[i-1]

        M = M1 + Kp * (e-e1) + Ki * e + Kd * ((e-e1) - (e1-e2))
        y_list.append(M)
        x_list.append(i)

    plt.plot(x_list, y_list)
    plt.ylim(0, goal*2)
    plt.show()
    

class Application(tk.Frame):
    
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("Scaleの作成")     # ウィンドウタイトル

        #---------------------------------------------------------------
        # Scaleの作成

        # Scale（デフォルトで作成）
        #scaleV = tk.Scale( self.master)
        #scaleV.pack(side = tk.RIGHT)

        # Scale（オプションをいくつか設定）
        Static1 = tk.Label(text=u'Pゲイン')
        Static1.pack()
        self.scale_var_p = tk.DoubleVar()
        scaleP = tk.Scale( self.master, 
                    variable = self.scale_var_p, 
                    command = self.slider_scroll,
                    orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 300,           # 全体の長さ
                    width = 20,             # 全体の太さ
                    sliderlength = 20,      # スライダー（つまみ）の幅
                    from_ = 0,            # 最小値（開始の値）
                    to = 1,               # 最大値（終了の値）
                    resolution=0.01,         # 変化の分解能(初期値:1)
                    tickinterval=0.1         # 目盛りの分解能(初期値0で表示なし)
                    )
        scaleP.pack()
        
        Static2 = tk.Label(text=u'iゲイン')
        Static2.pack()
        self.scale_var_i = tk.DoubleVar()
        scaleI = tk.Scale( self.master, 
                    variable = self.scale_var_i, 
                    command = self.slider_scroll,
                    orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 300,           # 全体の長さ
                    width = 20,             # 全体の太さ
                    sliderlength = 20,      # スライダー（つまみ）の幅
                    from_ = 0,            # 最小値（開始の値）
                    to = 1,               # 最大値（終了の値）
                    resolution=0.01,         # 変化の分解能(初期値:1)
                    tickinterval=0.1         # 目盛りの分解能(初期値0で表示なし)
                    )
        scaleI.pack()
        
        Static3 = tk.Label(text=u'dゲイン')
        Static3.pack()
        self.scale_var_d = tk.DoubleVar()
        scaleD = tk.Scale( self.master, 
                    variable = self.scale_var_d, 
                    command = self.slider_scroll,
                    orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 300,           # 全体の長さ
                    width = 20,             # 全体の太さ
                    sliderlength = 20,      # スライダー（つまみ）の幅
                    from_ = 0,            # 最小値（開始の値）
                    to = 1,               # 最大値（終了の値）
                    resolution=0.01,         # 変化の分解能(初期値:1)
                    tickinterval=0.1         # 目盛りの分解能(初期値0で表示なし)
                    )
        scaleD.pack()
        #---------------------------------------------------------------
        #ボタン
        Button = tk.Button(text=u'出力', width=50)
        Button.bind("<Button-1>",create_plt) 
        #左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
        Button.pack()
        
    
    def slider_scroll(self, event=None):
        '''スライダーを移動したとき'''
        global Kp,Ki,Kd
        Kp = self.scale_var_p.get()
        Ki = self.scale_var_i.get()
        Kd = self.scale_var_d.get()
        #print(str(self.scale_var_p.get()))
        
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()
