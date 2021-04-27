from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen,ScreenManager

import random


class WrongPage(Screen):
	def reset_btn(self):
		self.manager.screens[1].reset_btn()
		sn.current ="mygrid"


class MyGrid(Screen):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.num = random.randint(1,100)
	
	
	def reset_btn(self):
		self.ids.score.text = "0"
		self.num = random.randint(1,100)
	
	def btn(self):
		self.number = int(self.ids.number.text)
		self.score = int(self.ids.score.text) + 1
		

		if self.number == self.num:
			self.manager.screens[0].add_widget(Label(text=f"Try: {str(self.score)}"))
			sn.current ="wrongpage"
		elif self.number < self.num:
			self.ids.score.text = str(self.score)
			self.ids.gridlabel.text="The Secret number \nis higher!\nGuess Again (1-100)"
		elif self.number >self.num:
			self.ids.score.text = str(self.score)
			self.ids.gridlabel.text="The Secret number \nis Lower!\nGuess Again (1-100)"

	
		




class MainApp(App):
  def build(self):
  	global sn
  	sn = ScreenManager()
  	sn.add_widget(WrongPage(name="wrongpage"))
  	sn.add_widget(MyGrid(name="mygrid"))
  	sn.current ="mygrid"
  	return sn
    
MainApp().run()