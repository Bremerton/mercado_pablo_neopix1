light.set_pixel_color(0, light.rgb(255,165, 0))
light.set_pixel_color(1, light.rgb(173, 255, 47))
light.set_pixel_color(2, light.rgb(0, 255, 0))
light.set_pixel_color(3, light.rgb(0, 255, 190))
light.set_pixel_color(4, light.rgb(10, 158, 255))
light.set_pixel_color(5, light.rgb(0, 110, 255))
light.set_pixel_color(6, light.rgb(8, 78, 255))
light.set_pixel_color(7, light.rgb(147, 112, 219))
light.set_pixel_color(8, light.rgb(255, 0, 255))
light.set_pixel_color(9, light.rgb(255, 20, 147))    
while True:
    light.set_brightness(20)
    pause(3000)
    light.set_brightness(0)
    pause(3000)
    light.set_brightness(20)


