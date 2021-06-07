import learn
import source
class computer:
    def __int__(self):
        name = ""
        cpu = ""
        ram = ""
        hdd = ""

    def config(self):
        print("{0} is a computer with cpu {1}, ram {2}gb and storage of {3}gb.".format(self.name, self.cpu, self.ram,
                                                                                       self.hdd))


com1 = computer()
com2 = computer()

com1.name = 'dell'
com2.name = 'acer'

com1.cpu = "intel i5, 9th generation"
com2.cpu = "intel i7, 5th generation"

com1.ram = 8
com2.ram = 16

com1.hdd = 256
com2.hdd = 1024

com1.config()
com2.config()
