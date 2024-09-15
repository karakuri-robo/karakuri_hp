import math
import numpy as np
import tkinter as tk

# グローバル変数の宣言
gt_x = []
gt_y = []
pos = np.empty((0, 2))

# 2項係数計算
def BiCoe(n, k):
    if n < k:
        return -1
    return math.factorial(n) / (math.factorial(k) * math.factorial((n - k)))

# Bernstein多項式
def Bernstein(n, i, t):
    return BiCoe(n, i) * np.power((1-t), (n-i)) * np.power(t, i)

# ベジェ曲線
def BezierCurve(points, t):
    Gt = np.array([0.0, 0.0])  # 初期化（2次元ベクトル）
    n = len(points) - 1
    for k, point in enumerate(points):
        Gt += np.array(point) * Bernstein(n, k, t)
    return Gt

def DrawBezierCurve(points):
    global gt_x
    global gt_y
    x = np.arange(0, 1, 0.01, dtype=np.float32)
    x = np.append(x, 1.0)
    gt = [BezierCurve(points, t) for t in x]
    gt_x = [g[0] for g in gt]
    gt_y = [g[1] for g in gt]
    ct_x = [ct[0] for ct in points]
    ct_y = [ct[1] for ct in points]

def draw_Bezier_curves(event):
    global pos
    sta_poi_x, sta_poi_y = event.x, event.y
    tmp = np.array([[sta_poi_x, sta_poi_y]])  # 2次元配列として新しい点を準備
    pos = np.vstack([pos, tmp])  # 点を追加
    canvas.create_oval(sta_poi_x-2, sta_poi_y-2, sta_poi_x+2, sta_poi_y+2, fill="blue")  # 点の表示
    DrawBezierCurve(pos)

def draw_point():
    global gt_x, gt_y
    li_point = []
    for x, y in zip(gt_x, gt_y):
        li_point.append(x)
        li_point.append(y)
    canvas.create_line(li_point, smooth=True, width=3)

def clear():
    global pos
    canvas.delete("all")
    pos = np.empty((0, 2))

# メインウィンドウの作成
root = tk.Tk()
root.title("メインウィンドウ")

# キャンバスを作成
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# クリックイベントにdraw_Bezier_curves関数をバインド
canvas.bind("<Button-1>", draw_Bezier_curves)

# 操作ウィンドウの作成
def create_control_window():
    # Toplevelウィンドウの作成
    control_window = tk.Toplevel(root)
    control_window.title("操作")
    control_window.geometry("300x100")

    # ボタンのフレーム作成
    frame_d = tk.Frame(control_window)
    frame_d.pack(fill=tk.BOTH, padx=20, pady=10)

    frame_c = tk.Frame(control_window)
    frame_c.pack(fill=tk.BOTH, padx=20, pady=10)

    # ボタンのテキスト設定
    text_d = tk.StringVar(frame_d)
    text_d.set("draw")

    text_c = tk.StringVar(frame_c)
    text_c.set("clear")

    # ボタンのイベント設定
    button_d = tk.Button(frame_d, textvariable=text_d, command=draw_point)
    button_c = tk.Button(frame_c, textvariable=text_c, command=clear)

    # 各種ウィジェットの設置
    button_d.pack()
    button_c.pack()

    return control_window

# 操作ウィンドウを作成
create_control_window()

# メインループの実行
root.mainloop()