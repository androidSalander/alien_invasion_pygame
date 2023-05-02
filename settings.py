class Settings:
    """a class to store all settings for Alien Invasion"""
    def __init__(self):
        """initialize the game's settings"""
        # screen settings
        self.screen_width = 1800
        self.screen_height = 1400
        self.bg_color = (77, 0, 153)

        # ship settings
        self.ship_speed = 3.5

        # bullet settings
        self.bullet_speed = 3.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (102, 255, 178)
        self.bullets_allowed = 5

