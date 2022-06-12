import pygame, sys, time, random

pygame.init()

play_surface = pygame.display.set_mode((500, 500))

font = pygame.font.Font(None, 30)

fps = pygame.time.Clock()


def food():
    random_pos = random.randint(0,49)*10
    food_pos = [random_pos, random_pos]
    return food_pos


def main():

    snake_pos = [100, 50]
    snake_body = [[100,50],[90,50],[80,50]]
    change = "RIGHT"
    run = True
    food_pos = food()
    score = 0

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = "RIGHT"
                if event.key == pygame.K_LEFT:
                    change = "LEFT"
                if event.key == pygame.K_UP:
                    change = "UP"
                if event.key == pygame.K_DOWN:
                    change = "DOWN"
        if change == "RIGHT":
            snake_pos[0] += 10
        if change == "LEFT":
            snake_pos[0] -= 10
        if change == "UP":
            snake_pos[1] -= 10
        if change == "DOWN":
            snake_pos[1] += 10

        snake_body.insert(0, list(snake_pos))

        if snake_pos == food_pos:
            food_pos = food()
            score += 1
            print(score)
        else:
            snake_body.pop()
        
        head = snake_body[-1]
        for i in range(len(snake_body) - 1): 
            part = snake_body[i]
            if head[0] == part[0] and head[1] == part[1]:
                run = False
                print("YOU LOSE")

        play_surface.fill((0,0,0))

        for pos in snake_body:
            pygame.draw.rect(play_surface,(200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(play_surface,(169,6,6), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        
        text = font.render(str(score),0,(200,60,80))
        play_surface.blit(text, (480,20))

        if score < 10:
            fps.tick(10)
        if score >= 10:
            fps.tick(20)

        if snake_pos[0] <= 0 or snake_pos[0] >= 500:
            run = False
            print("YOU LOSE")
        if snake_pos[1] <= 0 or snake_pos[1] >= 500:
            run = False
            print("YOU LOSE")

        pygame.display.flip()

main()

pygame.quit()
