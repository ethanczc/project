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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"main-e2.1", pos = wx.DefaultPosition, size = wx.Size( 653,521 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		self.currentStage_Label = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Current Stage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.currentStage_Label.Wrap( -1 )
		gSizer2.Add( self.currentStage_Label, 0, wx.ALL, 5 )
		
		self.currentStage_Display = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.currentStage_Display.Wrap( -1 )
		gSizer2.Add( self.currentStage_Display, 0, wx.ALL, 5 )
		
		self.stage1Duration_Label = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Stage 1 Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Duration_Label.Wrap( -1 )
		gSizer2.Add( self.stage1Duration_Label, 0, wx.ALL, 5 )
		
		self.stage1Duration_Display = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Duration_Display.Wrap( -1 )
		gSizer2.Add( self.stage1Duration_Display, 0, wx.ALL, 5 )
		
		self.stage2Duration_Label = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Stage 2 Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Duration_Label.Wrap( -1 )
		gSizer2.Add( self.stage2Duration_Label, 0, wx.ALL, 5 )
		
		self.stage2Duration_Display = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Duration_Display.Wrap( -1 )
		gSizer2.Add( self.stage2Duration_Display, 0, wx.ALL, 5 )
		
		self.stage3Duration_Label = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Stage 3 Duratiion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Duration_Label.Wrap( -1 )
		gSizer2.Add( self.stage3Duration_Label, 0, wx.ALL, 5 )
		
		self.stage3Duration_Display = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Duration_Display.Wrap( -1 )
		gSizer2.Add( self.stage3Duration_Display, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		gSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.main_Panel, wx.ID_ANY, u"Ethernet" ), wx.VERTICAL )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.hostIp_Label = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Host IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hostIp_Label.Wrap( -1 )
		gSizer3.Add( self.hostIp_Label, 0, wx.ALL, 5 )
		
		self.hostIp_Txtctrl = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"10.42.0.1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.hostIp_Txtctrl, 0, wx.ALL, 5 )
		
		self.commandTopic_Label = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Command Topic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.commandTopic_Label.Wrap( -1 )
		gSizer3.Add( self.commandTopic_Label, 0, wx.ALL, 5 )
		
		self.commandTopic_Txtctrl = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"RACK1", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.commandTopic_Txtctrl, 0, wx.ALL, 5 )
		
		self.sensorsTopic_Label = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Sensors Topic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sensorsTopic_Label.Wrap( -1 )
		gSizer3.Add( self.sensorsTopic_Label, 0, wx.ALL, 5 )
		
		self.sensorsTopic_Txtctrl = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"RACK1S", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		self.irrigation1_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.irrigation1_Panel, wx.ID_ANY, u"Stage 1" ), wx.VERTICAL )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage1Fill1_Label = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Fill", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Fill1_Label.Wrap( -1 )
		gSizer6.Add( self.stage1Fill1_Label, 0, wx.ALL, 5 )
		
		self.stage1Fill1_Display = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Fill1_Display.Wrap( -1 )
		gSizer6.Add( self.stage1Fill1_Display, 0, wx.ALL, 5 )
		
		self.stage1Drain1_Label = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Drain1_Label.Wrap( -1 )
		gSizer6.Add( self.stage1Drain1_Label, 0, wx.ALL, 5 )
		
		self.stage1Drain1_Display = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Drain1_Display.Wrap( -1 )
		gSizer6.Add( self.stage1Drain1_Display, 0, wx.ALL, 5 )
		
		
		sbSizer5.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.irrigation1_Panel, wx.ID_ANY, u"Stage 2" ), wx.VERTICAL )
		
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage2Fill1_Label = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Fill", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Fill1_Label.Wrap( -1 )
		gSizer7.Add( self.stage2Fill1_Label, 0, wx.ALL, 5 )
		
		self.stage2Fill1_Display = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Fill1_Display.Wrap( -1 )
		gSizer7.Add( self.stage2Fill1_Display, 0, wx.ALL, 5 )
		
		self.stage2Drain1_Label = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Drain1_Label.Wrap( -1 )
		gSizer7.Add( self.stage2Drain1_Label, 0, wx.ALL, 5 )
		
		self.stage2Drain1_Display = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Drain1_Display.Wrap( -1 )
		gSizer7.Add( self.stage2Drain1_Display, 0, wx.ALL, 5 )
		
		
		sbSizer6.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.irrigation1_Panel, wx.ID_ANY, u"Stage 3" ), wx.VERTICAL )
		
		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage3Fill1_Display = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Fill", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Fill1_Display.Wrap( -1 )
		gSizer8.Add( self.stage3Fill1_Display, 0, wx.ALL, 5 )
		
		self.stage3Fill1_Display = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Fill1_Display.Wrap( -1 )
		gSizer8.Add( self.stage3Fill1_Display, 0, wx.ALL, 5 )
		
		self.stage3Drain1_Label = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Drain1_Label.Wrap( -1 )
		gSizer8.Add( self.stage3Drain1_Label, 0, wx.ALL, 5 )
		
		self.stage3Drain1_Display = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Drain1_Display.Wrap( -1 )
		gSizer8.Add( self.stage3Drain1_Display, 0, wx.ALL, 5 )
		
		
		sbSizer7.Add( gSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.irrigation1_Panel, wx.ID_ANY, u"Control" ), wx.VERTICAL )
		
		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.irrigation1_ToggleBtn = wx.ToggleButton( sbSizer8.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.irrigation1_ToggleBtn, 0, wx.ALL, 5 )
		
		
		sbSizer8.Add( gSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer8, 1, wx.EXPAND, 5 )
		
		
		self.irrigation1_Panel.SetSizer( bSizer2 )
		self.irrigation1_Panel.Layout()
		bSizer2.Fit( self.irrigation1_Panel )
		self.notebook.AddPage( self.irrigation1_Panel, u"Irrigation 1", False )
		self.led_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer181 = wx.StaticBoxSizer( wx.StaticBox( self.led_Panel, wx.ID_ANY, u"Stage 1" ), wx.VERTICAL )
		
		gSizer191 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage1Led1On_Label = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led1On_Label.Wrap( -1 )
		gSizer191.Add( self.stage1Led1On_Label, 0, wx.ALL, 5 )
		
		self.stage1Led1On_Display = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led1On_Display.Wrap( -1 )
		gSizer191.Add( self.stage1Led1On_Display, 0, wx.ALL, 5 )
		
		self.stage1Led1Off_Label = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led1Off_Label.Wrap( -1 )
		gSizer191.Add( self.stage1Led1Off_Label, 0, wx.ALL, 5 )
		
		self.stage1Led1Off_Display = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led1Off_Display.Wrap( -1 )
		gSizer191.Add( self.stage1Led1Off_Display, 0, wx.ALL, 5 )
		
		self.stage1Led1Pwr_Label = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led1Pwr_Label.Wrap( -1 )
		gSizer191.Add( self.stage1Led1Pwr_Label, 0, wx.ALL, 5 )
		
		self.stage1Led1Pwr_Display = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led1Pwr_Display.Wrap( -1 )
		gSizer191.Add( self.stage1Led1Pwr_Display, 0, wx.ALL, 5 )
		
		self.stage1Led1Dist_Label = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"Distance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led1Dist_Label.Wrap( -1 )
		gSizer191.Add( self.stage1Led1Dist_Label, 0, wx.ALL, 5 )
		
		self.stage1Led1Dist_Display = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led1Dist_Display.Wrap( -1 )
		gSizer191.Add( self.stage1Led1Dist_Display, 0, wx.ALL, 5 )
		
		
		sbSizer181.Add( gSizer191, 1, wx.EXPAND, 5 )
		
		
		bSizer61.Add( sbSizer181, 1, wx.EXPAND, 5 )
		
		sbSizer191 = wx.StaticBoxSizer( wx.StaticBox( self.led_Panel, wx.ID_ANY, u"Stage 2" ), wx.VERTICAL )
		
		gSizer201 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage2Led1On_Label = wx.StaticText( sbSizer191.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led1On_Label.Wrap( -1 )
		gSizer201.Add( self.stage2Led1On_Label, 0, wx.ALL, 5 )
		
		self.stage2Led1On_Display = wx.StaticText( sbSizer191.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led1On_Display.Wrap( -1 )
		gSizer201.Add( self.stage2Led1On_Display, 0, wx.ALL, 5 )
		
		self.stage2Led1Off_Label = wx.StaticText( sbSizer191.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led1Off_Label.Wrap( -1 )
		gSizer201.Add( self.stage2Led1Off_Label, 0, wx.ALL, 5 )
		
		self.stage2Led1Off_Display = wx.StaticText( sbSizer191.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led1Off_Display.Wrap( -1 )
		gSizer201.Add( self.stage2Led1Off_Display, 0, wx.ALL, 5 )
		
		self.stage2Led1Pwr_Label = wx.StaticText( sbSizer191.GetStaticBox(), wx.ID_ANY, u"Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led1Pwr_Label.Wrap( -1 )
		gSizer201.Add( self.stage2Led1Pwr_Label, 0, wx.ALL, 5 )
		
		self.stage2Led1Pwr_Display = wx.StaticText( sbSizer191.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led1Pwr_Display.Wrap( -1 )
		gSizer201.Add( self.stage2Led1Pwr_Display, 0, wx.ALL, 5 )
		
		self.stage2Led1Dist_Label = wx.StaticText( sbSizer191.GetStaticBox(), wx.ID_ANY, u"Distance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led1Dist_Label.Wrap( -1 )
		gSizer201.Add( self.stage2Led1Dist_Label, 0, wx.ALL, 5 )
		
		self.stage2Led1Dist_Display = wx.StaticText( sbSizer191.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led1Dist_Display.Wrap( -1 )
		gSizer201.Add( self.stage2Led1Dist_Display, 0, wx.ALL, 5 )
		
		
		sbSizer191.Add( gSizer201, 1, wx.EXPAND, 5 )
		
		
		bSizer61.Add( sbSizer191, 1, wx.EXPAND, 5 )
		
		sbSizer211 = wx.StaticBoxSizer( wx.StaticBox( self.led_Panel, wx.ID_ANY, u"Stage 3" ), wx.VERTICAL )
		
		gSizer211 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage3Led1On_Label = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led1On_Label.Wrap( -1 )
		gSizer211.Add( self.stage3Led1On_Label, 0, wx.ALL, 5 )
		
		self.stage3Led1On_Display = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led1On_Display.Wrap( -1 )
		gSizer211.Add( self.stage3Led1On_Display, 0, wx.ALL, 5 )
		
		self.stage3Led1Off_Label = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led1Off_Label.Wrap( -1 )
		gSizer211.Add( self.stage3Led1Off_Label, 0, wx.ALL, 5 )
		
		self.stage3Led1Off_Display = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led1Off_Display.Wrap( -1 )
		gSizer211.Add( self.stage3Led1Off_Display, 0, wx.ALL, 5 )
		
		self.stage3Led1Pwr_Label = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led1Pwr_Label.Wrap( -1 )
		gSizer211.Add( self.stage3Led1Pwr_Label, 0, wx.ALL, 5 )
		
		self.stage3Led1Pwr_Display = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led1Pwr_Display.Wrap( -1 )
		gSizer211.Add( self.stage3Led1Pwr_Display, 0, wx.ALL, 5 )
		
		self.stage3Led1Dist_Label = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"Distance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led1Dist_Label.Wrap( -1 )
		gSizer211.Add( self.stage3Led1Dist_Label, 0, wx.ALL, 5 )
		
		self.stage3Led1Dist_Display = wx.StaticText( sbSizer211.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led1Dist_Display.Wrap( -1 )
		gSizer211.Add( self.stage3Led1Dist_Display, 0, wx.ALL, 5 )
		
		
		sbSizer211.Add( gSizer211, 1, wx.EXPAND, 5 )
		
		
		bSizer61.Add( sbSizer211, 1, wx.EXPAND, 5 )
		
		sbSizer22 = wx.StaticBoxSizer( wx.StaticBox( self.led_Panel, wx.ID_ANY, u"Control" ), wx.VERTICAL )
		
		gSizer22 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.led1_ToggleBtn = wx.ToggleButton( sbSizer22.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer22.Add( self.led1_ToggleBtn, 0, wx.ALL, 5 )
		
		
		sbSizer22.Add( gSizer22, 1, wx.EXPAND, 5 )
		
		
		bSizer61.Add( sbSizer22, 1, wx.EXPAND, 5 )
		
		
		self.led_Panel.SetSizer( bSizer61 )
		self.led_Panel.Layout()
		bSizer61.Fit( self.led_Panel )
		self.notebook.AddPage( self.led_Panel, u"LED 1", False )
		self.irrigation2_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer51 = wx.StaticBoxSizer( wx.StaticBox( self.irrigation2_Panel, wx.ID_ANY, u"Stage 1" ), wx.VERTICAL )
		
		gSizer61 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage1Fill2_Label = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Fill", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Fill2_Label.Wrap( -1 )
		gSizer61.Add( self.stage1Fill2_Label, 0, wx.ALL, 5 )
		
		self.stage1Fill2_Display = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Fill2_Display.Wrap( -1 )
		gSizer61.Add( self.stage1Fill2_Display, 0, wx.ALL, 5 )
		
		self.stage1Drain2_Label = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Drain2_Label.Wrap( -1 )
		gSizer61.Add( self.stage1Drain2_Label, 0, wx.ALL, 5 )
		
		self.stage1Drain2_Display = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Drain2_Display.Wrap( -1 )
		gSizer61.Add( self.stage1Drain2_Display, 0, wx.ALL, 5 )
		
		
		sbSizer51.Add( gSizer61, 1, wx.EXPAND, 5 )
		
		
		bSizer21.Add( sbSizer51, 1, wx.EXPAND, 5 )
		
		sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self.irrigation2_Panel, wx.ID_ANY, u"Stage 2" ), wx.VERTICAL )
		
		gSizer71 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage2Fill2_Label = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Fill", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Fill2_Label.Wrap( -1 )
		gSizer71.Add( self.stage2Fill2_Label, 0, wx.ALL, 5 )
		
		self.stage2Fill2_Display = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Fill2_Display.Wrap( -1 )
		gSizer71.Add( self.stage2Fill2_Display, 0, wx.ALL, 5 )
		
		self.stage2Drain2_Label = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Drain2_Label.Wrap( -1 )
		gSizer71.Add( self.stage2Drain2_Label, 0, wx.ALL, 5 )
		
		self.stage2Drain2_Display = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Drain2_Display.Wrap( -1 )
		gSizer71.Add( self.stage2Drain2_Display, 0, wx.ALL, 5 )
		
		
		sbSizer61.Add( gSizer71, 1, wx.EXPAND, 5 )
		
		
		bSizer21.Add( sbSizer61, 1, wx.EXPAND, 5 )
		
		sbSizer71 = wx.StaticBoxSizer( wx.StaticBox( self.irrigation2_Panel, wx.ID_ANY, u"Stage 3" ), wx.VERTICAL )
		
		gSizer81 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage3Fill2_Display = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Fill", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Fill2_Display.Wrap( -1 )
		gSizer81.Add( self.stage3Fill2_Display, 0, wx.ALL, 5 )
		
		self.stage3Fill2_Display = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Fill2_Display.Wrap( -1 )
		gSizer81.Add( self.stage3Fill2_Display, 0, wx.ALL, 5 )
		
		self.stage3Drain2_Label = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Drain2_Label.Wrap( -1 )
		gSizer81.Add( self.stage3Drain2_Label, 0, wx.ALL, 5 )
		
		self.stage3Drain2_Display = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Drain2_Display.Wrap( -1 )
		gSizer81.Add( self.stage3Drain2_Display, 0, wx.ALL, 5 )
		
		
		sbSizer71.Add( gSizer81, 1, wx.EXPAND, 5 )
		
		
		bSizer21.Add( sbSizer71, 1, wx.EXPAND, 5 )
		
		sbSizer81 = wx.StaticBoxSizer( wx.StaticBox( self.irrigation2_Panel, wx.ID_ANY, u"Control" ), wx.VERTICAL )
		
		gSizer91 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.irrigation2_ToggleBtn = wx.ToggleButton( sbSizer81.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer91.Add( self.irrigation2_ToggleBtn, 0, wx.ALL, 5 )
		
		
		sbSizer81.Add( gSizer91, 1, wx.EXPAND, 5 )
		
		
		bSizer21.Add( sbSizer81, 1, wx.EXPAND, 5 )
		
		
		self.irrigation2_Panel.SetSizer( bSizer21 )
		self.irrigation2_Panel.Layout()
		bSizer21.Fit( self.irrigation2_Panel )
		self.notebook.AddPage( self.irrigation2_Panel, u"Irrigation 2", False )
		self.led2_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer611 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1811 = wx.StaticBoxSizer( wx.StaticBox( self.led2_Panel, wx.ID_ANY, u"Stage 1" ), wx.VERTICAL )
		
		gSizer1911 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage1Led2On_Label = wx.StaticText( sbSizer1811.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led2On_Label.Wrap( -1 )
		gSizer1911.Add( self.stage1Led2On_Label, 0, wx.ALL, 5 )
		
		self.stage1Led2On_Display = wx.StaticText( sbSizer1811.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led2On_Display.Wrap( -1 )
		gSizer1911.Add( self.stage1Led2On_Display, 0, wx.ALL, 5 )
		
		self.stage1Led2Off_Label = wx.StaticText( sbSizer1811.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led2Off_Label.Wrap( -1 )
		gSizer1911.Add( self.stage1Led2Off_Label, 0, wx.ALL, 5 )
		
		self.stage1Led2Off_Display = wx.StaticText( sbSizer1811.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led2Off_Display.Wrap( -1 )
		gSizer1911.Add( self.stage1Led2Off_Display, 0, wx.ALL, 5 )
		
		self.stage1Led2Pwr_Label = wx.StaticText( sbSizer1811.GetStaticBox(), wx.ID_ANY, u"Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led2Pwr_Label.Wrap( -1 )
		gSizer1911.Add( self.stage1Led2Pwr_Label, 0, wx.ALL, 5 )
		
		self.stage1Led2Pwr_Display = wx.StaticText( sbSizer1811.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led2Pwr_Display.Wrap( -1 )
		gSizer1911.Add( self.stage1Led2Pwr_Display, 0, wx.ALL, 5 )
		
		self.stage1Led2Dist_Label = wx.StaticText( sbSizer1811.GetStaticBox(), wx.ID_ANY, u"Distance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led2Dist_Label.Wrap( -1 )
		gSizer1911.Add( self.stage1Led2Dist_Label, 0, wx.ALL, 5 )
		
		self.stage1Led2Dist_Display = wx.StaticText( sbSizer1811.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Led2Dist_Display.Wrap( -1 )
		gSizer1911.Add( self.stage1Led2Dist_Display, 0, wx.ALL, 5 )
		
		
		sbSizer1811.Add( gSizer1911, 1, wx.EXPAND, 5 )
		
		
		bSizer611.Add( sbSizer1811, 1, wx.EXPAND, 5 )
		
		sbSizer1911 = wx.StaticBoxSizer( wx.StaticBox( self.led2_Panel, wx.ID_ANY, u"Stage 2" ), wx.VERTICAL )
		
		gSizer2011 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage2Led2On_Label = wx.StaticText( sbSizer1911.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led2On_Label.Wrap( -1 )
		gSizer2011.Add( self.stage2Led2On_Label, 0, wx.ALL, 5 )
		
		self.stage2Led2On_Display = wx.StaticText( sbSizer1911.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led2On_Display.Wrap( -1 )
		gSizer2011.Add( self.stage2Led2On_Display, 0, wx.ALL, 5 )
		
		self.stage2Led3Off_Label = wx.StaticText( sbSizer1911.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led3Off_Label.Wrap( -1 )
		gSizer2011.Add( self.stage2Led3Off_Label, 0, wx.ALL, 5 )
		
		self.stage2Led2Off_Display = wx.StaticText( sbSizer1911.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led2Off_Display.Wrap( -1 )
		gSizer2011.Add( self.stage2Led2Off_Display, 0, wx.ALL, 5 )
		
		self.stage2Led2Pwr_Label = wx.StaticText( sbSizer1911.GetStaticBox(), wx.ID_ANY, u"Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led2Pwr_Label.Wrap( -1 )
		gSizer2011.Add( self.stage2Led2Pwr_Label, 0, wx.ALL, 5 )
		
		self.stage2Led2Pwr_Display = wx.StaticText( sbSizer1911.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led2Pwr_Display.Wrap( -1 )
		gSizer2011.Add( self.stage2Led2Pwr_Display, 0, wx.ALL, 5 )
		
		self.stage2Led2Dist_Label = wx.StaticText( sbSizer1911.GetStaticBox(), wx.ID_ANY, u"Distance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led2Dist_Label.Wrap( -1 )
		gSizer2011.Add( self.stage2Led2Dist_Label, 0, wx.ALL, 5 )
		
		self.stage2Led2Dist_Display = wx.StaticText( sbSizer1911.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Led2Dist_Display.Wrap( -1 )
		gSizer2011.Add( self.stage2Led2Dist_Display, 0, wx.ALL, 5 )
		
		
		sbSizer1911.Add( gSizer2011, 1, wx.EXPAND, 5 )
		
		
		bSizer611.Add( sbSizer1911, 1, wx.EXPAND, 5 )
		
		sbSizer2111 = wx.StaticBoxSizer( wx.StaticBox( self.led2_Panel, wx.ID_ANY, u"Stage 3" ), wx.VERTICAL )
		
		gSizer2111 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage3Led2On_Label = wx.StaticText( sbSizer2111.GetStaticBox(), wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led2On_Label.Wrap( -1 )
		gSizer2111.Add( self.stage3Led2On_Label, 0, wx.ALL, 5 )
		
		self.stage3Led2On_Display = wx.StaticText( sbSizer2111.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led2On_Display.Wrap( -1 )
		gSizer2111.Add( self.stage3Led2On_Display, 0, wx.ALL, 5 )
		
		self.stage3Led2Off_Label = wx.StaticText( sbSizer2111.GetStaticBox(), wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led2Off_Label.Wrap( -1 )
		gSizer2111.Add( self.stage3Led2Off_Label, 0, wx.ALL, 5 )
		
		self.stage3Led2Off_Display = wx.StaticText( sbSizer2111.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led2Off_Display.Wrap( -1 )
		gSizer2111.Add( self.stage3Led2Off_Display, 0, wx.ALL, 5 )
		
		self.stage3Led2Pwr_Label = wx.StaticText( sbSizer2111.GetStaticBox(), wx.ID_ANY, u"Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led2Pwr_Label.Wrap( -1 )
		gSizer2111.Add( self.stage3Led2Pwr_Label, 0, wx.ALL, 5 )
		
		self.stage3Led2Pwr_Display = wx.StaticText( sbSizer2111.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led2Pwr_Display.Wrap( -1 )
		gSizer2111.Add( self.stage3Led2Pwr_Display, 0, wx.ALL, 5 )
		
		self.stage3Led2Dist_Label = wx.StaticText( sbSizer2111.GetStaticBox(), wx.ID_ANY, u"Distance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led2Dist_Label.Wrap( -1 )
		gSizer2111.Add( self.stage3Led2Dist_Label, 0, wx.ALL, 5 )
		
		self.stage3Led2Dist_Display = wx.StaticText( sbSizer2111.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Led2Dist_Display.Wrap( -1 )
		gSizer2111.Add( self.stage3Led2Dist_Display, 0, wx.ALL, 5 )
		
		
		sbSizer2111.Add( gSizer2111, 1, wx.EXPAND, 5 )
		
		
		bSizer611.Add( sbSizer2111, 1, wx.EXPAND, 5 )
		
		sbSizer221 = wx.StaticBoxSizer( wx.StaticBox( self.led2_Panel, wx.ID_ANY, u"Control" ), wx.VERTICAL )
		
		gSizer221 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.led2_ToggleBtn = wx.ToggleButton( sbSizer221.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer221.Add( self.led2_ToggleBtn, 0, wx.ALL, 5 )
		
		
		sbSizer221.Add( gSizer221, 1, wx.EXPAND, 5 )
		
		
		bSizer611.Add( sbSizer221, 1, wx.EXPAND, 5 )
		
		
		self.led2_Panel.SetSizer( bSizer611 )
		self.led2_Panel.Layout()
		bSizer611.Fit( self.led2_Panel )
		self.notebook.AddPage( self.led2_Panel, u"LED 2", False )
		self.doser_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self.doser_Panel, wx.ID_ANY, u"Stage 1" ), wx.VERTICAL )
		
		gSizer16 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage1Ec_Label = wx.StaticText( sbSizer15.GetStaticBox(), wx.ID_ANY, u"EC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Ec_Label.Wrap( -1 )
		gSizer16.Add( self.stage1Ec_Label, 0, wx.ALL, 5 )
		
		self.stage1Ec_Display = wx.StaticText( sbSizer15.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Ec_Display.Wrap( -1 )
		gSizer16.Add( self.stage1Ec_Display, 0, wx.ALL, 5 )
		
		self.stage1Topup_Label = wx.StaticText( sbSizer15.GetStaticBox(), wx.ID_ANY, u"Top up", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Topup_Label.Wrap( -1 )
		gSizer16.Add( self.stage1Topup_Label, 0, wx.ALL, 5 )
		
		self.stage1Topup_Display = wx.StaticText( sbSizer15.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Topup_Display.Wrap( -1 )
		gSizer16.Add( self.stage1Topup_Display, 0, wx.ALL, 5 )
		
		self.stage1Dose_Label = wx.StaticText( sbSizer15.GetStaticBox(), wx.ID_ANY, u"Dose", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Dose_Label.Wrap( -1 )
		gSizer16.Add( self.stage1Dose_Label, 0, wx.ALL, 5 )
		
		self.stage1Dose_Display = wx.StaticText( sbSizer15.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Dose_Display.Wrap( -1 )
		gSizer16.Add( self.stage1Dose_Display, 0, wx.ALL, 5 )
		
		
		sbSizer15.Add( gSizer16, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( sbSizer15, 1, wx.EXPAND, 5 )
		
		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self.doser_Panel, wx.ID_ANY, u"Stage 2" ), wx.VERTICAL )
		
		gSizer17 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage2Ec_Label = wx.StaticText( sbSizer16.GetStaticBox(), wx.ID_ANY, u"EC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Ec_Label.Wrap( -1 )
		gSizer17.Add( self.stage2Ec_Label, 0, wx.ALL, 5 )
		
		self.stage2Ec_Display = wx.StaticText( sbSizer16.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Ec_Display.Wrap( -1 )
		gSizer17.Add( self.stage2Ec_Display, 0, wx.ALL, 5 )
		
		self.stage2Topup_Label = wx.StaticText( sbSizer16.GetStaticBox(), wx.ID_ANY, u"Top up", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Topup_Label.Wrap( -1 )
		gSizer17.Add( self.stage2Topup_Label, 0, wx.ALL, 5 )
		
		self.stage2Topup_Display = wx.StaticText( sbSizer16.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Topup_Display.Wrap( -1 )
		gSizer17.Add( self.stage2Topup_Display, 0, wx.ALL, 5 )
		
		self.stage2Dose_Label = wx.StaticText( sbSizer16.GetStaticBox(), wx.ID_ANY, u"Dose", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Dose_Label.Wrap( -1 )
		gSizer17.Add( self.stage2Dose_Label, 0, wx.ALL, 5 )
		
		self.stage2Dose_Display = wx.StaticText( sbSizer16.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Dose_Display.Wrap( -1 )
		gSizer17.Add( self.stage2Dose_Display, 0, wx.ALL, 5 )
		
		
		sbSizer16.Add( gSizer17, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( sbSizer16, 1, wx.EXPAND, 5 )
		
		sbSizer18 = wx.StaticBoxSizer( wx.StaticBox( self.doser_Panel, wx.ID_ANY, u"Stage 3" ), wx.VERTICAL )
		
		gSizer18 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.stage3Ec_Label = wx.StaticText( sbSizer18.GetStaticBox(), wx.ID_ANY, u"EC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Ec_Label.Wrap( -1 )
		gSizer18.Add( self.stage3Ec_Label, 0, wx.ALL, 5 )
		
		self.stage3Ec_Display = wx.StaticText( sbSizer18.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Ec_Display.Wrap( -1 )
		gSizer18.Add( self.stage3Ec_Display, 0, wx.ALL, 5 )
		
		self.stage3Topup_Label = wx.StaticText( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Top up", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Topup_Label.Wrap( -1 )
		gSizer18.Add( self.stage3Topup_Label, 0, wx.ALL, 5 )
		
		self.stage3Topup_Display = wx.StaticText( sbSizer18.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Topup_Display.Wrap( -1 )
		gSizer18.Add( self.stage3Topup_Display, 0, wx.ALL, 5 )
		
		self.stage3Dose_Label = wx.StaticText( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Dose", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Dose_Label.Wrap( -1 )
		gSizer18.Add( self.stage3Dose_Label, 0, wx.ALL, 5 )
		
		self.stage3Dose_Display = wx.StaticText( sbSizer18.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Dose_Display.Wrap( -1 )
		gSizer18.Add( self.stage3Dose_Display, 0, wx.ALL, 5 )
		
		
		sbSizer18.Add( gSizer18, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( sbSizer18, 1, wx.EXPAND, 5 )
		
		sbSizer20 = wx.StaticBoxSizer( wx.StaticBox( self.doser_Panel, wx.ID_ANY, u"Control" ), wx.VERTICAL )
		
		gSizer21 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.doser_ToggleBtn = wx.ToggleButton( sbSizer20.GetStaticBox(), wx.ID_ANY, u"AUTO", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer21.Add( self.doser_ToggleBtn, 0, wx.ALL, 5 )
		
		self.m_staticText100 = wx.StaticText( sbSizer20.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText100.Wrap( -1 )
		gSizer21.Add( self.m_staticText100, 0, wx.ALL, 5 )
		
		self.ec_Label = wx.StaticText( sbSizer20.GetStaticBox(), wx.ID_ANY, u"EC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ec_Label.Wrap( -1 )
		gSizer21.Add( self.ec_Label, 0, wx.ALL, 5 )
		
		self.ec_Display = wx.StaticText( sbSizer20.GetStaticBox(), wx.ID_ANY, u"no data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ec_Display.Wrap( -1 )
		gSizer21.Add( self.ec_Display, 0, wx.ALL, 5 )
		
		
		sbSizer20.Add( gSizer21, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( sbSizer20, 1, wx.EXPAND, 5 )
		
		
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
		self.irrigation1_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.CheckIrrigationFields )
		self.led1_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.CheckLedFields )
		self.irrigation2_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.CheckIrrigationFields )
		self.led2_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.CheckLedFields )
		self.doser_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.CheckDoserFields )
	
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
	
	def CheckIrrigationFields( self, event ):
		event.Skip()
	
	def CheckLedFields( self, event ):
		event.Skip()
	
	
	
	def CheckDoserFields( self, event ):
		event.Skip()
	

