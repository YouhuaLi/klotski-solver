# Import necessary classes from Manim library
from manim import *

# Define a class for the Klotski game animation
class Klotski(Scene):
    def construct(self):
        # Create the game board
        board = Rectangle(width=6, height=6, fill_opacity=1, color=BLUE)
        self.play(Create(board))

        # Create the game pieces
        piece1 = Rectangle(width=2, height=2, fill_opacity=1, color=RED)
        piece2 = Rectangle(width=2, height=1, fill_opacity=1, color=ORANGE)
        piece3 = Rectangle(width=2, height=1, fill_opacity=1, color=YELLOW)
        piece4 = Rectangle(width=1, height=2, fill_opacity=1, color=GREEN)
        piece5 = Rectangle(width=1, height=2, fill_opacity=1, color=BLUE_D)
        piece6 = Rectangle(width=1, height=1, fill_opacity=1, color=PURPLE)

        # Position the game pieces on the board
        piece1.move_to(board.get_corner(UL))
        piece2.move_to(piece1.get_corner(DOWN)+DOWN)
        piece3.move_to(piece2.get_corner(DOWN)+DOWN)
        piece4.move_to(piece1.get_corner(RIGHT)+RIGHT)
        piece5.move_to(piece4.get_corner(RIGHT)+RIGHT)
        piece6.move_to(piece2.get_corner(RIGHT)+RIGHT)

        # Add the game pieces to the scene
        self.play(Create(piece1))
        self.play(Create(piece2))
        self.play(Create(piece3))
        self.play(Create(piece4))
        self.play(Create(piece5))
        self.play(Create(piece6))

        # Move the game pieces to their solution positions
        self.play(piece1.animate.move_to(board.get_corner(DR)-2*RIGHT))
        self.play(piece2.animate.move_to(board.get_corner(DR)-2*RIGHT+DOWN))
        self.play(piece3.animate.move_to(board.get_corner(DR)-2*RIGHT+2*DOWN))
        self.play(piece4.animate.move_to(board.get_corner(DR)-4*RIGHT))
        self.play(piece5.animate.move_to(board.get_corner(DR)-4*RIGHT+2*DOWN))
        self.play(piece6.animate.move_to(board.get_corner(DR)-3*RIGHT+DOWN))