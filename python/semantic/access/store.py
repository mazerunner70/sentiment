

class Store:
    def __init__(self):
        dotenv_path = join(os.getcwd(), '.env')
        load_dotenv(dotenv_path)
        jpw = str(os.getenv('jpw'))+'1'
