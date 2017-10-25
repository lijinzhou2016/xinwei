from dog import Dog
from dog import __hello


xiaobai = Dog("white", 'hashiqi', 'xiaobai')
print xiaobai.__tedian
print xiaobai.run()

class Taidi(Dog):
    def __init__(self, color, name, age, type_="taidi"):
        Dog.__init__(self, color, type_, name)
        self._age = age

    def get_age(self):
        return self._age

    def get_type(self):
        return self._type_

    def run(self, name=""):
        return name + " run"

    # def run(self, name):
    #     return name,"run"


xiaohuang = Taidi("yellow", "xiaohuang", 11)
print xiaohuang.run("taidi")
print xiaohuang.get_name()
print xiaohuang.get_age()
print xiaohuang.get_type()