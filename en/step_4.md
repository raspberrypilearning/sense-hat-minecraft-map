## Exploring the Minecraft world

Now you've had a go at setting the colours of the Sense HAT LED matrix, let's open up Minecraft and have a look around to see what block types you can identify.

- Open Minecraft from the application menu, under **Games**:

    ![Open Minecraft](images/minecraft-app-menu.png)

- Click **Start Game** and then either create a new world or enter an existing world.

- Press the `Tab` key to regain access to the mouse cursor and then move the Minecraft window to one side of your screen.

- Return to the Python windows. Open another new window from the Python shell and save it as `minecraft-colours.py` in the same project folder.

- Move this window so that it is on the other side of the screen, and you can see the Python window and the Minecraft window side by side.

- Enter the following code to get started:

    ```python
    from sense_hat import SenseHat
    from mcpi.minecraft import Minecraft
    from time import sleep

    sense = SenseHat()
    mc = Minecraft.create()

    mc.postToChat("Hello Minecraft!")
    sense.clear(0, 255, 0)
    ```

- Save and run your code!

    You should see the text "Hello Minecraft" appear in the Minecraft window and the Sense HAT should turn green!

- Now you've created a connection to both the Sense HAT and the Minecraft world, let's look at how you can determine what type of block you're standing on. Remove the `postToChat` and `sense.clear` lines and add the following code:

    ```python
    while True:
        x, y, z = mc.player.getTilePos()
        block = mc.getBlock(x, y-1, z)
        print(block)
        sleep(0.1)
    ```

- Save and run the code.

    You should now see numbers being constantly printed to the Python shell. These numbers represent the IDs of the block your player is standing on. Walk around over different terrain and you'll see the number change. Note that you use the WASD keys to walk around, and the space bar to jump or fly

    **How does it work?**

    - `while True`: this is an infinite loop.
    - `x, y, z = mc.player.getTilePos()`: this gets the coordinates of where your player is standing and sets them to variables `x`, `y` and `z`.
    - `block = mc.getBlock(x, y-1, z)`: this looks up the ID of the block directly beneath the player (`y-1` means one below the player's `y` coordinate, which is the vertical axis).
    - `print(block)`: this shows us which block ID was returned by `getBlock`.
    - `sleep(0.1)`: this pauses for a tenth of a second each time the loop runs, so it's not printing out too fast.

- You need to know the block types that are represented by the IDs you're seeing. Some common ones are:

    ```
    Air:   0
    Stone: 1
    Grass: 2
    Dirt:  3
    Water: 8
    Sand: 12
    Ice:  79
    ```

    See which block types you can identify while walking around the Minecraft world.

