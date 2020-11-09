from calculator import calculator

class Hello:
    @staticmethod
    def hello():
        print("Hello World")

Hello.hello()

try:
    assert(calculator.add(5,6)==11)
    print("1")
except:
    print("ADD function failed")

try:
    assert(calculator.sub(15,3)==12)
    print("2")
except:
    print("SUB function failed")

try:
    assert(calculator.mul(20,20)==400)
    print("3")
except:
    print("MUL function failed")

try:
    assert(calculator.div(100,5)==20)
    print("4")
except:
    print("DIV function failed")

try:
    assert(calculator.mod(4,6)==4)
    print("5")
except:
    print("MOD function failed")

print('END')
