# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Major League Soccer"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (52, 166, 36)
BLUE = (29, 116, 248)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
DARK_BLUE = (18, 0, 91)
DARK_GREEN = (0, 94, 0)
GRAY = (130, 130, 130)
YELLOW = (255, 255, 110)
SILVER = (200, 200, 200)
DAY_GREEN = (41, 129, 29)
NIGHT_GREEN = (0, 64, 0)
BRIGHT_YELLOW = (255, 244, 47)
NIGHT_GRAY = (104, 98, 115)
ck = (127, 33, 33)

DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

SEE_THROUGH = pygame.Surface((800, 180))
SEE_THROUGH.set_alpha(150)
SEE_THROUGH.fill((124, 118, 135))

# x and y are the values in which the random range will produce the stars position
def draw_stars(x, y):
    stars = []
    for n in range(200):
        x_pos = random.randrange(0, x)
        y_pos = random.randrange(0, y)
        r_pos = random.randrange(1, 2)
        stars.append([x_pos, y_pos, r_pos, r_pos])

    for s in stars:
         pygame.draw.ellipse(screen, WHITE, s)



def shape_cloud(x, y):
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])


#will shape the clouds using shape_cloud and also place them on the screen
def draw_clouds(x, y):
    clouds = []
    for i in range(20):
        x_pos = random.randrange(-100, x)
        y_pos = random.randrange(0, y)
        clouds.append([x_pos, y]_pos)
    
    for c in clouds:
        shape_cloud(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0))

    for c in clouds:
        c[0] -= 0.5
        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 150)


#changes scene to daytime colors 
def set_day():
    sky_color = BLUE
    field_color = GREEN
    stripe_color = DAY_GREEN
    cloud_color = WHITE

#changes scene to nighttime colors
def set_night():
    sky_color = DARK_BLUE
    field_color = DARK_GREEN
    stripe_color = NIGHT_GREEN
    cloud_color = NIGHT_GRAY

#checks for inputs that would alter the game
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_d:
                day = not day


# Game loop
done = False
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    check_events()

    # Game logic (Check for collisions, update points, etc.)
    if lights_on:
        light_color = YELLOW
    else:
        light_color = SILVER

    if day:
        set_day()
    else:
        set_night()
        draw_stars(800,200)

    draw_clouds(1600, 150)
    
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)

################################################################################################
#This is the field class, which draws the grass field and the stripes.
    class field:
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
        def draw(self):
            field_color = DARK_GREEN
            stripe_color = NIGHT_GREEN
            rect = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(screen, field_color,rect)
            listy = [180,264,368,492]
            listheight = [42,52,62,82]
            for i in range(4):
                pygame.draw.rect(screen, stripe_color, [self.x, listy[i], self.width,listheight[i]])
    #The input are the dimensions of the field
    soccerfield =  field(0,180,800,420)
    soccerfield.draw()

    #This is the fence class, which draws the fence
    class fence:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def draw(self):
            sky_color = BLUE

            for x in range(5, 800, 30):
                pygame.draw.polygon(screen, NIGHT_GRAY, [[x + 2, self.y], [x + 2, self.y + 15], [x, self.y + 15], [x, self.y]])

            for x in range(5, 800, 3):
                pygame.draw.line(screen, NIGHT_GRAY, [x, self.y], [x, self.y + 15], 1)

            for y in range(170, 185, 4):
                pygame.draw.line(screen, NIGHT_GRAY, [self.x, y], [self.x + 800, y], 1)

            if day:
                pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
            else:
                pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40]) 
                pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])
    
    #The inputs the the coordinates of the fence
    newFence = fence(0,170)
    newFence.draw()
    
    #This draws the clouds in the background
    for c in clouds:
        draw_clouds(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0))

    #draw_lines function is used to draw lines
    def draw_lines(start_pos, end_pos, width):
        pygame.draw.line(screen, WHITE, start_pos, end_pos, width)

    #drawing out of bounds lines
    draw_lines([0, 580], [800, 580], 5)
    draw_lines([0, 360], [140, 220], 5)
    draw_lines([140, 220], [660, 220], 3)
    draw_lines([660, 220], [800, 360], 5)
    #drawing 18 yard line goal box
    draw_lines([260, 220], [180, 300], 5)
    draw_lines([180, 300], [620, 300], 3)
    draw_lines([620, 300], [540, 220], 5)
    #drawing 6yard line goal box
    draw_lines([310, 220], [270, 270], 3)
    draw_lines([270, 270], [530, 270], 2)
    draw_lines([530, 270], [490, 220], 3)
 
    # This function draws the safety circle in the center of the field
    def draw_safetyCircle(rect, width):
        pygame.draw.ellipse(screen, WHITE, rect , width)
    
    #Input the desired size the thickness of the safety circle
    draw_safetyCircle([240, 500, 320, 160], 5)

    #This function draws the arc at the top of the goal box
    def draw_semicircle (x, y, width, height, thickness):
        pygame.draw.arc(screen, WHITE, [x, y, width, height], math.pi, 2 * math.pi, thickness)
    
    #Input the desired size of the semi-circle and its thickness
    draw_semicircle(330, 280, 140, 40,5)

    #This is the scoreBoard Class, which is responsible for drawing the score board
    class scoreBoard:
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
        # draw score board
        def draw(self):
            pygame.draw.rect(screen, GRAY, [self.x + 88,self.y + 78,20,70])
            pygame.draw.rect(screen, BLACK, [self.x - 2,self.y - 2,self.width + 2,self.height +2])
            pygame.draw.rect(screen, WHITE, [self.x,self.y,self.width,self.height], 2)
  
    #input the desired dimensions and location for the scoreboard
    scoreBoard1 = scoreBoard(302, 42, 198, 88)
    scoreBoard1.draw()

    #drawing the goal box
    pygame.draw.rect(screen, WHITE, [320, 140, 160, 80], 5)
    draw_lines([340, 200], [460, 200], 3)
    draw_lines([320, 220], [340, 200], 3)
    draw_lines([480, 220], [460, 200], 3)
    draw_lines([320, 140], [340, 200], 3)
    draw_lines([480, 140], [460, 200], 3)

    #This is the lightpole class, which is responsible for drawing the lightpoles
    class lightPole:
        def __init__(self,x,y):
            self.x = x
            self.y = y
        
        def draw(self):
            # Draw pole
            pygame.draw.rect(screen, GRAY, [self.x, self.y, 20, 140])
            pygame.draw.ellipse(screen, GRAY, [self.x, self.y + 135, 20, 10])

            list = [-40,-20,0,20,40]
            list2 = [0,20,40]

            # Draw lights
            for i in range(3):
                  pygame.draw.line(screen, GRAY, [self.x - 40, self.y - list2[i]], [self.x + 60, self.y-list2[i]], 2)
                  for j in range(5):
                    pygame.draw.ellipse(screen, light_color, [self.x + list[j], 20, 20, 20])
                    pygame.draw.ellipse(screen, light_color, [self.x + list[j], 40, 20, 20])
  
    #input the desired coordintates for the light poles
    pole1 = lightPole(150, 60)
    pole1.draw()

    pole2 = lightPole(630,60)
    pole2.draw()
################################################################################################
    #draw net
    
    def drawNet():
        i=int(325)
        j=int(341)
        x=int(0)
        while x < 8:
            pygame.draw.line(screen, WHITE, [i, 140], [j, 200], 1)
            i = i + 5
            j = j + 3
            x = x + 1
        i=int(364)
        j=int(364)
        x=int(0)
        while x < 19:
            pygame.draw.line(screen, WHITE, [i, 140], [j, 200], 1)
            i = i + 4
            j = j + 4
            x = x + 1
        pygame.draw.line(screen, WHITE, [440, 140], [438, 200], 1)
        x=int(0)
        i=int(440)
        j=int(438)
        while x < 7:
            i = i + 5
            j = j + 3
            pygame.draw.line(screen, WHITE, [i, 140], [j, 200], 1)
            x = x + 1
        #net part 2
        i=int(324)
        j=int(216)
        x=int(0)
        for x in range(0,9):
            pygame.draw.line(screen, WHITE, [320, 140], [i, j], 1)
            i = i + 2
            j = j - 2
        x=int(0)
        #net part 3
        i=int(476)
        j=int(216)
        for x in range(0,9):
            pygame.draw.line(screen, WHITE, [480, 140], [i, j], 1)
            i = i - 2
            j = j - 2
        x=int(0)
        #net part 4
        i=int(144)
        j=int(144)
        x=int(0)
        for x in range(0,10):
            pygame.draw.line(screen, WHITE, [324, i], [476, j], 1)
            i = i + 4
            j = j + 4
        pygame.draw.line(screen, WHITE, [335, 180], [470, 180], 1)
        i=int(180)
        j=int(470)
        x=int(0)
        for x in range(0,5):
            pygame.draw.line(screen, WHITE, [335, i], [465, i], 1)
            i = i + 4
            j = j + 4
    drawNet()
    def drawStands(color1,color2):
        #stands right
        pygame.draw.polygon(screen, color1, [[680, 220], [800, 340], [800, 290], [680, 180]])
        pygame.draw.polygon(screen, color2, [[680, 180], [800, 100], [800, 290]])

      
        #stands left
        pygame.draw.polygon(screen, color1, [[120, 220], [0, 340], [0, 290], [120, 180]])
        pygame.draw.polygon(screen, color2, [[120, 180], [0, 100], [0, 290]])
    drawStands(RED,WHITE)
    
    
    def drawFlags(color1,color2):
        #corner flag right
        pygame.draw.line(screen, color1, [140, 220], [135, 190], 3)
        pygame.draw.polygon(screen, color2, [[132, 190], [125, 196], [135, 205]])

        #corner flag left
        pygame.draw.line(screen, color1, [660, 220], [665, 190], 3)
        pygame.draw.polygon(screen, color2, [[668, 190], [675, 196], [665, 205]]) 
    drawFlags(BRIGHT_YELLOW, RED)
    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))    
    
    pygame.display.flip()

    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()
