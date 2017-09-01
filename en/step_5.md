## Minecraft Sense HAT Colour Walk

Now you've explored the Minecraft world and seen the different block IDs that are printed out as you walk around, you're going to learn to make the Sense HAT show a different colour depending on what type of block you're standing on in the Minecraft world!

- You're going need a way to create a mapping from a block ID to a colour; for example, grass should map to green, so block ID `2` should map to the colour code `(0, 255, 0)`.

- You can achieve this mapping using a Python dictionary.

[[[generic-python-basic-dictionaries]]]

- Now create a dictionary linking block ids to colours

--- hints --- --- hint ---
You know that a block with an id of `2` is grass, and so should be linked to the colour green, which is `(0, 255, 0)`
--- /hint --- --- hint ---
Here's how that would look in a dictionary. You just need to add more colours.
```python
colours = {
	2:(0, 255, 0)
	}
```
--- /hint --- --- hint ---
Here's a slightly fuller dictionary you could use.
```python
colours = {
	2: (0, 255, 0),
    1: (50, 50, 50),
    3: (135, 89, 51),
    7: (51, 23, 0),
    9: (0, 195, 255),
    12: (229, 255, 0),
    46: (255, 0, 0),
    49: (0, 0, 0)
	}
```
--- /hint --- --- /hints ---

- Start by adding some variables to identify block IDs. Add the following code above your `while` loop like so:

    ```python
    # blocks
    grass = 2
    water = 9
    sand = 12
    ```

- The first line is a comment helping explain what that bit of code is for. These variables are all integers (whole numbers) because that's what block IDs are represented by.

- Below that, add some more colours that represent these block types:

    ```python
    # colours
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    ```

- Next you need to create a dictionary that can map blocktypes to colours.

    ```python
    # block: colour
    colours = {
        grass: green,
        water: blue,
        sand: yellow,
    }
    ```
    A dictionary is a data type used for storing relations between two objects, like an address book mapping a name to a telephone number. The items in the dictionary are referred to as key-value pairs, so in an address book the name is the "key" and the phone number is the "value". In our case the block type is the "key" and the colour is the "value".

- Now all that's left to do is to look up the block you're standing on, see which colour it should be, and use `sense.clear` to change the colour of the Sense HAT display accordingly!

    To look up a value in a dictionary, you pass in the key. If the dictionary was an address book, you'd pass in the name and be given that person's phone number. So to look up the block type `grass` you'd use `colours[2]` or `colours[grass]` and you'd get back the value for green which is `(0, 255, 0)`.

    Modify your `while` loop to look like this:

    ```python
    while True:
        x, y, z = mc.player.getTilePos()
        block = mc.getBlock(x, y-1, z)
        colour = colours[block]
        print(colour)
        sleep(0.1)
    ```
    Here we're looking up the ID of the block the player is standing on, as before, and then looking that up in the `colours` dictionary, then printing out the colour code tuple.

- Save and run the code, and walk around the Minecraft world.

    You should see the colour code of the block you're standing on. Walk around to see different colour codes. When you walk on grass you should see `(0, 255, 0)`, when you're on sand you should see `(255, 255, 0)`, and on water, `(0, 0, 255)`.

- If you walk over a block that isn't in the dictionary, you'll get an error message. If you haven't found another block type yet, just jump in the air using the space bar, and you'll get this error:

    ![Dictionary KeyError](images/dictionary-keyerror.png)

    This error is a `KeyError`, which is a Python exception meaning you tried to look up the value of a key which isn't in the dictionary, like trying to get the telephone number of a name you haven't got recorded.

- First of all, let's deal with the `KeyError`. Modify your colour lookup like so:

    ```python
    if block in colours:
        colour = colours[block]
        print(colour)
    else:
        print("Don't know block ID %s" % block)
    sleep(0.1)
    ```

    Now it will check to see if the key is in the dictionary before looking up its value. If it's not, it will tell you which block ID it was.

- Finally, now you have a colour value representing the block type your player is standing on, you can tell the Sense HAT to show that colour on the LED display, simply by changing the `print(colour)` line to:

    ```python
    sense.clear(colour)
    ```

- Save and run the code, and walk around the Minecraft world and your Sense HAT should show green, blue or yellow when you walk on grass, water and sand.

- Now add more blocks and colours to your dictionary!

**Download a copy of [minecraft_colour.py](resources/minecraft_colour.py)**

