# =============================================================================
# Scoreboard Class - Manages Score Display and High Score Persistence
# Tracks current score, maintains high score in file, displays both on screen
# Handles score increases, game resets, and persistent data storage
# =============================================================================
from turtle import Turtle

# =============================================================================
# CONSTANTS - SCOREBOARD CONFIGURATION
# =============================================================================
ALIGNMENT = "center"  # Text alignment for score display
FONT = ("Courier", 24, "normal")  # Font family, size, and style


# =============================================================================
# SCOREBOARD CLASS DEFINITION
# =============================================================================
class Scoreboard(Turtle):
    """
    Manages game scoring system with persistent high score tracking
    Displays current score and all-time high score at top of screen
    """

    def __init__(self):
        """
        Initialise scoreboard with current score and load high score from file
        Position scoreboard at top of screen and display initial scores
        """
        super().__init__()  # Initialise parent Turtle class

        # =============================================================================
        # SCORE INITIALISATION
        # =============================================================================
        self.score = 0  # Current game score (starts at 0)

        # Load high score from persistent storage file
        with open("data.txt") as data:
            self.high_score = int(data.read())  # Read and convert to integer

        # =============================================================================
        # SCOREBOARD VISUAL SETUP
        # =============================================================================
        self.color("white")  # White text for visibility on black background
        self.penup()  # Don't draw lines when moving
        self.goto(0, 270)  # Position at top center of screen
        self.hideturtle()  # Hide turtle cursor, only show text

        # Display initial scoreboard
        self.update_scoreboard()

    # =============================================================================
    # SCOREBOARD DISPLAY METHODS
    # =============================================================================
    def update_scoreboard(self):
        """
        Refresh scoreboard display with current score and high score
        Called after score changes or game resets
        """
        self.clear()  # Clear previous text
        # Display formatted score text
        self.write(f"Score: {self.score} | High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    # =============================================================================
    # GAME RESET FUNCTIONALITY
    # =============================================================================
    def reset(self):
        """
        Handle game reset after collision
        Update high score if current score is higher, save to file, reset current score
        """
        # Check if current score beats high score
        if self.score > self.high_score:
            self.high_score = self.score  # Update high score

            # Save new high score to file for persistence
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        # Reset current score for new game
        self.score = 0
        self.update_scoreboard()  # Refresh display

    # =============================================================================
    # SCORE MANAGEMENT
    # =============================================================================
    def increase_score(self):
        """
        Increment current score by 1 (called when snake eats food)
        Update display to show new score
        """
        self.score += 1
        self.update_scoreboard()  # Refresh display with new score