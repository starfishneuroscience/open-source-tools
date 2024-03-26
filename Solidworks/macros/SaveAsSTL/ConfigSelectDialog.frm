VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} ConfigSelectDialog 
   Caption         =   "Select Configurations to Export"
   ClientHeight    =   7392
   ClientLeft      =   133
   ClientTop       =   483
   ClientWidth     =   4536
   OleObjectBlob   =   "ConfigSelectDialog.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "ConfigSelectDialog"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub Label1_Click()

End Sub

Private Sub ConfigBox_Click()

End Sub

Private Sub ExportSTL_Click()
    For i = 0 To ConfigBox.ListCount - 1
        If ConfigBox.Selected(i) = True Then
            'ExportConfigList.AddItem ConfigBox.List(i)
            swModel.ShowConfiguration2 (ConfigBox.List(i))
            Bodies = Save__STL_with_REV1.GetBodies()
            Call SaveBodiesAsSTL(Bodies, ConfigBox.List(i), outputPath)
            Debug.Print (CStr(BodyExportCount))
        End If
    Next i
    MsgBox CStr(BodyExportCount) & " Bodies Saved As STL in " & outputPath
    Shell "C:\WINDOWS\explorer.exe """ & outputPath & "", vbNormalFocus
    Unload Me
    
End Sub

Private Sub SelectAllBox_Click()
    If SelectAllBox.Value = True Then
        For i = 0 To ConfigBox.ListCount - 1
            ConfigBox.Selected(i) = True
        Next i
    End If
    
    If SelectAllBox.Value = False Then
        For i = 0 To ConfigBox.ListCount - 1
            ConfigBox.Selected(i) = False
        Next i
    End If
End Sub
