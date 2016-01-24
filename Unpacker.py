# -*- coding: utf-8 -*-
''' Created on 2015-8-11 @author: wmltogether '''
from LIBU3D4 import unpack_assets
import os
import traceback
def main():
    if not os.path.exists('assets/'):
        print('NO assets folder found,please put .assets into assets folder')
        os.makedirs('assets/')
    fl = os.listdir('assets')
    for fn in fl:
        unpack_assets(fn)
if __name__=='__main__':
    try:
        main()
    except:
        traceback.print_exc()
    os.system('pause')
    os._exit(0)

