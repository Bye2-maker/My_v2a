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
        self.button('單個檔案', self.v2m_single)
        self.button('資料夾檔案', self.v2m_batch)

        self.msg = tk.StringVar(value = '等待指令中！！')
        tk.Label(root, textvariable = self.msg, bg = '#9d9d90', fg = '#666666', wraplength = 350, font = ('Microsoft JhengHei', 9)).pack(pady = 30)


        #公用函式
        def _V2M_(self, inP, outP):
            with VideoFileClip(inP) as video:
                video.audio.write_audiofile(outP, bitrate = '192k', logger = None)

        def v2m_single(self):
            f = filedialog.askopenfilename(filetypes = [('影片','*.mp4','*.mkv')])
            s = filedialog.asksaveasfilename(defaultextension = '.mp3')
            if not f or not s:
                return
            
            self.msg.set('等一下！！！！')
            self.root.update()
            try:
                self._V2M_(f, s)
                messagebox.showinfo('OK','去看你的檔案吧')
            except Exception as e:
                messagebox.showerror('FAIL')
            self.msg.set('目前無任何指令')

        def v2m_batch(self):
            in_dir = filedialog.askdirectory()
            out_dir = filedialog.askdirectory()
            if not in_dir or not out_dir:
                return
            tar = os.path.join(out_dir, 'yourMP3')
            os.makedirs(tar, exist_ok = True)

            files = [f for f in os.listdir(in_dir) if f.lower().endswith(('.mp4', '.mkv'))]
            for idx, name in enumerate(files, 1):
                self.msg.set(f'目前進度{idx}/{len(files)}:{name}')
                self.root.update()
                try:
                    self._V2M_(os.path.join(in_dir, name), os.path.join(tar, os.path.splitext(name)[0]+'.mp3'))
                except:continue
            messagebox.showinfo('OK'，'趕進看看吧')
            self.msg('目前無指令執行')




        def button(self, txt, type):
            tk.Button(self.root, text = txt, command = type, width = 25, bg = '#eeeeee', relief = 'flat', pady = 8, font = ('Microsoft JhengHei', 10)).pack(pady = 10)

if  __name__ == '__main__':
    root = tk.TK()
    app = App(root)
    root.mainloop()



