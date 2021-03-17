    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-20, 20) * 10
        food.y = randrange(-20, 20) * 10
    else:
        snake.pop(0)
