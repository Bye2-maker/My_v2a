#import
import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.video.io.VideoFileClip import VideoFileClip


class App:
    def __init__(self, root):
        #外觀
        self.root = root
        self.root.title("HEX六邊行轉檔")
        self.root.geometry("450x400")
        self.root.configure(bg = "#9d9d90")
        
        #UI
        tk.Label(root, text = 'Hex六邊形轉檔工具', font = ('Microsoft JhengHei', 16, 'bold'), bg = '#9d9d90', fg = '#333333').pack(pady = 20)
        tk.Button(self.root, text = '單一檔案轉換', command = self.v2m_single, width=25, bg='#eeeeee', relief='flat', pady=8).pack(pady=10)
        tk.Button(self.root, text = '資料夾多檔案轉換', command = self.v2m_batch, width=25, bg='#eeeeee', relief='flat', pady=8).pack(pady=10)

        self.msg = tk.StringVar(value = '等待指令中！！')
        tk.Label(root, textvariable = self.msg, bg = '#9d9d90', fg = '#666666', wraplength = 350, font = ('Microsoft JhengHei', 9)).pack(pady = 30)


        #公用函式
    def _V2M_(self, inP, outP):
        with VideoFileClip(inP) as video:
            video.audio.write_audiofile(outP, bitrate = '192k', logger = None)

    def v2m_single(self):
        f = filedialog.askopenfilename(title = "第一步：選擇待處理檔案", filetypes = [('影片', '*.mp4 *.mkv')])
        if not f:
            return

        s = filedialog.asksaveasfilename(title = "第二步：選擇存哪", defaultextension = '.mp3', filetypes = [("MP3 檔案", '*.mp3')])
        if not s:
            return
        name, ext = os.path.splitext(s)
        s = name + '.mp3'
        
        self.msg.set('等一下！！！！')
        self.root.update()
        try:
            self._V2M_(f, s)
            messagebox.showinfo('OK','去看你的檔案吧')
        except Exception as e:
            messagebox.showerror('FAIL失敗了')
        self.msg.set('目前無任何指令')

    def v2m_batch(self):
        in_dir = filedialog.askdirectory(title = "第一步：選擇待處理影片資料夾")
        if not in_dir:
            return
        out_dir = filedialog.askdirectory(title = "第二步：選擇存哪")
        if not out_dir:
            return
        tar = os.path.join(out_dir, 'yourMP3')
        os.makedirs(tar, exist_ok = True)

        files = [f for f in os.listdir(in_dir) if f.lower().endswith(('.mp4', '.mkv'))]
        if not files:
            messagebox.showwarning('耍我嗎', '資料夾內沒有影片檔（.mp4/.mkv）')
            return
        for idx, name in enumerate(files, 1):
            self.msg.set(f'目前進度{idx}/{len(files)}:{name}')
            self.root.update()
            try:
                self._V2M_(os.path.join(in_dir, name), os.path.join(tar, os.path.splitext(name)[0]+'.mp3'))
            except:continue
        messagebox.showinfo('OK','趕進看看吧')
        self.msg('目前無指令執行')



if  __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()



