import os


def g():
  pass


def dictionary(n, t={}):
   for i in os.listdir(n):
        if os.path.isdir(n + '\\' + i):
            dictionari(n + '\\' + i)
        elif os.path.isfile(n + '\\' + i):
            t[n + '\\' + i] = os.stat(n + '\\' + i).st_size
    return t


def duplicate():
  pass


def duplicate2():
  pass


if __name__ == '__main__':
