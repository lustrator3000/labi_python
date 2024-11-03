def find_common_participants(s1, s2, separator=','):
    s1_new = s1.split(separator)
    s2_new = s2.split(separator) #stroka dlinnaya
    merger = set(s1_new).intersection(s2_new) #obshie
    return list(merger)
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров‚Сидоров,Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))