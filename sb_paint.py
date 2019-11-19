import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import colorchooser
from tkinter.font import Font
from PIL import Image, ImageTk
import tkfontchooser

import configure as cnf

class App:
    def __init__(self, master):
        self.activebutton = 'pen'
        self.width = tk.IntVar()
        self.font = ('Arial', 10, 'normal', 'roman', 0, 0)

        self.old_x = None
        self.old_y = None

        self.cnv_w = 900
        self.cnv_h = 550

        self.color_1 = 'black'
        self.color_2 =  'white'

        self.p_width = None
        self.b_widht = None
        self.e_width = None

        self.master = master
        self.master.grid()
        self.master.title('SB Paint')
        self.master.iconbitmap(cnf.icon_path)
        self.master.minsize(600, 400)
        self.master.geometry('1000x700+50+50')
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
        self.file_menu.add_command(label = 'Quit', command = self.close_programme)

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

        self.drawing_tools = ttk.LabelFrame(self.tool_frame1, text = 'Tools', style = 'My.TFrame')
        self.drawing_tools.grid(row = 0, column = 0, sticky = 'nw')

        self.pencil_icon = tk.PhotoImage(file=cnf.pencil_img)
        self.eraser_icon = tk.PhotoImage(file=cnf.eraser_img)
        self.brush_icon = tk.PhotoImage(file=cnf.brush_img)

        self.pencil_button = ttk.Button(self.drawing_tools, image = self.pencil_icon, command = self.use_pen)
        self.pencil_button.grid(row = 0, column = 0)

        self.brush_button = ttk.Button(self.drawing_tools, image = self.brush_icon, command = self.use_brush)
        self.brush_button.grid(row = 0, column = 1)

        self.eraser_button = ttk.Button(self.drawing_tools, image = self.eraser_icon, command = self.use_eraser)
        self.eraser_button.grid(row = 0, column = 2)

        self.tool_frame2 = ttk.Frame(self.notebook, style = 'My.TFrame')
        self.tool_frame2.pack(fill = tk.BOTH, expand=True)

        self.colors = ttk.LabelFrame(self.tool_frame1, text = 'Colors', style = 'My.TFrame')
        self.colors.grid(row = 0, column = 1, sticky = 'nw')

        self.color1 = tk.Label(self.colors, bg = self.color_1, width = 5, height = 2, borderwidth = 1, relief = 'ridge')
        self.color1.grid(row = 0, column = 0)

        self.color2 = tk.Label(self.colors, bg = self.color_2, width = 5, height = 2, borderwidth = 1, relief = 'ridge')
        self.color2.grid(row = 0, column = 1)

        self.color_pallet = ttk.LabelFrame(self.tool_frame1, text = 'Color pallet', style = 'My.TFrame')
        self.color_pallet.grid(row = 0, column = 2)

        self.color_red = tk.Button(self.color_pallet, bg = 'red', command = self.change_red, relief = 'flat', width = 2, height = 1)
        self.color_red.grid(row = 0, column = 0)

        self.color_orange = tk.Button(self.color_pallet, bg='orange', command = self.change_orange, relief='flat', width=2, height=1)
        self.color_orange.grid(row = 0, column = 1)

        self.color_yellow = tk.Button(self.color_pallet, bg='yellow', command = self.change_yellow, relief='flat', width=2, height=1)
        self.color_yellow.grid(row = 0, column = 2)

        self.color_lgreen = tk.Button(self.color_pallet, bg='lightgreen', command = self.change_lgreen, relief='flat', width=2, height=1)
        self.color_lgreen.grid(row = 0, column = 3)

        self.color_green = tk.Button(self.color_pallet, bg='green', command = self.change_green, relief='flat', width=2, height=1)
        self.color_green.grid(row = 0, column = 4)

        self.color_lblue = tk.Button(self.color_pallet, bg='lightblue', command = self.change_lblue, relief='flat', width=2, height=1)
        self.color_lblue.grid(row = 1, column = 0)

        self.color_cyan = tk.Button(self.color_pallet, bg='cyan', command = self.change_cyan, relief='flat', width=2, height=1)
        self.color_cyan.grid(row=1, column=1)

        self.color_blue = tk.Button(self.color_pallet, bg='blue', command = self.change_blue, relief='flat', width=2, height=1)
        self.color_blue.grid(row=1, column=2)

        self.color_magenta = tk.Button(self.color_pallet, bg='magenta', command = self.change_magenta, relief='flat', width=2, height=1)
        self.color_magenta.grid(row=1, column=3)

        self.color_pink = tk.Button(self.color_pallet, bg='pink', command = self.change_pink, relief='flat', width=2, height=1)
        self.color_pink.grid(row=1, column=4)

        self.edit_color = ttk.LabelFrame(self.tool_frame1, text = 'Color', style = 'My.TFrame')
        self.edit_color.grid(row = 0, column = 3, sticky = 'nw')

        self.edit_color_icon = tk.PhotoImage(file = cnf.color_img)

        self.edit_color_button = ttk.Button(self.edit_color, text = 'Choose', image = self.edit_color_icon, compound = tk.TOP,
                                            command = self.change_color_1, width = 7)
        self.edit_color_button.pack(fill = tk.BOTH, expand = True)

        self.bg_color = ttk.LabelFrame(self.tool_frame1, text = 'Canvas')
        self.bg_color.grid(row = 0, column = 4)

        self.bg_color_edit = ttk.Button(self.bg_color, text = 'Choose', image = self.edit_color_icon, compound = tk.TOP, width = 7,
                                        command = self.change_color_2)
        self.bg_color_edit.pack(fill = tk.BOTH, expand = True)

        self.width_frame = ttk.LabelFrame(self.tool_frame1, text = 'Line width', style = 'My.TFrame')
        self.width_frame.grid(row = 0, column = 6, padx = 10, sticky = 'nw')

        self.width_label = ttk.Label(self.width_frame, textvariable = self.width)
        self.width_label.pack()

        self.width_slider = ttk.Scale(self.width_frame, from_ = 1, to = 20, orient = tk.HORIZONTAL, command = lambda v: self.width.set(float(str(v)[:2])))
        self.width_slider.set(3)
        self.width_slider.pack()

        self.text_frame = ttk.LabelFrame(self.tool_frame1, text = 'Add Text')
        self.text_frame.grid(row = 0, column = 7)

        self.text_icon = tk.PhotoImage(file = cnf.text_img)

        self.word_art = ttk.Button(self.text_frame, text = 'Text', image = self.text_icon,compound = tk.TOP, command = self.add_text)
        self.word_art.pack()

        self.home_image = tk.PhotoImage(file = cnf.home_img)
        self.view_image = tk.PhotoImage(file = cnf.view_img)

        self.notebook.add(self.tool_frame1, text = 'Home', image = self.home_image, compound = tk.LEFT)
        self.notebook.add(self.tool_frame2, text = 'View', image = self.view_image, compound = tk.LEFT)

        self.cnv_frame = tk.Frame(self.master, bg = cnf.root_color)
        self.cnv_frame.pack(side = tk.LEFT, anchor = 'n', fill = tk.BOTH, expand = True)

        self.canvas = tk.Canvas(self.cnv_frame, bg = 'white', width = self.cnv_w, height = self.cnv_h,
                                scrollregion = (0, 0, self.cnv_w, self.cnv_h))

        self.xscroll = ttk.Scrollbar(self.cnv_frame, orient = tk.HORIZONTAL)
        self.xscroll.pack(side = tk.BOTTOM, fill = tk.X)
        self.xscroll.config(command = self.canvas.xview)
        self.canvas.config(xscrollcommand = self.xscroll.set)

        self.yscroll = ttk.Scrollbar(self.cnv_frame, orient = tk.VERTICAL)
        self.yscroll.config(command = self.canvas.yview)
        self.yscroll.pack(side = tk.RIGHT, fill = tk.Y)
        self.canvas.config(yscrollcommand = self.yscroll.set)

        self.canvas.pack(side = tk.LEFT, anchor = 'n')

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        self.master.protocol('WM_DELETE_WINDOW', self.close_programme)

    def use_pen(self):
        self.activebutton = 'pen'

    def use_brush(self):
        self.activebutton = 'brush'

    def use_eraser(self):
        self.activebutton = 'eraser'

    def paint(self, event):
        xx, _ = self.xscroll.get()
        yy, _ = self.yscroll.get()

        xx = self.cnv_w*xx
        yy = self.cnv_h*yy

        if self.activebutton == 'pen':
            tmp_fill = self.color_1
        elif self.activebutton == 'brush':
            tmp_fill = self.color_1
        else:
            tmp_fill = self.color_2

        if self.old_x and self.old_y:
            self.canvas.create_line(xx+self.old_x, yy+self.old_y, xx+event.x, yy+event.y, fill = tmp_fill, width = self.width.get())
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def close_programme(self):
        inp = messagebox.askquestion('Quit', 'Do you really want to quit?')
        if inp == 'yes':
            self.master.quit()

    def change_color_1(self):
        color = colorchooser.askcolor()
        if color[1] != None:
            self.color_1 = color[1]
            self.color1.config(bg = color[1])

    def change_color_2(self):
        color = colorchooser.askcolor()
        if color[1] != None:
            self.color_2 = color[1]
            self.canvas.config(bg = color[1])
            self.color2.config(bg = color[1])

    def change_red(self):
        self.color1.config(bg = 'red')
        self.color_1 = 'red'

    def change_orange(self):
        self.color1.config(bg = 'orange')
        self.color_1 = 'orange'

    def change_yellow(self):
        self.color1.config(bg = 'yellow')
        self.color_1 = 'yellow'

    def change_green(self):
        self.color1.config(bg = 'green')
        self.color_1 = 'green'

    def change_lgreen(self):
        self.color1.config(bg = 'lightgreen')
        self.color_1 = 'lightgreen'

    def change_lblue(self):
        self.color1.config(bg = 'lightblue')
        self.color_1 = 'lightblue'

    def change_cyan(self):
        self.color1.config(bg = 'cyan')
        self.color_1 = 'cyan'

    def change_blue(self):
        self.color1.config(bg = 'blue')
        self.color_1 = 'blue'

    def change_magenta(self):
        self.color1.config(bg = 'magenta')
        self.color_1 = 'magenta'

    def change_pink(self):
        self.color1.config(bg = 'pink')
        self.color_1 = 'pink'

    def add_text(self):
        self.top = tk.Toplevel()
        self.top.config(bg = cnf.bg_color)
        self.top.geometry('640x240+100+100')

        self.entry = tk.Entry(self.top, font = ('Arial', 24), width = 30)
        self.entry.pack(pady = 50)

        self.button_frame = tk.Frame(self.top, bg = cnf.bg_color)
        self.button_frame.pack()

        self.choose_font = tk.Button(self.button_frame, text = 'Font', font = ('Arial', 18), command = self.get_font, relief = 'flat')
        self.choose_font.grid(row = 0, column = 0, padx = 50)

        self.submit = tk.Button(self.button_frame, text = 'Add', font = ('Arial', 18), relief = 'flat', command = self.insert)
        self.submit.grid(row = 0, column = 1, padx = 50)

        self.cancel = tk.Button(self.button_frame, text = 'Cancel', font = ('Arial', 18), relief = 'flat', command = self.top.destroy)
        self.cancel.grid(row = 0, column = 3, padx = 50)

    def get_font(self):
        font = tkfontchooser.askfont()
        if font != '':
            self.font = list(font.values())

    def insert(self):
        self.txt = self.entry.get()
        if len(self.txt) > 0:
            self.top.destroy()
            messagebox.showinfo('Add text',
'''Please set the mouse pointer from where
you want to start the text, and then left
click on the mouse to insert or right click
for cancel''')
            self.canvas.bind('<Button-1>', self.insert__)
            self.canvas.bind('<Button-3>', self.cancel__)

    def insert__(self, event):
        font__ = Font(family = self.font[0], size = self.font[1], weight = self.font[2], slant = self.font[3], underline = self.font[4], overstrike = self.font[5])
        self.canvas.create_text(event.x, event.y, text = self.txt, font = font__)

    def cancel__(self, event):
        self.canvas.unbind('<Button-1>')
        self.canvas.unbind('<Button-3>')

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()