import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Configure un logger simple."""
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Exemple d'utilisation :
# logger = setup_logger('discord_bot', 'bot.log')
# logger.info("Le bot a démarré !")
