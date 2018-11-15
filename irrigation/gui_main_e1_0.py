# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc

###########################################################################
## Class GuiFrame
###########################################################################

class GuiFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"main-e1.0", pos = wx.DefaultPosition, size = wx.Size( 653,521 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.timer = wx.Timer()
		self.timer.SetOwner( self, wx.ID_ANY )
		self.timer.Start( 1000 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.main_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.main_Panel, wx.ID_ANY, u"Time" ), wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.clock_Display = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"00:00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.clock_Display.Wrap( -1 )
		self.clock_Display.SetFont( wx.Font( 13, 74, 90, 92, False, "Sans" ) )
		
		gSizer2.Add( self.clock_Display, 0, wx.ALL, 5 )
		
		self.date_Display = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"1/1/1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.date_Display.Wrap( -1 )
		self.date_Display.SetFont( wx.Font( 13, 74, 90, 92, False, "Sans" ) )
		
		gSizer2.Add( self.date_Display, 0, wx.ALL, 5 )
		
		self.startDate_Label = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Start Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startDate_Label.Wrap( -1 )
		gSizer2.Add( self.startDate_Label, 0, wx.ALL, 5 )
		
		self.startDate_Txtctrl = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.startDate_Txtctrl, 0, wx.ALL, 5 )
		
		self.daysPassed_Label = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Days Passed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.daysPassed_Label.Wrap( -1 )
		gSizer2.Add( self.daysPassed_Label, 0, wx.ALL, 5 )
		
		self.daysPassed_Display = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.daysPassed_Display.Wrap( -1 )
		gSizer2.Add( self.daysPassed_Display, 0, wx.ALL, 5 )
		
		self.ch1CurrentStage_Label = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Channel 1 Stage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch1CurrentStage_Label.Wrap( -1 )
		gSizer2.Add( self.ch1CurrentStage_Label, 0, wx.ALL, 5 )
		
		self.ch1CurrentStage_Display = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch1CurrentStage_Display.Wrap( -1 )
		gSizer2.Add( self.ch1CurrentStage_Display, 0, wx.ALL, 5 )
		
		self.ch1CurrentStage_Label = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Channel 2 Stage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch1CurrentStage_Label.Wrap( -1 )
		gSizer2.Add( self.ch1CurrentStage_Label, 0, wx.ALL, 5 )
		
		self.ch2CurrentStage_Display = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch2CurrentStage_Display.Wrap( -1 )
		gSizer2.Add( self.ch2CurrentStage_Display, 0, wx.ALL, 5 )
		
		self.m_staticText141 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"DWC Stage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )
		gSizer2.Add( self.m_staticText141, 0, wx.ALL, 5 )
		
		self.dwcCurrentStage_Display = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcCurrentStage_Display.Wrap( -1 )
		gSizer2.Add( self.dwcCurrentStage_Display, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		gSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.main_Panel, wx.ID_ANY, u"Ethernet" ), wx.VERTICAL )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.hostIp_Label = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Host IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hostIp_Label.Wrap( -1 )
		gSizer3.Add( self.hostIp_Label, 0, wx.ALL, 5 )
		
		self.hostIp_Txtctrl = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.hostIp_Txtctrl, 0, wx.ALL, 5 )
		
		self.commandTopic_Label = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Command Topic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.commandTopic_Label.Wrap( -1 )
		gSizer3.Add( self.commandTopic_Label, 0, wx.ALL, 5 )
		
		self.commandTopic_Txtctrl = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.commandTopic_Txtctrl, 0, wx.ALL, 5 )
		
		self.sensorsTopic_Label = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Sensors Topic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sensorsTopic_Label.Wrap( -1 )
		gSizer3.Add( self.sensorsTopic_Label, 0, wx.ALL, 5 )
		
		self.sensorsTopic_Txtctrl = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.sensorsTopic_Txtctrl, 0, wx.ALL, 5 )
		
		self.ConnectMqtt = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.ConnectMqtt, 0, wx.ALL, 5 )
		
		self.mqttStatus_Display = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Not Connected", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mqttStatus_Display.Wrap( -1 )
		gSizer3.Add( self.mqttStatus_Display, 0, wx.ALL, 5 )
		
		self.sendMqtt_Btn = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.sendMqtt_Btn, 0, wx.ALL, 5 )
		
		self.sendMqtt_Txtctrl = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.sendMqtt_Txtctrl, 0, wx.ALL, 5 )
		
		
		sbSizer2.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		
		gSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.main_Panel, wx.ID_ANY, u"Recipe" ), wx.VERTICAL )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.loadRecipe_Btn = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.loadRecipe_Btn, 0, wx.ALL, 5 )
		
		self.recipe_Display = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"No recipe", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.recipe_Display.Wrap( -1 )
		gSizer4.Add( self.recipe_Display, 0, wx.ALL, 5 )
		
		self.config_Label = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Configuration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.config_Label.Wrap( -1 )
		gSizer4.Add( self.config_Label, 0, wx.ALL, 5 )
		
		self.config_Txtctrl = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.config_Txtctrl, 0, wx.ALL, 5 )
		
		self.run_Label = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.run_Label.Wrap( -1 )
		gSizer4.Add( self.run_Label, 0, wx.ALL, 5 )
		
		self.run_Txtctrl = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.run_Txtctrl, 0, wx.ALL, 5 )
		
		self.plant_Label = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Plant", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.plant_Label.Wrap( -1 )
		gSizer4.Add( self.plant_Label, 0, wx.ALL, 5 )
		
		self.plant_Txtctrl = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.plant_Txtctrl, 0, wx.ALL, 5 )
		
		self.led_Label = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"LED", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.led_Label.Wrap( -1 )
		gSizer4.Add( self.led_Label, 0, wx.ALL, 5 )
		
		self.led_Txtctrl = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.led_Txtctrl, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		
		gSizer1.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.main_Panel, wx.ID_ANY, u"Logging" ), wx.VERTICAL )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.loadLog_Btn = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.loadLog_Btn, 0, wx.ALL, 5 )
		
		self.log_Display = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"No File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.log_Display.Wrap( -1 )
		gSizer5.Add( self.log_Display, 0, wx.ALL, 5 )
		
		self.autoLog_ToggleBtn = wx.ToggleButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.autoLog_ToggleBtn, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( gSizer5, 0, wx.EXPAND, 5 )
		
		
		gSizer1.Add( sbSizer4, 1, wx.EXPAND, 5 )
		
		
		self.main_Panel.SetSizer( gSizer1 )
		self.main_Panel.Layout()
		gSizer1.Fit( self.main_Panel )
		self.notebook.AddPage( self.main_Panel, u"Main", True )
		self.light1_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer181 = wx.StaticBoxSizer( wx.StaticBox( self.light1_Panel, wx.ID_ANY, u"Stage 1" ), wx.VERTICAL )
		
		gSizer191 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.light1Stage1On_Label = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light1Stage1On_Label.Wrap( -1 )
		gSizer191.Add( self.light1Stage1On_Label, 0, wx.ALL, 5 )
		
		self.light1Stage1On_Display = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light1Stage1On_Display.Wrap( -1 )
		gSizer191.Add( self.light1Stage1On_Display, 0, wx.ALL, 5 )
		
		self.light1Stage1Off_Label = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light1Stage1Off_Label.Wrap( -1 )
		gSizer191.Add( self.light1Stage1Off_Label, 0, wx.ALL, 5 )
		
		self.light1Stage1Off_Display = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light1Stage1Off_Display.Wrap( -1 )
		gSizer191.Add( self.light1Stage1Off_Display, 0, wx.ALL, 5 )
		
		
		sbSizer181.Add( gSizer191, 1, wx.EXPAND, 5 )
		
		
		bSizer61.Add( sbSizer181, 1, wx.EXPAND, 5 )
		
		sbSizer191 = wx.StaticBoxSizer( wx.StaticBox( self.light1_Panel, wx.ID_ANY, u"Stage 2" ), wx.VERTICAL )
		
		gSizer201 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.light1Stage2On_Label = wx.StaticText( sbSizer191.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light1Stage2On_Label.Wrap( -1 )
		gSizer201.Add( self.light1Stage2On_Label, 0, wx.ALL, 5 )
		
		self.light1Stage2On_Display = wx.StaticText( sbSizer191.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light1Stage2On_Display.Wrap( -1 )
		gSizer201.Add( self.light1Stage2On_Display, 0, wx.ALL, 5 )
		
		self.light1Stage2Off_Label = wx.StaticText( sbSizer191.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light1Stage2Off_Label.Wrap( -1 )
		gSizer201.Add( self.light1Stage2Off_Label, 0, wx.ALL, 5 )
		
		self.light1Stage2Off_Display = wx.StaticText( sbSizer191.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light1Stage2Off_Display.Wrap( -1 )
		gSizer201.Add( self.light1Stage2Off_Display, 0, wx.ALL, 5 )
		
		
		sbSizer191.Add( gSizer201, 1, wx.EXPAND, 5 )
		
		
		bSizer61.Add( sbSizer191, 1, wx.EXPAND, 5 )
		
		sbSizer211 = wx.StaticBoxSizer( wx.StaticBox( self.light1_Panel, wx.ID_ANY, u"Stage 3" ), wx.VERTICAL )
		
		gSizer211 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.light1Stage3On_Label = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light1Stage3On_Label.Wrap( -1 )
		gSizer211.Add( self.light1Stage3On_Label, 0, wx.ALL, 5 )
		
		self.light1Stage3On_Display = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light1Stage3On_Display.Wrap( -1 )
		gSizer211.Add( self.light1Stage3On_Display, 0, wx.ALL, 5 )
		
		self.light1Stage3Off_Label = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light1Stage3Off_Label.Wrap( -1 )
		gSizer211.Add( self.light1Stage3Off_Label, 0, wx.ALL, 5 )
		
		self.light1Stage3Off_Display = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light1Stage3Off_Display.Wrap( -1 )
		gSizer211.Add( self.light1Stage3Off_Display, 0, wx.ALL, 5 )
		
		
		sbSizer211.Add( gSizer211, 1, wx.EXPAND, 5 )
		
		
		bSizer61.Add( sbSizer211, 1, wx.EXPAND, 5 )
		
		sbSizer22 = wx.StaticBoxSizer( wx.StaticBox( self.light1_Panel, wx.ID_ANY, u"Control" ), wx.VERTICAL )
		
		gSizer22 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.autoLight1_ToggleBtn = wx.ToggleButton( sbSizer22.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.autoLight1_ToggleBtn, 0, wx.ALL, 5 )
		
		
		sbSizer22.Add( gSizer22, 1, wx.EXPAND, 5 )
		
		
		bSizer61.Add( sbSizer22, 1, wx.EXPAND, 5 )
		
		
		self.light1_Panel.SetSizer( bSizer61 )
		self.light1_Panel.Layout()
		bSizer61.Fit( self.light1_Panel )
		self.notebook.AddPage( self.light1_Panel, u"Light 1", False )
		self.light2_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer221 = wx.StaticBoxSizer( wx.StaticBox( self.light2_Panel, wx.ID_ANY, u"Stage 1" ), wx.VERTICAL )
		
		gSizer23 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.light2Stage1On_Label = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light2Stage1On_Label.Wrap( -1 )
		gSizer23.Add( self.light2Stage1On_Label, 0, wx.ALL, 5 )
		
		self.light2Stage1On_Display = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light2Stage1On_Display.Wrap( -1 )
		gSizer23.Add( self.light2Stage1On_Display, 0, wx.ALL, 5 )
		
		self.light2Stage1Off_Label = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light2Stage1Off_Label.Wrap( -1 )
		gSizer23.Add( self.light2Stage1Off_Label, 0, wx.ALL, 5 )
		
		self.light2Stage1Off_Display = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light2Stage1Off_Display.Wrap( -1 )
		gSizer23.Add( self.light2Stage1Off_Display, 0, wx.ALL, 5 )
		
		
		sbSizer221.Add( gSizer23, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( sbSizer221, 1, wx.EXPAND, 5 )
		
		sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self.light2_Panel, wx.ID_ANY, u"Stage 2" ), wx.VERTICAL )
		
		gSizer24 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.light2Stage2On_Label = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light2Stage2On_Label.Wrap( -1 )
		gSizer24.Add( self.light2Stage2On_Label, 0, wx.ALL, 5 )
		
		self.light2Stage2On_Display = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light2Stage2On_Display.Wrap( -1 )
		gSizer24.Add( self.light2Stage2On_Display, 0, wx.ALL, 5 )
		
		self.light2Stage2Off_Label = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light2Stage2Off_Label.Wrap( -1 )
		gSizer24.Add( self.light2Stage2Off_Label, 0, wx.ALL, 5 )
		
		self.light2Stage2Off_Display = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light2Stage2Off_Display.Wrap( -1 )
		gSizer24.Add( self.light2Stage2Off_Display, 0, wx.ALL, 5 )
		
		
		sbSizer23.Add( gSizer24, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( sbSizer23, 1, wx.EXPAND, 5 )
		
		sbSizer24 = wx.StaticBoxSizer( wx.StaticBox( self.light2_Panel, wx.ID_ANY, u"Stage 3" ), wx.VERTICAL )
		
		gSizer25 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.light2Stage3On_Label = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light2Stage3On_Label.Wrap( -1 )
		gSizer25.Add( self.light2Stage3On_Label, 0, wx.ALL, 5 )
		
		self.light2Stage3On_Display = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light2Stage3On_Display.Wrap( -1 )
		gSizer25.Add( self.light2Stage3On_Display, 0, wx.ALL, 5 )
		
		self.light2Stage3Off_Label = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light2Stage3Off_Label.Wrap( -1 )
		gSizer25.Add( self.light2Stage3Off_Label, 0, wx.ALL, 5 )
		
		self.light2Stage3Off_Display = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.light2Stage3Off_Display.Wrap( -1 )
		gSizer25.Add( self.light2Stage3Off_Display, 0, wx.ALL, 5 )
		
		
		sbSizer24.Add( gSizer25, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( sbSizer24, 1, wx.EXPAND, 5 )
		
		sbSizer25 = wx.StaticBoxSizer( wx.StaticBox( self.light2_Panel, wx.ID_ANY, u"Control" ), wx.VERTICAL )
		
		gSizer26 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.autoLight2_ToggleBtn = wx.ToggleButton( sbSizer25.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer26.Add( self.autoLight2_ToggleBtn, 0, wx.ALL, 5 )
		
		
		sbSizer25.Add( gSizer26, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( sbSizer25, 1, wx.EXPAND, 5 )
		
		
		self.light2_Panel.SetSizer( bSizer7 )
		self.light2_Panel.Layout()
		bSizer7.Fit( self.light2_Panel )
		self.notebook.AddPage( self.light2_Panel, u"Light 2", False )
		self.p1_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.p1_Panel, wx.ID_ANY, u"Stage 1" ), wx.VERTICAL )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.pump1Stage1Pump_Label = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Pump", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage1Pump_Label.Wrap( -1 )
		gSizer6.Add( self.pump1Stage1Pump_Label, 0, wx.ALL, 5 )
		
		self.pump1Stage1Pump_Display = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage1Pump_Display.Wrap( -1 )
		gSizer6.Add( self.pump1Stage1Pump_Display, 0, wx.ALL, 5 )
		
		self.pump1Stage1Drain_Label = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage1Drain_Label.Wrap( -1 )
		gSizer6.Add( self.pump1Stage1Drain_Label, 0, wx.ALL, 5 )
		
		self.pump1Stage1Drain_Display = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage1Drain_Display.Wrap( -1 )
		gSizer6.Add( self.pump1Stage1Drain_Display, 0, wx.ALL, 5 )
		
		self.ch1Stage1Duration_Label = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Stage Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch1Stage1Duration_Label.Wrap( -1 )
		gSizer6.Add( self.ch1Stage1Duration_Label, 0, wx.ALL, 5 )
		
		self.ch1Stage1Duration_Display = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch1Stage1Duration_Display.Wrap( -1 )
		gSizer6.Add( self.ch1Stage1Duration_Display, 0, wx.ALL, 5 )
		
		
		sbSizer5.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.p1_Panel, wx.ID_ANY, u"Stage 2" ), wx.VERTICAL )
		
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.pump1Stage2Pump_Label = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Pump", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage2Pump_Label.Wrap( -1 )
		gSizer7.Add( self.pump1Stage2Pump_Label, 0, wx.ALL, 5 )
		
		self.pump1Stage2Pump_Display = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage2Pump_Display.Wrap( -1 )
		gSizer7.Add( self.pump1Stage2Pump_Display, 0, wx.ALL, 5 )
		
		self.pump1Stage2Drain_Label = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage2Drain_Label.Wrap( -1 )
		gSizer7.Add( self.pump1Stage2Drain_Label, 0, wx.ALL, 5 )
		
		self.pump1Stage2Drain_Display = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage2Drain_Display.Wrap( -1 )
		gSizer7.Add( self.pump1Stage2Drain_Display, 0, wx.ALL, 5 )
		
		self.ch1Stage2Duration_Label = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Stage Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch1Stage2Duration_Label.Wrap( -1 )
		gSizer7.Add( self.ch1Stage2Duration_Label, 0, wx.ALL, 5 )
		
		self.ch1Stage2Duration_Display = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch1Stage2Duration_Display.Wrap( -1 )
		gSizer7.Add( self.ch1Stage2Duration_Display, 0, wx.ALL, 5 )
		
		
		sbSizer6.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.p1_Panel, wx.ID_ANY, u"Stage 3" ), wx.VERTICAL )
		
		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.pump1Stage3Pump_Label = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Pump", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage3Pump_Label.Wrap( -1 )
		gSizer8.Add( self.pump1Stage3Pump_Label, 0, wx.ALL, 5 )
		
		self.pump1Stage3Pump_Display = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage3Pump_Display.Wrap( -1 )
		gSizer8.Add( self.pump1Stage3Pump_Display, 0, wx.ALL, 5 )
		
		self.pump1Stage3Drain_Label = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage3Drain_Label.Wrap( -1 )
		gSizer8.Add( self.pump1Stage3Drain_Label, 0, wx.ALL, 5 )
		
		self.pump1Stage3Drain_Display = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage3Drain_Display.Wrap( -1 )
		gSizer8.Add( self.pump1Stage3Drain_Display, 0, wx.ALL, 5 )
		
		self.ch1Stage3Duration_Label = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Stage Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch1Stage3Duration_Label.Wrap( -1 )
		gSizer8.Add( self.ch1Stage3Duration_Label, 0, wx.ALL, 5 )
		
		self.ch1Stage3Duration_Display = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch1Stage3Duration_Display.Wrap( -1 )
		gSizer8.Add( self.ch1Stage3Duration_Display, 0, wx.ALL, 5 )
		
		
		sbSizer7.Add( gSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.p1_Panel, wx.ID_ANY, u"Control" ), wx.VERTICAL )
		
		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.autoPump1_ToggleBtn = wx.ToggleButton( sbSizer8.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.autoPump1_ToggleBtn, 0, wx.ALL, 5 )
		
		
		sbSizer8.Add( gSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer8, 1, wx.EXPAND, 5 )
		
		
		self.p1_Panel.SetSizer( bSizer2 )
		self.p1_Panel.Layout()
		bSizer2.Fit( self.p1_Panel )
		self.notebook.AddPage( self.p1_Panel, u"Pump 1", False )
		self.p2_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer51 = wx.StaticBoxSizer( wx.StaticBox( self.p2_Panel, wx.ID_ANY, u"Stage 1" ), wx.VERTICAL )
		
		gSizer61 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.pump2Stage1Pump_Label = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Pump", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage1Pump_Label.Wrap( -1 )
		gSizer61.Add( self.pump2Stage1Pump_Label, 0, wx.ALL, 5 )
		
		self.pump2Stage1Pump_Display = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage1Pump_Display.Wrap( -1 )
		gSizer61.Add( self.pump2Stage1Pump_Display, 0, wx.ALL, 5 )
		
		self.pump2Stage1Drain_Label = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage1Drain_Label.Wrap( -1 )
		gSizer61.Add( self.pump2Stage1Drain_Label, 0, wx.ALL, 5 )
		
		self.pump2Stage1Drain_Display = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage1Drain_Display.Wrap( -1 )
		gSizer61.Add( self.pump2Stage1Drain_Display, 0, wx.ALL, 5 )
		
		self.ch2Stage1Duration_Label = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Stage Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch2Stage1Duration_Label.Wrap( -1 )
		gSizer61.Add( self.ch2Stage1Duration_Label, 0, wx.ALL, 5 )
		
		self.ch2Stage1Duration_Display = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch2Stage1Duration_Display.Wrap( -1 )
		gSizer61.Add( self.ch2Stage1Duration_Display, 0, wx.ALL, 5 )
		
		
		sbSizer51.Add( gSizer61, 1, wx.EXPAND, 5 )
		
		
		bSizer21.Add( sbSizer51, 1, wx.EXPAND, 5 )
		
		sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self.p2_Panel, wx.ID_ANY, u"Stage 2" ), wx.VERTICAL )
		
		gSizer71 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.pump2Stage2Pump_Label = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Pump", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage2Pump_Label.Wrap( -1 )
		gSizer71.Add( self.pump2Stage2Pump_Label, 0, wx.ALL, 5 )
		
		self.pump2Stage2Pump_Display = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage2Pump_Display.Wrap( -1 )
		gSizer71.Add( self.pump2Stage2Pump_Display, 0, wx.ALL, 5 )
		
		self.pump2Stage2Drain_Label = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage2Drain_Label.Wrap( -1 )
		gSizer71.Add( self.pump2Stage2Drain_Label, 0, wx.ALL, 5 )
		
		self.pump2Stage2Drain_Display = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage2Drain_Display.Wrap( -1 )
		gSizer71.Add( self.pump2Stage2Drain_Display, 0, wx.ALL, 5 )
		
		self.ch2Stage2Duration_Label = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Stage Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch2Stage2Duration_Label.Wrap( -1 )
		gSizer71.Add( self.ch2Stage2Duration_Label, 0, wx.ALL, 5 )
		
		self.ch2Stage2Duration_Display = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch2Stage2Duration_Display.Wrap( -1 )
		gSizer71.Add( self.ch2Stage2Duration_Display, 0, wx.ALL, 5 )
		
		
		sbSizer61.Add( gSizer71, 1, wx.EXPAND, 5 )
		
		
		bSizer21.Add( sbSizer61, 1, wx.EXPAND, 5 )
		
		sbSizer71 = wx.StaticBoxSizer( wx.StaticBox( self.p2_Panel, wx.ID_ANY, u"Stage 3" ), wx.VERTICAL )
		
		gSizer81 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.pump2Stage3Pump_Label = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Pump", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage3Pump_Label.Wrap( -1 )
		gSizer81.Add( self.pump2Stage3Pump_Label, 0, wx.ALL, 5 )
		
		self.pump2Stage3Pump_Display = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage3Pump_Display.Wrap( -1 )
		gSizer81.Add( self.pump2Stage3Pump_Display, 0, wx.ALL, 5 )
		
		self.pump2Stage3Drain_Label = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage3Drain_Label.Wrap( -1 )
		gSizer81.Add( self.pump2Stage3Drain_Label, 0, wx.ALL, 5 )
		
		self.pump2Stage3Drain_Display = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage3Drain_Display.Wrap( -1 )
		gSizer81.Add( self.pump2Stage3Drain_Display, 0, wx.ALL, 5 )
		
		self.ch2Stage3Duration_Label = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Stage Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch2Stage3Duration_Label.Wrap( -1 )
		gSizer81.Add( self.ch2Stage3Duration_Label, 0, wx.ALL, 5 )
		
		self.ch2Stage3Duration_Display = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ch2Stage3Duration_Display.Wrap( -1 )
		gSizer81.Add( self.ch2Stage3Duration_Display, 0, wx.ALL, 5 )
		
		
		sbSizer71.Add( gSizer81, 1, wx.EXPAND, 5 )
		
		
		bSizer21.Add( sbSizer71, 1, wx.EXPAND, 5 )
		
		sbSizer81 = wx.StaticBoxSizer( wx.StaticBox( self.p2_Panel, wx.ID_ANY, u"Control" ), wx.VERTICAL )
		
		gSizer91 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.autoPump2_ToggleBtn = wx.ToggleButton( sbSizer81.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer91.Add( self.autoPump2_ToggleBtn, 0, wx.ALL, 5 )
		
		
		sbSizer81.Add( gSizer91, 1, wx.EXPAND, 5 )
		
		
		bSizer21.Add( sbSizer81, 1, wx.EXPAND, 5 )
		
		
		self.p2_Panel.SetSizer( bSizer21 )
		self.p2_Panel.Layout()
		bSizer21.Fit( self.p2_Panel )
		self.notebook.AddPage( self.p2_Panel, u"Pump 2", False )
		self.dwc_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer26 = wx.StaticBoxSizer( wx.StaticBox( self.dwc_Panel, wx.ID_ANY, u"Stage 1" ), wx.VERTICAL )
		
		gSizer27 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText105 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText105.Wrap( -1 )
		gSizer27.Add( self.m_staticText105, 0, wx.ALL, 5 )
		
		self.dwcStage1Power_Label = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcStage1Power_Label.Wrap( -1 )
		gSizer27.Add( self.dwcStage1Power_Label, 0, wx.ALL, 5 )
		
		self.m_staticText107 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Distance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText107.Wrap( -1 )
		gSizer27.Add( self.m_staticText107, 0, wx.ALL, 5 )
		
		self.dwcStage1Dist_Label = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcStage1Dist_Label.Wrap( -1 )
		gSizer27.Add( self.dwcStage1Dist_Label, 0, wx.ALL, 5 )
		
		self.m_staticText129 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText129.Wrap( -1 )
		gSizer27.Add( self.m_staticText129, 0, wx.ALL, 5 )
		
		self.dwcLightsStage1On_Timings = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcLightsStage1On_Timings.Wrap( -1 )
		gSizer27.Add( self.dwcLightsStage1On_Timings, 0, wx.ALL, 5 )
		
		self.m_staticText131 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		gSizer27.Add( self.m_staticText131, 0, wx.ALL, 5 )
		
		self.dwcLightsStage1Off_Timings = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcLightsStage1Off_Timings.Wrap( -1 )
		gSizer27.Add( self.dwcLightsStage1Off_Timings, 0, wx.ALL, 5 )
		
		self.m_staticText109 = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"Stage Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText109.Wrap( -1 )
		gSizer27.Add( self.m_staticText109, 0, wx.ALL, 5 )
		
		self.dwcStage1Duration_Label = wx.StaticText( sbSizer26.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcStage1Duration_Label.Wrap( -1 )
		gSizer27.Add( self.dwcStage1Duration_Label, 0, wx.ALL, 5 )
		
		
		sbSizer26.Add( gSizer27, 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( sbSizer26, 1, wx.EXPAND, 5 )
		
		sbSizer27 = wx.StaticBoxSizer( wx.StaticBox( self.dwc_Panel, wx.ID_ANY, u"Stage 2" ), wx.VERTICAL )
		
		gSizer28 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText111 = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )
		gSizer28.Add( self.m_staticText111, 0, wx.ALL, 5 )
		
		self.dwcStage2Power_Label = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcStage2Power_Label.Wrap( -1 )
		gSizer28.Add( self.dwcStage2Power_Label, 0, wx.ALL, 5 )
		
		self.m_staticText113 = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Distance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText113.Wrap( -1 )
		gSizer28.Add( self.m_staticText113, 0, wx.ALL, 5 )
		
		self.dwcStage2Distance_Label = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcStage2Distance_Label.Wrap( -1 )
		gSizer28.Add( self.dwcStage2Distance_Label, 0, wx.ALL, 5 )
		
		self.m_staticText133 = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText133.Wrap( -1 )
		gSizer28.Add( self.m_staticText133, 0, wx.ALL, 5 )
		
		self.dwcLightsStage2On_Timings = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcLightsStage2On_Timings.Wrap( -1 )
		gSizer28.Add( self.dwcLightsStage2On_Timings, 0, wx.ALL, 5 )
		
		self.m_staticText135 = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText135.Wrap( -1 )
		gSizer28.Add( self.m_staticText135, 0, wx.ALL, 5 )
		
		self.dwcLightsStage2Off_Timings = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcLightsStage2Off_Timings.Wrap( -1 )
		gSizer28.Add( self.dwcLightsStage2Off_Timings, 0, wx.ALL, 5 )
		
		self.m_staticText115 = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"Stage Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText115.Wrap( -1 )
		gSizer28.Add( self.m_staticText115, 0, wx.ALL, 5 )
		
		self.dwcStage2Duration_Label = wx.StaticText( sbSizer27.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcStage2Duration_Label.Wrap( -1 )
		gSizer28.Add( self.dwcStage2Duration_Label, 0, wx.ALL, 5 )
		
		
		sbSizer27.Add( gSizer28, 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( sbSizer27, 1, wx.EXPAND, 5 )
		
		sbSizer28 = wx.StaticBoxSizer( wx.StaticBox( self.dwc_Panel, wx.ID_ANY, u"Stage 3" ), wx.VERTICAL )
		
		gSizer29 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText117 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText117.Wrap( -1 )
		gSizer29.Add( self.m_staticText117, 0, wx.ALL, 5 )
		
		self.dwcStage3Power_Label = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcStage3Power_Label.Wrap( -1 )
		gSizer29.Add( self.dwcStage3Power_Label, 0, wx.ALL, 5 )
		
		self.m_staticText119 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Distance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText119.Wrap( -1 )
		gSizer29.Add( self.m_staticText119, 0, wx.ALL, 5 )
		
		self.dwcStage3Distance_Label = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcStage3Distance_Label.Wrap( -1 )
		gSizer29.Add( self.dwcStage3Distance_Label, 0, wx.ALL, 5 )
		
		self.m_staticText137 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText137.Wrap( -1 )
		gSizer29.Add( self.m_staticText137, 0, wx.ALL, 5 )
		
		self.dwcLightsStage3On_Timings = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcLightsStage3On_Timings.Wrap( -1 )
		gSizer29.Add( self.dwcLightsStage3On_Timings, 0, wx.ALL, 5 )
		
		self.m_staticText139 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText139.Wrap( -1 )
		gSizer29.Add( self.m_staticText139, 0, wx.ALL, 5 )
		
		self.dwcLightsStage3Off_Timings = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcLightsStage3Off_Timings.Wrap( -1 )
		gSizer29.Add( self.dwcLightsStage3Off_Timings, 0, wx.ALL, 5 )
		
		self.m_staticText121 = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"Stage Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )
		gSizer29.Add( self.m_staticText121, 0, wx.ALL, 5 )
		
		self.dwcStage3Duration_Label = wx.StaticText( sbSizer28.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcStage3Duration_Label.Wrap( -1 )
		gSizer29.Add( self.dwcStage3Duration_Label, 0, wx.ALL, 5 )
		
		
		sbSizer28.Add( gSizer29, 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( sbSizer28, 1, wx.EXPAND, 5 )
		
		sbSizer29 = wx.StaticBoxSizer( wx.StaticBox( self.dwc_Panel, wx.ID_ANY, u"Topping up" ), wx.VERTICAL )
		
		gSizer30 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText123 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Frequency (days)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText123.Wrap( -1 )
		gSizer30.Add( self.m_staticText123, 0, wx.ALL, 5 )
		
		self.dwcTopupDays_Label = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcTopupDays_Label.Wrap( -1 )
		gSizer30.Add( self.dwcTopupDays_Label, 0, wx.ALL, 5 )
		
		self.m_staticText125 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText125.Wrap( -1 )
		gSizer30.Add( self.m_staticText125, 0, wx.ALL, 5 )
		
		self.dwcTopupTime_Label = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"00:00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dwcTopupTime_Label.Wrap( -1 )
		gSizer30.Add( self.dwcTopupTime_Label, 0, wx.ALL, 5 )
		
		
		sbSizer29.Add( gSizer30, 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( sbSizer29, 1, wx.EXPAND, 5 )
		
		sbSizer30 = wx.StaticBoxSizer( wx.StaticBox( self.dwc_Panel, wx.ID_ANY, u"Control" ), wx.VERTICAL )
		
		gSizer31 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.dwcAuto_ToggleBtn = wx.ToggleButton( sbSizer30.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.dwcAuto_ToggleBtn, 0, wx.ALL, 5 )
		
		
		sbSizer30.Add( gSizer31, 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( sbSizer30, 1, wx.EXPAND, 5 )
		
		
		self.dwc_Panel.SetSizer( bSizer8 )
		self.dwc_Panel.Layout()
		bSizer8.Fit( self.dwc_Panel )
		self.notebook.AddPage( self.dwc_Panel, u"DWC", False )
		self.sensors_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self.sensors_Panel, wx.ID_ANY, u"Data" ), wx.VERTICAL )
		
		gSizer18 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.temp1_Label = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"Temp 1 (°C)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.temp1_Label.Wrap( -1 )
		gSizer18.Add( self.temp1_Label, 0, wx.ALL, 5 )
		
		self.temp1_Display = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.temp1_Display.Wrap( -1 )
		gSizer18.Add( self.temp1_Display, 0, wx.ALL, 5 )
		
		self.temp2_Label = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"Temp 2 (°C)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.temp2_Label.Wrap( -1 )
		gSizer18.Add( self.temp2_Label, 0, wx.ALL, 5 )
		
		self.temp2_Display = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.temp2_Display.Wrap( -1 )
		gSizer18.Add( self.temp2_Display, 0, wx.ALL, 5 )
		
		self.tempA_Label = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"Average Temp (°C)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tempA_Label.Wrap( -1 )
		gSizer18.Add( self.tempA_Label, 0, wx.ALL, 5 )
		
		self.tempA_Display = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tempA_Display.Wrap( -1 )
		gSizer18.Add( self.tempA_Display, 0, wx.ALL, 5 )
		
		self.humidity_Label = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"Humidity (%RH)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.humidity_Label.Wrap( -1 )
		gSizer18.Add( self.humidity_Label, 0, wx.ALL, 5 )
		
		self.humidity_Display = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.humidity_Display.Wrap( -1 )
		gSizer18.Add( self.humidity_Display, 0, wx.ALL, 5 )
		
		self.ec_Label = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"EC (mS/cm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ec_Label.Wrap( -1 )
		gSizer18.Add( self.ec_Label, 0, wx.ALL, 5 )
		
		self.ec_Display = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ec_Display.Wrap( -1 )
		gSizer18.Add( self.ec_Display, 0, wx.ALL, 5 )
		
		
		sbSizer17.Add( gSizer18, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( sbSizer17, 1, wx.EXPAND, 5 )
		
		sbSizer18 = wx.StaticBoxSizer( wx.StaticBox( self.sensors_Panel, wx.ID_ANY, u"Intervals" ), wx.VERTICAL )
		
		gSizer19 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.tempInterval_Label = wx.StaticText( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Temp Interval (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tempInterval_Label.Wrap( -1 )
		gSizer19.Add( self.tempInterval_Label, 0, wx.ALL, 5 )
		
		self.tempInterval_Txtctrl = wx.TextCtrl( sbSizer18.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer19.Add( self.tempInterval_Txtctrl, 0, wx.ALL, 5 )
		
		self.humidityInterval_Label = wx.StaticText( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Humidity Interval (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.humidityInterval_Label.Wrap( -1 )
		gSizer19.Add( self.humidityInterval_Label, 0, wx.ALL, 5 )
		
		self.humidityInterval_Txtctrl = wx.TextCtrl( sbSizer18.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer19.Add( self.humidityInterval_Txtctrl, 0, wx.ALL, 5 )
		
		
		sbSizer18.Add( gSizer19, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( sbSizer18, 1, wx.EXPAND, 5 )
		
		sbSizer19 = wx.StaticBoxSizer( wx.StaticBox( self.sensors_Panel, wx.ID_ANY, u"Control" ), wx.VERTICAL )
		
		gSizer20 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.updateSensorsInterval_Btn = wx.Button( sbSizer19.GetStaticBox(), wx.ID_ANY, u"Update Sensors Intervals", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer20.Add( self.updateSensorsInterval_Btn, 0, wx.ALL, 5 )
		
		
		sbSizer19.Add( gSizer20, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( sbSizer19, 1, wx.EXPAND, 5 )
		
		
		self.sensors_Panel.SetSizer( bSizer5 )
		self.sensors_Panel.Layout()
		bSizer5.Fit( self.sensors_Panel )
		self.notebook.AddPage( self.sensors_Panel, u"Sensors", False )
		self.doser_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer20 = wx.StaticBoxSizer( wx.StaticBox( self.doser_Panel, wx.ID_ANY, u"Setup" ), wx.VERTICAL )
		
		gSizer21 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.autoDoser_ToggleBtn = wx.ToggleButton( sbSizer20.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer21.Add( self.autoDoser_ToggleBtn, 0, wx.ALL, 5 )
		
		
		sbSizer20.Add( gSizer21, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( sbSizer20, 1, wx.EXPAND, 5 )
		
		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self.doser_Panel, wx.ID_ANY, u"Control" ), wx.VERTICAL )
		
		gSizer181 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.tankSize_Label = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Tank Size (mL)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tankSize_Label.Wrap( -1 )
		gSizer181.Add( self.tankSize_Label, 0, wx.ALL, 5 )
		
		self.tankSize_Display = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tankSize_Display.Wrap( -1 )
		gSizer181.Add( self.tankSize_Display, 0, wx.ALL, 5 )
		
		self.waterCheck_Label = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Water Check Timing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.waterCheck_Label.Wrap( -1 )
		gSizer181.Add( self.waterCheck_Label, 0, wx.ALL, 5 )
		
		self.waterCheck_Display = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.waterCheck_Display.Wrap( -1 )
		gSizer181.Add( self.waterCheck_Display, 0, wx.ALL, 5 )
		
		self.ecCheck_Label = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"EC Check Timing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ecCheck_Label.Wrap( -1 )
		gSizer181.Add( self.ecCheck_Label, 0, wx.ALL, 5 )
		
		self.ecCheck_Display = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ecCheck_Display.Wrap( -1 )
		gSizer181.Add( self.ecCheck_Display, 0, wx.ALL, 5 )
		
		self.stage1Ec_Label = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Stage 1 EC (mS/cm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Ec_Label.Wrap( -1 )
		gSizer181.Add( self.stage1Ec_Label, 0, wx.ALL, 5 )
		
		self.stage1Ec_Display = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Ec_Display.Wrap( -1 )
		gSizer181.Add( self.stage1Ec_Display, 0, wx.ALL, 5 )
		
		self.stage2Ec_Label = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Stage 2 EC (mS/cm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Ec_Label.Wrap( -1 )
		gSizer181.Add( self.stage2Ec_Label, 0, wx.ALL, 5 )
		
		self.stage2Ec_Display = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Ec_Display.Wrap( -1 )
		gSizer181.Add( self.stage2Ec_Display, 0, wx.ALL, 5 )
		
		self.stage3Ec_Label = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Stage 3 EC (mS/cm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Ec_Label.Wrap( -1 )
		gSizer181.Add( self.stage3Ec_Label, 0, wx.ALL, 5 )
		
		self.stage3Ec_Display = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Ec_Display.Wrap( -1 )
		gSizer181.Add( self.stage3Ec_Display, 0, wx.ALL, 5 )
		
		
		sbSizer21.Add( gSizer181, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( sbSizer21, 1, wx.EXPAND, 5 )
		
		
		self.doser_Panel.SetSizer( bSizer6 )
		self.doser_Panel.Layout()
		bSizer6.Fit( self.doser_Panel )
		self.notebook.AddPage( self.doser_Panel, u"Doser", False )
		
		bSizer1.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_TIMER, self.Tick, id=wx.ID_ANY )
		self.ConnectMqtt.Bind( wx.EVT_BUTTON, self.ConnectMQTT )
		self.sendMqtt_Btn.Bind( wx.EVT_BUTTON, self.SendMQTT )
		self.loadRecipe_Btn.Bind( wx.EVT_BUTTON, self.LoadRecipe )
		self.loadLog_Btn.Bind( wx.EVT_BUTTON, self.LoadLog )
		self.autoLog_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.ToggleLog )
		self.autoLight1_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.CheckLight1Fields )
		self.autoLight2_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.CheckLight2Fields )
		self.autoPump1_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.CheckIrrigation1Fields )
		self.autoPump2_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.CheckIrrigation2Fields )
		self.updateSensorsInterval_Btn.Bind( wx.EVT_BUTTON, self.UpdateSensorsIntervals )
		self.autoDoser_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.CheckDoserFields )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Tick( self, event ):
		event.Skip()
	
	def ConnectMQTT( self, event ):
		event.Skip()
	
	def SendMQTT( self, event ):
		event.Skip()
	
	def LoadRecipe( self, event ):
		event.Skip()
	
	def LoadLog( self, event ):
		event.Skip()
	
	def ToggleLog( self, event ):
		event.Skip()
	
	def CheckLight1Fields( self, event ):
		event.Skip()
	
	def CheckLight2Fields( self, event ):
		event.Skip()
	
	def CheckIrrigation1Fields( self, event ):
		event.Skip()
	
	def CheckIrrigation2Fields( self, event ):
		event.Skip()
	
	def UpdateSensorsIntervals( self, event ):
		event.Skip()
	
	def CheckDoserFields( self, event ):
		event.Skip()
	

