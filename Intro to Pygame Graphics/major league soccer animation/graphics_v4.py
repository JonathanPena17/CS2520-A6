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

def draw_cloud(x, y):
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])


# Config
lights_on = True
day = True

stars = []
for n in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 200)
    r = random.randrange(1, 2)
    stars.append([x, y, r, r])

clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0, 150)
    clouds.append([x, y])
    
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_d:
                day = not day

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 
    if lights_on:
        light_color = YELLOW
    else:
        light_color = SILVER

    if day:
        sky_color = BLUE
        field_color = GREEN
        stripe_color = DAY_GREEN
        cloud_color = WHITE
    else:
        sky_color = DARK_BLUE
        field_color = DARK_GREEN
        stripe_color = NIGHT_GREEN
        cloud_color = NIGHT_GRAY

    for c in clouds:
        c[0] -= 0.5

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 150)
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)
    
    if not day:
    #stars
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)
################################################################################################
    
    #This is the field class, which draws the grass field and the stripes.
    class field:
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
        def draw(self):
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
        draw_cloud(c[0], c[1])
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
    #net
    pygame.draw.line(screen, WHITE, [325, 140], [341, 200], 1)
    pygame.draw.line(screen, WHITE, [330, 140], [344, 200], 1)
    pygame.draw.line(screen, WHITE, [335, 140], [347, 200], 1)
    pygame.draw.line(screen, WHITE, [340, 140], [350, 200], 1)
    pygame.draw.line(screen, WHITE, [345, 140], [353, 200], 1)
    pygame.draw.line(screen, WHITE, [350, 140], [356, 200], 1)
    pygame.draw.line(screen, WHITE, [355, 140], [359, 200], 1)
    pygame.draw.line(screen, WHITE, [360, 140], [362, 200], 1)
    pygame.draw.line(screen, WHITE, [364, 140], [365, 200], 1)
    pygame.draw.line(screen, WHITE, [368, 140], [369, 200], 1)
    pygame.draw.line(screen, WHITE, [372, 140], [373, 200], 1)
    pygame.draw.line(screen, WHITE, [376, 140], [377, 200], 1)
    pygame.draw.line(screen, WHITE, [380, 140], [380, 200], 1)
    pygame.draw.line(screen, WHITE, [384, 140], [384, 200], 1)
    pygame.draw.line(screen, WHITE, [388, 140], [388, 200], 1)
    pygame.draw.line(screen, WHITE, [392, 140], [392, 200], 1)
    pygame.draw.line(screen, WHITE, [396, 140], [396, 200], 1)
    pygame.draw.line(screen, WHITE, [400, 140], [400, 200], 1)
    pygame.draw.line(screen, WHITE, [404, 140], [404, 200], 1)
    pygame.draw.line(screen, WHITE, [408, 140], [408, 200], 1)
    pygame.draw.line(screen, WHITE, [412, 140], [412, 200], 1)
    pygame.draw.line(screen, WHITE, [416, 140], [416, 200], 1)
    pygame.draw.line(screen, WHITE, [420, 140], [420, 200], 1)
    pygame.draw.line(screen, WHITE, [424, 140], [423, 200], 1)
    pygame.draw.line(screen, WHITE, [428, 140], [427, 200], 1)
    pygame.draw.line(screen, WHITE, [432, 140], [431, 200], 1)
    pygame.draw.line(screen, WHITE, [436, 140], [435, 200], 1)
    pygame.draw.line(screen, WHITE, [440, 140], [438, 200], 1)
    pygame.draw.line(screen, WHITE, [445, 140], [441, 200], 1)
    pygame.draw.line(screen, WHITE, [450, 140], [444, 200], 1)
    pygame.draw.line(screen, WHITE, [455, 140], [447, 200], 1)
    pygame.draw.line(screen, WHITE, [460, 140], [450, 200], 1)
    pygame.draw.line(screen, WHITE, [465, 140], [453, 200], 1)
    pygame.draw.line(screen, WHITE, [470, 140], [456, 200], 1)
    pygame.draw.line(screen, WHITE, [475, 140], [459, 200], 1)

    #net part 2
    pygame.draw.line(screen, WHITE, [320, 140], [324, 216], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [326, 214], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [328, 212], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [330, 210], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [332, 208], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [334, 206], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [336, 204], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [338, 202], 1)

    #net part 3
    pygame.draw.line(screen, WHITE, [480, 140], [476, 216], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [474, 214], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [472, 212], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [470, 210], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [468, 208], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [466, 206], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [464, 204], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [462, 202], 1)

    #net part 4
    pygame.draw.line(screen, WHITE, [324, 144], [476, 144], 1)
    pygame.draw.line(screen, WHITE, [324, 148], [476, 148], 1)
    pygame.draw.line(screen, WHITE, [324, 152], [476, 152], 1)
    pygame.draw.line(screen, WHITE, [324, 156], [476, 156], 1)
    pygame.draw.line(screen, WHITE, [324, 160], [476, 160], 1)
    pygame.draw.line(screen, WHITE, [324, 164], [476, 164], 1)
    pygame.draw.line(screen, WHITE, [324, 168], [476, 168], 1)
    pygame.draw.line(screen, WHITE, [324, 172], [476, 172], 1)
    pygame.draw.line(screen, WHITE, [324, 176], [476, 176], 1)
    pygame.draw.line(screen, WHITE, [335, 180], [470, 180], 1)
    pygame.draw.line(screen, WHITE, [335, 184], [465, 184], 1)
    pygame.draw.line(screen, WHITE, [335, 188], [465, 188], 1)
    pygame.draw.line(screen, WHITE, [335, 192], [465, 192], 1)
    pygame.draw.line(screen, WHITE, [335, 196], [465, 196], 1)

    #stands right
    pygame.draw.polygon(screen, RED, [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(screen, WHITE, [[680, 180], [800, 100], [800, 290]])

  
    #stands left
    pygame.draw.polygon(screen, RED, [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(screen, WHITE, [[120, 180], [0, 100], [0, 290]])
    #people
    

    #corner flag right
    pygame.draw.line(screen, BRIGHT_YELLOW, [140, 220], [135, 190], 3)
    pygame.draw.polygon(screen, RED, [[132, 190], [125, 196], [135, 205]])

    #corner flag left
    pygame.draw.line(screen, BRIGHT_YELLOW, [660, 220], [665, 190], 3)
    pygame.draw.polygon(screen, RED, [[668, 190], [675, 196], [665, 205]]) 

    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))    
    
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
