from calculator import calculator

class Hello:
    @staticmethod
    def hello():
        print("Hello World")

Hello.hello()

try:
    assert(calculator.add(5,6)==11)
except:
    print("ADD function failed")

try:
    assert(calculator.sub(15,3)==12)
except:
    print("SUB function failed")

try:
    assert(calculator.mul(20,20)==400)
except:
    print("MUL function failed")

try:
    assert(calculator.div(100,5)==20)
except:
    print("DIV function failed")

try:
    assert(calculator.mod(4,6)==4)
except:
    print("MOD function failed")

print('END')
