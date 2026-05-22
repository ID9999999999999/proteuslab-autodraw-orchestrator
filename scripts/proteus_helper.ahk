#Requires AutoHotkey v2.0
#SingleInstance Force

typeComponent(name) {
    Send "^a"
    Sleep 80
    Send name
    Sleep 350
    Send "{Enter}"
}

showMouse() {
    MouseGetPos &x, &y
    ToolTip "x=" x " y=" y
    SetTimer () => ToolTip(), -1500
}

copyMouse() {
    MouseGetPos &x, &y
    A_Clipboard := "{ ""x"": " x ", ""y"": " y " }"
    ToolTip "Copied x=" x " y=" y
    SetTimer () => ToolTip(), -1500
}

^!1:: typeComponent("74LS86")
^!2:: typeComponent("74LS04")
^!3:: typeComponent("LOGICSTATE")
^!4:: typeComponent("LOGICPROBE")
^!5:: typeComponent("74LS00")
^!6:: typeComponent("74LS138")
^!7:: typeComponent("74LS90")
^!8:: typeComponent("74LS48")
^!9:: typeComponent("7SEG")
^!0:: typeComponent("CLOCK")
^!m:: showMouse()
^!c:: copyMouse()
Esc::ExitApp
