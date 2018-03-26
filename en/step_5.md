## Display the block colour

Let's make the Sense HAT show a different colour depending on what type of block you're standing on in the Minecraft world!

You're going need a way to associate a block ID with a colour; for example, grass is mostly green, so the grass block ID `2` should map to the green colour code `(0, 255, 0)`.

This is called **mapping** and you can achieve this using a special data structure called a dictionary.

+ Choose some block types and add some variables so that you can store the corresponding block ID. You can choose whichever blocks you like.

Add your block variables above your `while` loop:

```python
grass = 2
water = 9
sand = 12
```
--- collapse ---
---
title: Minecraft block IDs
---
Choose some blocks to represent. Here is a list of some of the block types, but don't copy and paste from here as they are not in the format you need!
```
AIR                 = Block(0)
STONE               = Block(1)
GRASS               = Block(2)
DIRT                = Block(3)
COBBLESTONE         = Block(4)
WOOD_PLANKS         = Block(5)
SAPLING             = Block(6)
BEDROCK             = Block(7)
WATER               = Block(8)
WATER_STATIONARY    = Block(9)
LAVA                = Block(10)
LAVA_STATIONARY     = Block(11)
SAND                = Block(12)
GRAVEL              = Block(13)
GOLD_ORE            = Block(14)
IRON_ORE            = Block(15)
COAL_ORE            = Block(16)
WOOD                = Block(17)
LEAVES              = Block(18)
GLASS               = Block(20)
LAPIS_LAZULI_ORE    = Block(21)
LAPIS_LAZULI_BLOCK  = Block(22)
SANDSTONE           = Block(24)
BED                 = Block(26)
COBWEB              = Block(30)
GRASS_TALL          = Block(31)
WOOL                = Block(35)
FLOWER_YELLOW       = Block(37)
FLOWER_CYAN         = Block(38)
MUSHROOM_BROWN      = Block(39)
MUSHROOM_RED        = Block(40)
GOLD_BLOCK          = Block(41)
IRON_BLOCK          = Block(42)
STONE_SLAB_DOUBLE   = Block(43)
STONE_SLAB          = Block(44)
BRICK_BLOCK         = Block(45)
TNT                 = Block(46)
BOOKSHELF           = Block(47)
MOSS_STONE          = Block(48)
OBSIDIAN            = Block(49)
TORCH               = Block(50)
FIRE                = Block(51)
STAIRS_WOOD         = Block(53)
CHEST               = Block(54)
DIAMOND_ORE         = Block(56)
DIAMOND_BLOCK       = Block(57)
CRAFTING_TABLE      = Block(58)
FARMLAND            = Block(60)
FURNACE_INACTIVE    = Block(61)
FURNACE_ACTIVE      = Block(62)
DOOR_WOOD           = Block(64)
LADDER              = Block(65)
STAIRS_COBBLESTONE  = Block(67)
DOOR_IRON           = Block(71)
REDSTONE_ORE        = Block(73)
SNOW                = Block(78)
ICE                 = Block(79)
SNOW_BLOCK          = Block(80)
CACTUS              = Block(81)
CLAY                = Block(82)
SUGAR_CANE          = Block(83)
FENCE               = Block(85)
GLOWSTONE_BLOCK     = Block(89)
BEDROCK_INVISIBLE   = Block(95)
STONE_BRICK         = Block(98)
GLASS_PANE          = Block(102)
MELON               = Block(103)
FENCE_GATE          = Block(107)
GLOWING_OBSIDIAN    = Block(246)
NETHER_REACTOR_CORE = Block(247)
```
--- /collapse ---

+ Below that, add some variables containing colours which could represent these block types:

```python
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
```

+ Now create a dictionary called `colours` which links some block IDs to colours. Start by adding the grass example from above, and then choose some other blocks to add.

[[[generic-python-basic-dictionaries]]]

--- hints --- --- hint ---
You know that a block with an id of `2` is grass, and so should be linked to the colour green, which is `(0, 255, 0)`
--- /hint --- --- hint ---
Here's how that would look in a dictionary. Now you can add more blocks and their associated colours - but don't forget to define the variables for the blocks and the colours before you add them to your dictionary!
```python
colours = {
    grass: green,
    water: blue,
    sand: yellow
	}
```
--- /hint --- --- /hints ---

+ Inside your `while` loop, add a line of code at the end to look up the block ID the player is standing on in the dictionary.

```python
standing_on = colours[block_id]
```

To look up a value in a dictionary, you provide the key. If the dictionary was a phone book, you'd provide the name and be given that person's phone number. So to look up the block type `grass` you'd use `colours[grass]` and you'd get back the value for green which is `(0, 255, 0)`.

+ Now you know which colour this block should be, use `sense.clear` to display that colour on the Sense HAT LED matrix.

+ Add a `sleep` for 0.1 seconds after displaying the colour so you get a chance to see it before the next colour is displayed.

[[[generic-python-sleep]]]

+ Save and run your code, then walk around the Minecraft world. You should see the colour of the block you're standing on displayed on the Sense HAT.

You'l notice that if you walk over a block that isn't in the dictionary or fall off a ledge, you'll get an error message.

![Dictionary KeyError](images/dictionary-keyerror.png)

This `KeyError` means you tried to look up the value of a key which isn't in the dictionary. Or, in other words, you stood on a block that you hadn't defined a colour for. (Even air counts as a block, so you'll also see this message if you jump!)

- Add an `if` statement to check whether the block ID of the block you are standing on is in the `colours` dictionary. If it is, look up the corresponding colour and display it on the Sense HAT. If not, print a message saying that you don't know which block that is.

--- hints ---
--- hint ---
First, make sure you've imported the `sleep` function using:
```python
from time import sleep
```

**If** the **block_id** is **in** the **colours** dictionary:
-- **Look up** the colour
-- **Display** the colour on the Sense HAT LED matrix
**Else**
-- **Print** I don't know which block that is
--- /hint ---

--- hint ---
You can check whether a block_id is in the colours dictionary like this:

```python
if block_id in colours:
```
--- /hint ---
--- hint ---
Here is how your code should look:

```python
if block_id in colours:
    standing_on = colours[block_id]
    sense.clear(standing_on)
else:
    print("I don't know which block that is")
sleep(0.1)
```
--- /hint ---
--- /hints ---

+ Save and run the code, and walk around the Minecraft world. Your Sense HAT should show green, blue or yellow when you walk on grass, water and sand.
