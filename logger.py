class Logger:
    active = True

    @staticmethod
    def info(msg):
        print(f'This a message "{msg}"')
