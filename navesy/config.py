

class Configuration:
    """ Конфигурация приложения """
    DEBUG = False
    SECRET_KEY = [str(_) for _ in range(1, 30)]
