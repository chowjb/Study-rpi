import board
import terminalio
import displayio
from adafruit_ssd1306 import SSD1306_I2C
from adafruit_st7735r import ST7735R
from adafruit_display_text import label
from PIL import Image, ImageDraw, ImageFont

class StatusDisplayer:
    """ Displays the status of the prototype """
    def __init__(self, displayNum):
        self.displayNum = displayNum
        
        if displayNum == 1:
            # Define the Reset Pin
            # Can set to None because this OLED has auto-reset circuitry
            #oled_reset = digitalio.DigitalInOut(board.D4)
            oled_reset = None

            # Change these
            # to the right size for your display!
            self.WIDTH = 128
            self.HEIGHT = 32  # Change to 64 if needed
            self.BORDER = 5

            # Use for I2C.
            i2c = board.I2C()
            self.oled = SSD1306_I2C(self.WIDTH, self.HEIGHT, i2c, addr=0x3C, reset=oled_reset)
        elif displayNum == 2:
            # Release any resources currently in use for the displays
            displayio.release_displays()

            spi = board.SPI()

            tft_cs = board.CE0
            tft_dc = board.D25
            reset_pin = board.D24

            display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, 
                                            reset=reset_pin)

            self.display = ST7735R(display_bus, width=128, height=160, colstart=0, rowstart=0)
        else:
            print("Displayer number must be: 1 = OLED_128x32_SSD1306, 2 = TFT_128x160_ST07735r")
            exit()
                   
    def show(self, statusText):
        if self.displayNum == 1:
            # Clear display.
            self.oled.fill(0)
            self.oled.show()

            # Create blank image for drawing.
            # Make sure to create image with mode '1' for 1-bit color.
            image = Image.new("1", (self.oled.width, self.oled.height))

            # Get drawing object to draw on image.
            draw = ImageDraw.Draw(image)

            # Draw a white background
            draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=255, fill=255)

            # Draw a smaller inner rectangle
            draw.rectangle(
                (self.BORDER, self.BORDER, self.oled.width - self.BORDER - 1, self.oled.height - self.BORDER - 1),
                outline=0,
                fill=0,)

            # Load default font.
            font = ImageFont.load_default()

            # Draw Some Text
            (font_width, font_height) = font.getsize(statusText)
            draw.text(
                (self.oled.width // 2 - font_width // 2, self.oled.height // 2 - font_height // 2),
                statusText, font=font, fill=255,)

            # Display image
            self.oled.image(image)
            self.oled.show()
            
        elif self.displayNum == 2:
            # Make the display context
            splash = displayio.Group(max_size=30) # max_size doesn't work. Need to change in Group.py
            self.display.show(splash)
            #display.show(None)

            color_bitmap = displayio.Bitmap(128, 160, 1)
            color_palette = displayio.Palette(1)
            color_palette[0] = 0xAAFF00  # Bright Green

            bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
            splash.append(bg_sprite)

            # Draw a smaller inner rectangle
            inner_bitmap = displayio.Bitmap(108, 140, 1)
            inner_palette = displayio.Palette(1)
            inner_palette[0] = 0xAA0088  # Purple
            inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=10, y=10)
            splash.append(inner_sprite)

            print('test test')

            # Draw a label
            text_area = label.Label(terminalio.FONT, text=statusText, color=0xFFFF00, x=30, y=64)
            splash.append(text_area)

            # *** Key call to make it work on RPi0
            self.display.refresh()
            
        else:
            raise Exception("Displayer number must be: 1 = OLED_128x32_SSD1306, 2 = TFT_128x160_ST07735r")