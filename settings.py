class Screen_set:
    def __init__(self, width, length, bg_color):
        self.width = width
        self.length = length
        self.bg_color = bg_color


class Bullet_set:
    def __init__(self, speed, width, height, color):
        self.speed = speed
        self.width = width
        self.height = height
        self.color = color
        self.allowed = 3


class Settings:
    def __init__(self):
        self.screen = Screen_set(600, 450, (230, 230, 230))
        self.bullet = Bullet_set(0.5, 3, 15, (60, 60, 60))
        self.ship_speed = 0.6
