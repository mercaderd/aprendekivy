from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Definimos la clase MiLayoutRaíz que hereda de BoxLayout
class MiLayoutRaiz(BoxLayout):
	def __init__(self, **kwargs):
		# Llamamos al método __init__ de la clase BoxLayout
		super(MiLayoutRaiz, self).__init__(**kwargs)
		#Definimos la orientación 'vertical' mediante el atributo orientation
		self.orientation='vertical'
		#Creamos un BoxLayout hijo con orientación horizontal.
		self.BoxLayoutHijo=BoxLayout(orientation='horizontal',size_hint=(1,0.2))
		#Creamos los widgets que necesitamos
		self.tiAviso = TextInput(text='', multiline=False, input_type='number',size_hint=(0.8,1))
		self.lEtiqueta1=Label(text='Avisar en:',size_hint=(0.2,1))
		self.bBorrar=Button(text='Borrar',size_hint=(1,0.2))
		self.lContador=Label(text='0')
		self.bContar=Button(text='+1')
		# Añadimos al BoxLayotHijo los widgets que debe contener
		self.BoxLayoutHijo.add_widget(self.lEtiqueta1)
		self.BoxLayoutHijo.add_widget(self.tiAviso)
		#Añadimos a MiLayoutRaiz el BoxLayoutHijo y el resto de widgets
		self.add_widget(self.BoxLayoutHijo)
		self.add_widget(self.bBorrar)
		self.add_widget(self.lContador)
		self.add_widget(self.bContar)
	
		
	
# Definimos la clase MiApp herededada de la clase App y definimos su método build() devolviendo MiLayoutRaiz
class MiApp(App):
	
	def build(self):
		return MiLayoutRaiz()

if __name__ == '__main__':
	MiApp().run()

