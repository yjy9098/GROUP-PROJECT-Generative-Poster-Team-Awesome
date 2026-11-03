# Generative Poster Project Team Awesome

![Example final poster](example_poster.png)

**Created by:** Jingyi, Emma, and Tae 
**Course:** Creative Coding, Pratt Institute  
**Semester:** Fall 2026

## About the Project

This project is used to create an interactive poster design where users can customize an array of different colorful tiles. It uses color palette and designs from all three creators to make a unified composition.

## The Interface

Users can modify poster title, authorship, color palette, and how many rows and columns of tiles the poster uses.

## Meet the Designers

- **Jingyi:** [Brief description of their tile designs or contribution.]
- **Emma:** [Brief description of their tile designs or contribution.]
- **Tae:** Designed user-facing prompts and created randomized palette. 

## Try it yourself

Copy this code into a Colab Notebook.

```python
!git clone (https://github.com/yjy9098/GROUP-PROJECT-Generative-Poster-Team-Awesome.git)
%cd cc-f26-group-project
!pip install -r requirements.txt
from project import generate_poster
generate_poster()
```

Or click below to open an example notebook in Google Colab and generate your own poster!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1iho7fD12AxIXqKzoNI5bAI-NxnKauBgz?usp=sharing)

### How to Use

1. Open the notebook in Google Colab.
2. Run the setup cells to download the project code and install the required libraries.
3. Run the cell that calls the function and prompts the user to choose a title, grid dimensions, and color palette.
4. Your own poster will be saved as poster.svg!

## Files

- `project.py` – Main poster-generation program.
- `TileFunctions.py` – Collection of custom tile-drawing functions.
- `PaletteOptions.py` – Available color palettes.
- `requirements.txt` – Required Python libraries.
- `example_poster.svg` – Scalable vector version of an example final poster image.
