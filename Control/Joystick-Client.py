import pygame
from time import sleep
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname('raspberrypi')
port = 10013
address = (ip, port)
client.connect(address)

TreverseState = 0

def communicate(data):
    client.send(Edata.encode())
    #reply = client.recv(1024)
    #print(reply.decode())
    return


# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

# Set the width and height of the screen [width,height]
size = [200, 100]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Aircraft Controls")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# Get ready to print
textPrint = TextPrint()

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")


    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count) )
    textPrint.indent()

    # For each joystick:

    joystick = pygame.joystick.Joystick(1)
    joystick.init()


    #for i in range( axes ):
    axis = joystick.get_axis( 2 )
    textPrint.print(screen, "Axis {} value: {:>6.3f}".format(1, axis) )
    value = (axis + 1) * 50
    value = int(value)
    value = (value * -1) + 100
    value = str(value)
    Edata = 'Engine-' + value
    Edata = Edata.ljust(64)
    communicate(value)
    Evalue = "Engine Power: " + value
    textPrint.print(screen, Evalue)
    TreverseButton = joystick.get_button (0)
    textPrint.print(screen, str(TreverseState))
    if TreverseButton != TreverseState:
        TreverseState = TreverseButton
        TreverseMsg = "Reverse-Toggle"
        TreverseMsg = TreverseMsg.ljust(64)
        communicate(TreverseMsg)




        #textPrint.unindent()







    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(1)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
