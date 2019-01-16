[
    {
        "id": "f73b7795.e6163",
        "type": "tab",
        "label": "Planter-2.1 Channel 2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "70f26622.ce0898",
        "type": "function",
        "z": "f73b7795.e6163",
        "name": "channel 2 stage 1",
        "func": "context.recipe = context.recipe || {};\n\nswitch (msg.topic) {\n    case \"fill\":     context.recipe.fill = msg.payload; break;\n    case \"drain\":    context.recipe.drain = msg.payload; break;\n    case \"lightOn\":  context.recipe.lightOn = msg.payload; break;\n    case \"lightOff\": context.recipe.lightOff = msg.payload; break;\n    case \"lightPwr\":  context.recipe.lightPwr = msg.payload; break;\n    case \"lightDist\": context.recipe.lightDist = msg.payload; break;\n}\njsonObj={}\njsonObj.payload = {\n    \"topic\" : \"recipe\",\n    \"channel\": 2,\n    \"stage\": 1,\n    \"fill\":         (context.recipe.fill).split(\",\"),\n    \"drain\":        (context.recipe.drain).split(\",\"),\n    \"lightOn\":      (context.recipe.lightOn).split(\",\"),\n    \"lightOff\":     (context.recipe.lightOff).split(\",\"),\n    \"lightPwr\":     context.recipe.lightPwr,\n    \"lightDist\":    context.recipe.lightDist * 1000\n}\nreturn jsonObj;\n",
        "outputs": 1,
        "noerr": 0,
        "x": 310,
        "y": 140,
        "wires": [
            [
                "1bb63b33.74d4a5"
            ]
        ]
    },
    {
        "id": "cb4ac9a3.86dfe8",
        "type": "debug",
        "z": "f73b7795.e6163",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "x": 610,
        "y": 100,
        "wires": []
    },
    {
        "id": "4bf6c3ab.ec3a94",
        "type": "ui_text_input",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "fill",
        "tooltip": "",
        "group": "1a88daa1.43febd",
        "order": 2,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "fill",
        "x": 90,
        "y": 40,
        "wires": [
            [
                "70f26622.ce0898"
            ]
        ]
    },
    {
        "id": "32dca083.dffc4",
        "type": "ui_text_input",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "drain",
        "tooltip": "",
        "group": "1a88daa1.43febd",
        "order": 3,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "drain",
        "x": 90,
        "y": 80,
        "wires": [
            [
                "70f26622.ce0898"
            ]
        ]
    },
    {
        "id": "12fa0143.01191f",
        "type": "ui_slider",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "Power",
        "tooltip": "",
        "group": "1a88daa1.43febd",
        "order": 7,
        "width": "7",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "lightPwr",
        "min": 0,
        "max": "250",
        "step": "10",
        "x": 90,
        "y": 200,
        "wires": [
            [
                "70f26622.ce0898"
            ]
        ]
    },
    {
        "id": "a1ceaee7.394028",
        "type": "ui_slider",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "Distance",
        "tooltip": "",
        "group": "1a88daa1.43febd",
        "order": 8,
        "width": "7",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "lightDist",
        "min": 0,
        "max": "15",
        "step": "1",
        "x": 80,
        "y": 240,
        "wires": [
            [
                "70f26622.ce0898"
            ]
        ]
    },
    {
        "id": "30968433.edbadc",
        "type": "mqtt out",
        "z": "f73b7795.e6163",
        "name": "",
        "topic": "planter_recipe",
        "qos": "2",
        "retain": "",
        "broker": "a113a6e8.11ab8",
        "x": 640,
        "y": 140,
        "wires": []
    },
    {
        "id": "1bb63b33.74d4a5",
        "type": "json",
        "z": "f73b7795.e6163",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": true,
        "x": 470,
        "y": 140,
        "wires": [
            [
                "30968433.edbadc",
                "cb4ac9a3.86dfe8"
            ]
        ]
    },
    {
        "id": "669d0877.db6bf8",
        "type": "ui_text_input",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "Light off",
        "tooltip": "",
        "group": "1a88daa1.43febd",
        "order": 6,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "lightOff",
        "x": 80,
        "y": 160,
        "wires": [
            [
                "70f26622.ce0898"
            ]
        ]
    },
    {
        "id": "ffa46eb0.a1e38",
        "type": "ui_text_input",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "Light on",
        "tooltip": "",
        "group": "1a88daa1.43febd",
        "order": 5,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "lightOn",
        "x": 80,
        "y": 120,
        "wires": [
            [
                "70f26622.ce0898"
            ]
        ]
    },
    {
        "id": "602925b7.d71584",
        "type": "debug",
        "z": "f73b7795.e6163",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "x": 610,
        "y": 340,
        "wires": []
    },
    {
        "id": "c6fb8740.baba58",
        "type": "mqtt out",
        "z": "f73b7795.e6163",
        "name": "",
        "topic": "planter_recipe",
        "qos": "2",
        "retain": "",
        "broker": "a113a6e8.11ab8",
        "x": 640,
        "y": 380,
        "wires": []
    },
    {
        "id": "7a9a1cf2.151074",
        "type": "json",
        "z": "f73b7795.e6163",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": true,
        "x": 470,
        "y": 380,
        "wires": [
            [
                "c6fb8740.baba58",
                "602925b7.d71584"
            ]
        ]
    },
    {
        "id": "141d36fa.c90c69",
        "type": "function",
        "z": "f73b7795.e6163",
        "name": "channel 2 stage 2",
        "func": "context.recipe = context.recipe || {};\n\nswitch (msg.topic) {\n    case \"fill\":     context.recipe.fill = msg.payload; break;\n    case \"drain\":    context.recipe.drain = msg.payload; break;\n    case \"lightOn\":  context.recipe.lightOn = msg.payload; break;\n    case \"lightOff\": context.recipe.lightOff = msg.payload; break;\n    case \"lightPwr\":  context.recipe.lightPwr = msg.payload; break;\n    case \"lightDist\": context.recipe.lightDist = msg.payload; break;\n}\njsonObj={}\njsonObj.payload = {\n    \"topic\" : \"recipe\",\n    \"channel\": 2,\n    \"stage\": 2,\n    \"fill\":         (context.recipe.fill).split(\",\"),\n    \"drain\":        (context.recipe.drain).split(\",\"),\n    \"lightOn\":      (context.recipe.lightOn).split(\",\"),\n    \"lightOff\":     (context.recipe.lightOff).split(\",\"),\n    \"lightPwr\":     context.recipe.lightPwr,\n    \"lightDist\":    context.recipe.lightDist * 1000\n}\nreturn jsonObj;\n",
        "outputs": 1,
        "noerr": 0,
        "x": 310,
        "y": 380,
        "wires": [
            [
                "7a9a1cf2.151074"
            ]
        ]
    },
    {
        "id": "11ad1431.34a2c4",
        "type": "ui_text_input",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "fill",
        "tooltip": "",
        "group": "e5c5ed71.f909b8",
        "order": 1,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "fill",
        "x": 90,
        "y": 280,
        "wires": [
            [
                "141d36fa.c90c69"
            ]
        ]
    },
    {
        "id": "825dfbe4.9f541",
        "type": "ui_text_input",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "drain",
        "tooltip": "",
        "group": "e5c5ed71.f909b8",
        "order": 2,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "drain",
        "x": 90,
        "y": 320,
        "wires": [
            [
                "141d36fa.c90c69"
            ]
        ]
    },
    {
        "id": "57f9b73c.b59af8",
        "type": "ui_text_input",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "Light on",
        "tooltip": "",
        "group": "e5c5ed71.f909b8",
        "order": 3,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "lightOn",
        "x": 80,
        "y": 360,
        "wires": [
            [
                "141d36fa.c90c69"
            ]
        ]
    },
    {
        "id": "c71f8a2f.01ed28",
        "type": "ui_text_input",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "Light off",
        "tooltip": "",
        "group": "e5c5ed71.f909b8",
        "order": 4,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "lightOff",
        "x": 80,
        "y": 400,
        "wires": [
            [
                "141d36fa.c90c69"
            ]
        ]
    },
    {
        "id": "e430d1c1.0dfe88",
        "type": "ui_slider",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "Power",
        "tooltip": "",
        "group": "e5c5ed71.f909b8",
        "order": 5,
        "width": "7",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "lightPwr",
        "min": 0,
        "max": "250",
        "step": "10",
        "x": 90,
        "y": 440,
        "wires": [
            [
                "141d36fa.c90c69"
            ]
        ]
    },
    {
        "id": "5378f4cb.93e854",
        "type": "ui_slider",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "Distance",
        "tooltip": "",
        "group": "e5c5ed71.f909b8",
        "order": 6,
        "width": "7",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "lightDist",
        "min": 0,
        "max": "15",
        "step": "1",
        "x": 80,
        "y": 480,
        "wires": [
            [
                "141d36fa.c90c69"
            ]
        ]
    },
    {
        "id": "11fb4e6d.1792aa",
        "type": "debug",
        "z": "f73b7795.e6163",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "x": 610,
        "y": 580,
        "wires": []
    },
    {
        "id": "5a4eac14.d94994",
        "type": "mqtt out",
        "z": "f73b7795.e6163",
        "name": "",
        "topic": "planter_recipe",
        "qos": "2",
        "retain": "",
        "broker": "a113a6e8.11ab8",
        "x": 640,
        "y": 620,
        "wires": []
    },
    {
        "id": "20d10401.408bd4",
        "type": "json",
        "z": "f73b7795.e6163",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": true,
        "x": 470,
        "y": 620,
        "wires": [
            [
                "5a4eac14.d94994",
                "11fb4e6d.1792aa"
            ]
        ]
    },
    {
        "id": "fde78eff.070e6",
        "type": "function",
        "z": "f73b7795.e6163",
        "name": "channel 2 stage 3",
        "func": "context.recipe = context.recipe || {};\n\nswitch (msg.topic) {\n    case \"fill\":     context.recipe.fill = msg.payload; break;\n    case \"drain\":    context.recipe.drain = msg.payload; break;\n    case \"lightOn\":  context.recipe.lightOn = msg.payload; break;\n    case \"lightOff\": context.recipe.lightOff = msg.payload; break;\n    case \"lightPwr\":  context.recipe.lightPwr = msg.payload; break;\n    case \"lightDist\": context.recipe.lightDist = msg.payload; break;\n}\njsonObj={}\njsonObj.payload = {\n    \"topic\" : \"recipe\",\n    \"channel\": 2,\n    \"stage\": 3,\n    \"fill\":         (context.recipe.fill).split(\",\"),\n    \"drain\":        (context.recipe.drain).split(\",\"),\n    \"lightOn\":      (context.recipe.lightOn).split(\",\"),\n    \"lightOff\":     (context.recipe.lightOff).split(\",\"),\n    \"lightPwr\":     context.recipe.lightPwr,\n    \"lightDist\":    context.recipe.lightDist * 1000\n}\nreturn jsonObj;\n",
        "outputs": 1,
        "noerr": 0,
        "x": 310,
        "y": 620,
        "wires": [
            [
                "20d10401.408bd4"
            ]
        ]
    },
    {
        "id": "dd14e601.06e6e",
        "type": "ui_text_input",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "fill",
        "tooltip": "",
        "group": "abfd2b22.16a7b8",
        "order": 1,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "fill",
        "x": 90,
        "y": 520,
        "wires": [
            [
                "fde78eff.070e6"
            ]
        ]
    },
    {
        "id": "609c0f97.deb338",
        "type": "ui_text_input",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "drain",
        "tooltip": "",
        "group": "abfd2b22.16a7b8",
        "order": 2,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "drain",
        "x": 90,
        "y": 560,
        "wires": [
            [
                "fde78eff.070e6"
            ]
        ]
    },
    {
        "id": "8706f987.7b3a08",
        "type": "ui_text_input",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "Light on",
        "tooltip": "",
        "group": "abfd2b22.16a7b8",
        "order": 3,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "lightOn",
        "x": 80,
        "y": 600,
        "wires": [
            [
                "fde78eff.070e6"
            ]
        ]
    },
    {
        "id": "70c189a9.1a195",
        "type": "ui_text_input",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "Light off",
        "tooltip": "",
        "group": "abfd2b22.16a7b8",
        "order": 4,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "lightOff",
        "x": 80,
        "y": 640,
        "wires": [
            [
                "fde78eff.070e6"
            ]
        ]
    },
    {
        "id": "2733af3a.3cfd3",
        "type": "ui_slider",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "Power",
        "tooltip": "",
        "group": "abfd2b22.16a7b8",
        "order": 5,
        "width": "7",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "lightPwr",
        "min": 0,
        "max": "250",
        "step": "10",
        "x": 90,
        "y": 680,
        "wires": [
            [
                "fde78eff.070e6"
            ]
        ]
    },
    {
        "id": "64e1bb9b.a4fa8c",
        "type": "ui_slider",
        "z": "f73b7795.e6163",
        "name": "",
        "label": "Distance",
        "tooltip": "",
        "group": "abfd2b22.16a7b8",
        "order": 6,
        "width": "7",
        "height": "1",
        "passthru": true,
        "outs": "end",
        "topic": "lightDist",
        "min": 0,
        "max": "15",
        "step": "1",
        "x": 80,
        "y": 720,
        "wires": [
            [
                "fde78eff.070e6"
            ]
        ]
    },
    {
        "id": "1a88daa1.43febd",
        "type": "ui_group",
        "z": "",
        "name": "Stage 1",
        "tab": "82b721a9.0955",
        "order": 1,
        "disp": true,
        "width": "7",
        "collapse": false
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
        "id": "e5c5ed71.f909b8",
        "type": "ui_group",
        "z": "",
        "name": "Stage 2",
        "tab": "82b721a9.0955",
        "order": 2,
        "disp": true,
        "width": "7",
        "collapse": false
    },
    {
        "id": "abfd2b22.16a7b8",
        "type": "ui_group",
        "z": "",
        "name": "Stage 3",
        "tab": "82b721a9.0955",
        "order": 3,
        "disp": true,
        "width": "7",
        "collapse": false
    },
    {
        "id": "82b721a9.0955",
        "type": "ui_tab",
        "z": "",
        "name": "Planter-2.1 Channel 2",
        "icon": "dashboard",
        "order": 11,
        "disabled": false,
        "hidden": false
    }
]
