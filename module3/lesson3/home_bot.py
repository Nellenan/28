import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from cb_rf import get_course
from wiki import get_article


token = 'vk1.a.ZD79SvplLFT6YRR2JGeNOJT4V6R1jyLgc1VqMFcUbfjUzdQ7cstsBgdwJVRPwGyeNsO7qFrZkt-twlizkOQDCNzz7lCORudfr0GHpqY8QJe0NgBZYeI-ajnvlvS2dwfENtFmY8jiK3vVXpGuGb9gA5n7CpPizKlDkAH1zhgSfSnnv2VPCKiaA-jc2s3MEZHRkWctHG6IzmBPSwgHJsICSw'


vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        user_id = event.user_id
        if user_message[:2] == '-к':
            course_name = user_message[2:]
            response = get_course(course_name)
        elif user_message[:2] == '-в':
            article = user_message[2:]
            response = get_article(article)
        else:
            response = 'Неизвестная команда'
        vk.messages.send(
            user_id=user_id,
            message=response,
            random_id=random.randint(-10**7, 10**7),
        )
