[
    {
        "id": "8f21f826.8fb24",
        "type": "tab",
        "label": "Planter-2.1 Main",
        "disabled": false,
        "info": ""
    },
    {
        "id": "cad9f092.c95788",
        "type": "inject",
        "z": "8f21f826.8fb24",
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
                "f39c283b.56b3f8"
            ]
        ]
    },
    {
        "id": "eca62655.f29c7",
        "type": "inject",
        "z": "8f21f826.8fb24",
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
                "baface86.795288"
            ]
        ]
    },
    {
        "id": "baface86.795288",
        "type": "function",
        "z": "8f21f826.8fb24",
        "name": "AEC parser",
        "func": "data = (msg.payload).split(\" \");\nmessage = {};\nmessage.payload = {\n    \"topic\": \"AEC\",\n    \"ec\": data[1]\n}\nreturn message;",
        "outputs": 1,
        "noerr": 0,
        "x": 290,
        "y": 80,
        "wires": [
            [
                "fa4495bc.802e8",
                "46d94d17.7360bc"
            ]
        ]
    },
    {
        "id": "f39c283b.56b3f8",
        "type": "function",
        "z": "8f21f826.8fb24",
        "name": "clock",
        "func": "message = {};\nmessage.payload = {\n    \"topic\": \"clock\",\n    \"payload\": \"1s\"\n}\nreturn message;",
        "outputs": 1,
        "noerr": 0,
        "x": 270,
        "y": 40,
        "wires": [
            [
                "fa4495bc.802e8"
            ]
        ]
    },
    {
        "id": "fa4495bc.802e8",
        "type": "mqtt out",
        "z": "8f21f826.8fb24",
        "name": "",
        "topic": "planter_recipe",
        "qos": "2",
        "retain": "",
        "broker": "a113a6e8.11ab8",
        "x": 500,
        "y": 40,
        "wires": []
    },
    {
        "id": "8aca7af2.85784",
        "type": "function",
        "z": "8f21f826.8fb24",
        "name": "main recipe",
        "func": "context.recipe = context.recipe || {};\n\nswitch (msg.topic) {\n    case \"stage1Duration\":     context.recipe.stage1Duration = msg.payload; break;\n    case \"stage2Duration\":    context.recipe.stage2Duration = msg.payload; break;\n    case \"stage3Duration\":  context.recipe.stage3Duration = msg.payload; break;\n    case \"stage1Ec\": context.recipe.stage1Ec = msg.payload; break;\n    case \"stage2Ec\":  context.recipe.stage2Ec = msg.payload; break;\n    case \"stage3Ec\": context.recipe.stage3Ec = msg.payload; break;\n    case \"startDate\": context.recipe.startDate = msg.payload; break;\n    case \"autoMode\": context.recipe.autoMode = msg.payload; break;\n}\njsonObj={}\njsonObj.payload = {\n    \"topic\" : \"recipeMain\",\n    \"stage1Duration\" : context.recipe.stage1Duration,\n    \"stage2Duration\" : context.recipe.stage2Duration,\n    \"stage3Duration\" : context.recipe.stage3Duration,\n    \"stage1Ec\" : context.recipe.stage1Ec,\n    \"stage2Ec\" : context.recipe.stage2Ec,\n    \"stage3Ec\" : context.recipe.stage3Ec,\n    \"startDate\" : context.recipe.startDate,\n    \"autoMode\" : context.recipe.autoMode\n}\nreturn jsonObj;\n",
        "outputs": 1,
        "noerr": 0,
        "x": 350,
        "y": 420,
        "wires": [
            [
                "4110a22d.bfbd64"
            ]
        ]
    },
    {
        "id": "eecfe36e.7eb438",
        "type": "ui_text_input",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "Start Date",
        "tooltip": "",
        "group": "7699a3e1.eb10d4",
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
                "8aca7af2.85784"
            ]
        ]
    },
    {
        "id": "873dc6f4.78acb8",
        "type": "ui_switch",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "Auto",
        "tooltip": "",
        "group": "7699a3e1.eb10d4",
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
                "8aca7af2.85784"
            ]
        ]
    },
    {
        "id": "dff1b61e.2cd648",
        "type": "ui_slider",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "Stage 1 duration",
        "tooltip": "",
        "group": "7699a3e1.eb10d4",
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
                "8aca7af2.85784"
            ]
        ]
    },
    {
        "id": "e17f0a05.0793",
        "type": "ui_slider",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "Stage 2 Duration",
        "tooltip": "",
        "group": "7699a3e1.eb10d4",
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
                "8aca7af2.85784"
            ]
        ]
    },
    {
        "id": "ef7aeea4.a52fb",
        "type": "ui_slider",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "Stage 3 Duration",
        "tooltip": "",
        "group": "7699a3e1.eb10d4",
        "order": 9,
        "width": "8",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "stage3Duration",
        "min": 0,
        "max": "15",
        "step": 1,
        "x": 110,
        "y": 520,
        "wires": [
            [
                "8aca7af2.85784"
            ]
        ]
    },
    {
        "id": "7deefb2a.18db9c",
        "type": "ui_slider",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "stage 1 ec",
        "tooltip": "",
        "group": "7699a3e1.eb10d4",
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
                "8aca7af2.85784"
            ]
        ]
    },
    {
        "id": "c2f0743d.4b5de",
        "type": "function",
        "z": "8f21f826.8fb24",
        "name": "Command Parser to Output",
        "func": "var output = {payload:msg.payload};\n\nvar words = msg.payload.split(\" \");\n\nif (words[0]==\"PU1\" || words[0]==\"DR1\" || \nwords[0]==\"PU2\" || words[0]==\"DR2\" ||\nwords[0]==\"PU3\" || words[0]==\"DR3\" ||\nwords[0]==\"PU4\" || words[0]==\"DR4\") {\n    return [output,[],[]];\n}\nif (words[0]==\"LP1\" || words[0]==\"LD1\" ||\nwords[0]==\"LP2\" || words[0]==\"LD2\" ||\nwords[0]==\"LP3\" || words[0]==\"LD3\") {\n    return [[],output,[]];\n}\nif (words[0]==\"AEC\" || words[0]==\"EC\" ||\nwords[0]==\"NP\" || words[0]==\"PU\" ||\nwords[0]==\"NPA\" || words[0]==\"NPB\") {\n    return [[],[],output];\n}\n",
        "outputs": 3,
        "noerr": 0,
        "x": 380,
        "y": 200,
        "wires": [
            [
                "d5cefff2.e58b48"
            ],
            [
                "b5470159.a9c34"
            ],
            [
                "3dd22f7c.c6e2a"
            ]
        ]
    },
    {
        "id": "a82fc766.e176d8",
        "type": "ui_text",
        "z": "8f21f826.8fb24",
        "group": "7699a3e1.eb10d4",
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
        "id": "83780fdb.ad4c1",
        "type": "function",
        "z": "8f21f826.8fb24",
        "name": "days pass stage check",
        "func": "words = (msg.payload).split(\" \")\n\nif (words[0] == \"DAYS\") {\n    output = {payload : words[1]}\n    return [output,[],[]];\n}\nelse if (words[0] == \"STAGE\") {\n    output = {payload: words[1]}\n    return [[],output,[]];\n}\nelse if (words[0] == \"EC\") {\n    output = {payload:words[1]}\n    return [[],[],output]\n}\n",
        "outputs": 3,
        "noerr": 0,
        "x": 350,
        "y": 280,
        "wires": [
            [
                "a82fc766.e176d8"
            ],
            [
                "21957563.b9637a"
            ],
            []
        ]
    },
    {
        "id": "21957563.b9637a",
        "type": "ui_text",
        "z": "8f21f826.8fb24",
        "group": "7699a3e1.eb10d4",
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
        "id": "b1716b29.0a2488",
        "type": "ui_text_input",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "CMD Input",
        "tooltip": "",
        "group": "7699a3e1.eb10d4",
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
                "c2f0743d.4b5de"
            ]
        ]
    },
    {
        "id": "3e879fec.1941a",
        "type": "mqtt in",
        "z": "8f21f826.8fb24",
        "name": "",
        "topic": "planter_command",
        "qos": "2",
        "broker": "a113a6e8.11ab8",
        "x": 130,
        "y": 220,
        "wires": [
            [
                "c2f0743d.4b5de",
                "83780fdb.ad4c1",
                "2b083e96.d05d82"
            ]
        ]
    },
    {
        "id": "e17732aa.a0105",
        "type": "ui_slider",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "stage 2 ec",
        "tooltip": "",
        "group": "7699a3e1.eb10d4",
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
                "8aca7af2.85784"
            ]
        ]
    },
    {
        "id": "1f5f7a0.4ed0b86",
        "type": "ui_slider",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "stage 3 ec",
        "tooltip": "",
        "group": "7699a3e1.eb10d4",
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
                "8aca7af2.85784"
            ]
        ]
    },
    {
        "id": "4110a22d.bfbd64",
        "type": "json",
        "z": "8f21f826.8fb24",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": true,
        "x": 510,
        "y": 420,
        "wires": [
            [
                "d9bce6ec.715508",
                "eef552a9.4df988"
            ]
        ]
    },
    {
        "id": "d9bce6ec.715508",
        "type": "mqtt out",
        "z": "8f21f826.8fb24",
        "name": "",
        "topic": "planter_recipe",
        "qos": "2",
        "retain": "",
        "broker": "a113a6e8.11ab8",
        "x": 680,
        "y": 420,
        "wires": []
    },
    {
        "id": "eef552a9.4df988",
        "type": "debug",
        "z": "8f21f826.8fb24",
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
        "id": "2b083e96.d05d82",
        "type": "debug",
        "z": "8f21f826.8fb24",
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
        "id": "46d94d17.7360bc",
        "type": "ui_text",
        "z": "8f21f826.8fb24",
        "group": "7699a3e1.eb10d4",
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
        "id": "34a09cd5.13507c",
        "type": "serial in",
        "z": "8f21f826.8fb24",
        "name": "",
        "serial": "a62176f8.8fb498",
        "x": 110,
        "y": 120,
        "wires": [
            [
                "baface86.795288"
            ]
        ]
    },
    {
        "id": "d5cefff2.e58b48",
        "type": "serial out",
        "z": "8f21f826.8fb24",
        "name": "",
        "serial": "5b659562.0df30c",
        "x": 610,
        "y": 140,
        "wires": []
    },
    {
        "id": "b5470159.a9c34",
        "type": "serial out",
        "z": "8f21f826.8fb24",
        "name": "",
        "serial": "dc46d5ea.9669",
        "x": 610,
        "y": 180,
        "wires": []
    },
    {
        "id": "3dd22f7c.c6e2a",
        "type": "serial out",
        "z": "8f21f826.8fb24",
        "name": "",
        "serial": "a62176f8.8fb498",
        "x": 610,
        "y": 220,
        "wires": []
    },
    {
        "id": "9ea1f2f.feb799",
        "type": "function",
        "z": "8f21f826.8fb24",
        "name": "Command Parser",
        "func": "var output = {payload:msg.payload};\n\nvar words = msg.payload.split(\" \");\n\nif (words[0]==\"PU1\" || words[0]==\"DR1\" || \nwords[0]==\"PU2\" || words[0]==\"DR2\" ||\nwords[0]==\"PU3\" || words[0]==\"DR3\" ||\nwords[0]==\"PU4\" || words[0]==\"DR4\") {\n    return [output,[],[]];\n}\nif (words[0]==\"LP1\" || words[0]==\"LD1\" ||\nwords[0]==\"LP2\" || words[0]==\"LD2\" ||\nwords[0]==\"LP3\" || words[0]==\"LD3\") {\n    return [[],output,[]];\n}\nif (words[0]==\"AEC\" || words[0]==\"EC\" ||\nwords[0]==\"NP\" || words[0]==\"PU\" ||\nwords[0]==\"NPA\" || words[0]==\"NPB\") {\n    return [[],[],output];\n}\n",
        "outputs": 3,
        "noerr": 0,
        "x": 370,
        "y": 700,
        "wires": [
            [
                "3ef8b3fb.cf1444"
            ],
            [
                "9e33b2ad.e514f8"
            ],
            [
                "5c0e8920.bafe18"
            ]
        ]
    },
    {
        "id": "3ef8b3fb.cf1444",
        "type": "serial out",
        "z": "8f21f826.8fb24",
        "name": "",
        "serial": "5b659562.0df30c",
        "x": 570,
        "y": 660,
        "wires": []
    },
    {
        "id": "9e33b2ad.e514f8",
        "type": "serial out",
        "z": "8f21f826.8fb24",
        "name": "",
        "serial": "dc46d5ea.9669",
        "x": 570,
        "y": 700,
        "wires": []
    },
    {
        "id": "5c0e8920.bafe18",
        "type": "serial out",
        "z": "8f21f826.8fb24",
        "name": "",
        "serial": "a62176f8.8fb498",
        "x": 570,
        "y": 740,
        "wires": []
    },
    {
        "id": "37c183bd.e877cc",
        "type": "ui_switch",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "1 Pump",
        "tooltip": "",
        "group": "9c3a2210.c88648",
        "order": 1,
        "width": "5",
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
                "9ea1f2f.feb799"
            ]
        ]
    },
    {
        "id": "d0b5e199.9fd218",
        "type": "ui_switch",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "1 Light",
        "tooltip": "",
        "group": "9c3a2210.c88648",
        "order": 2,
        "width": "5",
        "height": "1",
        "passthru": true,
        "decouple": "false",
        "topic": "",
        "style": "",
        "onvalue": "LP1 1",
        "onvalueType": "str",
        "onicon": "",
        "oncolor": "",
        "offvalue": "LP1 0",
        "offvalueType": "str",
        "officon": "",
        "offcolor": "",
        "x": 150,
        "y": 640,
        "wires": [
            [
                "9ea1f2f.feb799"
            ]
        ]
    },
    {
        "id": "d1901104.16a9b8",
        "type": "ui_button",
        "z": "8f21f826.8fb24",
        "name": "",
        "group": "9c3a2210.c88648",
        "order": 3,
        "width": "5",
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
        "x": 120,
        "y": 680,
        "wires": [
            [
                "9ea1f2f.feb799"
            ]
        ]
    },
    {
        "id": "a8d58a7e.5aa348",
        "type": "ui_switch",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "2 Pump",
        "tooltip": "",
        "group": "9c3a2210.c88648",
        "order": 5,
        "width": "5",
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
        "y": 720,
        "wires": [
            [
                "9ea1f2f.feb799"
            ]
        ]
    },
    {
        "id": "97ce9284.62c9d",
        "type": "ui_switch",
        "z": "8f21f826.8fb24",
        "name": "",
        "label": "2 Light",
        "tooltip": "",
        "group": "9c3a2210.c88648",
        "order": 6,
        "width": "5",
        "height": "1",
        "passthru": true,
        "decouple": "false",
        "topic": "",
        "style": "",
        "onvalue": "LP2 1",
        "onvalueType": "str",
        "onicon": "",
        "oncolor": "",
        "offvalue": "LP2 0",
        "offvalueType": "str",
        "officon": "",
        "offcolor": "",
        "x": 150,
        "y": 760,
        "wires": [
            [
                "9ea1f2f.feb799"
            ]
        ]
    },
    {
        "id": "b15bb646.5393e",
        "type": "ui_button",
        "z": "8f21f826.8fb24",
        "name": "",
        "group": "9c3a2210.c88648",
        "order": 7,
        "width": "5",
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
        "y": 800,
        "wires": [
            [
                "9ea1f2f.feb799"
            ]
        ]
    },
    {
        "id": "a113a6e8.11ab8",
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
        "id": "7699a3e1.eb10d4",
        "type": "ui_group",
        "z": "",
        "name": "Setup",
        "tab": "cabd45ec.61c37",
        "order": 1,
        "disp": true,
        "width": "16",
        "collapse": false
    },
    {
        "id": "a62176f8.8fb498",
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
        "id": "5b659562.0df30c",
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
        "id": "dc46d5ea.9669",
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
        "id": "9c3a2210.c88648",
        "type": "ui_group",
        "z": "",
        "name": "Controls",
        "tab": "cabd45ec.61c37",
        "order": 2,
        "disp": true,
        "width": "16",
        "collapse": false
    },
    {
        "id": "cabd45ec.61c37",
        "type": "ui_tab",
        "z": "",
        "name": "Planter-2.1 Main",
        "icon": "dashboard",
        "order": 8,
        "disabled": false,
        "hidden": false
    }
]
