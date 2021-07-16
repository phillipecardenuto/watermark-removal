import argparse
import re

from PDFSolvent import *

parser = argparse.ArgumentParser(prog='PDFSolvent', description="Removes 'RETRACTED' watermarks from Academic PDF articles.", formatter_class=argparse.MetavarTypeHelpFormatter)
parser.add_argument("--input_pdf","-i", required=True, type=str ,nargs='?',
                    help="Path to the PDF input.")
parser.add_argument("--output_pdf","-o", type=str ,nargs='?', required=True,
                    help="Path to the output.")
parser.add_argument("--mode", "-m", type=int ,nargs='?', default=2, metavar=("mode"),
                    help=
"""
    Aggresivity Level 1:\n
        All PDF stream resources that explicit contains the information saying that it is a Watermark is removed.\n\n

    Aggresivity Level 2 (DEFAULT MODE):\n
        All Watermarks from 1 and element Graphics that appers more than onces along the PDF pages are removed.\n
        In addition, all 'RETRACTED' words are also removed.\n
        For some PDF this aggresivity level could remove the entire text from a Page.\n\n
                        
    Aggresivity Level 3:\n
        All WM from 1 and 2, and all graphical elements are removed from the PDF.\n
        The only change for the Retraction Watermark not be removed with such level\n
        of aggresivity is the Retraction Watermark embedded as an Image File.\n
        In this case, we will preserve the Watermark, since this funciton is designed to not erase\n
        any image/photo from the PDF.\n
""")

args = vars(parser.parse_args())


def main():
    input_pdf = args['input_pdf']
    output_pdf = args['output_pdf']
    if type(args['mode']) == list:
        mode = args['mode'][0]
    else:
        mode = args['mode']
    remove_watermarks( input_pdf, output_pdf, mode)
    

if __name__ == "__main__":
    main()