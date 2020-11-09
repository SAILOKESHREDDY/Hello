from calculator import calculator

class Hello:
    @staticmethod
    def hello():
        print("Hello World")

Hello.hello()

assert(calculator.add(5,6)==11)
assert(calculator.sub(15,3)==12)
assert(calculator.mul(20,25)==450)
assert(calculator.div(100,5)==20)
assert(calculator.mod(4,6)==4)

print('END')
