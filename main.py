import random
import kivy
import os
import magic
import vlc
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color,Rectangle,InstructionGroup
from kivy.utils import get_color_from_hex
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class TextInput(TextInput):
	def __init__(self,**kwargs):
		super(TextInput,self).__init__(**kwargs)

class ButtonWidget(Button):

	p = vlc.MediaPlayer("/home/baeji/Music/test.mp3")
	song_color = (0.1,0.4,0.6,1)
	music_path = '/home/baeji/Desktop/YL/'
	current_song = ''

	def __init__(self,**kwargs):
		super(ButtonWidget,self).__init__(**kwargs)
		#self.bind(on_press = self.callback)

	def playSong(self,instance):
		os.chdir(self.music_path)

		
		if(instance.text != "STOP" and instance.text!="PAUSE" and instance.text!="PLAY"):
			k = instance.parent.parent.parent.children[0].children[2]
			self.p.stop()
			self.p = vlc.MediaPlayer(self.music_path + instance.text + '.mp3')
			self.p.play()
			for i in instance.parent.children:
				i.background_color = self.song_color
			instance.background_color =  (0.22,0.6,1,1)
			k.text = instance.text
			self.current_song = instance.text

		if(instance.text == "STOP"):
			self.p.stop()
			#t = self.parent.parent.parent.children[0].children[0].children[0]
			#print t.children.length

		if(instance.text == "PLAY"):
			self.p.play()
			instance.text = "PAUSE"
			instance.background_color = (0.9,0.7,0.1,1)
			self.parent.parent.do_layout()
			return

		if(instance.text == "PAUSE"):
			self.p.pause()
			instance.text = "PLAY"
			instance.background_color = (0.25,0.5,0.1,1)
			self.parent.parent.do_layout()
		#time.sleep(10)
		#p.stop()

	def library(self,instance):
		print "Show library"
		k = instance.parent.parent.parent.children[0]
		k.clear_widgets()
		s = GridLayout(cols = 1, spacing = 3, size_hint_y = None)
		s.bind(minimum_height = s.setter('height'))
		os.chdir(self.music_path)
		for i in os.listdir(u'.'):
			#if 'audio' in magic.from_file(self.music_path + i , mime = True):
			if '.mp3' in i:
				i = i.encode('utf-8')
				print type(i), i
				s.add_widget(Button(
					text = i[:-4],
					color = (1,1,1,1),
					size_hint_y = None,
					height = 70,
					on_press = self.playSong,
					background_color = self.song_color,
					background_normal = ''
				))

		g = ScrollView(size_hint = (1,0.5), pos_hint = {'x': 0, 'y': 0})
		g.add_widget(s)
		d = StackLayout(size_hint = (1,0.3),pos_hint = {'center_x': 0.5, 'y': 0.5}, orientation = 'lr-tb')
		d.add_widget(Button(text = self.current_song,color = (0,0,0,1),size_hint = (1,0.5),pos_hint = {'x': 0,'y':0.5}, background_normal = '', background_color = (1,1,1,1)))
		d.add_widget(Button(text = "STOP",size_hint = (0.5,0.5), on_press = self.playSong, background_normal = '', background_color = (0.9,0.1,0.1,1)))
		d.add_widget(Button(text = "PAUSE",size_hint = (0.5,0.5), on_press = self.playSong, background_normal = '', background_color = (0.9,0.7,0.1,1)))
		k.add_widget(g)
		k.add_widget(d)
	
	def on_enter(self,instance):
		print instance.text
		os.chdir('/home/baeji/Desktop/Web Scraping/mdl/mdl/spiders')
		os.system('python yl.py \'' + instance.text + '\'' )

	def download(self,instance):
		print "Download music"
		k = instance.parent.parent.parent.children[0]
		k.clear_widgets()
		h = TextInput(multiline = False)
		h.bind(on_text_validate = self.on_enter)
		k.add_widget(h)

class RootWidget(BoxLayout):
	pass

class MusicApp(App):
	def build(self):
		self.root = root = RootWidget()
		return root

if __name__ == '__main__':
	MusicApp().run()