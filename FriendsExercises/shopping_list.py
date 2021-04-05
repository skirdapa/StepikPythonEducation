def print_shopping_list(pizza, salad):
    pizza1 = set(pizza)
    salad1 = set(salad)
    products = pizza1.union(salad1)
    for item in products:
        if item in pizza1 and item in salad1:
            result = pizza[item] + salad[item]
            print(item, ':', result)
        else:
            if item in pizza1:
                result = pizza[item]
            else:
                result = salad[item]
            print(item, ':', result)


# Если вам надо 5 кг помидоров для салата и 3 кг для супа, вы сразу покупаете 8 килограммов.
# Напишите функцию, которая напечатает на экран, какие продукты надо купить, и сколько их нужно. Информацию о каждом
# ингредиенте выводите на отдельной строке в формате: огурцы, кг: 1.5. Каждый продукт должен присутствовать в выводе
# только один раз.

def create_shop_list(*dishs):
    for dish in dishs:






pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}

print_shopping_list(pizza, salad)
