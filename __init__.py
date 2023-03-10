from mycroft import MycroftSkill, intent_file_handler


class InventorName(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('name.inventor.intent')
    def handle_name_inventor(self, message):
        self.speak_dialog('name.inventor')


def create_skill():
    return InventorName()

