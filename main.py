import requests
import locale
import math
import datetime
import arabic_reshaper
import bidi.algorithm
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.uix.widget import Widget

def get_weather_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def get_user_language():
    return "ar"

def translate_weather_description(description, language):
    translations = {
        "fr": {
            "clear sky": "ciel dégagé",
            "few clouds": "quelques nuages",
            "scattered clouds": "nuages épars",
            "broken clouds": "nuages dispersés",
            "light rain": "pluie légère",
            "moderate rain": "pluie modérée",
            "overcast clouds": "nuages couverts",
            "shower rain": "averses de pluie",
            "rain": "pluie",
            "thunderstorm": "orage",
            "snow": "neige",
            "mist": "brume",
            "morning": "matin",
            "night": "nuit",
            "Monday": "Lundi",
            "Tuesday": "Mardi",
            "Wednesday": "Mercredi",
            "Thursday": "Jeudi",
            "Friday": "Vendredi",
            "Saturday": "Samedi",
            "Sunday": "Dimanche",
        },
        "ar": {
            "clear sky": "سماء صافية",
            "few clouds": "بعض السحب",
            "scattered clouds": "سحب متفرقة",
            "broken clouds": "سحب متفككة",
            "light rain": "مطر خفيف",
            "moderate rain": "مطر متوسط",
            "overcast clouds": "سحب ملبدة",
            "shower rain": "أمطار متفرقة",
            "rain": "مطر",
            "thunderstorm": "عاصفة رعدية",
            "snow": "ثلج",
            "mist": "ضباب",
            "morning": "صباحًا",
            "night": "مساءًا",
            "Monday": "الاثنين",
            "Tuesday": "الثلاثاء",
            "Wednesday": "الأربعاء",
            "Thursday": "الخميس",
            "Friday": "الجمعة",
            "Saturday": "السبت",
            "Sunday": "الأحد",
        },
        "en": {
            # Ajoutez ici les traductions en anglais si nécessaire
        },
    }
    translated_description = translations.get(language, {}).get(description, description)
    return translated_description

def format_timestamp(timestamp, language):
    dt = datetime.datetime.fromtimestamp(timestamp)
    day = dt.strftime("%A")
    date = dt.strftime("%d/%m")
    hour = dt.strftime("%I:%M %p")  # Format 12 heures
    if language == "ar":
        # Conversion des chiffres en occidental-indien
        hour = hour.replace("AM", "صباحًا").replace("PM", "مساءًا")
        day = translate_weather_description(day, language)
    return f"{day}, {date}, {hour}"

class WeatherApp(App):

    @staticmethod
    def load_fonts():
        # Charger la police arabe
        LabelBase.register(name="Arabic", fn_regular="Arabic.ttf")

    def build(self):
        api_key = "726979203dff399d0794ed1c43a248d6"
        location = "Schiltigheim"

        # Obtenir la langue du téléphone
        user_language = get_user_language()

        # Appeler l'API OpenWeatherMap pour obtenir les données météorologiques
        weather_data = get_weather_data(api_key, location)

        # Créer la mise en page de l'interface graphique
        layout = BoxLayout(orientation='vertical')

        # Créer l'arrière-plan de couleur
        background_color = get_color_from_hex("#00C8FF")
        Window.clearcolor = background_color

        # Créer le widget de dessin pour les lignes
        canvas = GridLayout(cols=1, spacing=dp(30), size_hint_y=None, padding=(dp(30), dp(25)))

        current_day_date = None

        now = datetime.datetime.now()
        current_hour = now.hour
        current_time_label = None

        for forecast in weather_data["list"]:
            timestamp = forecast["dt"]
            temperature_kelvin = forecast["main"]["temp"]
            weather_description = forecast["weather"][0]["description"]

            temperature_celsius = round(temperature_kelvin - 273.15)
            temperature_celsius = math.ceil(temperature_celsius)

            translated_description = translate_weather_description(weather_description, user_language)
            formatted_timestamp = format_timestamp(timestamp, user_language)

            day = formatted_timestamp.split(", ")[0]
            date = formatted_timestamp.split(", ")[1]
            hour = formatted_timestamp.split(", ")[2]

            if day != current_day_date:
                current_day_date = day

                # Reshaper et bidi l'affichage du jour avec jour/mois
                reshaped_day_date = arabic_reshaper.reshape(f"{current_day_date}   {date}")
                bidi_day_date = bidi.algorithm.get_display(reshaped_day_date)

                # Ajouter le jour avec jour/mois au centre
                day_date_label = Label(text=f"[color=0000FF]{bidi_day_date}[/color]", font_size=dp(24), halign='center', markup=True, font_name="Arabic")
                canvas.add_widget(day_date_label)
                
                # Ajouter une ligne horizontale après la date
                line = BoxLayout(size_hint=(1, None), height=dp(1), orientation='horizontal')
                canvas.add_widget(line)

            # Reshaper et bidi l'affichage de l'heure
            reshaped_hour = arabic_reshaper.reshape(hour)
            bidi_hour = bidi.algorithm.get_display(reshaped_hour)

            # Ajouter l'heure avec la météo correspondante
            time_label = Label(text=f"[color=FF0000]{bidi_hour}[/color]", font_size=dp(18), halign='center', markup=True, font_name="Arabic")
            canvas.add_widget(time_label)

            # Ajouter la température
            temperature_label = Label(text=f"[color=FF0000]{temperature_celsius} °C[/color]", font_size=dp(18), halign='center', markup=True, font_name="Arabic")
            canvas.add_widget(temperature_label)

            # Ajouter la description de la météo
            reshaped_description = arabic_reshaper.reshape(translated_description)
            bidi_description = bidi.algorithm.get_display(reshaped_description)

            weather_label = Label(text=f"[color=FFFFFF]{bidi_description}[/color]", font_size=dp(25), halign='center', markup=True, font_name="Arabic")
            canvas.add_widget(weather_label)

            # Ajouter une ligne horizontale après la description de la météo
            line = BoxLayout(size_hint=(1, None), height=1, orientation='horizontal')    
            canvas.add_widget(line)

        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scroll_view.add_widget(canvas)
        layout.add_widget(scroll_view)

        return layout

if __name__ == '__main__':
    WeatherApp().run()
