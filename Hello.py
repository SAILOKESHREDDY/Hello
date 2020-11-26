from calculator import calculator

class Hello:
    @staticmethod
    def hello():
        print("Hello World")

Hello.hello()

try:
    assert(calculator.add(5,6)==11)
    print("first function success")
except:
    print("ADD function failed")

try:
    assert(calculator.sub(15,3)==12)
    print("second function success")
except:
    print("SUB function failed")

try:
    assert(calculator.mul(20,20)==400)
    print("third function success")
except:
    print("MUL function failed")

try:
    assert(calculator.div(100,5)==20)
    print("fourth function success")
except:
    print("DIV function failed")

try:
    assert(calculator.mod(4,6)==4)
    print("fifth function success")
except:
    print("MOD function failed")

print("push starts in main")
print('END of Hello Unit test')
