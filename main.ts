light.setPixelColor(0, light.rgb(255, 165, 0))
light.setPixelColor(1, light.rgb(173, 255, 47))
light.setPixelColor(2, light.rgb(0, 255, 0))
light.setPixelColor(3, light.rgb(0, 255, 190))
light.setPixelColor(4, light.rgb(10, 158, 255))
light.setPixelColor(5, light.rgb(0, 110, 255))
light.setPixelColor(6, light.rgb(8, 78, 255))
light.setPixelColor(7, light.rgb(147, 112, 219))
light.setPixelColor(8, light.rgb(255, 0, 255))
light.setPixelColor(9, light.rgb(255, 20, 147))
while (true) {
    light.setBrightness(20)
    pause(3000)
    light.setBrightness(0)
    pause(3000)
    light.setBrightness(20)
}
