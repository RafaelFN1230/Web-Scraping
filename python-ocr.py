# Importando o módulo Pillow (Manipulação de Imagens) para abrir a imagem no script
from importlib.resources import path
from PIL import Image
# Módulo para a utilização da tecnologia OCR
import pytesseract

im = Image.open('CaptchaImage.jfif')
im.save('CaptchaImage.jpg')
#"C:\Users\rafae\Desktop\PROGRAMAÇÃO\PHYTON\projeto\CaptchaImage.jfif"
# Caminho do tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Extraindo o texto da imagem
print( pytesseract.image_to_string( Image.open('CaptchaImage.jpg'), lang='por') )

