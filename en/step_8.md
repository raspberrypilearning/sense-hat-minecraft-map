## Reduce the lag with caching

In order to reduce the lag, you'll need to use a technique called caching. This means you record a value the first time you look it up, and refer to the saved value when you need it the next time, rather than look it up again. To do this, you're going to use a dictionary to store the known blocks. That way, you can look up a set of coordinates in the `known_blocks` dictionary, and only use `mc.getBlock()` if you need to. This will save lots of time and make your lookup run much faster.

- First, create an empty dictionary called `known_blocks` before your `get_blocks` function:

    ```python
    known_blocks = {}
    ```
- Now you need some code that will see if a block is in the dictionary. If it is in there, then there's no need to use the Minecraft API to look it up.

- Try and alter your `get_blocks` function so that it does the following.
  1. create a new tuple containing the `dx`, `y` and `dz` coordinates within the nested `for` loops.
  1. Check if the tuple is inside the `known_blocks` dictionary.
  1. **If** it is, then set `block` to that value in the dictionary.
  1. **Else** you'll need to use `getBlock` to set the block, and then add it to the dictionary.
  
--- hints --- --- hint ---
Start by creating the tuple.
```python
for dz in range(z-3, z+5):
	for dx in range(x-3, x+5):
		b = (dx, y, dz)
```
--- /hint --- --- hint ---
Now check if that tupple is in the dictionary, and if it is, use the value as the `block` id
```python
for dz in range(z-3, z+5):
	for dx in range(x-3, x+5):
		b = (dx, y, dz)
		if b in known_blocks:
			block = known_blocks[b]
```
--- /hint --- --- hint ---
If it's not in the dictionary, then you need to find the block id and then the coordinate `key` to the block id `value`
```python
for dz in range(z-3, z+5):
	for dx in range(x-3, x+5):
		b = (dx, y, dz)
		if b in known_blocks:
			block = known_blocks[b]
		else:
			block = mc.getBlock(dx, y, dz)
			known_blocks[b] = block
```
--- /hint --- --- /hints ---

- Run the code and walk around. You should see it's a lot quicker at printing the blocks list out. Try reducing the `sleep` down to `0.1` and see if it can still cope.
  
