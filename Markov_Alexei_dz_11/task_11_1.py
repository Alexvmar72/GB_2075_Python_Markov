#Реализовать класс Дата, функция-конструктор которого должна принимать дату в виде строки формата день-месяц-год.
# В рамках класса реализовать два метода:
#
#Первый — с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import re


class My_Data:
    def __init__(self, input_data: str):
        if try:
            self.input_data = input_data
            print(input_data)
        else:
            print(f'Введите корректную дату согласно условию')



    @classmethod
    def select_number(cls, input_data):
        day, month, year = map(int, input_data.split('-'))
        return day, month, year



    #@staticmethod
    def valid_number(self, input_data):


My_Data(input('Введите дату в формате день-месяц-год: '))
#My_Data.select_number(input('Введите дату в формате день-месяц-год: '))
print(My_Data.select_number(input('Введите дату в формате день-месяц-год: ')))