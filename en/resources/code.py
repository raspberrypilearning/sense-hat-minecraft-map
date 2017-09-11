from sense_hat import SenseHat
import mcpi.minecraft as minecraft
from time import sleep

sense = SenseHat()
mc = minecraft.Minecraft.create()

grass = 2
water = 9
sand = 12

green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)

colours = {
    grass: green,
    water: blue,
    sand: yellow,
    }

known_blocks = {}

def get_blocks():
    global known_blocks
    blocks = []
    x, y, z = mc.player.getTilePos()
    y -= 1
    for dz in range(z-3, z+5):
        for dx in range(x-3, x+5):
            b = (dx, y, dz)
            if b in known_blocks:
                block = known_blocks[b]
            else:
                block = mc.getBlock(dx, y, dz)
                known_blocks[b] = block
            blocks.append(block)
    return blocks

def map_blocks_to_colours(blocks):
    pixels = []
    for block in blocks:
        if block in colours:
            pixels.append(colours[block])
        else:
            pixels.append(white)
    return pixels

def map_blocks_to_colours(blocks):
    return [colours[block] if block in colours else white for block in blocks]

while True:
    blocks = get_blocks()
    pixels = map_blocks_to_colours(blocks)
    pixels[27] = [0,0,0]
    sense.set_pixels(pixels)
