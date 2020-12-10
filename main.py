print("Light Level:" + input.light_level())
while True:  
    if input.light_level()<40:
        light.set_all(light.rgb(0, 0, 255))
    elif input.light_level()>40:
        light.set_all(light.rgb(0, 0,0))