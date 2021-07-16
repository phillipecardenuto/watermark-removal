# PDF SOLVENT - A Solvent for PDF RETRACTION Watermarks

Removes 'RETRACTED' watermarks from Academic PDF articles.

This software has three levels of aggressivity; as higher the level more damage it can cause to the final result.
Even for the maximum level of aggressivity, the images/photos embedded in the PDF are still preserved.  



**Aggressivity Level 1:**
    All PDF stream resources that explicitly contain the information saying that it is a Watermark are removed.

**Aggressivity Level 2 (Default):**
    All Watermarks from 1 and element Graphics that appear more than once along the PDF pages are removed.
    In addition, all 'RETRACTED' words are also removed.
    For some PDFs, this aggressivity level could remove the entire text from a Page.

**Aggressivity Level 3:**
    All WM from 1 and 2 and all graphical elements are removed from the PDF.
    The only change for the Retraction Watermark not to be removed with such a level of aggressivity is the Retraction Watermark embedded as an Image File.
    In this case, we will preserve the Watermark since this function is designed not to erase any image/photo from the PDF.



### Quick Start

Environment used to run the project:

- Python >= 3.8
- PyPDF4, PyMuPDF

There is a requirements.txt that can help with the environment.
``` bash
$ pip install -f requirements.txt
```

### Usage

Run Watermark removal
``` bash
$ python PDFSolvent -i <PDF-input> -o <PDF-output> -m [mode of aggressivity] 
```

##### AUTHOR

João Phillipe Cardenuto,

```
				 UNICAMP (University of Campinas) RECOD Lab
```