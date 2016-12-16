import sys
import traceback
import os
import LibUnity


def main():
    print("Unity Assets Unpacker")
    if not os.path.exists('assets/'):
        print('NO assets folder found,please put .assets into assets folder')
        os.makedirs('assets/')
    fl = os.listdir('assets')
    for fn in fl:
        if (os.path.isfile("assets/%s" % fn)):
            if ("level" in fn or ".assets" in fn):
                assetsReader = LibUnity.AssetsLoader("assets/%s" % fn)
                assetsReader.Pack("assets/%s_unpacked" % fn)

if __name__ == '__main__':
    try:
        main()
    except:
        traceback.print_exc()
