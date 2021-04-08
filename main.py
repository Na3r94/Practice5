# init
print('loading...')

f = open('naser_translate/translate.txt')

big_text = f.read()

parts = big_text.split('\n')

#print(parts)

#for i in range(len(parts)):
words = []
i = 0
print(len(parts))
while i < len(parts):
    my_dict = {'english' : parts[i] ,'persian' : parts[i+1]}
    words.append(my_dict)
    i += 2
    
    #my_dict = {}

    #my_dict['english'] = parts[i]
    #i += 1
    #my_dict['persian'] = parts[i]

    #words.append(my_dict)
for i in range(len(words)):
    print(words[i])

print('data loaded')
print('welcome dear user,please enter your text')

while True:
    print('\n 1 - add new word' , '\n 2 - translation Eng to Per' ,
     '\n 3 - translation Per to Eng', '\n 4 - Exit' )
    
    a = int(input())

    if a == 1:
        eng = input('English = ')
        per = input('Persian = ')
        my_dict = {'english' : eng , 'persian' : per}
        words.append(my_dict)
        f = open('naser_translate/translate.txt' , 'a')
        f.write('\n' + eng)
        f.write('\n' + per)
        f.close()
        print('Done!')

    elif a == 2:
        user_string = input()
        user_sentence = user_string.split('.') 
        
        for i in range(len(user_sentence)):
            user_obj = user_sentence[i]
            user_words = user_obj.split(' ')

            for j in range(len(user_words)):
                for i in range(len(words)):

                    if words[i]['english'] == user_words[j]:
                        print(words[i]['persian'],end = ' ')
                        break

                else: #word not found
                    print(user_words[j])

    elif a == 3:
        user_string = input()
        user_sentence = user_string.split('.') 
        
        for i in range(len(user_sentence)):
            user_obj = user_sentence[i]
            user_words = user_obj.split(' ')

            for j in range(len(user_words)):
                for i in range(len(words)):

                    if words[i]['persian'] == user_words[j]:
                        print(words[i]['english'],end = ' ')
                        break

                else: #word not found
                    print(user_words[j])


    elif a == 4:
        exit()




















