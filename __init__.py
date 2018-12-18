from mycroft import MycroftSkill, intent_file_handler


class OpenWebApp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('app.web.open.intent')
    def handle_app_web_open(self, message):
        self.speak_dialog('app.web.open')


def create_skill():
    return OpenWebApp()

