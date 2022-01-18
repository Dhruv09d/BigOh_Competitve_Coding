'''

Write a function Boolean isValidURL(String url)
eg url : https://www.google.com
         http://www.google.com

'''

def isValidUrl(url):
    check_1 = "https://www"
    check_2 = "http://www"
    check_3 = "com"
    is_check_1 = True
    is_check_2 = True
    is_check_3 = True

    #  split by '.'
    check_1_lst = []
    check_2_lst = []
    check_3_lst = []
    counter = 0
    for i in range(len(url)):
        if counter == 0 :
            if url[i] != '.':
                check_1_lst.append(url[i])
            else:
                counter += 1
        elif counter == 1:
            if url[i] != '.':
                check_2_lst.append(url[i])
            else:
                counter += 1
        else:
            check_3_lst.append(url[i])

    print(check_1_lst, check_2_lst, check_3_lst)


    for i in range(len(check_1)):
        if check_1[i] == check_1_lst[i]:
            is_check_1 = True

    if is_check_1 == False:
        for i in range(len(check_2)):
            if check_2[i] == check_2_lst[i]:
                is_check_2 = True

    for i in range(len(check_2_lst)):
        if (ord(check_2_lst[i]) >= 65 and ord(check_2_lst[i]) >= 90) or (ord(check_2_lst[i]) >= 97 and ord(check_2_lst[i]) <= 122) or (ord(check_2_lst[i]) >= 48 and ord(check_2_lst[i])<= 57):
            pass
        else:
            is_check_2 = False
            break

    if (is_check_2 == True or is_check_1 == True) and is_check_3 == True:
        return True
    else:
        return False



print(isValidUrl("https://www.google.com"))



