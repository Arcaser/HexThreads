from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

ct1 = ColorThief("images/brazil_jersey.jpg")
ct2 = ColorThief("images/portugal_jersey.jpg")
ct3 = ColorThief("images/chelsea_jersey.jpg")

palette1 = ct1.get_palette(color_count=2)
palette2 = ct2.get_palette(color_count=2)
palette3 = ct3.get_palette(color_count=5)

plt.imshow([[palette1[i] for i in range(2)]])
plt.show()
plt.imshow([[palette2[i] for i in range(2)]])
plt.show()
plt.imshow([[palette3[i] for i in range(5)]])
plt.show()

for color in palette1:
    print(color)
    print("f#{color[0]:02x}{color[1]:02x}{color[2]}")
    print(colorsys.rgb_to_hsv(*color))
    print(colorsys.rgb_to_hls(*color))

print()

for color in palette2:
    print(color)
    print("f#{color[0]:02x}{color[1]:02x}{color[2]}")
    print(colorsys.rgb_to_hsv(*color))
    print(colorsys.rgb_to_hls(*color))

print()

for color in palette3:
    print(color)
    print("f#{color[0]:02x}{color[1]:02x}{color[2]}")
    print(colorsys.rgb_to_hsv(*color))
    print(colorsys.rgb_to_hls(*color))
