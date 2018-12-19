from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder
import webbrowser
import os

class OpenWebApp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    #@intent_file_handler('app.web.open.intent')

    @intent_handler(IntentBuilder("").require('read'))
    def handle_read_command(self, message):
        parameter_value = 'pocket'
        print('parameter value is: ' + parameter_value)
        url = "http://www.google.com/search?q="+parameter_value + "&btnI"
        webbrowser.open(url)
        self.speak_dialog('Opening Pocket')

    @intent_handler(IntentBuilder("").require('open').require("AppName"))
    def handle_app_web_open(self, message):
        parameter_value = message.data.get("AppName")
        print('parameter value is: ' + parameter_value)
        url = "http://www.google.com/search?q="+parameter_value + "&btnI"
        webbrowser.open(url)
        self.speak_dialog('app.web.open')


def create_skill():
    return OpenWebApp()

