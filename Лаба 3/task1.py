def find_item_(list_, item):
    k = 0
    while k < len(list_):
        if list_[k] == item:
            return k
        k += 1

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'персик']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_(items_list, find_item)
    if index_item is not None:
        print(f"первое вхождение '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"товар '{find_item}' не найден в списке")
