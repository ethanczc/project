[
    {
        "id": "3c63c6f6.beb2e2",
        "type": "tab",
        "label": "Planter-2.1 Channel 1",
        "disabled": false,
        "info": "recipe broken down into \n2 channels x 3 stages + 1 main = 10 recipes\nreduce workload on node red flows"
    },
    {
        "id": "ccc0fa30.7b29b",
        "type": "function",
        "z": "3c63c6f6.beb2e2",
        "name": "channel 1 stage 1",
        "func": "context.recipe = context.recipe || {};\n\nswitch (msg.topic) {\n    case \"fill\":     context.recipe.fill = msg.payload; break;\n    case \"drain\":    context.recipe.drain = msg.payload; break;\n    case \"lightOn\":  context.recipe.lightOn = msg.payload; break;\n    case \"lightOff\": context.recipe.lightOff = msg.payload; break;\n    case \"lightPwr\":  context.recipe.lightPwr = msg.payload; break;\n    case \"lightDist\": context.recipe.lightDist = msg.payload; break;\n}\njsonObj={}\njsonObj.payload = {\n    \"topic\" : \"recipe\",\n    \"channel\": 1,\n    \"stage\": 1,\n    \"fill\":         (context.recipe.fill).split(\",\"),\n    \"drain\":        (context.recipe.drain).split(\",\"),\n    \"lightOn\":      (context.recipe.lightOn).split(\",\"),\n    \"lightOff\":     (context.recipe.lightOff).split(\",\"),\n    \"lightPwr\":     context.recipe.lightPwr,\n    \"lightDist\":    context.recipe.lightDist * 1000\n}\nreturn jsonObj;\n",
        "outputs": 1,
        "noerr": 0,
        "x": 310,
        "y": 120,
        "wires": [
            [
                "6650615c.b670b8"
            ]
        ]
    },
    {
        "id": "c053a26.9a386e",
        "type": "debug",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "x": 610,
        "y": 80,
        "wires": []
    },
    {
        "id": "19b30634.eda372",
        "type": "ui_text_input",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "fill",
        "tooltip": "",
        "group": "e98ece5d.842c88",
        "order": 2,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "fill",
        "x": 90,
        "y": 20,
        "wires": [
            [
                "ccc0fa30.7b29b"
            ]
        ]
    },
    {
        "id": "135d6ea7.557259",
        "type": "ui_text_input",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "drain",
        "tooltip": "",
        "group": "e98ece5d.842c88",
        "order": 3,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "drain",
        "x": 90,
        "y": 60,
        "wires": [
            [
                "ccc0fa30.7b29b"
            ]
        ]
    },
    {
        "id": "97cd3c93.10d598",
        "type": "ui_slider",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "Power",
        "tooltip": "",
        "group": "e98ece5d.842c88",
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
        "y": 180,
        "wires": [
            [
                "ccc0fa30.7b29b"
            ]
        ]
    },
    {
        "id": "b3c2b8cd.10b588",
        "type": "ui_slider",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "Distance",
        "tooltip": "",
        "group": "e98ece5d.842c88",
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
        "y": 220,
        "wires": [
            [
                "ccc0fa30.7b29b"
            ]
        ]
    },
    {
        "id": "6913c80f.039ab8",
        "type": "mqtt out",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "topic": "planter_recipe",
        "qos": "2",
        "retain": "",
        "broker": "a113a6e8.11ab8",
        "x": 640,
        "y": 120,
        "wires": []
    },
    {
        "id": "6650615c.b670b8",
        "type": "json",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": true,
        "x": 470,
        "y": 120,
        "wires": [
            [
                "6913c80f.039ab8",
                "c053a26.9a386e"
            ]
        ]
    },
    {
        "id": "719632c4.81a08c",
        "type": "ui_text_input",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "Light off",
        "tooltip": "",
        "group": "e98ece5d.842c88",
        "order": 6,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "lightOff",
        "x": 80,
        "y": 140,
        "wires": [
            [
                "ccc0fa30.7b29b"
            ]
        ]
    },
    {
        "id": "d6bf4522.6b3bd8",
        "type": "ui_text_input",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "Light on",
        "tooltip": "",
        "group": "e98ece5d.842c88",
        "order": 5,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "lightOn",
        "x": 80,
        "y": 100,
        "wires": [
            [
                "ccc0fa30.7b29b"
            ]
        ]
    },
    {
        "id": "8fa471e9.a20468",
        "type": "debug",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "x": 610,
        "y": 320,
        "wires": []
    },
    {
        "id": "81aef57d.a8503",
        "type": "mqtt out",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "topic": "planter_recipe",
        "qos": "2",
        "retain": "",
        "broker": "a113a6e8.11ab8",
        "x": 640,
        "y": 360,
        "wires": []
    },
    {
        "id": "f7ad4bc9.03545",
        "type": "json",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": true,
        "x": 470,
        "y": 360,
        "wires": [
            [
                "81aef57d.a8503",
                "8fa471e9.a20468"
            ]
        ]
    },
    {
        "id": "b927c1d0.e1b14",
        "type": "function",
        "z": "3c63c6f6.beb2e2",
        "name": "channel 1 stage 2",
        "func": "context.recipe = context.recipe || {};\n\nswitch (msg.topic) {\n    case \"fill\":     context.recipe.fill = msg.payload; break;\n    case \"drain\":    context.recipe.drain = msg.payload; break;\n    case \"lightOn\":  context.recipe.lightOn = msg.payload; break;\n    case \"lightOff\": context.recipe.lightOff = msg.payload; break;\n    case \"lightPwr\":  context.recipe.lightPwr = msg.payload; break;\n    case \"lightDist\": context.recipe.lightDist = msg.payload; break;\n}\njsonObj={}\njsonObj.payload = {\n    \"topic\" : \"recipe\",\n    \"channel\": 1,\n    \"stage\": 2,\n    \"fill\":         (context.recipe.fill).split(\",\"),\n    \"drain\":        (context.recipe.drain).split(\",\"),\n    \"lightOn\":      (context.recipe.lightOn).split(\",\"),\n    \"lightOff\":     (context.recipe.lightOff).split(\",\"),\n    \"lightPwr\":     context.recipe.lightPwr,\n    \"lightDist\":    context.recipe.lightDist * 1000\n}\nreturn jsonObj;\n",
        "outputs": 1,
        "noerr": 0,
        "x": 310,
        "y": 360,
        "wires": [
            [
                "f7ad4bc9.03545"
            ]
        ]
    },
    {
        "id": "ce04e4a9.e5d068",
        "type": "ui_text_input",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "fill",
        "tooltip": "",
        "group": "d39915af.37f5e8",
        "order": 1,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "fill",
        "x": 90,
        "y": 260,
        "wires": [
            [
                "b927c1d0.e1b14"
            ]
        ]
    },
    {
        "id": "fb5ef4db.e8318",
        "type": "ui_text_input",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "drain",
        "tooltip": "",
        "group": "d39915af.37f5e8",
        "order": 2,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "drain",
        "x": 90,
        "y": 300,
        "wires": [
            [
                "b927c1d0.e1b14"
            ]
        ]
    },
    {
        "id": "e1f361d0.0d6b08",
        "type": "ui_text_input",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "Light on",
        "tooltip": "",
        "group": "d39915af.37f5e8",
        "order": 3,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "lightOn",
        "x": 80,
        "y": 340,
        "wires": [
            [
                "b927c1d0.e1b14"
            ]
        ]
    },
    {
        "id": "43658fdb.2433e8",
        "type": "ui_text_input",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "Light off",
        "tooltip": "",
        "group": "d39915af.37f5e8",
        "order": 4,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "lightOff",
        "x": 80,
        "y": 380,
        "wires": [
            [
                "b927c1d0.e1b14"
            ]
        ]
    },
    {
        "id": "79df8e20.8d727",
        "type": "ui_slider",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "Power",
        "tooltip": "",
        "group": "d39915af.37f5e8",
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
        "y": 420,
        "wires": [
            [
                "b927c1d0.e1b14"
            ]
        ]
    },
    {
        "id": "43feb833.f56ff8",
        "type": "ui_slider",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "Distance",
        "tooltip": "",
        "group": "d39915af.37f5e8",
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
        "y": 460,
        "wires": [
            [
                "b927c1d0.e1b14"
            ]
        ]
    },
    {
        "id": "cc6a7330.9d709",
        "type": "debug",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "x": 610,
        "y": 560,
        "wires": []
    },
    {
        "id": "8b6ff170.ea89b",
        "type": "mqtt out",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "topic": "planter_recipe",
        "qos": "2",
        "retain": "",
        "broker": "a113a6e8.11ab8",
        "x": 640,
        "y": 600,
        "wires": []
    },
    {
        "id": "178a0bf8.8db2e4",
        "type": "json",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": true,
        "x": 470,
        "y": 600,
        "wires": [
            [
                "8b6ff170.ea89b",
                "cc6a7330.9d709"
            ]
        ]
    },
    {
        "id": "c3937c3c.247fc8",
        "type": "function",
        "z": "3c63c6f6.beb2e2",
        "name": "channel 1 stage 3",
        "func": "context.recipe = context.recipe || {};\n\nswitch (msg.topic) {\n    case \"fill\":     context.recipe.fill = msg.payload; break;\n    case \"drain\":    context.recipe.drain = msg.payload; break;\n    case \"lightOn\":  context.recipe.lightOn = msg.payload; break;\n    case \"lightOff\": context.recipe.lightOff = msg.payload; break;\n    case \"lightPwr\":  context.recipe.lightPwr = msg.payload; break;\n    case \"lightDist\": context.recipe.lightDist = msg.payload; break;\n}\njsonObj={}\njsonObj.payload = {\n    \"topic\" : \"recipe\",\n    \"channel\": 1,\n    \"stage\": 3,\n    \"fill\":         (context.recipe.fill).split(\",\"),\n    \"drain\":        (context.recipe.drain).split(\",\"),\n    \"lightOn\":      (context.recipe.lightOn).split(\",\"),\n    \"lightOff\":     (context.recipe.lightOff).split(\",\"),\n    \"lightPwr\":     context.recipe.lightPwr,\n    \"lightDist\":    context.recipe.lightDist * 1000\n}\nreturn jsonObj;\n",
        "outputs": 1,
        "noerr": 0,
        "x": 310,
        "y": 600,
        "wires": [
            [
                "178a0bf8.8db2e4"
            ]
        ]
    },
    {
        "id": "a920dec7.752138",
        "type": "ui_text_input",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "fill",
        "tooltip": "",
        "group": "ac15980e.e12748",
        "order": 1,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "fill",
        "x": 90,
        "y": 500,
        "wires": [
            [
                "c3937c3c.247fc8"
            ]
        ]
    },
    {
        "id": "43240929.efd368",
        "type": "ui_text_input",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "drain",
        "tooltip": "",
        "group": "ac15980e.e12748",
        "order": 2,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "drain",
        "x": 90,
        "y": 540,
        "wires": [
            [
                "c3937c3c.247fc8"
            ]
        ]
    },
    {
        "id": "2d45ffde.5d8b58",
        "type": "ui_text_input",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "Light on",
        "tooltip": "",
        "group": "ac15980e.e12748",
        "order": 3,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "lightOn",
        "x": 80,
        "y": 580,
        "wires": [
            [
                "c3937c3c.247fc8"
            ]
        ]
    },
    {
        "id": "f5800252.46b8d8",
        "type": "ui_text_input",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "Light off",
        "tooltip": "",
        "group": "ac15980e.e12748",
        "order": 4,
        "width": "7",
        "height": "1",
        "passthru": true,
        "mode": "text",
        "delay": "3000",
        "topic": "lightOff",
        "x": 80,
        "y": 620,
        "wires": [
            [
                "c3937c3c.247fc8"
            ]
        ]
    },
    {
        "id": "dca02849.c33ef8",
        "type": "ui_slider",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "Power",
        "tooltip": "",
        "group": "ac15980e.e12748",
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
        "y": 660,
        "wires": [
            [
                "c3937c3c.247fc8"
            ]
        ]
    },
    {
        "id": "afb6e0cb.cc8148",
        "type": "ui_slider",
        "z": "3c63c6f6.beb2e2",
        "name": "",
        "label": "Distance",
        "tooltip": "",
        "group": "ac15980e.e12748",
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
        "y": 700,
        "wires": [
            [
                "c3937c3c.247fc8"
            ]
        ]
    },
    {
        "id": "e98ece5d.842c88",
        "type": "ui_group",
        "z": "",
        "name": "Stage 1",
        "tab": "851eff6.628da",
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
        "id": "d39915af.37f5e8",
        "type": "ui_group",
        "z": "",
        "name": "Stage 2",
        "tab": "851eff6.628da",
        "order": 2,
        "disp": true,
        "width": "7",
        "collapse": false
    },
    {
        "id": "ac15980e.e12748",
        "type": "ui_group",
        "z": "",
        "name": "Stage 3",
        "tab": "851eff6.628da",
        "order": 3,
        "disp": true,
        "width": "7",
        "collapse": false
    },
    {
        "id": "851eff6.628da",
        "type": "ui_tab",
        "z": "",
        "name": "Planter-2.1 Channel 1",
        "icon": "dashboard",
        "order": 10,
        "disabled": false,
        "hidden": false
    }
]
