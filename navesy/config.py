

class Configuration:
    """ Конфигурация приложения """
    DEBUG = True
    SECRET_KEY = [str(_) for _ in range(1, 30)]
