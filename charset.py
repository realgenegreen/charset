'''chars generator'''
import random

def charset(value: int, numbers= False, symbols= False, letterless= False) -> str:
    '''
    GENERATOR
        // value is how long will be line
        // numbers is the presence of numbers in line
        // symbols is the presence of symbols in line
        // letterless remove letters
    '''
    chset = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    nuset = '1234567890'
    syset = '-:;!?.,'

    if letterless is True:
        chset = ''

    def _chlist():
        set_list = ''
        if numbers is True and symbols is False:
            set_list = chset+(nuset*4)
        if symbols is True and numbers is False:
            set_list = chset+(syset*6)
        if numbers is True and symbols is True:
            set_list = chset+(nuset*2)+(syset*3)
        if numbers is False and symbols is False:
            set_list = chset
        return set_list

    li = _chlist()
    pwd = ''.join([random.choice(li) for x in range(value)])
    return pwd
