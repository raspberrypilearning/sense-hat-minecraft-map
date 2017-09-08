## Create a mini map

Now you have the Sense HAT showing the colour of the block you're standing on, you can use the same logic to show a different colour for each block around you to make a mini map of the Minecraft world on the LED display.

In order to make an 8x8 map, you'll need to retrieve the block IDs for all blocks immediately surrounding your player - enough to fill the 8x8 display. The Minecraft API does have an `mc.getBlocks()` function, but unfortunately it doesn't actually work, so you'll have to write your own function.

+ Open up the `minecraft-map.py` file you were working on earlier.

+ Underneath the import code, define a function called `get_blocks()`

[[[generic-python-simple-functions]]]

The function will eventually look up the block the player is standing on and find the block IDs of enough of the surrounding blocks to fill the LED matrix.

Let's start simple and look up the player's position and the 3 blocks to the right of the player, to return a list of four block IDs:

![First get_blocks loop](images/first-get-blocks-loop.png)

+ Inside your function, create an empty list called `blocks`. This is where we will store the blocks we find.

[[[generic-python-create-list]]]

+ Add a line of code to find the player's `x`, `y`, `z` coordinates, just like you did before.

+ Subtract one from the `y` coordinate. This is so that we are looking at the layer of blocks _beneath_ the player.

+ Still inside the function, add a `for` loop which runs in the range `x` to `x + 4`. This means that the first block looked at will be the one immediately underneath the player, and the loop will stop looking at blocks when it gets to the block 4 spaces away from the player.

```python
for new_x in range(x, x+4):
```

+ Inside the loop, find the block ID of the block at the position `new_x`, and `append` it to the blocks list.

+ Finally, after your `for` loop, return the data from the `blocks` list

--- hints ---


--- /hints ---


- `for dx in range(x, x+4):`: use `x` values from the player to 3 blocks away from the player.
- `block = mc.getBlock(dx, y, z)`: look up the block at this location.
- `blocks.append(block)`: add this block to the list.
- `return blocks`: by the time the program gets to this line, this contains 4 blocks as it's been through the loop 4 times.

- Add a line to the end of your code to print out the result of the `get_blocks` function:

    ```python
    print(get_blocks())
    ```

- Run the code and you should see a list of four numbers (block IDs), which will be the block you are standing on and the three blocks to the side of you (the direction depends on which way you're facing).

- Now you'll want to make the function do the same for a 2-dimensional space. This version loops over `x` and `z` 4 times and returns 16 values:

    ```python
    def get_blocks():
        blocks = []
        x, y, z = mc.player.getTilePos()
        y -= 1
        for dz in range(z, z+4):
            for dx in range(x, x+4):
                block = mc.getBlock(dx, y, dz)
                blocks.append(block)
        return blocks
    ```

    **What does it do?**

    - `blocks = []`: creates a new empty list.
    - `x, y, z = mc.player.getTilePos()`: get the player's position.
    - `y -= 1`: subtract one from the `y` coordinate to look at the level below the player.
    - `for dz in range(z, z+4):`: use `z` values from the player to 3 blocks away from the player (4 rows in total).
    - `for dx in range(x, x+4):`: use `x` values from the player to 3 blocks away from the player (4 columns in total).
    - `block = mc.getBlock(dx, y, dz)`: look up the block at this location.
    - `blocks.append(block)`: add this block to the list.
    - `return blocks`: by the time the program gets to this line, this contains 16 blocks as it's been through each loop 4 times.

- Run the code and you should see a list of 16 block IDs, starting with the block you're standing on and the 7 to the side of you, followed by each row of 8 blocks away from you.

- Now you'll want to make it loop over 8 rows and 8 columns, and make sure it looks to the left and right, and both behind and ahead of you. This version loops over `x` and `z` 8 times and returns 64 values:

    ```python
    def get_blocks():
        blocks = []
        x, y, z = mc.player.getTilePos()
        y -= 1
        for dz in range(z-3, z+5):
            for dx in range(x-3, x+5):
                block = mc.getBlock(dx, y, dz)
                blocks.append(block)
        return blocks
    ```

    **What does it do?**

    - `for dz in range(z-3, z+5):`: use `z` values from 3 behind the player up to 5 ahead (8 rows in total).
    - `for dx in range(x-3, x+5):`: use `x` values from 3 left of the player over to 5 to the right (8 columns in total).
    - `return blocks` - by the time the program gets to this line, this contains 64 blocks as it's been through each loop 8 times.

- Run the code and you should see a list of 64 block IDs. This time they should be the 8x8 grid of blocks surrounding your player, with you in the middle (there's no centre point of an 8x8 grid so you're just off-centre):

    ![Third get_blocks loop](images/third-get-blocks-loop.png)

- Next, add a `while` loop to print the result of `get_blocks` every second:

    ```python
    while True:
        print(get_blocks())
        sleep(1)
    ```

- Run the code and see it update as you walk around.

    You will probably find that it's a bit laggy: it takes a small amount of time to retrieve each block ID, and you're trying to do 64 every second.
