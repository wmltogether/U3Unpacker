# -*- coding: utf-8 -*-
from LIBU3D4 import pack_assets
import os
def main():
    if not os.path.exists('assets/'):
        os.makedirs('assets/')
    fl = os.listdir('assets')
    for fn in fl:
        pack_assets(fn)
    os.system('pause')
if __name__=='__main__':
    try:
        main()
    except:
        traceback.print_exc()
    os.system('pause')
    os._exit(0)

