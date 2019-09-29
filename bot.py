import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload
import config
import imagehelper

vk_session = vk_api.VkApi(token=config.TOKEN)
longpoll = VkBotLongPoll(vk_session, config.GROUP_ID)
api = vk_session.get_api()
upload = VkUpload(vk_session)
def main():
        for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    text = event.obj.text.lower()
                    user_id = event.obj.from_id
                    if text =='омон' or text =='omon':
                        if event.obj.attachments != [] and event.obj.attachments[0]['type'] =='photo':
                            url = get_max_size_image_url(event.obj.attachments[0]['photo']['sizes'])
                            img = imagehelper.set_omon_free(url)
                            send_message(user_id,attachment=prepare_attachment(img))
                        else:
                            send_message(user_id,'ВЫ забыли прикрепить изображение')

                    
def send_message(user_id,message=None,keyboard=None,attachment=None):
    api.messages.send(user_id=user_id, message = message, random_id = get_random_id(),keyboard=keyboard,attachment=attachment,dont_parse_links=1)

def prepare_attachment(img):
    photo = upload.photo_messages(photos=img)[0]
    attachments = []
    attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
    return ','.join(attachments)

def get_max_size_image_url(sizes):
    sizes.sort(key= lambda x: int(x['height']), reverse = True)
    return sizes[0]['url']

if __name__ == '__main__':
    main()
