# =============================================================================
# Snake Class - Handles Snake Creation, Movement, and Direction Control
# Manages snake segments, growth, reset functionality, and movement logic
# =============================================================================
from turtle import Turtle

# =============================================================================
# CONSTANTS - SNAKE CONFIGURATION
# =============================================================================
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial 3-segment positions
MOVE_DISTANCE = 20  # Pixels to move per step (matches segment size)
UP = 90  # Turtle heading for upward movement
DOWN = 270  # Turtle heading for downward movement
LEFT = 180  # Turtle heading for leftward movement
RIGHT = 0  # Turtle heading for rightward movement


# =============================================================================
# SNAKE CLASS DEFINITION
# =============================================================================
class Snake:

    def __init__(self):
        """
        Initialise snake with starting segments and set head reference
        Creates 3 white square segments in horizontal line
        """
        self.segments = []  # List to store all snake segments
        self.create_snake()  # Build initial snake
        self.head = self.segments[0]  # Reference to first segment (head)

    # =============================================================================
    # SNAKE CREATION METHODS
    # =============================================================================
    def create_snake(self):
        """
        Create initial snake with 3 segments at predefined positions
        Called during initialisation and reset
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Create new snake segment at specified position
        Used for initial creation and when snake grows after eating food

        Args:
            position (tuple): (x, y) coordinates for new segment
        """
        new_segment = Turtle("square")  # Create square turtle segment
        new_segment.color("white")  # White colour for visibility on black background
        new_segment.penup()  # Don't draw lines when moving
        new_segment.goto(position)  # Move to specified position
        self.segments.append(new_segment)  # Add to segments list

    # =============================================================================
    # SNAKE RESET FUNCTIONALITY
    # =============================================================================
    def reset(self):
        """
        Reset snake to starting state after collision
        Moves old segments off-screen, creates new snake
        """
        # Move all existing segments far off-screen (cleanup)
        for seg in self.segments:
            seg.goto(1000, 1000)

        # Clear segments list and recreate snake
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]  # Reset head reference

    # =============================================================================
    # SNAKE GROWTH
    # =============================================================================
    def extend(self):
        """
        Add new segment to snake tail (growth after eating food)
        New segment appears at the position of the current last segment
        """
        self.add_segment(self.segments[-1].position())

    # =============================================================================
    # SNAKE MOVEMENT
    # =============================================================================
    def move(self):
        """
        Move snake forward by one step
        Each segment moves to the position of the segment in front of it
        Head moves forward in its current direction
        """
        # Move each segment to the position of the segment in front
        # Start from tail and work backwards to avoid overwriting positions
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # X position of segment ahead
            new_y = self.segments[seg_num - 1].ycor()  # Y position of segment ahead
            self.segments[seg_num].goto(new_x, new_y)  # Move current segment

        # Move head forward in its current direction
        self.head.forward(MOVE_DISTANCE)

    # =============================================================================
    # DIRECTION CONTROL METHODS
    # =============================================================================
    def up(self):
        """
        Change snake direction to up (prevent 180-degree turns)
        Only allow if not currently moving down
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Change snake direction to down (prevent 180-degree turns)
        Only allow if not currently moving up
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Change snake direction to left (prevent 180-degree turns)
        Only allow if not currently moving right
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Change snake direction to right (prevent 180-degree turns)
        Only allow if not currently moving left
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)