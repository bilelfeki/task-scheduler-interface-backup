# helloworld.py
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "first-ui.ui"

schedulerButton= 'scheduler'
inputTime='time'
inputScriptPath='path'
class EventHandler:

    def __init__(self, builder:pygubu.Builder):
        

        self.builder = builder

    def on_button_click(self,entry):
        print(self.builder.get_object(inputTime).get())
        print(self.builder.get_object(inputScriptPath).cget('path'))

class SchedulerApp:
    def __init__(self, master=None):
        # 1: Create a builder and setup resources path (if you have images)
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)

        # 2: Load an ui file
        builder.add_from_file(PROJECT_UI)

        # 3: Create the mainwindow
        self.mainwindow = builder.get_object('mainwindow', master)

        self.event_handler = EventHandler(self.builder)

        # 4: Connect callbacks
        builder.connect_callbacks(self.event_handler)
        
    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = SchedulerApp()
    app.run()
