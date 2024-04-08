#Requires AutoHotkey v2.0
Esc::ExitApp
#SingleInstance Force

Parameters := [
    [75,15,1,4000,1],
    [75,15,1,4000,2],
    [75,15,1,4000,4],
    [75,15,1,4000,6],
    [75,15,1,4000,8],
    [75,15,1,4000,12],
    [75,15,1,4000,16],
    [75,15,1,4000,24],
    [75,15,1,4000,32],
    [75,15,1,4000,48],
    [75,15,1,4000,64],
    [75,15,1,4000,96],
    [75,15,1,4000,128],
    [75,15,1,4000,192],
    [75,15,1,4000,256],
    [75,15,1,4000,512],
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

