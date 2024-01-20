import pygame
import random
from time import sleep


'''
when i press x, if player one score and player two score are both above 10, a sound will play when i press x. 
if only either player one xcore or player two score is above 10, a different sound will play when i press x.Else, no sound will play.
press q, w, s, a to change player score. press r to reset player score. press space to exit program.
'''


WIDTH = 500
HEIGHT = 300
r =255
g = 255
b = 255
color = r, g, b
BACKGROUND = (r, g, b)

class Scoreboard:
    def __init__(self, p1, p2) :
        global r, g, b
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.font1 = pygame.font.Font('freesansbold.ttf', 120)

        # Scoreboard
        self.label = "Scoreboard"
        self.TextLabel = self.font.render(str(self.label), True, (0, 0, 0), (r, g, b))
        self.TextRect = self.TextLabel.get_rect(center=(WIDTH//2, 45))  

        # Player 1
        self.playerOneLabel = "Player 1"
        self.playerOneTextLabel = self.font.render(str(self.playerOneLabel), True, (0, 0, 0), (r, g, b))
        self.playerOneTextRect = self.playerOneTextLabel.get_rect(center=(100, 125))
        self.playerOneScore = p1
        self.playerOneScoreText = self.font.render(str(self.playerOneScore), True, (0, 0, 0), (r, g, b))           
        self.playerOneScoreRect = self.playerOneScoreText.get_rect(center=(100, 225))

        # LINE
        self.dividerLabel = "|"
        self.dividerTextLabel = self.font1.render(str(self.dividerLabel), True, (0, 0, 0), (r, g, b))
        self.dividerTextLabelRect = self.dividerTextLabel.get_rect(center=(WIDTH//2, HEIGHT//2))
        
        # Player 2
        self.playerTwoLabel = "Player 2"
        self.playerTwoTextLabel = self.font.render(str(self.playerTwoLabel), True, (0, 0, 0), (r, g, b))
        self.playerTwoTextRect = self.playerTwoTextLabel.get_rect(center=(WIDTH-100,125))
        self.playerTwoScore = p2
        self.playerTwoScoreText = self.font.render(str(self.playerTwoScore), True, (0, 0, 0), (r, g, b))   
        self.playerTwoScoreRect = self.playerTwoScoreText.get_rect(center=(WIDTH-100, 225))

def main():
    global r, g, b, BACKGROUND
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    Player1 = 0
    Player2 = 0
    state = 0

    run = True
    sound1 = pygame.mixer.Sound('sm64_happy_message.wav')
    sound2 = pygame.mixer.Sound('sm64_here_we_go.wav')
    delta = 5
    while run:
        screen.fill(BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and state == 0:
                if event.key == pygame.K_a:
                    if Player1 < 20:
                        Player1 += 1
                elif event.key == pygame.K_s:
                    if Player2 < 20:
                        Player2 += 1
                elif event.key == pygame.K_q:
                    if Player1 != 0:
                        Player1 -= 1
                elif event.key == pygame.K_w:
                    if Player2 != 0:
                        Player2 -= 1
                elif event.key == pygame.K_r:
                    Player1 = 0
                    Player2 = 0
                elif event.key == pygame.K_SPACE:
                    run = False
                elif event.key == pygame.K_u:
                    r += delta
                    if r > 255:
                        r = 255
                elif event.key == pygame.K_j:
                    r -= delta
                    if r < 0:
                        r = 0
                elif event.key == pygame.K_i:
                    g += delta
                    if g > 255:
                        g = 255
                elif event.key == pygame.K_k:
                    g -= delta
                    if g < 0:
                        g = 0
                elif event.key == pygame.K_o:
                    b += delta
                    if b > 255:
                        b = 255
                elif event.key == pygame.K_l:
                    b -= delta
                    if b < 0:
                        b = 0
                elif event.key == pygame.K_x:
                    if screen1.playerOneScore >= 10 and screen1.playerTwoScore >= 10:
                        sound2.play()
                    elif screen1.playerOneScore >= 10 or screen1.playerTwoScore >= 10:
                        sound1.play()
        color = r, g, b
        BACKGROUND = r, g, b
        if state == 0:
            screen1 = Scoreboard(Player1, Player2)
            screen.blit(screen1.TextLabel, screen1.TextRect)
            screen.blit(screen1.playerOneTextLabel, screen1.playerOneTextRect)
            screen.blit(screen1.playerOneScoreText, screen1.playerOneScoreRect)
            screen.blit(screen1.dividerTextLabel, screen1.dividerTextLabelRect)
            screen.blit(screen1.playerTwoTextLabel, screen1.playerTwoTextRect)
            screen.blit(screen1.playerTwoScoreText, screen1.playerTwoScoreRect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()