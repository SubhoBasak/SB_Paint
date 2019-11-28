import os

home_path = os.environ.get('HOMEPATH')
# base_path = os.path.join(home_path, 'SB_Paint')
# conf_path = os.path.join(base_path, 'conf.txt')
cur_path = os.path.dirname(__file__)

icon_path = os.path.join(cur_path, 'icons/icon.ico')
home_img = os.path.join(cur_path, 'icons/home_icon.png')
view_img = os.path.join(cur_path, 'icons/view_icon.png')
pencil_img = os.path.join(cur_path, 'icons/pencil.png')
eraser_img = os.path.join(cur_path, 'icons/eraser.png')
brush_img = os.path.join(cur_path, 'icons/brush.png')
color_img = os.path.join(cur_path, 'icons/color.png')
text_img = os.path.join(cur_path, 'icons/text.png')
rounder_img = os.path.join(cur_path, 'icons/rounder.png')

root_color = '#b3bab9'
bg_color = '#cce8e3'