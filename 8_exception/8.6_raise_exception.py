#raise exception

#diy your own exception


class OverRangeException(Exception):

    info = "over the range "


    def __init__(self,info):
        OverRangeException.info = info
        pass

    def __str__(self):
        return OverRangeException.info

    pass



def test():
    ore = OverRangeException("over the range 50")
    a = 60
    if a>50:
        raise ore
    pass

test()

