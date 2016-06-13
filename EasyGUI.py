import easygui

color = easygui.buttonbox("What is your favourite color",
                    choices= ["Yello", "Green", "Red"])
easygui.msgbox("You picked " + color)

animal = easygui.enterbox("Tell me your favourite animal")
easygui.msgbox("You chose" +  animal +  ".")
