## Reduce the lag with caching

In order to reduce the lag, you'll need to use a technique called caching. This means you record a value the first time you look it up, and refer to the saved value when you need it the next time, rather than look it up again. To do this, you're going to use a dictionary to store the known blocks. That way, you can look up a set of coordinates in the `known_blocks` dictionary, and only use `mc.getBlock()` if you need to. This will save lots of time and make your lookup run much faster.

- First, create an empty dictionary called `known_blocks` before your `get_blocks` function:

    ```python
    known_blocks = {}
    ```

- You'll need to access the `known_blocks` dictionary from within your `get_blocks` function. Python will let you read a variable you declared outside the function, but not write to it. In order to write to it, you'll need to make it a **global** within the function like so:

    ```python
    def get_blocks():
        global known_blocks
    ```
    Global means you're changing the scope of the variable from being read-only to read/write.

- Inside the function, modify the loop to look like this:

    ```python
    for dz in range(z-3, z+5):
        for dx in range(x-3, x+5):
            b = (dx, y, dz)
            if b in known_blocks:
                block = known_blocks[b]
            else:
                block = mc.getBlock(dx, y, dz)
                known_blocks[b] = block
            blocks.append(block)
    ```

    **What does it do?**

    - `b = (dx, y, dz)`: create a 3-tuple of the current coordinates.
    - `if b in known_blocks`: check if the block has already been looked up.
    - `block = known_blocks[b]`: look up the block by its coordinates.
    - `known_blocks[b] = block`: once a block is looked up for the first time, add it to the `known_blocks` dictionary.

- Run the code and walk around. You should see it's a lot quicker at printing the blocks list out. Try reducing the `sleep` down to `0.1` and see if it can still cope.

