import argparse
import re

from PDFSolvent import *

parser = argparse.ArgumentParser(prog='PDFSolvent', description="Removes 'RETRACTED' watermarks from Academic PDF articles..", formatter_class=argparse.MetavarTypeHelpFormatter)
parser.add_argument("--input_pdf","-i", required=True, type=str ,nargs='?',
                    help="Path to the PDF input.")
parser.add_argument("--output_pdf","-o", type=str ,nargs='?', required=True,
                    help="Path to the output.")
parser.add_argument("--mode", "-m", type=int ,nargs='?', default=2, metavar=("mode"),
                    help=
"""
    This program has three levels of aggressivity; as higher the level more damage it can cause to the final result.
    Even though, even for the maximum level of aggressivity, the images/photos embedded in the PDF are preserved.  

    Aggressivity Level 1:
        All PDF stream resources that explicitly contain the information saying that it is a Watermark are removed.

    Aggressivity Level 2:
        All Watermarks from 1 and element Graphics that appear more than once along the PDF pages are removed.
        In addition, all 'RETRACTED' words are also removed.
        For some PDFs, this aggressivity level could remove the entire text from a Page.

    Aggressivity Level 3:
        All WM from 1 and 2 and all graphical elements are removed from the PDF.
        The only change for the Retraction Watermark not to be removed with such a level of aggressivity is the Retraction Watermark embedded as an Image File.
        In this case, we will preserve the Watermark since this function is designed not to erase any image/photo from the PDF.
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