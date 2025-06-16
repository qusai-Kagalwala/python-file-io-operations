# =============================================================================
# Food Class - Manages Food Object for Snake Game
# Creates blue circular food that appears at random positions
# Inherits from Turtle class for easy positioning and display
# =============================================================================
from turtle import Turtle
import random


# =============================================================================
# FOOD CLASS DEFINITION
# =============================================================================
class Food(Turtle):
    """
    Food object that snake can eat to grow and increase score
    Appears as small blue circle at random positions within game boundaries
    """

    def __init__(self):
        """
        Initialise food object with visual properties and random position
        Inherits from Turtle class for built-in graphics capabilities
        """
        super().__init__()  # Initialise parent Turtle class

        # =============================================================================
        # FOOD VISUAL PROPERTIES
        # =============================================================================
        self.shape("circle")  # Use circular shape for food
        self.penup()  # Don't draw lines when moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make smaller than default
        self.color("blue")  # Blue colour for contrast against black background
        self.speed("fastest")  # Fastest speed for instant position changes

        # =============================================================================
        # INITIAL FOOD PLACEMENT
        # =============================================================================
        self.refresh()  # Place food at random position when created

    def refresh(self):
        """
        Move food to new random position within game boundaries
        Called when snake eats food or during initialisation
        Boundaries: -280 to 280 (leaves 20px border from 600px screen)
        """
        # Generate random coordinates within playable area
        random_x = random.randint(-280, 280)  # Random X coordinate
        random_y = random.randint(-280, 280)  # Random Y coordinate

        # Move food to new random position instantly
        self.goto(random_x, random_y)