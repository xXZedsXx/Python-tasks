def vovel_counter(sentence: str):
    vovels = "aeoiu"
    vovel_count = 0
    for i in sentence:
        if i.lower() in VOVELS:
            vovel_count += 1
            return vovel_count

def open_my_file(file):
    with open(file,'rt') as input_file:
        file_data = input_file.read()
    words_count = len(file_data.split(" "))
    vovel_count = vovel_counter(file_data)
    space_count = file_data.count(' ')

    dict_how_many = {'words':words_count, 'vovels':vovel_count, 'spaces':space_count}
    for key, value in dict_how_many.items():
        print(f'{key}: {value} \n')
open_my_file("test.txt")