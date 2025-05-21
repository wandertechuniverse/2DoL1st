from PIL import Image, ImageDraw

img = Image.new("RGBA", (32, 32), (0, 0, 0, 0)) # Transparent background
draw = ImageDraw.Draw(img)

# Dark gray background for the main part of the icon
draw.rectangle([0, 0, 31, 31], fill=(80, 80, 80, 255))

# White checkmark (simplified)
# Part 1 of checkmark (thicker)
draw.line([ (8, 16), (14, 22), (14, 22) ], fill=(255, 255, 255, 255), width=4)
# Part 2 of checkmark (thicker)
draw.line([ (14, 22), (24, 10), (24, 10) ], fill=(255, 255, 255, 255), width=4)

img.save("tray_icon.png", "PNG")
print("tray_icon.png created successfully.")
