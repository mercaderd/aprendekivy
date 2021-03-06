﻿from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
from kivy.core.audio import SoundLoader


# Definimos la clase MiLayoutRaíz que hereda de BoxLayout
class MiLayoutRaiz(BoxLayout):

    # Creamos una propiedad numérica que contendra el valor del contador
    pContador=NumericProperty(0)
    
    def __init__(self, **kwargs):
        # Llamamos al método __init__ de la clase BoxLayout
        super(MiLayoutRaiz, self).__init__(**kwargs)
        #Definimos la orientación 'vertical' mediante el atributo orientation
        self.orientation='vertical'
        #Creamos un objeto SoundLoader para reproducir una alarma
        self.sound = SoundLoader.load('alarma.wav')        
        #Creamos un BoxLayout hijo con orientación horizontal.
        self.BoxLayoutHijo=BoxLayout(orientation='horizontal',size_hint=(1,0.1))
        #Creamos los widgets que necesitamos
        self.tiAviso = TextInput(text='', multiline=False, input_type='number',size_hint=(0.3,1),padding_y=(0,0))
        self.lEtiqueta1=Label(text='Avisar en:',size_hint=(0.7,1))
        self.bBorrar=Button(text='Borrar',size_hint=(1,0.2))
        self.lContador=Label(text='0',size_hint=(1,0.35))
        self.bContar=Button(text='+1',size_hint=(1,0.35))
        # Añadimos al BoxLayotHijo los widgets que debe contener
        self.BoxLayoutHijo.add_widget(self.lEtiqueta1)
        self.BoxLayoutHijo.add_widget(self.tiAviso)
        #Añadimos a MiLayoutRaiz el BoxLayoutHijo y el resto de widgets
        self.add_widget(self.BoxLayoutHijo)
        self.add_widget(self.bBorrar)
        self.add_widget(self.lContador)
        self.add_widget(self.bContar)
        # Se hancen las asociaciones (bind) evento-método necesarias        
        self.bContar.bind(on_press=self.plus_one)
        self.bBorrar.bind(on_press=self.clear_Contador)
        # Asociamos el método resize_text al evento de cambio de la propiedad altura de cada widget
        for child in self.children:
            child.bind(height = self.resize_text)
        for child in self.BoxLayoutHijo.children:
            child.bind(height = self.resize_text)
      
				
    # Método para cambiar tamaño de texto de un widget
    def resize_text(self,instance,value):
			instance.font_size = value*0.75
    # Método para gestionar cambios en la propiedad creada
    def on_pContador(self, instance, pos):
         self.lContador.text=str(self.pContador)
         if self.tiAviso.text == self.lContador.text:
             print 'OHHH'
             if self.sound: 
			self.sound.stop()
			self.sound.play()
    
    
    def plus_one(self, instance):
        self.pContador=self.pContador+1
        
    def clear_Contador(self, instance):
        self.pContador=0
   
		
# Definimos la clase MiApp herededada de la clase App y definimos su método build() devolviendo MiLayoutRaiz
class MiApp(App):
	
	def build(self):
		return MiLayoutRaiz()
	
	
		

			

if __name__ == '__main__':
	MiApp().run()

