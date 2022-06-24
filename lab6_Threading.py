from threading import Thread
class MyThread (Thread):

    def __init__(self, name):
        Thread.__init__(self, name = name)

    def run(self):
        print("Hello, my name is %s" % self.getName())


def main():
    MyThread("Micha").start()


if __name__ == "__main__":
     main()






