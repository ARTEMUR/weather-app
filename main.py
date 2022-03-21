from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from pyowm import OWM
from pyowm.utils.config import get_default_config
dict_config = get_default_config()
dict_config['language'] = 'ru'
owm = OWM('6c5f730cd197646e0b0a8e607e407d09')
mgr = owm.weather_manager()
class mainApp(App):
    def build(self):
        bl = BoxLayout()
        btn = Button(text = "Искать",font_size = "50",size_hint = (.6,1))
        self.lb = Label(text = '',font_size = '28')
        self.ti = TextInput(font_size = '50',size_hint = (.6,1))
        btn.bind(on_release = self.weather)
        bl.add_widget(btn)
        bl.add_widget(self.lb)
        bl.add_widget(self.ti)
        return bl
    def weather(self, instanse):
        try:
            global mgr
            observation = mgr.weather_at_place(self.ti.text)
            w = observation.weather
            t = w.temperature('celsius')
            temp = t['temp']
            temp_max = t['temp_max']
            temp_min = t['temp_min']
            feels = t['feels_like']
            
            speed = w.wind()['speed']
            state = w.detailed_status
            clouds = w.clouds
            humidity = w.humidity
            
            self.lb.text = 'Температура в городе\стране-\n'+self.ti.text+': '+str(temp)+'C°'+'\nМинимальная: '+str(temp_min)+'C°'+'\nМаксимальная: '+str(temp_max)+'C°'+'\nОщущается как: '+str(feels)+'C°'+'\nСкорость ветра: '+str(speed)+'м/с'+'\nCостояние: \n'+ state+ '\nОблака: '+str(clouds)+'%'+'\nВлажность: '+str(humidity)+'%' 
        except:
            self.lb.text = "Такого города не найдено!"
            
if __name__=='__main__':
    mainApp().run()