# Copy all the tile functions in here

def draw_emma_tile(t, x, y, size, rotation, palette, tile_type="center"):
  """
  Draws a parameterized geometric tile centered at (x, y).

  Parameters:
  - t: Turtle object
  - x, y (float/int): Center coordinates of the tile
  - size (float/int): Width and height of the tile bounding box
  - rotation (int): Orientation angle (0, 90, 180, 270)
  - palette (dict): RGB tuples with keys 'bg', 'primary', 'secondary', 'accent'
  - tile_type (str): "center", "border", or "corner" (defaults to "center")
  """

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  # Useful relative dimension constants (derived from size)
  half = size / 2
  quarter = size / 4

  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================
  # Move to the bottom-left corner relative to orientation
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  # Return turtle to the true center of the tile
  t.jumpto(x, y)
  t.setheading(rotation)

  ######################### YOUR CHANGES START HERE ###########################

  # ==========================================
  # CONDITIONAL GEOMETRY (Based on tile_type)
  # ==========================================

  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # ------------------------------------------
  if tile_type == "corner":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################

      band = size * 0.14

      t.forward(-half)
      t.left(90)
      t.forward(-half)
      t.right(90)

      t.color(palette["primary"], palette["primary"])
      t.pendown()
      t.begin_fill()
      t.forward(size)
      t.left(90)
      t.forward(band)
      t.left(90)
      t.forward(size - band)
      t.right(90)
      t.forward(size - band)
      t.left(90)
      t.forward(band)
      t.left(90)
      t.forward(size)
      t.end_fill()
      t.penup()


      t.jumpto(x, y)
      t.setheading(rotation)
      t.forward(-half + band * 1.8)
      t.left(90)
      t.forward(-half + band * 1.8)
      t.right(90)


      t.pencolor(palette["accent"])
      t.pensize(3)
      t.pendown()
      t.forward(quarter * 1.5)
      t.backward(quarter * 1.5)
      t.left(90)
      t.forward(quarter * 1.5)
      t.backward(quarter * 1.5)
      t.right(90)
      t.penup()


      t.color(palette["primary"])
      t.dot(size * 0.20)
      t.color(palette["secondary"])
      t.dot(size * 0.12)
      t.color(palette["accent"])
      t.dot(size * 0.05)


      arc_radius = size * 0.4
      t.forward(arc_radius)
      t.left(90)
      t.pencolor(palette["secondary"])
      t.pensize(3)
      t.pendown()
      t.circle(arc_radius, 90)
      t.penup()

  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################

      tri = quarter

      t.forward(-half)
      t.left(90)
      t.forward(-half)
      t.right(90)

      t.color(palette["secondary"], palette["primary"])
      t.pensize(2)
      for i in range(4):
          t.pendown()
          t.begin_fill()
          for j in range(3):
              t.forward(tri)
              t.left(120)
          t.end_fill()
          t.penup()
          t.forward(tri)


      t.jumpto(x, y)
      t.setheading(rotation)
      t.forward(-half + tri / 2)
      t.left(90)
      t.forward(-half + tri * 0.87 + size * 0.09)
      t.right(90)

      t.color(palette["accent"])
      for i in range(4):
          t.dot(size * 0.07)
          t.forward(tri)


      t.jumpto(x, y)
      t.setheading(rotation)
      t.forward(-half)
      t.left(90)
      t.forward(-size * 0.05)
      t.right(90)

      t.pencolor(palette["accent"])
      t.pensize(3)
      t.pendown()
      t.forward(size)
      t.penup()

  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.jumpto(x, y)
      t.setheading(rotation)
      t.left(90)
      t.forward(-size * 0.46)
      t.setheading(rotation + 45)

      t.pencolor(palette["secondary"])
      t.pensize(2)
      t.pendown()
      for i in range(4):
          t.forward(size * 0.65)
          t.left(90)
      t.penup()


      for i in range(4):
          t.jumpto(x, y)
          t.setheading(rotation + 45 + i * 90)
          t.forward(size * 0.54)
          t.color(palette["secondary"])
          t.dot(size * 0.12)
          t.color(palette["accent"])
          t.dot(size * 0.06)


      t.color(palette["secondary"], palette["primary"])
      t.pensize(2)
      for i in range(8):
          t.jumpto(x, y)
          t.setheading(rotation + i * 45)
          t.pendown()
          t.begin_fill()
          for j in range(3):
              t.forward(size * 0.38)
              t.left(120)
          t.end_fill()
          t.penup()


      t.pencolor(palette["accent"])
      t.pensize(2)
      for i in range(8):
          t.jumpto(x, y)
          t.setheading(rotation + i * 45 + 30)
          t.pendown()
          t.forward(size * 0.33)
          t.penup()


      circle_radius = size * 0.15
      t.jumpto(x, y)
      t.setheading(rotation)
      t.left(90)
      t.forward(-circle_radius)
      t.right(90)

      t.color(palette["secondary"], palette["accent"])
      t.pensize(3)
      t.pendown()
      t.begin_fill()
      t.circle(circle_radius)
      t.end_fill()
      t.penup()


      t.jumpto(x, y)
      t.color(palette["bg"])
      t.dot(size * 0.08)
      t.color(palette["secondary"])
      t.dot(size * 0.04)

  # ==========================================
  # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
  # ==========================================

  ############## This part is my own drawing #######################
  ################## Change it to your design ######################
  t.pencolor(palette["secondary"])
  t.pensize(2)


  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)


  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  ######################### YOUR CHANGES END HERE #############################

  # ==========================================
  # TURTLE TEARDOWN
  # Reset pen, heading, and state for the next user
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))

# Function definition for person 2 here
def draw_tae_tile(t, x, y, size, rotation, palette, tile_type="center"):
  """
  Draws a parameterized geometric tile centered at (x, y).

  Parameters:
  - t: Turtle object
  - x, y (float/int): Center coordinates of the tile
  - size (float/int): Width and height of the tile bounding box
  - rotation (int): Orientation angle (0, 90, 180, 270)
  - palette (dict): RGB tuples with keys 'bg', 'primary', 'secondary', 'accent'
  - tile_type (str): "center", "border", or "corner" (defaults to "center")
  """

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  # Useful relative dimension constants (derived from size)
  half = size / 2
  quarter = size / 4

  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================
  # Move to the bottom-left corner relative to orientation
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  # Return turtle to the true center of the tile
  t.jumpto(x, y)
  t.setheading(rotation)

  ######################### YOUR CHANGES START HERE ###########################

  # ==========================================
  # CONDITIONAL GEOMETRY (Based on tile_type)
  # ==========================================

  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # ------------------------------------------
  if tile_type == "corner":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.pencolor(palette["accent"])
      t.pensize(6)
      t.forward(quarter)
      t.right(90)
      t.forward(quarter)
      t.left(160)

      t.pendown()
      t.forward(half)
      t.left(90)
      t.forward(half)
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.color(palette["primary"], palette["primary"])
      t.forward(quarter + quarter / 2)
      t.left(90)
      t.forward(quarter)

      t.pendown()
      t.begin_fill()
      t.circle(quarter / 2)
      t.end_fill()
      t.left(90)
      t.forward(quarter / 2)
      t.color(palette["accent"])
      t.dot(quarter / 4)
      t.penup()

  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.color(palette["primary"], palette["primary"])
      t.forward(-half)
      t.left(90)
      t.forward(quarter)
      t.right(90)

      t.pendown()
      t.begin_fill()
      for _ in range(2):
          t.forward(size)
          t.left(90)
          t.forward(quarter)
          t.left(90)
      t.end_fill()
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(3)
      t.forward(-half)
      t.pendown()
      t.forward(size)
      t.penup()

  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################

      t.pencolor(palette["secondary"])
      t.jumpto(x, y)
      t.setheading(rotation + 65)
      t.forward(quarter * 1.2)
      t.left(90)
      t.forward(quarter * 1.2)
      t.pendown()
      for i in range(4):
          t.left(90)
          t.forward(half * 1.2)
      t.left(90)
      t.penup()

      t.forward(half * 0.9)

      t.color(palette["secondary"])
      t.pendown()
      for i in range(5):
        t.left(144)
        t.forward(half * 0.2)
      t.penup()


      t.color(palette["primary"], palette["primary"])
      t.setheading(rotation + 60)
      for i in range(4):
        t.jumpto(x, y)
        t.pendown()
        t.begin_fill()
        for j in range(3):
            t.forward(quarter * 1.4)
            t.left(120)
        t.end_fill()
        t.penup()
        t.left(30)

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(2)

      for _ in range(8):
          t.pendown()
          t.forward(quarter * 0.9)
          t.penup()
          t.jumpto(x, y)
          t.right(45)




  # ==========================================
  # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
  # ==========================================

  ############## This part is my own drawing #######################
  ################## Change it to your design ######################
  t.pencolor(palette["secondary"])
  t.pensize(2)

  # Go to the corner
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  # Draw the border
  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  ######################### YOUR CHANGES END HERE #############################

  # ==========================================
  # TURTLE TEARDOWN
  # Reset pen, heading, and state for the next user
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))

# Function definition for person 3 here

def draw_jingyi_tile(t, x, y, size, rotation, palette, tile_type="center"):
  """
  Draws a parameterized geometric tile centered at (x, y).

  Parameters:
  - t: Turtle object
  - x, y (float/int): Center coordinates of the tile
  - size (float/int): Width and height of the tile bounding box
  - rotation (int): Orientation angle (0, 90, 180, 270)
  - palette (dict): RGB tuples with keys 'bg', 'primary', 'secondary', 'accent'
  - tile_type (str): "center", "border", or "corner" (defaults to "center")
  """

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  # Useful relative dimension constants
  half = size / 2
  quarter = size / 4


  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================

  # Move to the bottom-left corner
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  # Set the background color
  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)

  # Draw the background square
  t.pendown()
  t.begin_fill()

  for _ in range(4):
      t.forward(size)
      t.left(90)

  t.end_fill()
  t.penup()

  # Return to the center
  t.jumpto(x, y)
  t.setheading(rotation)


  ######################### YOUR CHANGES START HERE ###########################


  # ==========================================
  # CONDITIONAL GEOMETRY
  # ==========================================


  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # ------------------------------------------

  if tile_type == "corner":

      t.penup()
      t.jumpto(x, y)
      t.setheading(rotation)


      t.backward(half)


      t.pencolor(palette["primary"])
      t.pensize(5)
      t.pendown()


      t.forward(quarter * 1.2)


      t.left(90)
      t.forward(quarter * 1.2)


      t.left(90)
      t.forward(quarter * 0.8)


      t.left(90)
      t.forward(quarter * 0.6)


      t.left(90)
      t.forward(quarter * 0.4)


      t.left(90)
      t.forward(quarter)


      t.right(90)
      t.forward(quarter * 1.2)


      t.left(90)
      t.forward(quarter * 0.4)

      t.penup()


  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------

  elif tile_type == "border":


      t.penup()
      t.jumpto(x, y)
      t.setheading(rotation)


      t.backward(half)


      t.pencolor(palette["primary"])
      t.pensize(5)
      t.pendown()


      t.forward(size)

      t.penup()


  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------

  else:


      t.penup()
      t.jumpto(x, y)
      t.setheading(rotation + 45)


      t.backward(quarter * 1.1)
      t.left(90)
      t.backward(quarter * 1.1)
      t.right(90)


      t.pencolor(palette["secondary"])
      t.pensize(3)
      t.pendown()

      for i in range(4):
          t.forward(quarter * 2.2)
          t.left(90)

      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)


      t.backward(quarter * 0.65)
      t.left(90)
      t.backward(quarter * 0.65)
      t.right(90)


      t.pencolor(palette["primary"])
      t.pensize(3)
      t.pendown()

      for i in range(4):
          t.forward(quarter * 1.3)
          t.left(90)

      t.penup()




      t.pencolor(palette["primary"])
      t.pensize(2)

      for i in range(4):

          t.penup()
          t.jumpto(x, y)
          t.setheading(rotation + i * 90)

          t.pendown()
          t.forward(quarter * 1.5)

      t.penup()


      # ======================================
      # DRAW FOUR DIAGONAL LINES
      # ======================================

      t.pencolor(palette["secondary"])
      t.pensize(2)

      for i in range(4):

          t.penup()
          t.jumpto(x, y)
          t.setheading(rotation + 45 + i * 90)

          t.pendown()
          t.forward(quarter * 1.2)

      t.penup()


      # ======================================
      # DRAW THE CENTER DOTS
      # ======================================

      t.jumpto(x, y)

      # Large red dot
      t.pencolor(palette["accent"])
      t.dot(quarter * 0.65)

      # Small ivory dot
      t.pencolor(palette["secondary"])
      t.dot(quarter * 0.25)


  # ==========================================
  # DRAW BORDER
  # ==========================================

  # Do not draw a square border around each tile.
  # The corner and border tiles will form one large
  # border when all tiles are placed together.


  ######################### YOUR CHANGES END HERE #############################


  # ==========================================
  # TURTLE TEARDOWN
  # Reset pen, heading, and state
  # ==========================================

  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))



tile_functions = [draw_emma_tile, draw_tae_tile, draw_jingyi_tile]
