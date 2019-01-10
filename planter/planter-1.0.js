[
    {
        "id": "b0d89d.a5c83f6",
        "type": "tab",
        "label": "planter-1.0",
        "disabled": false,
        "info": "flow that works with planter-1.0.py"
    },
    {
        "id": "2cf5b911.2c2fd6",
        "type": "inject",
        "z": "b0d89d.a5c83f6",
        "name": "CLOCK",
        "topic": "CLK",
        "payload": "CLK 1",
        "payloadType": "str",
        "repeat": "1",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 180,
        "y": 60,
        "wires": [
            [
                "f14416b0.d7ef58"
            ]
        ]
    },
    {
        "id": "f14416b0.d7ef58",
        "type": "mqtt out",
        "z": "b0d89d.a5c83f6",
        "name": "",
        "topic": "RACK1S",
        "qos": "2",
        "retain": "",
        "broker": "7a5cc18b.d2b4d8",
        "x": 380,
        "y": 60,
        "wires": []
    },
    {
        "id": "3d4b55d3.ebdbf2",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "Load button",
        "group": "914d09d8.a443a8",
        "order": 1,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "LOAD",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "LOAD 1",
        "payloadType": "str",
        "topic": "",
        "x": 170,
        "y": 120,
        "wires": [
            [
                "74edab37.f81844"
            ]
        ]
    },
    {
        "id": "74edab37.f81844",
        "type": "mqtt out",
        "z": "b0d89d.a5c83f6",
        "name": "",
        "topic": "RACK1S",
        "qos": "2",
        "retain": "",
        "broker": "7a5cc18b.d2b4d8",
        "x": 380,
        "y": 120,
        "wires": []
    },
    {
        "id": "606bf47b.bbed44",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "Change state button",
        "group": "7231eec0.8789b8",
        "order": 1,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "CHANGE STATE",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "STATE 1",
        "payloadType": "str",
        "topic": "",
        "x": 140,
        "y": 180,
        "wires": [
            [
                "4f1608ea.7e281"
            ]
        ]
    },
    {
        "id": "4f1608ea.7e281",
        "type": "mqtt out",
        "z": "b0d89d.a5c83f6",
        "name": "",
        "topic": "RACK1S",
        "qos": "2",
        "retain": "",
        "broker": "7a5cc18b.d2b4d8",
        "x": 380,
        "y": 180,
        "wires": []
    },
    {
        "id": "92784d60.0cc658",
        "type": "mqtt in",
        "z": "b0d89d.a5c83f6",
        "name": "",
        "topic": "RACKSTATUS",
        "qos": "2",
        "broker": "7a5cc18b.d2b4d8",
        "x": 100,
        "y": 400,
        "wires": [
            [
                "9762f475.0cd778"
            ]
        ]
    },
    {
        "id": "9762f475.0cd778",
        "type": "json",
        "z": "b0d89d.a5c83f6",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": false,
        "x": 270,
        "y": 400,
        "wires": [
            [
                "93cf6994.2013c8",
                "743d4838.f85128"
            ]
        ]
    },
    {
        "id": "93cf6994.2013c8",
        "type": "function",
        "z": "b0d89d.a5c83f6",
        "name": "filter parameters",
        "func": "var message = msg.payload\nif (message.name == \"parameters\") {\n    var recipe_name = {payload: message.recipe_name}\n    var configuration = {payload: message.configuration}\n    var run_number = {payload: message.run_number}\n    var plant_type = {payload: message.plant_type}\n    var led_type = {payload: message.led_type}\n    var start_date = {payload: message.start_date}\n}\nreturn [recipe_name,configuration,run_number,plant_type,led_type,start_date];",
        "outputs": 6,
        "noerr": 0,
        "x": 480,
        "y": 320,
        "wires": [
            [
                "253487ca.776768"
            ],
            [
                "4aed3d93.ce555c"
            ],
            [
                "d163e2f6.497ed8"
            ],
            [
                "3f19575b.f92fc"
            ],
            [
                "f48d1206.9f8028"
            ],
            [
                "331eebb.035c894"
            ]
        ]
    },
    {
        "id": "253487ca.776768",
        "type": "ui_text",
        "z": "b0d89d.a5c83f6",
        "group": "914d09d8.a443a8",
        "order": 3,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Recipe Name",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 720,
        "y": 220,
        "wires": []
    },
    {
        "id": "4aed3d93.ce555c",
        "type": "ui_text",
        "z": "b0d89d.a5c83f6",
        "group": "914d09d8.a443a8",
        "order": 4,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Configuration",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 710,
        "y": 260,
        "wires": []
    },
    {
        "id": "d163e2f6.497ed8",
        "type": "ui_text",
        "z": "b0d89d.a5c83f6",
        "group": "914d09d8.a443a8",
        "order": 5,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Run Number",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 710,
        "y": 300,
        "wires": []
    },
    {
        "id": "3f19575b.f92fc",
        "type": "ui_text",
        "z": "b0d89d.a5c83f6",
        "group": "914d09d8.a443a8",
        "order": 6,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Plant type",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 700,
        "y": 340,
        "wires": []
    },
    {
        "id": "f48d1206.9f8028",
        "type": "ui_text",
        "z": "b0d89d.a5c83f6",
        "group": "914d09d8.a443a8",
        "order": 7,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "led type",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 700,
        "y": 380,
        "wires": []
    },
    {
        "id": "331eebb.035c894",
        "type": "ui_text",
        "z": "b0d89d.a5c83f6",
        "group": "914d09d8.a443a8",
        "order": 8,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Start Date",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 700,
        "y": 420,
        "wires": []
    },
    {
        "id": "d3f27bc2.7d70d8",
        "type": "function",
        "z": "b0d89d.a5c83f6",
        "name": "Change Mode",
        "func": "var message = msg.payload;\nvar autoMessage = {payload: \"AUTO\"}\nvar manualMessage = {payload: \"MANUAL\" }\n\nif (message == \"STATE 1\") {\n    return [autoMessage,[]];\n}\nelse if (message == \"STATE 0\") {\n    return [[], manualMessage];\n}",
        "outputs": 2,
        "noerr": 0,
        "x": 360,
        "y": 580,
        "wires": [
            [
                "c835dc38.7e06b8"
            ],
            [
                "c88f0629.dc039"
            ]
        ]
    },
    {
        "id": "2bd80362.df5aac",
        "type": "ui_text",
        "z": "b0d89d.a5c83f6",
        "group": "7231eec0.8789b8",
        "order": 2,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "MODE",
        "format": "<font color= {{msg.color}}>{{msg.payload}}</font>",
        "layout": "row-spread",
        "x": 750,
        "y": 580,
        "wires": []
    },
    {
        "id": "743d4838.f85128",
        "type": "function",
        "z": "b0d89d.a5c83f6",
        "name": "filter status",
        "func": "var status = msg.payload\nif (status.name == \"status\") {\n    var daysPassed = {payload: status.daysPassed}\n    var currentStage = {payload: status.currentStage}\n}\nreturn [daysPassed,currentStage];",
        "outputs": 2,
        "noerr": 0,
        "x": 470,
        "y": 500,
        "wires": [
            [
                "de7706b3.976f7"
            ],
            [
                "7860ba60.1843a4"
            ]
        ]
    },
    {
        "id": "7860ba60.1843a4",
        "type": "ui_text",
        "z": "b0d89d.a5c83f6",
        "group": "914d09d8.a443a8",
        "order": 11,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Current Stage",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 720,
        "y": 520,
        "wires": []
    },
    {
        "id": "de7706b3.976f7",
        "type": "ui_text",
        "z": "b0d89d.a5c83f6",
        "group": "914d09d8.a443a8",
        "order": 10,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Days Passed",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 710,
        "y": 480,
        "wires": []
    },
    {
        "id": "75a57000.1be058",
        "type": "mqtt in",
        "z": "b0d89d.a5c83f6",
        "name": "",
        "topic": "RACK1",
        "qos": "2",
        "broker": "7a5cc18b.d2b4d8",
        "x": 150,
        "y": 660,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "4f11abfd.92a914",
        "type": "function",
        "z": "b0d89d.a5c83f6",
        "name": "Command Parser",
        "func": "var output = {payload:msg.payload};\n\nvar words = msg.payload.split(\" \");\nif (words[0]==\"PU1\" || words[0]==\"DR1\" || \nwords[0]==\"PU2\" || words[0]==\"DR2\" ||\nwords[0]==\"PU3\" || words[0]==\"DR3\" ||\nwords[0]==\"PU4\" || words[0]==\"DR4\") {\n    return [output,[],[]];\n}\nif (words[0]==\"LP1\" || words[0]==\"LD1\" ||\nwords[0]==\"LP2\" || words[0]==\"LD2\" ||\nwords[0]==\"LP3\" || words[0]==\"LD3\" ||\nwords[0]==\"LP0\" || words[0]==\"LD0\") {\n    return [[],output,[]];\n}\nif (words[0]==\"AEC\" || words[0]==\"EC\" ||\nwords[0]==\"NP\" || words[0]==\"PU\" ||\nwords[0]==\"NPA\" || words[0]==\"NPB\") {\n    return [[],[],output];\n}",
        "outputs": 3,
        "noerr": 0,
        "x": 450,
        "y": 740,
        "wires": [
            [
                "5af423ac.3e4f6c",
                "94557e85.62fd2"
            ],
            [
                "8aeff1cc.6a04d8",
                "4f521af.0a763e4"
            ],
            [
                "2adda91f.1ab7ce",
                "2c4d8e54.e78eca"
            ]
        ]
    },
    {
        "id": "da21252e.610648",
        "type": "ui_text_input",
        "z": "b0d89d.a5c83f6",
        "name": "",
        "label": "Manual cmd",
        "tooltip": "",
        "group": "7231eec0.8789b8",
        "order": 3,
        "width": 0,
        "height": 0,
        "passthru": true,
        "mode": "text",
        "delay": "0",
        "topic": "",
        "x": 130,
        "y": 720,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "8aeff1cc.6a04d8",
        "type": "debug",
        "z": "b0d89d.a5c83f6",
        "name": "USB1",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "x": 750,
        "y": 740,
        "wires": []
    },
    {
        "id": "2adda91f.1ab7ce",
        "type": "debug",
        "z": "b0d89d.a5c83f6",
        "name": "USB2",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "x": 750,
        "y": 780,
        "wires": []
    },
    {
        "id": "8685cef4.d5904",
        "type": "mqtt in",
        "z": "b0d89d.a5c83f6",
        "name": "",
        "topic": "RACK1",
        "qos": "2",
        "broker": "7a5cc18b.d2b4d8",
        "x": 170,
        "y": 580,
        "wires": [
            [
                "d3f27bc2.7d70d8"
            ]
        ]
    },
    {
        "id": "c835dc38.7e06b8",
        "type": "change",
        "z": "b0d89d.a5c83f6",
        "name": "auto set green",
        "rules": [
            {
                "t": "set",
                "p": "color",
                "pt": "msg",
                "to": "lime",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 560,
        "y": 560,
        "wires": [
            [
                "2bd80362.df5aac"
            ]
        ]
    },
    {
        "id": "c88f0629.dc039",
        "type": "change",
        "z": "b0d89d.a5c83f6",
        "name": "manual sett red",
        "rules": [
            {
                "t": "set",
                "p": "color",
                "pt": "msg",
                "to": "red",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 560,
        "y": 600,
        "wires": [
            [
                "2bd80362.df5aac"
            ]
        ]
    },
    {
        "id": "5af423ac.3e4f6c",
        "type": "debug",
        "z": "b0d89d.a5c83f6",
        "name": "USB0",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "x": 750,
        "y": 700,
        "wires": []
    },
    {
        "id": "b7860928.0073e",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH1 PUMP ON",
        "group": "54130e1f.ba719",
        "order": 3,
        "width": "3",
        "height": "2",
        "passthru": false,
        "label": "PUMP ON",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "PU1 1",
        "payloadType": "str",
        "topic": "",
        "x": 200,
        "y": 780,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "9231387b.0ae568",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH1 PUMP OFF",
        "group": "54130e1f.ba719",
        "order": 3,
        "width": "3",
        "height": "2",
        "passthru": false,
        "label": "PUMP OFF",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "PU1 0",
        "payloadType": "str",
        "topic": "",
        "x": 200,
        "y": 820,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "1eccf474.48c854",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH1 DRAIN ON",
        "group": "54130e1f.ba719",
        "order": 3,
        "width": "3",
        "height": "2",
        "passthru": false,
        "label": "DRAIN ON",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "DR1 1",
        "payloadType": "str",
        "topic": "",
        "x": 200,
        "y": 860,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "4f8ff490.b0bc64",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH1 DRAIN OFF",
        "group": "54130e1f.ba719",
        "order": 3,
        "width": "3",
        "height": "2",
        "passthru": false,
        "label": "DRAIN OFF",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "DR1 0",
        "payloadType": "str",
        "topic": "",
        "x": 190,
        "y": 900,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "77a105b5.0df734",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "FILL TANK",
        "group": "7231eec0.8789b8",
        "order": 3,
        "width": "6",
        "height": "2",
        "passthru": false,
        "label": "FILL TANK",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "PU 1",
        "payloadType": "str",
        "topic": "",
        "x": 210,
        "y": 960,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "afc2a1e3.df38e",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CHECK EC",
        "group": "7231eec0.8789b8",
        "order": 3,
        "width": "6",
        "height": "2",
        "passthru": false,
        "label": "CHECK EC",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "EC 1",
        "payloadType": "str",
        "topic": "",
        "x": 210,
        "y": 1000,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "5b0a9072.8a8b08",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "ADD NUTRIENTS",
        "group": "7231eec0.8789b8",
        "order": 3,
        "width": "6",
        "height": "2",
        "passthru": false,
        "label": "ADD NUTRIENTS",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "AEC 1",
        "payloadType": "str",
        "topic": "",
        "x": 190,
        "y": 1040,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "7ed58c89.a4d2f4",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH1 LIGHT ON",
        "group": "54130e1f.ba719",
        "order": 3,
        "width": "3",
        "height": "2",
        "passthru": false,
        "label": "LIGHT ON",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "LP1 100",
        "payloadType": "str",
        "topic": "",
        "x": 460,
        "y": 840,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "e618adf6.5fd68",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH1 LIGHT OFF",
        "group": "54130e1f.ba719",
        "order": 3,
        "width": "3",
        "height": "2",
        "passthru": false,
        "label": "LIGHT OFF",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "LP1 0",
        "payloadType": "str",
        "topic": "",
        "x": 450,
        "y": 880,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "4e3a3f1e.a1dde",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH1 LIGHT HOME",
        "group": "54130e1f.ba719",
        "order": 3,
        "width": "6",
        "height": "3",
        "passthru": false,
        "label": "LIGHT HOME",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "LD1 0",
        "payloadType": "str",
        "topic": "",
        "x": 450,
        "y": 920,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "6dc86c24.f9d1ac",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH2 PUMP ON",
        "group": "3273adf.aed92d2",
        "order": 3,
        "width": "3",
        "height": "2",
        "passthru": false,
        "label": "PUMP ON",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "PU2 1",
        "payloadType": "str",
        "topic": "",
        "x": 200,
        "y": 1100,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "abd5a6db.1f4eb",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH2 PUMP OFF",
        "group": "3273adf.aed92d2",
        "order": 3,
        "width": "3",
        "height": "2",
        "passthru": false,
        "label": "PUMP OFF",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "PU2 0",
        "payloadType": "str",
        "topic": "",
        "x": 200,
        "y": 1140,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "42ce9473.a38d7c",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH2 DRAIN ON",
        "group": "3273adf.aed92d2",
        "order": 3,
        "width": "3",
        "height": "2",
        "passthru": false,
        "label": "DRAIN ON",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "DR2 1",
        "payloadType": "str",
        "topic": "",
        "x": 200,
        "y": 1180,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "44a505f4.89728c",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH2 DRAIN OFF",
        "group": "3273adf.aed92d2",
        "order": 3,
        "width": "3",
        "height": "2",
        "passthru": false,
        "label": "DRAIN OFF",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "DR2 0",
        "payloadType": "str",
        "topic": "",
        "x": 190,
        "y": 1220,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "37ef7dfc.114e32",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH2 LIGHT ON",
        "group": "3273adf.aed92d2",
        "order": 3,
        "width": "3",
        "height": "2",
        "passthru": false,
        "label": "LIGHT ON",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "LP2 100",
        "payloadType": "str",
        "topic": "",
        "x": 460,
        "y": 980,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "eb4764a2.991de",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH2 LIGHT OFF",
        "group": "3273adf.aed92d2",
        "order": 3,
        "width": "3",
        "height": "2",
        "passthru": false,
        "label": "LIGHT OFF",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "LP2 0",
        "payloadType": "str",
        "topic": "",
        "x": 450,
        "y": 1020,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "b0aa1f89.d20c88",
        "type": "ui_button",
        "z": "b0d89d.a5c83f6",
        "name": "CH2 LIGHT HOME",
        "group": "3273adf.aed92d2",
        "order": 3,
        "width": "6",
        "height": "3",
        "passthru": false,
        "label": "LIGHT HOME",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "LD2 0",
        "payloadType": "str",
        "topic": "",
        "x": 450,
        "y": 1060,
        "wires": [
            [
                "4f11abfd.92a914"
            ]
        ]
    },
    {
        "id": "94557e85.62fd2",
        "type": "serial out",
        "z": "b0d89d.a5c83f6",
        "name": "",
        "serial": "bb54c2d0.41da8",
        "x": 933.5000152587891,
        "y": 699,
        "wires": []
    },
    {
        "id": "4f521af.0a763e4",
        "type": "serial out",
        "z": "b0d89d.a5c83f6",
        "name": "",
        "serial": "410cfb9.57c5504",
        "x": 933,
        "y": 738.3333740234375,
        "wires": []
    },
    {
        "id": "2c4d8e54.e78eca",
        "type": "serial out",
        "z": "b0d89d.a5c83f6",
        "name": "",
        "serial": "39164a69.1f1356",
        "x": 936,
        "y": 783.3333740234375,
        "wires": []
    },
    {
        "id": "7a5cc18b.d2b4d8",
        "type": "mqtt-broker",
        "z": "",
        "name": "localhost",
        "broker": "localhost",
        "port": "1883",
        "clientid": "",
        "usetls": false,
        "compatmode": true,
        "keepalive": "60",
        "cleansession": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "closeTopic": "",
        "closeQos": "0",
        "closePayload": "",
        "willTopic": "",
        "willQos": "0",
        "willPayload": ""
    },
    {
        "id": "914d09d8.a443a8",
        "type": "ui_group",
        "z": "",
        "name": "STATUS",
        "tab": "a0a500c9.02ed88",
        "order": 1,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "7231eec0.8789b8",
        "type": "ui_group",
        "z": "",
        "name": "CONTROL MAIN",
        "tab": "a0a500c9.02ed88",
        "order": 2,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "54130e1f.ba719",
        "type": "ui_group",
        "z": "",
        "name": "CONTROL CHANNEL 1",
        "tab": "a0a500c9.02ed88",
        "order": 3,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "3273adf.aed92d2",
        "type": "ui_group",
        "z": "",
        "name": "CONTROL CHANNEL 2",
        "tab": "a0a500c9.02ed88",
        "order": 4,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "bb54c2d0.41da8",
        "type": "serial-port",
        "z": "",
        "serialport": "/dev/ttyUSB0",
        "serialbaud": "9600",
        "databits": "8",
        "parity": "none",
        "stopbits": "1",
        "newline": "\\n",
        "bin": "false",
        "out": "char",
        "addchar": false,
        "responsetimeout": "10000"
    },
    {
        "id": "410cfb9.57c5504",
        "type": "serial-port",
        "z": "",
        "serialport": "/dev/ttyUSB1",
        "serialbaud": "9600",
        "databits": "8",
        "parity": "none",
        "stopbits": "1",
        "newline": "\\n",
        "bin": "false",
        "out": "char",
        "addchar": false,
        "responsetimeout": "10000"
    },
    {
        "id": "39164a69.1f1356",
        "type": "serial-port",
        "z": "",
        "serialport": "/dev/ttyUSB2",
        "serialbaud": "9600",
        "databits": "8",
        "parity": "none",
        "stopbits": "1",
        "newline": "\\n",
        "bin": "false",
        "out": "char",
        "addchar": false,
        "responsetimeout": "10000"
    },
    {
        "id": "a0a500c9.02ed88",
        "type": "ui_tab",
        "z": "",
        "name": "Planter",
        "icon": "dashboard",
        "order": 1,
        "disabled": false,
        "hidden": false
    }
]
