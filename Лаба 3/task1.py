def find_item_(list_, item):
    k = 0
    while k < len(list_):
        if list_[k] == item:
            return k
        k += 1

items_list = ['������', '�����', '��������', '�����', '����', '������']

for find_item in ['�����', '�����', '������']:
    index_item = find_item_(items_list, find_item)
    if index_item is not None:
        print(f"������ ��������� '{find_item}' ����� ������ {index_item}.")
    else:
        print(f"����� '{find_item}' �� ������ � ������")
