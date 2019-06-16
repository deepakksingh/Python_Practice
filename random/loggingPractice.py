import logging

logging.basicConfig(level = logging.DEBUG,
    filename="loggingPractice.log",
    format = "%(asctime)s:%(levelname)s:%(message)s at line %(lineno)s of %(filename)s")


logging.disable(logging.CRITICAL)

logging.debug("+++===+++")



class Pizza():
    def __init__(self,name,value):
        self.name = name
        self.value = value
        initializelogger = logging.getLogger("init_logger")
        initializelogger.debug("Pizza created:{} (${})".format(self.name,self.value))


    def make(self,quantity=1):
        makelogger = logging.getLogger("make_module")
        makelogger.debug("Made {} {} pizza(s)".format(quantity,self.name))

    def eat(self,quantity=1):
        eatlogger = logging.getLogger("eat_module")
        eatlogger.info("Ate {} pizza(s)".format(quantity,self.name))

pizza1 = Pizza("artichoke",15)
pizza1.make()
pizza1.eat()

pizza2 = Pizza("margherita",12)
pizza2.make()
pizza2.eat()

