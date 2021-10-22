print('Это калькулятор, для начала работы введите вид операции (+ или - или * или /)')

operator=input();

print('теперь введите первое число')

numb1=float(input("1 число = "))

print('теперь введите второе число')

numb2=float(input("2 число = "))

if operator=="+":
    x=numb1+numb2;
    print (int(x))
if operator=="-":
    x=numb1-numb2;
    print (int(x))
if operator=="/":
    x=numb1/numb2;
    print (int(x))
if operator=="*":
    x=numb1*numb2;
    print (int(x))