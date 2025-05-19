# Задание 1
# Дан текстовыйфайл. Необходимо создать новыйфайл,
# в который требуется переписать из исходного файла все
# слова, состоящие не менее чем из семи букв.

with open('text.txt','w') as f:
    f.write("banana mango me the math mango-banana guava-it-python")

buffer = ''
with open('text.txt','r') as f:
    buffer = f.readline()

print(buffer)
buffer_list = buffer.split(" ")
print(buffer_list)
with open("text_result.txt",'w') as f:
    for i in range(len(buffer_list)-1):
        if len(buffer_list[i]) > 7:
            f.writelines(buffer_list[i]+"\n")
# Дан текстовый файл. Необходимо переписать его
# строки в другой файл. Порядок строк во втором файле
# должен совпадать с порядком строк в заданном файле.
with open('text_result.txt',"r") as f:
    with open('new_text_result.txt',"w")as fi:
        fi.writelines(f.readlines())
