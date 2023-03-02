import sys
import os
import datetime


class create:
    def __init__(self):
        self.typing = None
        self.path = '/'
        self.nameFile = None
        self.lines = []

    def cycleArgv(self):
        for arg in sys.argv[1:]:

            if arg == '-d' or arg == '-f':
                self.typing = arg
            elif self.typing == '-d':
                if not os.path.exists(arg):
                    os.makedirs(arg)
                os.chdir(arg)
                self.path += f'{arg}/'
            elif self.typing == '-f':
                self.nameFile = arg

    def createFile(self):
        if self.nameFile:
            if os.path.exists(f'{self.nameFile}'):
                f = open(f'{self.nameFile}', "a+")
                f.write('\n\n')
            else:
                f = open(f'{self.nameFile}', "w")
            f.writelines(
                str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            while True:
                result = input('Enter content line: ')
                if result != 'stop':
                    self.lines.append(f'\n{len(self.lines) + 1} {result}')
                else:
                    break
            f.writelines(self.lines)


creatingClass = create()
creatingClass.cycleArgv()
creatingClass.createFile()
