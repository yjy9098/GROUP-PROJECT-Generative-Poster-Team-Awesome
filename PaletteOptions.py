import numpy as np

palette_options = {}

#First persons color palette
emma_palette = {
        "bg": (196, 233, 218),
        "primary": (255, 192, 133),
        "secondary": (226, 58, 119),
        "accent": (198, 201, 84)
    }

palette_options["emma_palette"] = emma_palette

#Second persons color palette
tae_palette = {
        "bg": (15, 12, 28),
        "primary": (255, 0, 110),
        "secondary": (0, 245, 212),
        "accent": (170, 170, 170)
    }
palette_options["tae_palette"] = tae_palette

#Third persons color palette
jingyi_palette = {
    "bg": (18, 47, 45),
    "primary": (218, 174, 80),
    "secondary": (226, 215, 180),
    "accent": (155, 38, 38)
}
palette_options["Jingyi_palette"] = jingyi_palette

random = {
    "bg": (np.random.rand(255), np.random.rand(255), np.random.rand(255)),
    "primary": (np.random.rand(255), np.random.rand(255), np.random.rand(255)),
    "secondary": (np.random.rand(255), np.random.rand(255), np.random.rand(255)),
    "accent": (np.random.rand(255), np.random.rand(255), np.random.rand(255))
}

palette_names = list(palette_options)
palette_names.append("random")
print(f"The available color palettes are: {palette_names}")
