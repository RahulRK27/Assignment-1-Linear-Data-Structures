# def are_rotations(str1, str2):
#     size1 = len(str1)
#     size2 = len(str2)
#     temp = ''
    
#     if size1 != size2:
#         return 0
    
#     temp = str1 + str1
    
#     if (temp.count(str2)> 0):
#         return 1
#     else:
#         return 0

# str1 = 'ABCDEF'
# str2 = 'DEFABC'

# if are_rotations(str1, str2):
#     print ('The Strings are rotations of each other')
# else:
#     print ('The Strings are not rotations of each other')



def first_non_repeating_char(str1):
    char_order =[]
    char_count = {}
    for i in str1:
        if i in char_count:
            char_count[i] +=1
        else:
            char_count[i]=1
            char_order.append(i)
        for i in char_order:
            if char_count[i]==1:
                return i
            return None

print(first_non_repeating_char('string'))


