from appJar import gui

def press(button):
    if button == "Cancel":
        app.stop()
    elif button == "Start":
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
    elif button == "Set Source":
        directorio = app.directoryBox()
        app.setEntry("Source",directorio)
        print directorio
    elif button == "Set Save":
        directorio = app.directoryBox()
        app.setEntry("Save to",directorio)
        print directorio

def menuPress(menu):
    app.infoBox("About Comic Resizer","Made By Javier Alvarez, 2017")

app = gui("Comic Resizer", "600x200")
app.setFont(14)

app.addLabel("title", "Welcome to appJar")

app.addMenuList("Help",["Help","-","About Comic Resizer"],menuPress)

app.addLabelEntry("Source",0,0,2)
app.addLabelEntry("Save to",1,0,2)
app.addNamedButton("Browse","Set Source",press,0,2)
app.addNamedButton("Browse","Save to",press,1,2)

app.addHorizontalSeparator(colour="red")

app.addLabelScale("Height")
app.setScaleRange("Height",0,1280)
app.showScaleValue("Height")

app.addLabelScale("Quality")
app.showScaleValue("Quality")

app.addCheckBox("Split")

app.addButton("Start",press,3,2)
app.addButton("Cancel",press,4,2)
app.setButtonWidth("Start",6)

app.setFocus("Source")

app.go()
