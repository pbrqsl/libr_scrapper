import logging

logger = logging.getLogger('libscrap.messageslogic')

class MessagesLogic():


    @classmethod
    def check_for_new_messages(cls,new_messages, old_messages):

        logger.info('checking for new messages')
        cls.old_messages = old_messages
        cls.new_messages = new_messages
        cls.new_messages_list = []

        for message in cls.new_messages:
                if message not in cls.old_messages:
                    cls.new_messages_list.append(message)

        return cls.new_messages_list

    @classmethod
    def check_for_removed_messages(cls,new_marks, old_marks):
        cls.old_messages = old_messages
        cls.new_messages = new_messages
        cls.removed_messages_dict = []

        for message in cls.old_messages:
            if message not in cls.new_messages:
                cls.removed_messages_dict.append(message)

        return cls.removed_messages_dict



    @classmethod
    def format_message(cls, message):
        #format:
        #{'author': 'Gąsłowska Anna (Gąsłowska Anna)', 'title': 'Nauczanie zdalne 7a cd.', 'date': '2021-12-13 12:55:55'}
        return f'<b>"{message["title"]}"</b>, {message["author"]}] ,Data: {message["date"]}\n'


    @classmethod
    def generate_messages_change_message(cls, new_messages, old_messages):
        added_messages = MessagesLogic.check_for_new_messages(new_messages, old_messages)

        message = ''
        if added_messages:
            logger.info('Found new messages')
            message += f'Nowa wiadomość: \n'

            for message_item in added_messages:
                message = message + MessagesLogic.format_message(message_item)
            message = message + '\n'
        else:
            logger.info('No new messages found')

        return message
