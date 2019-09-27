import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload

import config

vk_session = vk_api.VkApi(token=config.TOKEN)
longpoll = VkBotLongPoll(vk_session, config.GROUP_ID)
api = vk_session.get_api()
upload = VkUpload(vk_session)
def main():
        for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    print(event.obj)
                    # user_id = event.obj.from_id
                    # text = event.obj.text.lower()
                    


def send_message(user_id,message=None,keyboard=None,attachment=None):
    api.messages.send(user_id=user_id, message = message, random_id = get_random_id(),keyboard=keyboard,attachment=attachment,dont_parse_links=1)

# def prepare_attachment(user_id,index):
#     user = api.users.get(user_id=user_id)[0]
#     img = mg.get_image(user['first_name'], user['last_name'],index+1)
#     photo = upload.photo_messages(photos=img)[0]
#     attachments = []
#     attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
#     return ','.join(attachments)
    
if __name__ == '__main__':
    main()
