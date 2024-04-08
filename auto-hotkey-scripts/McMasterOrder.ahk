﻿#Requires AutoHotkey v2.0
Esc::ExitApp
#SingleInstance Force

Parts := [
    ; ["92949A106",1],
    ; ["92949A108",1],
    ; ["92949A110",1],
    ; ["92949A112",1],
    ; ["92949A113",1],
    ; ["92949A114",1],
    ; ["92949A116",1],
    ; ["92949A118",1],
    ; ["92949A120",1],
    ; ["92949A415",1],
    ; ["92210A105",1],
    ; ["92210A108",1],
    ; ["92210A110",1],
    ; ["92210A112",1],
    ; ["92210A113",1],
    ; ["92210A102",1],
    ; ["92210A115",1],
    ; ["92210A118",1],
    ; ["92210A120",2],
    ; ["92210A121",1],
    ; ["91831A005",1],
    ; ["91841A005",1],
    ; ["90107A005",1],
    ; ["27055A31",3],
    ; ["92949A144",1],
    ; ["92949A146",1],
    ; ["92949A148",1],
    ; ["92949A150",1],
    ; ["92949A151",1],
    ; ["92949A152",1],
    ; ["92949A153",1],
    ; ["92949A160",1],
    ; ["92949A157",1],
    ; ["92949A335",1],
    ; ["92210A144",1],
    ; ["92210A146",1],
    ; ["92210A148",1],
    ; ["92210A150",1],
    ; ["92210A151",1],
    ; ["92210A152",1],
    ; ["92210A153",1],
    ; ["92210A155",1],
    ; ["92210A157",1],
    ; ["92210A160",2],
    ; ["91831A007",1],
    ; ["91841A007",1],
    ; ["90107A007",1],
    ; ["27055A34",3],
    ; ["92949A190",1],
    ; ["92949A192",1],
    ; ["92949A194",1],
    ; ["92949A196",1],
    ; ["92949A197",1],
    ; ["92949A198",1],
    ; ["92949A199",1],
    ; ["92949A203",1],
    ; ["92949A207",2],
    ; ["92949A423",1],
    ; ["92210A190",1],
    ; ["92210A192",1],
    ; ["92210A194",1],
    ; ["92210A196",1],
    ; ["92210A197",1],
    ; ["92210A198",1],
    ; ["92210A199",1],
    ; ["92210A203",1],
    ; ["92210A208",2],
    ; ["92210A210",1],
    ; ["91831A009",1],
    ; ["91841A009",1],
    ; ["90107A010",1],
    ; ["27055A36",3],
    ; ["92949A242",1],
    ; ["92949A244",1],
    ; ["92949A245",1],
    ; ["92949A246",1],
    ; ["92949A247",1],
    ; ["92949A249",1],
    ; ["92949A251",1],
    ; ["92949A252",1],
    ; ["92949A253",1],
    ; ["92949A257",2],
    ; ["92210A242",1],
    ; ["92210A244",1],
    ; ["92210A245",1],
    ; ["92210A246",2],
    ; ["92210A247",2],
    ; ["92210A249",1],
    ; ["92210A251",1],
    ; ["92210A252",2],
    ; ["92210A253",2],
    ; ["92210A258",2],
    ; ["91841A011",1],
    ; ["91831A011",1],
    ; ["90107A011",1],
    ; ["27055A37",3],
    ; ["92949A537",1],
    ; ["92949A539",1],
    ; ["92949A540",1],
    ; ["92949A541",1],
    ; ["92949A542",1],
    ; ["92949A544",1],
    ; ["92949A546",1],
    ; ["92949A548",1],
    ; ["92949A550",1],
    ; ["92949A554",2],
    ; ["92210A537",2],
    ; ["92210A539",1],
    ; ["92210A540",1],
    ; ["92210A541",2],
    ; ["92210A542",1],
    ; ["92210A544",1],
    ; ["92210A546",2],
    ; ["92210A548",1],
    ; ["92210A550",1],
    ; ["92210A555",2],
    ; ["91831A029",1],
    ; ["91847A029",1],
    ; ["90107A029",1],
    ; ["27055A42",3],
    ; ["92949A578",2],
    ; ["92949A580",2],
    ; ["92949A581",2],
    ; ["92949A583",2],
    ; ["92949A582",2],
    ; ["92949A585",1],
    ; ["92949A587",2],
    ; ["92949A589",2],
    ; ["92949A591",2],
    ; ["92949A594",2],
    ; ["92210A578",1],
    ; ["92210A580",1],
    ; ["92210A581",1],
    ; ["92210A584",2],
    ; ["92210A583",2],
    ; ["92210A585",1],
    ; ["92210A587",1],
    ; ["92210A589",1],
    ; ["92210A591",2],
    ; ["92210A595",1],
    ; ["91831A030",1],
    ; ["91847A030",1],
    ; ["90107A030",1],
    ; ["27055A44",3],
    ; ["92949A619",2],
    ; ["92949A621",2],
    ; ["92949A622",2],
    ; ["92949A623",2],
    ; ["92949A624",2],
    ; ["92949A626",1],
    ; ["92949A628",2],
    ; ["92949A630",1],
    ; ["92949A632",2],
    ; ["92949A636",4],
    ; ["92210A619",2],
    ; ["92210A621",2],
    ; ["92210A622",2],
    ; ["92210A623",2],
    ; ["92210A624",2],
    ; ["92210A626",1],
    ; ["92210A628",2],
    ; ["92210A630",1],
    ; ["92210A632",2],
    ; ["92210A636",2],
    ; ["91831A127",1],
    ; ["91847A031",1],
    ; ["90107A127",2],
    ; ["27055A46",3],
    ; ["92949A352",1],
    ; ["92949A710",2],
    ; ["92949A712",2],
    ; ["92949A714",2],
    ; ["92949A716",2],
    ; ["92949A718",2],
    ; ["92949A720",2],
    ; ["92949A722",5],
    ; ["92949A724",5],
    ; ["92949A726",5],
    ; ["92210A352",5],
    ; ["92210A710",2],
    ; ["92210A712",2],
    ; ["92210A714",2],
    ; ["92210A716",1],
    ; ["92210A718",1],
    ; ["92210A720",1],
    ; ["92210A722",5],
    ; ["92210A724",5],
    ; ["92210A726",5],
    ; ["91831A137",1],
    ; ["91847A520",1],
    ; ["90107A033",2],
    ; ["27055A51",3],
    ; ["92095A113",1],
    ; ["92095A456",2],
    ; ["92095A457",2],
    ; ["92095A458",2],
    ; ["92095A459",2],
    ; ["92095A460",2],
    ; ["92095A461",2],
    ; ["92095A504",4],
    ; ["92095A114",1],
    ; ["92095A115",1],
    ; ["91801A550",1],
    ; ["92125A082",1],
    ; ["92125A083",2],
    ; ["92125A084",2],
    ; ["92125A086",2],
    ; ["92125A088",2],
    ; ["92125A090",2],
    ; ["92125A085",2],
    ; ["92125A102",1],
    ; ["92125A612",4],
    ; ["93625A102",1],
    ; ["90710A025",1],
    ; ["98689A111",1],
    ; ["25595A15",3],
    ; ["92095A471",1],
    ; ["92095A177",1],
    ; ["92095A179",1],
    ; ["92095A181",1],
    ; ["92095A182",1],
    ; ["92095A183",1],
    ; ["92095A168",2],
    ; ["92095A184",1],
    ; ["92095A185",2],
    ; ["92095A186",2],
    ; ["92125A127",2],
    ; ["92125A125",1],
    ; ["92125A126",1],
    ; ["92125A128",1],
    ; ["92125A130",1],
    ; ["92125A132",1],
    ; ["92125A133",1],
    ; ["92125A134",1],
    ; ["92125A136",1],
    ; ["92125A138",1],
    ; ["93625A100",1],
    ; ["90710A030",1],
    ; ["98689A112",1],
    ; ["8296A21",3],
    ; ["92095A477",1],
    ; ["92095A188",1],
    ; ["92095A189",1],
    ; ["92095A190",1],
    ; ["92095A192",1],
    ; ["92095A193",2],
    ; ["92095A194",1],
    ; ["92095A196",1],
    ; ["92095A197",1],
    ; ["92095A198",2],
    ; ["92125A185",2],
    ; ["92125A186",1],
    ; ["92125A188",1],
    ; ["92125A190",1],
    ; ["92125A192",1],
    ; ["92125A193",1],
    ; ["92125A194",1],
    ; ["92125A198",1],
    ; ["92125A202",1],
    ; ["92125A203",1],
    ; ["93625A150",1],
    ; ["90710A035",1],
    ; ["98689A113",1],
    ; ["8296A23",3],
    ["92095A208",1],
    ["92095A210",2],
    ["92095A211",2],
    ["92095A212",2],
    ["92095A214",1],
    ["92095A216",1],
    ["92095A218",1],
    ["92095A220",2],
    ["92095A206",2],
    ["92095A207",1],
    ["92125A208",1],
    ["92125A210",1],
    ["92125A211",2],
    ["92125A212",2],
    ["92125A214",1],
    ["92125A216",1],
    ["92125A220",1],
    ["92125A222",2],
    ["92125A217",1],
    ["92125A206",2],
    ["93625A200",1],
    ["90710A037",1],
    ["98689A114",1],
    ["8296A24",3],
    ; ["92095A239",2],
    ; ["92095A224",2],
    ; ["92095A226",2],
    ; ["92095A227",2],
    ; ["92095A238",2],
    ; ["92095A240",1],
    ; ["92095A242",1],
    ; ["92095A244",1],
    ; ["92095A246",1],
    ; ["92095A248",2],
    ; ["92125A232",1],
    ; ["92125A234",1],
    ; ["92125A236",1],
    ; ["92125A237",2],
    ; ["92125A238",1],
    ; ["92125A240",1],
    ; ["92125A242",1],
    ; ["92125A244",1],
    ; ["92125A246",1],
    ; ["92125A248",2],
    ; ["93625A250",1],
    ; ["90710A038",1],
    ; ["98689A115",1],
    ; ["8296A25",3],
    ; ["92095A256",2],
    ; ["92095A258",1],
    ; ["92095A260",1],
    ; ["92095A284",1],
    ; ["92095A286",1],
    ; ["92095A290",1],
    ; ["92095A292",1],
    ; ["92095A294",1],
    ; ["92095A298",2],
    ; ["92095A300",2],
    ; ["92125A278",1],
    ; ["92125A280",1],
    ; ["92125A282",1],
    ; ["92125A284",1],
    ; ["92125A286",1],
    ; ["92125A290",1],
    ; ["92125A292",1],
    ; ["92125A294",1],
    ; ["92125A298",2],
    ; ["92125A302",2],
    ; ["93625A300",1],
    ; ["90710A120",1],
    ; ["98689A116",1],
    ; ["8296A28",3],
    ; ["92095A408",1],
    ; ["92095A410",1],
    ; ["92095A413",1],
    ; ["92095A416",1],
    ; ["92095A418",2],
    ; ["92095A420",1],
    ; ["92095A424",1],
    ; ["92095A429",5],
    ; ["92095A500",5],
    ; ["92095A265",1],
    ; ["92125A330",1],
    ; ["92125A333",1],
    ; ["92125A336",1],
    ; ["92125A337",1],
    ; ["92125A339",1],
    ; ["92125A342",1],
    ; ["92125A348",1],
    ; ["92125A351",1],
    ; ["92125A357",1],
    ; ["92125A363",5],
    ; ["93625A350",2],
    ; ["90710A125",1],
    ; ["98689A117",1],
    ; ["8296A31",3],
    ; ["92095A502",5],
    ; ["92095A428",1],
    ; ["92095A427",1],
    ; ["92095A431",1],
    ; ["92095A432",1],
    ; ["92095A434",5],
    ; ["92095A437",5],
    ; ["92095A442",5],
    ; ["92095A446",5],
    ; ["92095A501",5],
    ; ["92125A622",5],
    ; ["92125A410",1],
    ; ["92125A413",1],
    ; ["92125A416",1],
    ; ["92125A419",1],
    ; ["92125A423",1],
    ; ["92125A429",1],
    ; ["92125A432",1],
    ; ["92125A435",5],
    ; ["92125A438",5],
    ; ["93625A400",2],
    ; ["90710A130",1],
    ; ["98689A118",1],
    ; ["8296A33",3],
    ; ["90145A305",1],
    ; ["90145A312",1],
    ; ["90145A317",1],
    ; ["90145A415",1],
    ; ["90145A419",1],
    ; ["90145A423",1],
    ["90145A469",1],
    ["90145A471",1],
    ["90145A473",1],
    ["90145A475",1],
    ["90145A884",1],
    ["90145A480",1],
    ; ["90145A537",1],
    ; ["90145A542",1],
    ; ["90145A546",1],
    ; ["90145A549",1],
    ; ["90145A551",2],
    ; ["90145A553",2],
    ; ["90145A619",1],
    ; ["90145A624",2],
    ; ["90145A632",6],
    ; ["90145A712",2],
    ; ["90145A720",6],
    ; ["90145A725",6],
    ; ["91585A032",1],
    ; ["91585A035",1],
    ; ["91585A091",1],
    ; ["91585A186",1],
    ; ["91585A194",1],
    ; ["91585A221",1],
    ["91585A345",1],
    ["91585A351",1],
    ["91585A374",1],
    ["91585A390",1],
    ["91585A402",1],
    ["91585A491",1],
    ; ["91585A496",1],
    ; ["91585A531",1],
    ; ["91585A559",1],
    ; ["91585A778",1],
    ; ["91585A624",1],
    ; ["91585A650",1],
    ; ["91585A880",2],
    ; ["91585A889",2],
    ; ["91585A898",2],
    ; ["91585A942",6],
    ; ["91585A954",6],
    ; ["91585A963",6],
]
^q::{
    for p in Parts {
                Send p[1]
                Send "{Tab}"
                Sleep 100
                Send p[2]
                Send "{Tab}"
                Sleep 500
            }

}
return

