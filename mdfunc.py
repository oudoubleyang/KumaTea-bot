import random
import re


def randomjoke(nojo=False):
    jkfl = random.choice(range(7))
    with open('joke/soviet' + str(jkfl), 'r', encoding='utf-8') as joke:
        jk = random.choice(list(joke)).replace('br', '\n')
        if nojo:
            nojoke = re.compile('[^0-9\\n，。、？！（…“”：；‘’《》）]|_')
            jk = re.sub(nojoke, '　', jk)
        return jk
