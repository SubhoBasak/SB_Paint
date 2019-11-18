import os
import tkinter as tk
import tkinter.ttk as ttk
import tkfontchooser

import configure as cnf

class App:
    def __init__(self, master):
        self.old_x = None
        self.old_y = None

        self.master = master
        self.master.grid()
        self.master.title('SB Paint')
        self.master.iconbitmap(cnf.icon_path)
        self.master.minsize(600, 400)
        self.master.config(bg = cnf.root_color, padx = 3, pady = 3)

        self.main_menu = tk.Menu(self.master, tearoff = False)
        self.master.config(menu = self.main_menu)

        self.file_menu = tk.Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = 'File', menu = self.file_menu)
        self.file_menu.add_command(label = 'New', command = None, accelerator = 'Ctrl+N')
        self.file_menu.add_command(label = 'Open', command = None, accelerator = 'Ctrl+O')
        self.file_menu.add_command(label = 'Save', command = None, accelerator = 'Ctrl+S', state = tk.DISABLED)
        self.file_menu.add_command(label = 'Save as', command = None, accelerator = 'Ctrl+Shift+S', state = tk.DISABLED)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = 'Quit', command = self.main_menu.quit)

        self.edit_menu = tk.Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = 'Edit', menu = self.edit_menu)
        self.edit_menu.add_command(label = 'Undo', command = None, accelerator = 'Ctrl+Z', state = tk.DISABLED)
        self.edit_menu.add_command(label = 'Redo', command = None, accelerator = 'Ctrl+Shift+Z', state = tk.DISABLED)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label = 'Copy', command = None, accelerator = 'Ctrl+C', state = tk.DISABLED)
        self.edit_menu.add_command(label = 'Cut', command = None, accelerator = 'Ctrl+X', state = tk.DISABLED)
        self.edit_menu.add_command(label = 'Paste', command = None, accelerator = 'Ctrl+V')
        self.edit_menu.add_command(label = 'Delete', command = None, accelerator = 'Ctrl+D', state = tk.DISABLED)

        self.ttk_style = ttk.Style()
        self.ttk_style.configure('My.TFrame', background = cnf.bg_color)
        self.ttk_style.configure('My.Notebook.Tab', background = cnf.bg_color)

        self.notebook = ttk.Notebook(self.master, style = 'My.Notebook.Tab')
        self.notebook.pack(fill = tk.X, side = tk.TOP)

        self.tool_frame1 = ttk.Frame(self.notebook, style = 'My.TFrame')
        self.tool_frame1.pack(fill = tk.BOTH, expand = True)

        self.tool_frame2 = ttk.Frame(self.notebook, style = 'My.TFrame')
        self.tool_frame2.pack(fill = tk.BOTH, expand=True)

        self.home_image = tk.PhotoImage(file = cnf.home_img)
        self.view_image = tk.PhotoImage(file = cnf.view_img)

        self.notebook.add(self.tool_frame1, text = 'Home', image = self.home_image, compound = tk.LEFT)
        self.notebook.add(self.tool_frame2, text = 'View', image = self.view_image, compound = tk.LEFT)

        self.cnv_frame = tk.Frame(self.master, bg = cnf.root_color)
        self.cnv_frame.pack(side = tk.LEFT, anchor = 'n')

        self.canvas = tk.Canvas(self.cnv_frame, bg = cnf.bg_color, scrollregion = (0, 0, 1000, 1000))
        self.canvas.config(scrollregion = self.canvas.bbox('all'))

        self.xscroll = tk.Scrollbar(self.cnv_frame, orient = tk.HORIZONTAL)
        self.xscroll.pack(side = tk.BOTTOM, fill = tk.X)
        self.xscroll.config(command = self.canvas.xview)
        self.canvas.config(xscrollcommand = self.xscroll.set)

        self.yscroll = tk.Scrollbar(self.cnv_frame, orient = tk.VERTICAL)
        self.yscroll.config(command = self.canvas.yview)
        self.yscroll.pack(side = tk.RIGHT, fill = tk.Y)
        self.canvas.config(yscrollcommand = self.yscroll.set)

        self.canvas.pack(side = tk.LEFT, fill = tk.BOTH)

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def paint(self, event):
        xx, _ = self.xscroll.get()
        yy, _ = self.yscroll.get()
        xx *= 1000
        yy *= 1000
        if self.old_x and self.old_y:
            self.canvas.create_line(xx+self.old_x, yy+self.old_y, xx+event.x, yy+event.y)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()