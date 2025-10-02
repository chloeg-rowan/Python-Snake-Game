# Simple Snake Project
# Chloe Garvey
# 30 Nov 2024

import pygame as p, random, time
p.init()


def main():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    p.display.set_caption("Chloe's Snake Game!") # That's me!
    clock = p.time.Clock()
    # --- Title screen ---
    imp = p.image.load("titleScreen.png")
    screen.blit(imp, (0,0))
    p.display.flip()

    titleScreen = True
    while titleScreen:
        for event in p.event.get():
            if event.type == p.QUIT:
                titleScreen = False
                p.quit()
                return
            if event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:
                    # Start the game and allow replaying after game over
                    while True:
                        playGame(screen, SCREEN_HEIGHT, SCREEN_WIDTH, clock)

                        # Show end screen image and wait for player input
                        try:
                            end_img = p.image.load("EndScreen.png")
                            screen.blit(end_img, (0, 0))
                        except Exception:
                            # If the image can't be loaded, clear screen to black
                            screen.fill((0, 0, 0))
                        p.display.flip()

                        waiting = True
                        while waiting:
                            for ev in p.event.get():
                                if ev.type == p.QUIT:
                                    p.quit()
                                    return
                                if ev.type == p.KEYDOWN:
                                    if ev.key == p.K_SPACE:
                                        # Replay: break waiting and start a new game
                                        waiting = False
                                        break
                                    elif ev.key == p.K_ESCAPE:
                                        # Exit the program
                                        p.quit()
                                        return
                            clock.tick(10)

                elif event.key == p.K_ESCAPE:
                    titleScreen = False
                    p.quit()
                    return

        clock.tick(15)
    

def playGame(screen, SCREEN_HEIGHT, SCREEN_WIDTH, clock):
    playerX = 300
    playerY = 550
    player = p.Rect(playerX, playerY, 25, 25)
    # Pellet initially spawned offscreen. Immediately moved into bounds when the game starts
    pellet = p.Rect(1000, 1000, 25, 25)

    # Making a bunch of variables that will be used in running the game
    run = True # True so long as the while loop should be running
    newPellet = True # True at the start and whenever a pellet is eaten, instantly set to false after pellet creation
    grew = False # Set true when a pellet is eaten, set back to false afterwards
    score = 0 # Self explanatory, incremented when a pellet is eaten
    snakeLength = 0 # Same as score
    body = [player] # List of body parts
    direction = "UP" # Changes every time a new direction is inputted
    while run:
        lastX = playerX
        lastY = playerY
        p.display.set_caption(f"Chloe's Snake Game! Score: {score}")
        screen.fill((0,0,0))
        # Spawns a new pellet in a random position not currently occupied by the snake.
        if newPellet: 
            searching = True
            while searching:
                searching = False
                pelletX = myround(random.randint(0, SCREEN_WIDTH-25))
                pelletY = myround(random.randint(0, SCREEN_HEIGHT-25))
                for segment in body:
                    if pelletX == segment.x and pelletY == segment.y:
                        searching = True
            pellet.x = pelletX
            pellet.y = pelletY
            newPellet = False
        
        # Moves every snake segment up to the one before it.
        i = len(body)-1
        while i > 0:
            body[i].x = body[i-1].x
            body[i].y = body[i-1].y
            i -= 1

        key = p.key.get_pressed()

        # Checks if there's been a new input. Does not allow 180 degree turns.
        if key[p.K_a] == True and direction != "RIGHT":
            direction = "LEFT"
        elif key[p.K_d] == True and direction != "LEFT":
            direction = "RIGHT"
        elif key[p.K_w] == True and direction != "DOWN":
            direction = "UP"
        elif key[p.K_s] == True and direction != "UP":
            direction = "DOWN"
        
        # Continue moving in the same direction until a new input is detected
        if direction == "LEFT":
            playerX -= 25
            player.x = playerX
            player.y = playerY
            if checkBounds(player, body, playerX, playerY):
                run = False
                break
        elif direction == "RIGHT":
            playerX += 25
            player.x = playerX
            player.y = playerY
            if checkBounds(player, body, playerX, playerY):
                run = False
                break
        elif direction == "UP":
            playerY -= 25
            player.x = playerX
            player.y = playerY
            if checkBounds(player, body, playerX, playerY):
                run = False
                break
        elif direction == "DOWN":
            playerY += 25
            player.x = playerX
            player.y = playerY
            if checkBounds(player, body, playerX, playerY):
                run = False
                break

        # Grows the snake. Makes a new rect at the previous position prior to moving the head.
        if grew:
            newRect = p.Rect(lastX, lastY, 25, 25)
            body.append(newRect)
            grew = False

        # Checks if the snake collides with a pellet. If so, create a new one, increment score, and increase the player's length
        if(pelletX == playerX and pelletY == playerY):
            newPellet = True
            score += 1
            snakeLength += 1
            grew = True

        # Drawing pellet, player head, and each segment.
        p.draw.rect(screen, (0, 255, 0), pellet)
        for segment in body:
            if segment == body[0]:
                p.draw.rect(screen, (255, 100, 0), segment)
            else:
                p.draw.rect(screen, (255, 0, 0), segment)

        # Exits the program
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
        p.display.update()
        clock.tick(15)

# Rounding positions to 25-pixel blocks
def myround(x, base=25):
    return base * round(x/25)

# Checks if the snake has gone out of bounds or touched its body
def checkBounds(player: p.Rect, body: list[p.Rect], playerX: int, playerY: int):
    if 0 > playerX or 775 < playerX or 0 > playerY or 575 < playerY:
        time.sleep(3)
        return True
    else:
        for segment in body:
            if not segment is player and player.x == segment.x and player.y == segment.y:
                time.sleep(3)
                return True
    return False

main()