#Requires AutoHotkey v2.0
Esc::ExitApp
#SingleInstance Force

Parameters := [
    [250,100,1,64,1],
    [250,100,1,64,2],
    [250,100,1,64,4],
    [250,100,1,64,8],
    [250,100,1,64,16],
    [250,100,1,64,32],
    [250,100,1,64,64],
    [250,100,1,64,100],
    [250,100,1,64,150],
    [250,100,1,64,200],
    [250,100,1,64,250],
    [250,100,1,64,300],
    [250,100,1,64,350],
    [250,100,1,64,400],
    [250,100,1,64,450],
    [250,100,1,64,500],
]
!j::{
    for p in Parameters {
                Send p[1]
                Send "{Tab}"
                Sleep 100
                Send p[2]
                Send "{Tab}"
                Sleep 100
                Send p[3]
                Send "{Tab}"
                Sleep 100
                Send p[4]
                Send "{Tab}"
                Sleep 100
                Send p[5]
                Send "{Tab}"                
                Sleep 100
            }

}
return

