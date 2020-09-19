def singleton(the_class):
    instances: dict = {}
    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
            return instances
    return get_class


@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '18px'

if __name__=='__main__':
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)