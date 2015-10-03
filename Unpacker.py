# -*- coding: utf-8 -*-
''' Created on 2015-8-11 @author: wmltogether '''
from LIBU3D5 import unpack_assets
import os
import traceback
import logging 
import logging.handlers 
def main():
    LOG_FILE = 'Unity_TOOL_DEBUG.log'
    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*2048, backupCount = 5)
    fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger = logging.getLogger('Unity Output')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    if not os.path.exists('assets/'):
        print('NO assets folder found,please put .assets into assets folder')
        os.makedirs('assets/')
    fl = os.listdir('assets')
    for fn in fl:
        unpack_assets(fn , logger)
if __name__=='__main__':
    if os.path.exists("Unity_TOOL_DEBUG.log"):os.remove("Unity_TOOL_DEBUG.log")
    try:
        main()
    except:
        traceback.print_exc()
    os.system('pause')
    os._exit(0)
