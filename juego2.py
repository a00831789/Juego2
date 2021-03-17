 if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-18, 18) * 10
        food.y = randrange(-18, 18) * 10 
    else:
        snake.pop(0)

    clear()

    for body in snake:

        colors = ['#0092fa', '#2ec742', '#000000', '#c72c79', '#f5814c']

        color = colors[randrange(0, 5)]

        square(body.x, body.y, 9, color)
    

    square(food.x, food.y, 9, color)  
    update()
    ontimer(move, 100)
