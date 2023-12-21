from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

class AverageCalculator(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"  # Set primary color to Purple

        self.result_label = MDLabel(
            text="Ortalama: ",
            theme_text_color="Secondary",  # Set text color to secondary color
            halign="center",
            font_style="H5",
        )

        # Dosya seçme butonunu oluşturun
        file_btn = MDRaisedButton(
            text="Dosya Seç",
            on_press=self.show_file_chooser,
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"center_x": 0.5},
        )

        # Butonun tıklanma olayını belirlemek için fonksiyonu tanımlayın
        calc_btn = MDRaisedButton(
            text="Ortalama Hesapla",
            on_press=self.calculate_average,
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"center_x": 0.5},
        )

        # Arayüzü düzenleyen bir düzen ekleyin
        layout = MDBoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20,
            md_bg_color=self.theme_cls.bg_dark,
        )
        layout.add_widget(file_btn)
        layout.add_widget(calc_btn)
        layout.add_widget(self.result_label)

        # Dosya seçim penceresini oluşturun
        self.file_chooser = FileChooserListView()

        return layout

    def show_file_chooser(self, instance):
        # Dosya seçim penceresini açın
        popup = Popup(
            title="Dosya Seç",
            content=self.file_chooser,
            size_hint=(None, None),
            size=(400, 400),
        )
        popup.open()

    def calculate_average(self, instance):
        try:
            selected_file = self.file_chooser.selection and self.file_chooser.selection[0] or None
            if selected_file:
                # Seçilen dosyayı açın ve okuyun
                with open(selected_file, "r") as file:
                    data = file.read()

                # Satırları sayılara ayırın ve ortalamayı hesaplayın
                numbers = [float(num) for num in data.split() if num.strip()]
                average = sum(numbers) / len(numbers)

                # Sonucu etikete güncelleyin
                self.result_label.text = f"Ortalama: {average:.2f}"

            else:
                self.result_label.text = "Dosya seçilmedi."

        except (FileNotFoundError, ValueError, ZeroDivisionError) as e:
            
            self.result_label.text = f"Hata: {str(e)}"

if __name__ == "__main__":
    AverageCalculator().run()
