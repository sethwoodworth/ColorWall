import random
import time

class Effect(object):
    def __init__(self, wall):
        self.wall = wall
        self.wall.clear()

    def run(self):
        pass

class SolidColorTest(Effect):
    def run(self):
        hue = 1
        saturation = 1
        value = 1

        hsv = (hue, saturation, value)
        for x in range(self.wall.width):
            for y in range(self.wall.height):
                self.wall.set_pixel(x, y, hsv)

        self.wall.draw()
        time.sleep(2)

class HueTest(Effect):
    def run(self):
        hue = random.random()
        start_time = time.time()
        while time.time() - start_time < 5:
            hsv = (hue, 1, 1)
            for x in range(self.wall.width):
                for y in range(self.wall.height):
                    self.wall.set_pixel(x, y, hsv)
            self.wall.draw()
            hue = (hue + .01) % 1
            time.sleep(.05)

class SaturationTest(Effect):
    def run(self):
        hue = random.random()
        saturation = 0
        start_time = time.time()
        while time.time() - start_time < 5:
            hsv = (hue, saturation, 1)
            for x in range(self.wall.width):
                for y in range(self.wall.height):
                    self.wall.set_pixel(x, y, hsv)
            self.wall.draw()
            saturation = (saturation + .05) % 1
            time.sleep(.05)

class ValueTest(Effect):
    def run(self):
        hue = random.random()
        value = 0
        start_time = time.time()
        while time.time() - start_time < 5:
            hsv = (hue, 1, value)
            for x in range(self.wall.width):
                for y in range(self.wall.height):
                    self.wall.set_pixel(x, y, hsv)
            self.wall.draw()
            value = (value + .05) % 1
            time.sleep(.05)

Effects = [SolidColorTest, HueTest, SaturationTest, ValueTest]
