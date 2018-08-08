class Setting():
    def __init__(self):
        self.screen_width=500
        self.screen_height=800
        self.bg_color=(230,230,230)

        self.ship_speed=.5
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=6


        self.alien_loacl=[[10,10],[90,34],[170,10],[250,34],[360,20]]
        self.alien_speed_factor = .1

        self.ship_limit=3

        self.alien_points=10