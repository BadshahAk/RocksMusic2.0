# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit


from typing import List, Dict, Union


admins: Dict[int, List[int]] = {}


def set(chat_id: int, admins_: List[int]):
    admins[chat_id] = admins_


def get(chat_id: int) -> Union[List[int], bool]:
    if chat_id in admins:
        return admins[chat_id]

    return False


# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.
