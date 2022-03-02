import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
fold_main = os.path.join(BASE_DIR, 'my_project')
lst_fold = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(fold_main):
    os.mkdir(fold_main)
    for el in lst_fold:
        el = os.path.join(fold_main, el)
        os.mkdir(el)