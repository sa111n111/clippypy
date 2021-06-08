#            _ __            _   
#           | /_ |          | |  
#  ___  __ _| || | ___ _ __ | |_ 
# / __|/ _` | || |/ _ \ '_ \| __|
# \__ \ (_| | || |  __/ | | | |_ 
# |___/\__,_|_||_|\___|_| |_|\__|

import os
import textwrap
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Clippy():
    def __init__(self, text : str = None, output_name : str = None) -> None:
        self.text = text
        self.output_name = output_name
            
        
    def generate_clippy(self) -> None:
        ''' Generate a clippy image with your desired text '''
        if self.text == None:
            # what's even the point
            return
        width = 46
        wrapped_text = textwrap.fill(self.text, width)
        image = Image.open(r'assets/clippy.jpg')
        font = ImageFont.truetype("assets/comicsans.ttf")
        draw = ImageDraw.Draw(image)

        draw.text((12,12), text=wrapped_text, fill='rgb(0,0,0)', font=font          )
        # Save generated image.
        print(f"image saved: {self.output_name}.jpg")
        image.save(fp=f"{self.output_name}.jpg")



def main():
    if __name__ == '__main__':
        i = input("Enter the text you'd like for clippy to say: \n> ")
        if len(i) == 0:
            print( "Nothing provided, exiting..." )
        j = input("Enter the output file name (Note: You do not need to put the file extension)\n>")
        
        c = Clippy(f'''{i}''', j)
        c.generate_clippy()
    

main()
