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
