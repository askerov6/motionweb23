#(aws)   (django)    (django rest)    (django orm)   (django templates)

#django откозуу-pip install django
#

'''numbers = [5, 7, 4, 7, 10, 4, 7,8 ,3]

for i in numbers:
    if i <= 5:
        print(i)

'fruits = ('apple', 'banana', 'cherry', 'carrot')

for i in fruits:
    print(i.capitalize())
'''

'''cars = ['tesla', 'bmw', 'honda', 'audi', 'tiko']
for a in (cars):
    print(a.upper())
'''

'''cars = ['audi', 'bmw', 'byd', 'tesla']

name = input('write name of car: ').lower()
cars.remove(name)

print(cars)
'''

'''cars = [0, 4, -4, 8, 55]

max_number = 0
for i in cars:
    if i > max_number:
        max_number = i
print(max_number)
'''

'''numbers = [57, 6, 0, -1, 5, -45, -1, 0, 5]

new_numbers = []

for i in numbers:
    if i <= 0:
        new_numbers.append(i)

print(new_numbers)
'''

'''numbers = [5, 3, 9, 1, 7]
min_value = numbers[0]
for number in numbers:
    if number < min_value:
        min_value = number
print(min_value)
'''

'''def multiply_by_index(nums):
    new_list = []
    for i in range(len(nums)):
        new_list.append(2 * nums[i])

    print(new_list)
multiply_by_index([1, 2, 3, 4, 5])
'''
'''
Ctrl + r = обновить страницу
Ctrl + c = копировать
Ctrl + v = вставить 
Ctrl + z = отмена (назад)
Ctrl + s = сохранить , порядок
Ctrl + x =вырезать + копировать 
Ctrl + a = выделение всех элементов
Ctrl + y = повторить отмененное действие
Alt + tab = переключения между вкладками
'''



def change_numbers(lst):
    return [num * idx for idx, num in enumerate(lst)]

print(change_numbers([4, 5, 2, 7, 8]))