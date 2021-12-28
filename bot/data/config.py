from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
MODERATORS = env.list("MODERATORS")
OPERATORS = env.list("OPERATORS")
IP = env.str("ip")

