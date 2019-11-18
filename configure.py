import os

home_path = os.environ.get('HOMEPAHT')
# base_path = os.path.join(home_path, 'SB_Paint')
cur_path = os.path.dirname(__file__)
icon_path = os.path.join(cur_path, 'icons/icon.ico')
home_img = os.path.join(cur_path, 'icons/home_icon.png')
view_img = os.path.join(cur_path, 'icons/view_icon.png')
# conf_path = os.path.join(base_path, 'conf.txt')

root_color = '#525452'
bg_color = '#3c3d3c'