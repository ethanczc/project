[
    {
        "id": "46caaa5d.d13e24",
        "type": "tab",
        "label": "Planter-2.1 Main",
        "disabled": false,
        "info": ""
    },
    {
        "id": "d5123153.cc133",
        "type": "inject",
        "z": "46caaa5d.d13e24",
        "name": "CLOCK",
        "topic": "clock",
        "payload": "1s",
        "payloadType": "str",
        "repeat": "1",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 120,
        "y": 40,
        "wires": [
            [
                "77eb6991.d3bed8"
            ]
        ]
    },
    {
        "id": "7dd2fbf7.082784",
        "type": "inject",
        "z": "46caaa5d.d13e24",
        "name": "",
        "topic": "",
        "payload": "EC 1.0",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 110,
        "y": 80,
        "wires": [
            [
                "c29c18d4.f66ff8"
            ]
        ]
    },
    {
        "id": "c29c18d4.f66ff8",
        "type": "function",
        "z": "46caaa5d.d13e24",
        "name": "AEC parser",
        "func": "data = (msg.payload).split(\" \");\nmessage = {};\nif (data[0] == \"EC\") {\n    message.payload = {\n        \"topic\": \"EC\",\n        \"ec\": data[1]\n    }\n}\nelse if (data[0] == \"AEC\"){\n    message.payload = {\n        \"topic\": \"AEC\",\n        \"ec\": data[1]\n    }\n}\n\nreturn message;",
        "outputs": 1,
        "noerr": 0,
        "x": 290,
        "y": 80,
        "wires": [
            [
                "3b08ed1d.c48502",
                "411aaa66.f71d94"
            ]
        ]
    },
    {
        "id": "77eb6991.d3bed8",
        "type": "function",
        "z": "46caaa5d.d13e24",
        "name": "clock",
        "func": "message = {};\nmessage.payload = {\n    \"topic\": \"clock\",\n    \"payload\": \"1s\"\n}\nreturn message;",
        "outputs": 1,
        "noerr": 0,
        "x": 270,
        "y": 40,
        "wires": [
            [
                "3b08ed1d.c48502"
            ]
        ]
    },
    {
        "id": "3b08ed1d.c48502",
        "type": "mqtt out",
        "z": "46caaa5d.d13e24",
        "name": "",
        "topic": "planter_recipe",
        "qos": "2",
        "retain": "",
        "broker": "5faf7bfe.0debb4",
        "x": 500,
        "y": 40,
        "wires": []
    },
    {
        "id": "5d655023.b0805",
        "type": "function",
        "z": "46caaa5d.d13e24",
        "name": "main recipe",
        "func": "context.recipe = context.recipe || {};\n\nswitch (msg.topic) {\n    case \"stage1Duration\":     context.recipe.stage1Duration = msg.payload; break;\n    case \"stage2Duration\":    context.recipe.stage2Duration = msg.payload; break;\n    case \"stage3Duration\":  context.recipe.stage3Duration = msg.payload; break;\n    case \"stage1Ec\": context.recipe.stage1Ec = msg.payload; break;\n    case \"stage2Ec\":  context.recipe.stage2Ec = msg.payload; break;\n    case \"stage3Ec\": context.recipe.stage3Ec = msg.payload; break;\n    case \"startDate\": context.recipe.startDate = msg.payload; break;\n    case \"autoMode\": context.recipe.autoMode = msg.payload; break;\n}\njsonObj={}\njsonObj.payload = {\n    \"topic\" : \"recipeMain\",\n    \"stage1Duration\" : context.recipe.stage1Duration,\n    \"stage2Duration\" : context.recipe.stage2Duration,\n    \"stage3Duration\" : context.recipe.stage3Duration,\n    \"stage1Ec\" : context.recipe.stage1Ec,\n    \"stage2Ec\" : context.recipe.stage2Ec,\n    \"stage3Ec\" : context.recipe.stage3Ec,\n    \"startDate\" : context.recipe.startDate,\n    \"autoMode\" : context.recipe.autoMode\n}\nreturn jsonObj;\n",
        "outputs": 1,
        "noerr": 0,
        "x": 350,
        "y": 420,
        "wires": [
            [
                "ce18f5a0.667e68"
            ]
        ]
    },
    {
        "id": "b18957b0.182a08",
        "type": "ui_text_input",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "Start Date",
        "tooltip": "",
        "group": "c65ce6fc.7abe58",
        "order": 1,
        "width": "4",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "startDate",
        "x": 130,
        "y": 320,
        "wires": [
            [
                "5d655023.b0805"
            ]
        ]
    },
    {
        "id": "1e8505e5.b4635a",
        "type": "ui_switch",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "Auto",
        "tooltip": "",
        "group": "c65ce6fc.7abe58",
        "order": 12,
        "width": "4",
        "height": "1",
        "passthru": true,
        "decouple": "false",
        "topic": "autoMode",
        "style": "",
        "onvalue": "true",
        "onvalueType": "bool",
        "onicon": "",
        "oncolor": "",
        "offvalue": "false",
        "offvalueType": "bool",
        "officon": "",
        "offcolor": "",
        "x": 150,
        "y": 280,
        "wires": [
            [
                "5d655023.b0805"
            ]
        ]
    },
    {
        "id": "82f67a5c.7208a8",
        "type": "ui_slider",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "Stage 1 duration",
        "tooltip": "",
        "group": "c65ce6fc.7abe58",
        "order": 5,
        "width": "8",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "stage1Duration",
        "min": 0,
        "max": "15",
        "step": 1,
        "x": 110,
        "y": 360,
        "wires": [
            [
                "5d655023.b0805"
            ]
        ]
    },
    {
        "id": "fb269cce.b0343",
        "type": "ui_slider",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "Stage 2 Duration",
        "tooltip": "",
        "group": "c65ce6fc.7abe58",
        "order": 7,
        "width": "8",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "stage2Duration",
        "min": 0,
        "max": "15",
        "step": 1,
        "x": 110,
        "y": 440,
        "wires": [
            [
                "5d655023.b0805"
            ]
        ]
    },
    {
        "id": "97518bdd.6b51a8",
        "type": "ui_slider",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "Stage 3 Duration",
        "tooltip": "",
        "group": "c65ce6fc.7abe58",
        "order": 9,
        "width": "8",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "stage3Duration",
        "min": 0,
        "max": "50",
        "step": 1,
        "x": 110,
        "y": 520,
        "wires": [
            [
                "5d655023.b0805"
            ]
        ]
    },
    {
        "id": "91daeffb.c9c2f",
        "type": "ui_slider",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "stage 1 ec",
        "tooltip": "",
        "group": "c65ce6fc.7abe58",
        "order": 6,
        "width": "8",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "stage1Ec",
        "min": 0,
        "max": "2.0",
        "step": "0.1",
        "x": 130,
        "y": 400,
        "wires": [
            [
                "5d655023.b0805"
            ]
        ]
    },
    {
        "id": "1d53b438.94532c",
        "type": "function",
        "z": "46caaa5d.d13e24",
        "name": "Command Parser to Output",
        "func": "var output = {payload:msg.payload};\n\nvar words = msg.payload.split(\" \");\n\nif (words[0]==\"PU1\" || words[0]==\"DR1\" || \nwords[0]==\"PU2\" || words[0]==\"DR2\" ||\nwords[0]==\"PU3\" || words[0]==\"DR3\" ||\nwords[0]==\"PU4\" || words[0]==\"DR4\") {\n    return [output,[],[]];\n}\nif (words[0]==\"LP1\" || words[0]==\"LD1\" ||\nwords[0]==\"LP2\" || words[0]==\"LD2\" ||\nwords[0]==\"LP3\" || words[0]==\"LD3\") {\n    return [[],output,[]];\n}\nif (words[0]==\"AEC\" || words[0]==\"EC\" ||\nwords[0]==\"NP\" || words[0]==\"PU\" ||\nwords[0]==\"NPA\" || words[0]==\"NPB\") {\n    return [[],[],output];\n}\n",
        "outputs": 3,
        "noerr": 0,
        "x": 380,
        "y": 200,
        "wires": [
            [
                "55f4df7c.0c632"
            ],
            [
                "76f3fb15.39fa74"
            ],
            [
                "c96eadd5.09c19"
            ]
        ]
    },
    {
        "id": "2d259544.2bebfa",
        "type": "ui_text",
        "z": "46caaa5d.d13e24",
        "group": "c65ce6fc.7abe58",
        "order": 2,
        "width": "4",
        "height": "1",
        "name": "",
        "label": "Days Passed",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 580,
        "y": 260,
        "wires": []
    },
    {
        "id": "8f914180.3f5f3",
        "type": "function",
        "z": "46caaa5d.d13e24",
        "name": "days pass stage check",
        "func": "words = (msg.payload).split(\" \")\n\nif (words[0] == \"DAYS\") {\n    output = {payload : words[1]}\n    return [output,[],[]];\n}\nelse if (words[0] == \"STAGE\") {\n    output = {payload: words[1]}\n    return [[],output,[]];\n}\nelse if (words[0] == \"EC\") {\n    output = {payload:words[1]}\n    return [[],[],output]\n}\n",
        "outputs": 3,
        "noerr": 0,
        "x": 350,
        "y": 280,
        "wires": [
            [
                "2d259544.2bebfa"
            ],
            [
                "ca7fccd1.cc135"
            ],
            []
        ]
    },
    {
        "id": "ca7fccd1.cc135",
        "type": "ui_text",
        "z": "46caaa5d.d13e24",
        "group": "c65ce6fc.7abe58",
        "order": 3,
        "width": "4",
        "height": "1",
        "name": "",
        "label": "Current Stage",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 580,
        "y": 300,
        "wires": []
    },
    {
        "id": "98d17dba.e6d42",
        "type": "ui_text_input",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "CMD Input",
        "tooltip": "",
        "group": "c65ce6fc.7abe58",
        "order": 11,
        "width": "4",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "0",
        "topic": "",
        "x": 150,
        "y": 160,
        "wires": [
            [
                "1d53b438.94532c"
            ]
        ]
    },
    {
        "id": "74c96a4d.5b1b34",
        "type": "mqtt in",
        "z": "46caaa5d.d13e24",
        "name": "",
        "topic": "planter_command",
        "qos": "2",
        "broker": "5faf7bfe.0debb4",
        "x": 130,
        "y": 220,
        "wires": [
            [
                "1d53b438.94532c",
                "8f914180.3f5f3",
                "62625dee.a5b454"
            ]
        ]
    },
    {
        "id": "e8855c6.11dfea",
        "type": "ui_slider",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "stage 2 ec",
        "tooltip": "",
        "group": "c65ce6fc.7abe58",
        "order": 8,
        "width": "8",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "stage2Ec",
        "min": 0,
        "max": "2.0",
        "step": "0.1",
        "x": 130,
        "y": 480,
        "wires": [
            [
                "5d655023.b0805"
            ]
        ]
    },
    {
        "id": "108ae4d6.87420b",
        "type": "ui_slider",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "stage 3 ec",
        "tooltip": "",
        "group": "c65ce6fc.7abe58",
        "order": 10,
        "width": "8",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "stage3Ec",
        "min": 0,
        "max": "2.0",
        "step": "0.1",
        "x": 130,
        "y": 560,
        "wires": [
            [
                "5d655023.b0805"
            ]
        ]
    },
    {
        "id": "ce18f5a0.667e68",
        "type": "json",
        "z": "46caaa5d.d13e24",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": true,
        "x": 510,
        "y": 420,
        "wires": [
            [
                "8502ceb7.9c5ea",
                "1064d2b7.ed333d"
            ]
        ]
    },
    {
        "id": "8502ceb7.9c5ea",
        "type": "mqtt out",
        "z": "46caaa5d.d13e24",
        "name": "",
        "topic": "planter_recipe",
        "qos": "2",
        "retain": "",
        "broker": "5faf7bfe.0debb4",
        "x": 680,
        "y": 420,
        "wires": []
    },
    {
        "id": "1064d2b7.ed333d",
        "type": "debug",
        "z": "46caaa5d.d13e24",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "x": 650,
        "y": 380,
        "wires": []
    },
    {
        "id": "62625dee.a5b454",
        "type": "debug",
        "z": "46caaa5d.d13e24",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 330,
        "y": 140,
        "wires": []
    },
    {
        "id": "411aaa66.f71d94",
        "type": "ui_text",
        "z": "46caaa5d.d13e24",
        "group": "c65ce6fc.7abe58",
        "order": 13,
        "width": "4",
        "height": "1",
        "name": "",
        "label": "Current Ec",
        "format": "{{msg.payload.ec}}",
        "layout": "row-spread",
        "x": 510,
        "y": 100,
        "wires": []
    },
    {
        "id": "a95f2d14.a6373",
        "type": "serial in",
        "z": "46caaa5d.d13e24",
        "name": "",
        "serial": "2621bf80.7ebba",
        "x": 110,
        "y": 120,
        "wires": [
            [
                "c29c18d4.f66ff8"
            ]
        ]
    },
    {
        "id": "55f4df7c.0c632",
        "type": "serial out",
        "z": "46caaa5d.d13e24",
        "name": "",
        "serial": "d9d29073.85a0f",
        "x": 610,
        "y": 140,
        "wires": []
    },
    {
        "id": "76f3fb15.39fa74",
        "type": "serial out",
        "z": "46caaa5d.d13e24",
        "name": "",
        "serial": "3019d63f.b71efa",
        "x": 610,
        "y": 180,
        "wires": []
    },
    {
        "id": "c96eadd5.09c19",
        "type": "serial out",
        "z": "46caaa5d.d13e24",
        "name": "",
        "serial": "2621bf80.7ebba",
        "x": 610,
        "y": 220,
        "wires": []
    },
    {
        "id": "e413fcb7.39d71",
        "type": "function",
        "z": "46caaa5d.d13e24",
        "name": "Command Parser",
        "func": "var output = {payload:msg.payload};\n\nvar words = msg.payload.split(\" \");\n\nif (words[0]==\"PU1\" || words[0]==\"DR1\" || \nwords[0]==\"PU2\" || words[0]==\"DR2\" ||\nwords[0]==\"PU3\" || words[0]==\"DR3\" ||\nwords[0]==\"PU4\" || words[0]==\"DR4\") {\n    return [output,[],[]];\n}\nif (words[0]==\"LP1\" || words[0]==\"LD1\" ||\nwords[0]==\"LP2\" || words[0]==\"LD2\" ||\nwords[0]==\"LP3\" || words[0]==\"LD3\") {\n    return [[],output,[]];\n}\nif (words[0]==\"AEC\" || words[0]==\"EC\" ||\nwords[0]==\"NP\" || words[0]==\"PU\" ||\nwords[0]==\"NPA\" || words[0]==\"NPB\") {\n    return [[],[],output];\n}\n",
        "outputs": 3,
        "noerr": 0,
        "x": 370,
        "y": 700,
        "wires": [
            [
                "4e41ecc7.2b1454"
            ],
            [
                "edca748f.429908"
            ],
            [
                "b8027037.5b709"
            ]
        ]
    },
    {
        "id": "4e41ecc7.2b1454",
        "type": "serial out",
        "z": "46caaa5d.d13e24",
        "name": "",
        "serial": "d9d29073.85a0f",
        "x": 570,
        "y": 660,
        "wires": []
    },
    {
        "id": "edca748f.429908",
        "type": "serial out",
        "z": "46caaa5d.d13e24",
        "name": "",
        "serial": "3019d63f.b71efa",
        "x": 570,
        "y": 700,
        "wires": []
    },
    {
        "id": "b8027037.5b709",
        "type": "serial out",
        "z": "46caaa5d.d13e24",
        "name": "",
        "serial": "2621bf80.7ebba",
        "x": 570,
        "y": 740,
        "wires": []
    },
    {
        "id": "b20f4be.c6949b8",
        "type": "ui_switch",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "1 Pump",
        "tooltip": "",
        "group": "2f40e90a.9781c6",
        "order": 1,
        "width": "4",
        "height": "1",
        "passthru": true,
        "decouple": "false",
        "topic": "",
        "style": "",
        "onvalue": "PU1 1",
        "onvalueType": "str",
        "onicon": "",
        "oncolor": "",
        "offvalue": "PU1 0",
        "offvalueType": "str",
        "officon": "",
        "offcolor": "",
        "x": 140,
        "y": 600,
        "wires": [
            [
                "e413fcb7.39d71"
            ]
        ]
    },
    {
        "id": "ff57a698.eb9f58",
        "type": "ui_switch",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "1 Light",
        "tooltip": "",
        "group": "2f40e90a.9781c6",
        "order": 3,
        "width": "4",
        "height": "1",
        "passthru": true,
        "decouple": "false",
        "topic": "",
        "style": "",
        "onvalue": "LP1 50",
        "onvalueType": "str",
        "onicon": "",
        "oncolor": "",
        "offvalue": "LP1 0",
        "offvalueType": "str",
        "officon": "",
        "offcolor": "",
        "x": 150,
        "y": 680,
        "wires": [
            [
                "e413fcb7.39d71"
            ]
        ]
    },
    {
        "id": "52675e3.9d950a",
        "type": "ui_button",
        "z": "46caaa5d.d13e24",
        "name": "",
        "group": "2f40e90a.9781c6",
        "order": 4,
        "width": "4",
        "height": "1",
        "passthru": false,
        "label": "1 Light Home",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "LD1 0",
        "payloadType": "str",
        "topic": "",
        "x": 130,
        "y": 720,
        "wires": [
            [
                "e413fcb7.39d71"
            ]
        ]
    },
    {
        "id": "de459648.8a2a78",
        "type": "ui_switch",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "2 Pump",
        "tooltip": "",
        "group": "2f40e90a.9781c6",
        "order": 5,
        "width": "4",
        "height": "1",
        "passthru": true,
        "decouple": "false",
        "topic": "",
        "style": "",
        "onvalue": "PU2 1",
        "onvalueType": "str",
        "onicon": "",
        "oncolor": "",
        "offvalue": "PU2 0",
        "offvalueType": "str",
        "officon": "",
        "offcolor": "",
        "x": 140,
        "y": 760,
        "wires": [
            [
                "e413fcb7.39d71"
            ]
        ]
    },
    {
        "id": "de0f120a.fb293",
        "type": "ui_switch",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "2 Light",
        "tooltip": "",
        "group": "2f40e90a.9781c6",
        "order": 7,
        "width": "4",
        "height": "1",
        "passthru": true,
        "decouple": "false",
        "topic": "",
        "style": "",
        "onvalue": "LP2 50",
        "onvalueType": "str",
        "onicon": "",
        "oncolor": "",
        "offvalue": "LP2 0",
        "offvalueType": "str",
        "officon": "",
        "offcolor": "",
        "x": 150,
        "y": 840,
        "wires": [
            [
                "e413fcb7.39d71"
            ]
        ]
    },
    {
        "id": "10365621.e96e8a",
        "type": "ui_button",
        "z": "46caaa5d.d13e24",
        "name": "",
        "group": "2f40e90a.9781c6",
        "order": 8,
        "width": "4",
        "height": "1",
        "passthru": false,
        "label": "2 Light Home",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "LD2 0",
        "payloadType": "str",
        "topic": "",
        "x": 120,
        "y": 880,
        "wires": [
            [
                "e413fcb7.39d71"
            ]
        ]
    },
    {
        "id": "4e9e2c6d.6d58a4",
        "type": "ui_switch",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "1 Drain",
        "tooltip": "",
        "group": "2f40e90a.9781c6",
        "order": 2,
        "width": "4",
        "height": "1",
        "passthru": true,
        "decouple": "false",
        "topic": "",
        "style": "",
        "onvalue": "DR1 1",
        "onvalueType": "str",
        "onicon": "",
        "oncolor": "",
        "offvalue": "DR1 0",
        "offvalueType": "str",
        "officon": "",
        "offcolor": "",
        "x": 140,
        "y": 640,
        "wires": [
            [
                "e413fcb7.39d71"
            ]
        ]
    },
    {
        "id": "c97dde.6bc1822",
        "type": "ui_switch",
        "z": "46caaa5d.d13e24",
        "name": "",
        "label": "2 Drain",
        "tooltip": "",
        "group": "2f40e90a.9781c6",
        "order": 6,
        "width": "4",
        "height": "1",
        "passthru": true,
        "decouple": "false",
        "topic": "",
        "style": "",
        "onvalue": "DR2 1",
        "onvalueType": "str",
        "onicon": "",
        "oncolor": "",
        "offvalue": "DR2 0",
        "offvalueType": "str",
        "officon": "",
        "offcolor": "",
        "x": 140,
        "y": 800,
        "wires": [
            [
                "e413fcb7.39d71"
            ]
        ]
    },
    {
        "id": "5faf7bfe.0debb4",
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
        "id": "c65ce6fc.7abe58",
        "type": "ui_group",
        "z": "",
        "name": "Setup",
        "tab": "5382749a.63059c",
        "order": 1,
        "disp": true,
        "width": "16",
        "collapse": false
    },
    {
        "id": "2621bf80.7ebba",
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
        "id": "d9d29073.85a0f",
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
        "id": "3019d63f.b71efa",
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
        "id": "2f40e90a.9781c6",
        "type": "ui_group",
        "z": "",
        "name": "Controls",
        "tab": "5382749a.63059c",
        "order": 2,
        "disp": true,
        "width": "16",
        "collapse": false
    },
    {
        "id": "5382749a.63059c",
        "type": "ui_tab",
        "z": "",
        "name": "Planter-2.1 Main",
        "icon": "dashboard",
        "order": 8,
        "disabled": false,
        "hidden": false
    }
]
