import vk_api
import random
from module3.lesson3.cb_rf import get_dollar_course


token = 'vk1.a.ZD79SvplLFT6YRR2JGeNOJT4V6R1jyLgc1VqMFcUbfjUzdQ7cstsBgdwJVRPwGyeNsO7qFrZkt-twlizkOQDCNzz7lCORudfr0GHpqY8QJe0NgBZYeI-ajnvlvS2dwfENtFmY8jiK3vVXpGuGb9gA5n7CpPizKlDkAH1zhgSfSnnv2VPCKiaA-jc2s3MEZHRkWctHG6IzmBPSwgHJsICSw'

vk = vk_api.VkApi(token=token)

while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] > 0:
        message_text = messages['items'][0]['last_message']['text']

        if message_text == 'курс':
            ans = f'Курс доллара на сегодня составляет {get_dollar_course()} руб.'
        else:
            ans = 'Неизвестная команда'

        user_id = messages['items'][0]['last_message']['from_id']
        random_id = random.randint(-10 ** 7, 10 ** 7)

        vk.method('messages.send', {'user_id': user_id,
                                    'random_id': random_id,
                                    'message': ans
                                    })
















