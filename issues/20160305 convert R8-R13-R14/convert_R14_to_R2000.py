import glob
import os

import ezdxf

R14_DIR = r"D:\Source\dxftest\R14_test_files"


def convert_dxf_file(dxfin, dxfout):
    print("Opening %s" % dxfin)
    dwg = ezdxf.readfile(dxfin)
    dwg.saveas(dxfout)
    print("Ready.")


def main():
    for filename in glob.glob(os.path.join(R14_DIR, '*.dxf')):
        folder, name = os.path.split(filename)
        convert_dxf_file(filename, os.path.join(R14_DIR, 'converted_to_R2000', name))


if __name__ == '__main__':
    main()
