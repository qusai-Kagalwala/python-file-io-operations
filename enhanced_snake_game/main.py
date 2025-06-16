# =============================================================================
# Snake Game - Main Entry Point
# Classic Snake game with persistent high score tracking
# Controls: Arrow keys for movement, collision detection with walls/tail/food
# =============================================================================
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# =============================================================================
# SETUP GAME SCREEN
# =============================================================================
screen = Screen()
screen.setup(width=600, height=600)  # 600x600 pixel game window
screen.bgcolor("black")  # Black background for classic look
screen.title("My Snake Game")  # Window title
screen.tracer(0)  # Turn off automatic screen updates for smooth animation

# =============================================================================
# INSTANTIATE GAME OBJECTS
# =============================================================================
snake = Snake()  # Create snake object (starts with 3 segments)
food = Food()  # Create food object (blue circle, random position)
scoreboard = Scoreboard()  # Create scoreboard (tracks current score + high score)

# =============================================================================
# KEYBINDINGS - SNAKE MOVEMENT CONTROLS
# =============================================================================
screen.listen()  # Enable screen to listen for key presses
screen.onkey(snake.up, "Up")  # Up arrow moves snake up
screen.onkey(snake.down, "Down")  # Down arrow moves snake down
screen.onkey(snake.left, "Left")  # Left arrow moves snake left
screen.onkey(snake.right, "Right")  # Right arrow moves snake right

# =============================================================================
# MAIN GAME LOOP
# =============================================================================
game_is_on = True
while game_is_on:
    screen.update()  # Manually update screen (since tracer is off)
    time.sleep(0.1)  # Control game speed - pause for 0.1 seconds
    snake.move()  # Move snake forward one step

    # =============================================================================
    # COLLISION DETECTION - FOOD
    # =============================================================================
    # Check if snake head touches food (within 15 pixels)
    if snake.head.distance(food) < 15:
        food.refresh()  # Move food to new random position
        snake.extend()  # Add new segment to snake (grow)
        scoreboard.increase_score()  # Increment score by 1

    # =============================================================================
    # COLLISION DETECTION - WALLS
    # =============================================================================
    # Check if snake hits any of the four walls (boundaries at ±280)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()  # Update high score if needed, reset current score
        snake.reset()  # Reset snake to starting position and size

    # =============================================================================
    # COLLISION DETECTION - SNAKE TAIL
    # =============================================================================
    # Check if snake head collides with any part of its own body
    for segment in snake.segments:
        if segment == snake.head:  # Skip the head itself
            pass
        elif snake.head.distance(segment) < 10:  # Collision detected
            scoreboard.reset()  # Update high score if needed, reset current score
            snake.reset()  # Reset snake to starting position and size

# =============================================================================
# GAME EXIT
# =============================================================================
# Click screen to exit game when game loop ends
screen.exitonclick()