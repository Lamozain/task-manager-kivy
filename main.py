from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime

class DialogContent(MDBoxLayout):
    # Initial function for class constructors
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = datetime.now().strftime("%A %d %B %Y")

    # Show date function
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save = self.on_save)
        date_dialog.open()

    # Get date and save it in friendly form
    def on_save(self, instance, value, date_range):
        date = value.strftime("%A %d %B %Y")
        self.ids.date_text.text = str(date)



# The main App class
class MainApp(MDApp):
    # Flag
    task_list_dialog = None
    # The build function for setting the theme
    def build(self):
        self.theme_cls.primary_palette = ("Orange")

    # The show task function
    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title="Create Task",
                type= "custom",
                content_cls = DialogContent())
            self.task_list_dialog.open()

    # Add tasks
    def add_task(self, task, task_date):
        print(task.text, task_date)

    # Close dialog
    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()




    

        




if __name__ == "__main__":
    app = MainApp()
    app.run()