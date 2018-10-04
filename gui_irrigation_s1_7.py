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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"irrigation-s1.7", pos = wx.DefaultPosition, size = wx.Size( 653,521 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.timer = wx.Timer()
		self.timer.SetOwner( self, wx.ID_ANY )
		self.timer.Start( 500 )
		
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
		
		self.currentStage_Display = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.currentStage_Display.Wrap( -1 )
		gSizer2.Add( self.currentStage_Display, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		gSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.main_Panel, wx.ID_ANY, u"Serial" ), wx.VERTICAL )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.serialPortConnect_Btn = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Connect Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.serialPortConnect_Btn, 0, wx.ALL, 5 )
		
		serialPort_CboxChoices = [ u"/dev/ttyUSB0", u"/dev/ttyUSB1", u"/dev/ttyUSB2", u"/dev/ttyUSB3", u"/dev/ttyUSB4", u"/dev/ttyUSB5", u"/dev/ttyUSB6", u"/dev/ttyUSB7" ]
		self.serialPort_Cbox = wx.ComboBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, serialPort_CboxChoices, 0 )
		self.serialPort_Cbox.SetSelection( 0 )
		gSizer3.Add( self.serialPort_Cbox, 0, wx.ALL, 5 )
		
		self.connectedPort_Label = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Connected Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.connectedPort_Label.Wrap( -1 )
		gSizer3.Add( self.connectedPort_Label, 0, wx.ALL, 5 )
		
		self.connectedPort_Display = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Nil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.connectedPort_Display.Wrap( -1 )
		gSizer3.Add( self.connectedPort_Display, 0, wx.ALL, 5 )
		
		self.sendSerial_Btn = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Send Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.sendSerial_Btn, 0, wx.ALL, 5 )
		
		self.serialInput_Txtctrl = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.serialInput_Txtctrl, 0, wx.ALL, 5 )
		
		
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
		self.notebook.AddPage( self.main_Panel, u"Main", False )
		self.p1_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.p1_Panel, wx.ID_ANY, u"Stage 1" ), wx.VERTICAL )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.pump1Stage1Pump_Label = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Pump", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage1Pump_Label.Wrap( -1 )
		gSizer6.Add( self.pump1Stage1Pump_Label, 0, wx.ALL, 5 )
		
		self.pump1Stage1Pump_Display = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage1Pump_Display.Wrap( -1 )
		gSizer6.Add( self.pump1Stage1Pump_Display, 0, wx.ALL, 5 )
		
		self.pump1Stage1Drain_Label = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage1Drain_Label.Wrap( -1 )
		gSizer6.Add( self.pump1Stage1Drain_Label, 0, wx.ALL, 5 )
		
		self.pump1Stage1Drain_Display = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage1Drain_Display.Wrap( -1 )
		gSizer6.Add( self.pump1Stage1Drain_Display, 0, wx.ALL, 5 )
		
		self.pump1Stage1Duration_Label = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Stage Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage1Duration_Label.Wrap( -1 )
		gSizer6.Add( self.pump1Stage1Duration_Label, 0, wx.ALL, 5 )
		
		self.stage1Duration_Display = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage1Duration_Display.Wrap( -1 )
		gSizer6.Add( self.stage1Duration_Display, 0, wx.ALL, 5 )
		
		
		sbSizer5.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.p1_Panel, wx.ID_ANY, u"Stage 2" ), wx.VERTICAL )
		
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.pump1Stage2Pump_Label = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Pump", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage2Pump_Label.Wrap( -1 )
		gSizer7.Add( self.pump1Stage2Pump_Label, 0, wx.ALL, 5 )
		
		self.pump1Stage2Pump_Display = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage2Pump_Display.Wrap( -1 )
		gSizer7.Add( self.pump1Stage2Pump_Display, 0, wx.ALL, 5 )
		
		self.pump1Stage2Drain_Label = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage2Drain_Label.Wrap( -1 )
		gSizer7.Add( self.pump1Stage2Drain_Label, 0, wx.ALL, 5 )
		
		self.pump1Stage2Drain_Display = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage2Drain_Display.Wrap( -1 )
		gSizer7.Add( self.pump1Stage2Drain_Display, 0, wx.ALL, 5 )
		
		self.pump1Stage2Duration_Label = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Stage Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage2Duration_Label.Wrap( -1 )
		gSizer7.Add( self.pump1Stage2Duration_Label, 0, wx.ALL, 5 )
		
		self.stage2Duration_Display = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage2Duration_Display.Wrap( -1 )
		gSizer7.Add( self.stage2Duration_Display, 0, wx.ALL, 5 )
		
		
		sbSizer6.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.p1_Panel, wx.ID_ANY, u"Stage 3" ), wx.VERTICAL )
		
		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.pump1Stage3Pump_Label = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Pump", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage3Pump_Label.Wrap( -1 )
		gSizer8.Add( self.pump1Stage3Pump_Label, 0, wx.ALL, 5 )
		
		self.pump1Stage3Pump_Display = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage3Pump_Display.Wrap( -1 )
		gSizer8.Add( self.pump1Stage3Pump_Display, 0, wx.ALL, 5 )
		
		self.pump1Stage3Drain_Label = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage3Drain_Label.Wrap( -1 )
		gSizer8.Add( self.pump1Stage3Drain_Label, 0, wx.ALL, 5 )
		
		self.pump1Stage3Drain_Display = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage3Drain_Display.Wrap( -1 )
		gSizer8.Add( self.pump1Stage3Drain_Display, 0, wx.ALL, 5 )
		
		self.pump1Stage3Duration_Label = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Stage Duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump1Stage3Duration_Label.Wrap( -1 )
		gSizer8.Add( self.pump1Stage3Duration_Label, 0, wx.ALL, 5 )
		
		self.stage3Duration_Display = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stage3Duration_Display.Wrap( -1 )
		gSizer8.Add( self.stage3Duration_Display, 0, wx.ALL, 5 )
		
		
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
		
		self.pump2Stage1Pump_Display = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage1Pump_Display.Wrap( -1 )
		gSizer61.Add( self.pump2Stage1Pump_Display, 0, wx.ALL, 5 )
		
		self.pump2Stage1Drain_Label = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage1Drain_Label.Wrap( -1 )
		gSizer61.Add( self.pump2Stage1Drain_Label, 0, wx.ALL, 5 )
		
		self.pump2Stage1Drain_Display = wx.StaticText( sbSizer51.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage1Drain_Display.Wrap( -1 )
		gSizer61.Add( self.pump2Stage1Drain_Display, 0, wx.ALL, 5 )
		
		
		sbSizer51.Add( gSizer61, 1, wx.EXPAND, 5 )
		
		
		bSizer21.Add( sbSizer51, 1, wx.EXPAND, 5 )
		
		sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self.p2_Panel, wx.ID_ANY, u"Stage 2" ), wx.VERTICAL )
		
		gSizer71 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.pump2Stage2Pump_Label = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Pump", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage2Pump_Label.Wrap( -1 )
		gSizer71.Add( self.pump2Stage2Pump_Label, 0, wx.ALL, 5 )
		
		self.pump2Stage2Pump_Display = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage2Pump_Display.Wrap( -1 )
		gSizer71.Add( self.pump2Stage2Pump_Display, 0, wx.ALL, 5 )
		
		self.pump2Stage2Drain_Label = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage2Drain_Label.Wrap( -1 )
		gSizer71.Add( self.pump2Stage2Drain_Label, 0, wx.ALL, 5 )
		
		self.pump2Stage2Drain_Display = wx.StaticText( sbSizer61.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage2Drain_Display.Wrap( -1 )
		gSizer71.Add( self.pump2Stage2Drain_Display, 0, wx.ALL, 5 )
		
		
		sbSizer61.Add( gSizer71, 1, wx.EXPAND, 5 )
		
		
		bSizer21.Add( sbSizer61, 1, wx.EXPAND, 5 )
		
		sbSizer71 = wx.StaticBoxSizer( wx.StaticBox( self.p2_Panel, wx.ID_ANY, u"Stage 3" ), wx.VERTICAL )
		
		gSizer81 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.pump2Stage3Pump_Label = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Pump", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage3Pump_Label.Wrap( -1 )
		gSizer81.Add( self.pump2Stage3Pump_Label, 0, wx.ALL, 5 )
		
		self.pump2Stage3Pump_Display = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage3Pump_Display.Wrap( -1 )
		gSizer81.Add( self.pump2Stage3Pump_Display, 0, wx.ALL, 5 )
		
		self.pump2Stage3Drain_Label = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"Drain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage3Drain_Label.Wrap( -1 )
		gSizer81.Add( self.pump2Stage3Drain_Label, 0, wx.ALL, 5 )
		
		self.pump2Stage3Drain_Display = wx.StaticText( sbSizer71.GetStaticBox(), wx.ID_ANY, u"No data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pump2Stage3Drain_Display.Wrap( -1 )
		gSizer81.Add( self.pump2Stage3Drain_Display, 0, wx.ALL, 5 )
		
		
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
		self.sensors_Panel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self.sensors_Panel, wx.ID_ANY, u"Data" ), wx.VERTICAL )
		
		gSizer18 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.temp1_Label = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"Temp 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.temp1_Label.Wrap( -1 )
		gSizer18.Add( self.temp1_Label, 0, wx.ALL, 5 )
		
		self.temp1_Display = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.temp1_Display.Wrap( -1 )
		gSizer18.Add( self.temp1_Display, 0, wx.ALL, 5 )
		
		self.temp2_Label = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"Temp 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.temp2_Label.Wrap( -1 )
		gSizer18.Add( self.temp2_Label, 0, wx.ALL, 5 )
		
		self.temp2_Display = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.temp2_Display.Wrap( -1 )
		gSizer18.Add( self.temp2_Display, 0, wx.ALL, 5 )
		
		self.tempA_Label = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"Average Temp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tempA_Label.Wrap( -1 )
		gSizer18.Add( self.tempA_Label, 0, wx.ALL, 5 )
		
		self.tempA_Display = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tempA_Display.Wrap( -1 )
		gSizer18.Add( self.tempA_Display, 0, wx.ALL, 5 )
		
		self.humidity_Label = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"Humidity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.humidity_Label.Wrap( -1 )
		gSizer18.Add( self.humidity_Label, 0, wx.ALL, 5 )
		
		self.humidity_Display = wx.StaticText( sbSizer17.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.humidity_Display.Wrap( -1 )
		gSizer18.Add( self.humidity_Display, 0, wx.ALL, 5 )
		
		
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
		self.notebook.AddPage( self.sensors_Panel, u"Sensors", True )
		
		bSizer1.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_TIMER, self.Tick, id=wx.ID_ANY )
		self.serialPortConnect_Btn.Bind( wx.EVT_BUTTON, self.ConnectSerial )
		self.sendSerial_Btn.Bind( wx.EVT_BUTTON, self.SendSerial )
		self.loadRecipe_Btn.Bind( wx.EVT_BUTTON, self.LoadRecipe )
		self.loadLog_Btn.Bind( wx.EVT_BUTTON, self.LoadLog )
		self.autoLog_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.ToggleLog )
		self.autoPump1_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.CheckIrrigation1Fields )
		self.autoPump2_ToggleBtn.Bind( wx.EVT_TOGGLEBUTTON, self.CheckIrrigation2Fields )
		self.updateSensorsInterval_Btn.Bind( wx.EVT_BUTTON, self.UpdateSensorsIntervals )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Tick( self, event ):
		event.Skip()
	
	def ConnectSerial( self, event ):
		event.Skip()
	
	def SendSerial( self, event ):
		event.Skip()
	
	def LoadRecipe( self, event ):
		event.Skip()
	
	def LoadLog( self, event ):
		event.Skip()
	
	def ToggleLog( self, event ):
		event.Skip()
	
	def CheckIrrigation1Fields( self, event ):
		event.Skip()
	
	def CheckIrrigation2Fields( self, event ):
		event.Skip()
	
	def UpdateSensorsIntervals( self, event ):
		event.Skip()
	

