from calculator import calculator

class Hello:
    @staticmethod
    def hello():
        print("Hello World")

Hello.hello()

print(calculator.add(5,6))
print(calculator.sub(15,3))
print(calculator.mul(20,25))
print(calculator.div(100,5))
print(calculator.mod(4,6))

print('END')
