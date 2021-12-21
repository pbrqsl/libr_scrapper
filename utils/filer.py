import json
import os

marks_file = 'database.json'
messages_file = 'messages.json'

class FileOperations:

    @classmethod
    def load_marks_file(cls, username):
        try:
            marks_file_path = f'{username}\\{marks_file}'
            with open(marks_file_path, 'r') as file:
                marks_load = json.loads(file.read())
                #print('file load')
            return marks_load
        except:
            print('something went wrong, couldn\'t read marks from the file')

    @classmethod
    def load_messages_file(cls, username):
        try:
            message_file_path = f'{username}\\{messages_file}'
            with open(message_file_path, 'r') as file:
                messages_load = json.loads(file.read())
                #print('file load')
            return messages_load
        except:
            print('something went wrong, couldn\'t read marks from the file')


    @classmethod
    def save_marks_file(cls,username, marks):
        marks_file_path = f'{username}\\{marks_file}'
        os.makedirs(os.path.dirname(marks_file_path), exist_ok=True)
        with open(marks_file_path, 'w') as file:
            file.write(json.dumps(marks))
            #print('Marks saved to file')
        # except:
        #     print('something went wrong, couldn\'t save marks to file')

    @classmethod
    def save_messages_file(cls, username, marks):
        message_file_path = f'{username}\\{messages_file}'
        os.makedirs(os.path.dirname(message_file_path), exist_ok=True)
        with open(message_file_path, 'w') as file:
            file.write(json.dumps(marks))
            #print('Marks saved to file')