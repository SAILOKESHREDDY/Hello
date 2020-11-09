from calculator import calculator

class Hello:
    @staticmethod
    def hello():
        print("Hello World")

Hello.hello()

assert(calculator.add(5,6))
assert(calculator.sub(15,3))
assert(calculator.mul(20,25,9))
assert(calculator.div(100,5))
assert(calculator.mod(4,6))

print('END')
