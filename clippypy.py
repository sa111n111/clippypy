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

        draw.text((12,12), text=wrapped_text, fill='rgb(0,0,0)', font=font)
        # Save generated image.
        print(f"image saved: {self.output_name}.jpg")
        image.save(fp=f"{self.output_name}.jpg")



def main():
    if __name__ == '__main__':
        while True:
            i = input("Enter the text you'd like for clippy to say: \n> ")

            j = input("Enter the output file name (Note: You do not need to put the file extension)\n(Note: If you would like to exit, simply hit CTRL+C)>")
            c = Clippy(f'''{i}''', j)

            if len(i) == 0:
                print( "Nothing provided, exiting..." )
                break

            c.generate_clippy()
    

main()
