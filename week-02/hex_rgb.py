def hex_to_rgb(color):
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)
    return r, g, b

print("Enter Hex Color:")
user_color = input('#')
print("The RGB is:", hex_to_rgb(user_color))