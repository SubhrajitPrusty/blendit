import sys
from PIL import Image
import click

@click.command()
@click.option("--show", is_flag=True, help="shows images with generated colors")
@click.argument("filename", type=click.Path(exists=True))

def cli(show,filename):
    
    argb,argbi = calculate(filename)
    if show:
        show_images(argb, argbi)

def calculate(imgname):
    img = Image.open(imgname)

    data = list(img.getdata())

    rsum, gsum, bsum = 0,0,0
    pixels = len(data)

    for pixel in data:
        rsum+=pixel[0]
        gsum+=pixel[1]
        bsum+=pixel[2]

    ravg = rsum//pixels
    gavg = gsum//pixels
    bavg = gsum//pixels

    avg_RGB = (ravg,gavg,bavg)
    avg_RGB_hex = '#'+"".join(hex(x)[2:].zfill(2) for x in avg_RGB)
        
    invert_RGB = tuple([255-x for x in avg_RGB])
    invert_RGB_hex = '#'+"".join(hex(x)[2:].zfill(2) for x in invert_RGB)

    print("Blended values")
    print(avg_RGB)
    print(avg_RGB_hex)
        
    print("Inverted values, for color scheme")
    print(invert_RGB)
    print(invert_RGB_hex)

    return (avg_RGB_hex, invert_RGB_hex)

def show_images(rgb1, rgb2):        
    avg_im = Image.new('RGB',(200,200),rgb1)
    avg_im.show()
        
    avgi_im = Image.new('RGB',(200,200),rgb2)
    avgi_im.show()

