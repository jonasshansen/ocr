import pytesseract
import sys
import argparse
try:
    import Image
except ImportError:
    from PIL import Image
from subprocess import check_output
#from spellchecker import SpellChecker

def resolve(path):
	print("Resampling the Image")
	check_output(['convert', path, '-resample', '600', path])
	return pytesseract.image_to_string(Image.open(path))

#def spellcheck(word):
#	spell = SpellChecker()
#	misspelled = spell.unknown(word)
#	return spell.correction(word)

if __name__=="__main__":
	argparser = argparse.ArgumentParser()
	argparser.add_argument('path',help = 'Captcha file path')
	args = argparser.parse_args()
	path = args.path
	print('Resolving Captcha')
	captcha_text = resolve(path)
print('Extracted Text',captcha_text)
