from ColabTurtlePlus.Turtle import *
import numpy as np

# Import your own code from TileFunctions.py and PaletteOptions.py
from TileFunctions import *
from PaletteOptions import *

# Create one function to handle everything
def generate_poster():
  
 title_text = input("What would you like the poster title to be?")
poster_name = input("What is your name?")

color_choice = input("What color palette would you like?")

while color_choice not in palette_names:
    color_choice = input("Try again! The palette options are emma_palette, tae_palette, jingyi_palette, and random:")

print("Good job!")

nrows = int(input("Tile grid height: "))
while nrows < 4 or nrows > 10:
  print("Pick a number between 4 and 10.")
  nrows = int(input("Tile grid height: "))

ncols = int(input("Tile grid width: "))
while ncols < 4 or ncols > 10:
  print("Pick a number between 4 and 10.")
  ncols = int(input("Tile grid width: "))

print("Drawing your poster...")

screen_width = 950
screen_height = 700

border = 20
vertical_spacing_below = 180
shrink = 0.8

if color_choice == "random":
    random_name = list(palette_options)[np.random.randint(len(palette_options))]
    palette = palette_options[random_name]
    print(f"Random picked: {random_name}")
else:
    palette = palette_options[color_choice]


size_horiz = (screen_width - border * 2) / ncols
size_vert = (screen_height - border - vertical_spacing_below) / nrows
size = min(size_horiz, size_vert) * shrink

print(f"Tile size: {size}")

clearscreen()
setup(screen_width, screen_height)
t = Turtle()
t.speed(0)


x_offset = -screen_width / 2 + border + size / 2
y_offset = screen_height / 2 - border - size / 2

corner_home = {
    "draw_emma_tile": 225,
    "draw_tae_tile": 45,
    "draw_jingyi_tile": 135,
}

for row in range(nrows):
  y = y_offset - size * row

  for col in range(ncols):
    x = x_offset + size * col

    F = tile_functions[np.random.randint(len(tile_functions))]

    if row == 0:
      if col == 0:
        tile_type = "corner"
        corner_angle = 135
      elif col == ncols - 1:
        tile_type = "corner"
        corner_angle = 45
      else:
        tile_type = "border"
        rotation = np.random.randint(2) * 180
    elif row == nrows - 1:
      if col == 0:
        tile_type = "corner"
        corner_angle = 225
      elif col == ncols - 1:
        tile_type = "corner"
        corner_angle = 315
      else:
        tile_type = "border"
        rotation = np.random.randint(2) * 180
    else:
      if col == 0 or col == ncols - 1:
        tile_type = "border"
        rotation = 90 + np.random.randint(2) * 180
      else:
        tile_type = "center"
        rotation = np.random.randint(4) * 90

    if tile_type == "corner":
      rotation = (corner_angle - corner_home.get(F.__name__, 135)) % 360

    F(t, x, y, size, rotation, palette, tile_type)


t.hideturtle()
done()
