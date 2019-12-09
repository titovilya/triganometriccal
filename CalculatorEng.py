# Works only for simple trigonometric expressions
# Not a single library used!

# The program can process all trigonometric equations
# Extra spaces at the end are forbidden. Will be considered an incorrect entry.
# Equations should fit the standard. cos(x) + sin^2(t) = y
# Where under t and x can be 1x/3, 412x/5, x. Moreover, x is mandatory before division
# Under y can be sqrt (2), sqrt (5) / 3, 24123 and all kinds of numbers
# Instead of cosine and sine, you can also use all tangent and cotangent
# However, I could not write an algorithm to solve any addition, multiplication
# The program will give an answer only for simple trigonometric expressions of the form:
#            cos(12x) = 1
#            sin(3x/4) = 1/2
#            ctg(50x/21) = sqrt(3/3)
#            tg(x) = sqrt(2)/2


# Divides the input expression into 2 parts. Separator is equal.
# The input entered by the user goes to the input
# At the output of 2 lists: before and after. In addition, each element is separate.
# At the same time, we discard part of the errors.
def main_separation(main_input_string):
    index_input_first = 0
    try:
        while main_input_string[index_input_first] != '=':
            index_input_first += 1
        first_word = main_input_string[:index_input_first-1] #Before equal
        second_word = main_input_string[index_input_first+2:] #After equal
        arithmetic_operators = ['*', '+', '-', '/']
        if second_word[-1] == ' ': # space is forbidden
            return False
        try:
            index_first = 0 #main counter for processing elements
            null_index = 0 #considers to exclude spaces at the beginning of input
            index_third = 0 #to count everything in the second round
            len_first_word = len(first_word) #the length of the part before equal
            main_index_first = 0 #on the left side, the part of the expression counts how many characters
            list_first_word = []
            while len_first_word != main_index_first:
                if first_word[index_first] == ' ':
                    while first_word[index_first] == ' ':
                        index_first += 1
                        null_index += 1
                        main_index_first += 1
                        index_third += 1
                if first_word[index_first] in arithmetic_operators: #if there are arithmetic operators
                    list_first_word.append(first_word[index_first])  #then add the operator to the list
                    index_first += 1
                    main_index_first += 1
                    index_third += 1
                if first_word[index_first] == ' ':
                    index_first += 1
                    main_index_first += 1
                    index_third += 1
                while first_word[index_first] != '(':
                    index_first += 1
                    main_index_first += 1
                index_second = index_first
                if '^' in first_word[index_third:index_first]:
                    first_multi_index = first_word.find('^') #if there is a degree
                    list_first_word.append(first_word[index_third:index_first-2])
                    list_first_word.append(first_word[first_multi_index])
                    list_first_word.append(first_word[first_multi_index+1])
                else:
                    list_first_word.append(first_word[index_third:index_first])
                main_index_first += 1
                while first_word[index_second] != ')':
                    index_second += 1
                    main_index_first += 1
                list_first_word.append(first_word[index_first+1:index_second])
                index_first = index_second+1
                index_third = index_first
        except IndexError:
            return False
        try:
            list_second_word = [] #go to the right side
            index_second = 0 #use for processing elements
            null_index_second = 0 #used to remove spaces
            if second_word[null_index_second] == ' ': #remove extra spaces
                while second_word[null_index_second] == ' ':
                    null_index_second += 1
                    index_second += 1
            if '(' in second_word: #if there is a root
                while second_word[index_second] != '(':
                    index_second += 1
                list_second_word.append(second_word[null_index_second:index_second])
                index_second_begin = index_second+1
                while second_word[index_second] != ')':
                    index_second += 1
                list_second_word.append(second_word[index_second_begin:index_second])
                for operator in arithmetic_operators:
                    if operator in second_word:
                        index_second += 1
                        list_second_word.append(second_word[index_second])
                        list_second_word.append(second_word[index_second+1])
            else:
                if '/' in second_word: #if there is a division
                    point_input = second_word.find('/')
                    list_second_word.append(second_word[:point_input])
                    list_second_word.append(second_word[point_input])
                    list_second_word.append(second_word[point_input+1:])
                else:
                    list_second_word.append(second_word[null_index_second:])
        except IndexError:
            return False
        return [list_first_word] + [list_second_word]
    except IndexError:
        return False

# Check the left side for correctness
# The entire left side is at the entrance
# The output is a boolean value
# Works through list length
def conditional_check_left(first_list):
    allowed_words = ['cos', 'sin', 'tg', 'ctg']
    allowed_operators = ['*', '+', '-', '/']
    len_first = len(first_list)
    # It simply cannot be below such lengths
    if (len_first < 2) or (len_first > 7):
        return False
    elif len_first == 3:
        return False
    elif len_first == 6:
        return False
    #----------------------------------------
    #for cos(x) and for same
    elif len_first == 2:
        if first_list[0] in allowed_words:
            if ('x' in first_list[1]) or ('y' in first_list[1]):
                return True
            else:
                return False
        else:
            return False
    elif len_first == 4:
        # --------for cos^2(x)-----------
        if '^' in first_list:
            if first_list[0] in allowed_words:
                if ('x' in first_list[3]) or ('y' in first_list[3]):
                    if first_list[1] == '^':
                        if (first_list[2] == '3') or (first_list[2] == '2'):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            #-------------for cos(x)cos(y)-------------
            if first_list[0] in allowed_words:
                if ('x' in first_list[1]) or ('y' in first_list[1]):
                    if first_list[2] in allowed_words:
                        if ('x' in first_list[3]) or ('y' in first_list[3]):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
    elif len_first == 5:
        #for cos(x)*cos(y)
        if first_list[0] in allowed_words:
            if ('x' in first_list[1]) or ('y' in first_list[1]):
                if first_list[2] in allowed_operators:
                    if first_list[3] in allowed_words:
                        if ('x' in first_list[4]) or ('y' in first_list[4]):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
        #for cos(x) + sin^2(x)
    elif len_first == 7:
        if ('x' in first_list[3]) or ('y' in first_list[3]):
            if first_list[0] in allowed_words:
                if first_list[1] == '^':
                    if (first_list[2] == '3') or (first_list[2] == '2'):
                        if first_list[4] in allowed_operators:
                            if first_list[5] in allowed_words:
                                if ('x' in first_list[6]) or ('y' in first_list[6]):
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            #for sin^2(x) + cos(x)
            if first_list[0] in allowed_words:
                if ('x' in first_list[1]) or ('y' in first_list[1]):
                    if first_list[4] == '^':
                        if (first_list[5] == '3') or (first_list[5] == '2'):
                            if first_list[2] in allowed_operators:
                                if first_list[3] in allowed_words:
                                    if ('x' in first_list[6]) or ('y' in first_list[6]):
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False


# Check the right side for correctness
# On the entrance, the entire right side
# The output is a boolean value
# Works through the length of the list, similar to the left
def conditional_check_right(second_list):
    len_second = len(second_list)
    if (len_second < 1) or (len_second > 4):
        return False
    elif len_second == 1: #if it`s a digit
        if ''.join(second_list).isdigit():
            return True
        else:
            return False
    elif len_second == 2: #if there is a root of a number like sqrt (3) and the same
        if second_list[0] == "sqrt":
            if ''.join(second_list[1]).isdigit():
                return True
            elif ('-' in second_list) and (''.join(second_list[1]).isdigit()):
                return True
            else:
                return False
        else:
            return False
    elif len_second == 3: # if there is a division of the form 1/2 and the same
        if second_list[1] == '/':
            if (''.join(second_list[0]).isdigit()) and (''.join(second_list[2]).isdigit()):
                return True
            else:
                return False
        else:
            return False
    elif len_second == 4: #if there is division and root of the form sqrt (2)/2 and the same
        if second_list[0] == 'sqrt':
            if (''.join(second_list[1]).isdigit()) and (''.join(second_list[3]).isdigit()):
                if second_list[2] == '/':
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

# The whole solution algorithm starts and ends in this function
# At the entrance, the divided left and right parts.
# The output is the answer x.
# Unfortunately, I was able to write only an algorithm for solving simple trigs. equations
#Examples:    cos(12x) = 1
#            sin(3x/4) = 1/2
#            ctg(50x/21) = sqrt(3/3)
#            tg(x) = sqrt(2)/2
def solve_main(seperate_first, seperate_second):
    answer_xm = '' #saves the first answer here
    answer_xmm = '' #saves the second answer here
    if len(seperate_first) == 2: #only for the simplest equations
        sep_first_two = seperate_first[1]
        index_of_slash = sep_first_two.find('/')
        if '/' in sep_first_two:
            #miltiplicator - this is an argument in brackets containing x
            multiplicator = '*' + sep_first_two[:index_of_slash-1] + sep_first_two[index_of_slash:] #if it`s a division
        else:
            multiplicator  = '/' + sep_first_two[:-1] #if there is no division
        answer_first = 'There is no answer.'
        try:
            multiplicator = int(multiplicator)
        except (ValueError, TypeError):
            pass
#-----------------------------------for cos-----------------------------
        #the whole solution is obvious, looks at the right side of the equation and immediately write the answer
        if seperate_first[0] == 'cos':
            if len(seperate_second) == 1:
                seperate_second[-1] = int(seperate_second[-1])
                if seperate_second[-1] == 1:
                    answer_first = ''
                elif seperate_second[-1] == 0:
                    answer_first = 'pi/2'
                elif seperate_second[-1] == -1:
                    answer_first = ''
                else:
                    answer_first = 'There is no answer.'
            elif len(seperate_second) == 3:
                #for example: 1/3, 2/5
                seperate_second[0] = int(seperate_second[0])
                seperate_second[-1] = int(seperate_second[-1])
                seperate_second_cos_three = seperate_second[0] / seperate_second[-1] #quotient
                seperate_second[0] = str(seperate_second[0])
                seperate_second[-1] = str(seperate_second[-1])
                if seperate_second_cos_three == 0.5:
                    answer_first = '(+/-)pi/3'
                elif (seperate_second_cos_three > -1) and (seperate_second_cos_three < 1): #if there is no integer but suitable
                    answer_first = '(+/-)arccos(' + ''.join(seperate_second) + ')'
                else:
                    answer_first = 'There is no answer.'
            elif len(seperate_second) == 4:
                #for example sqrt(3)/2, sqrt(23)/5
                seperate_second[1] = int(seperate_second[1])
                seperate_second[-1] = int(seperate_second[-1])
                seperate_second_cos_four = (seperate_second[1]**(1/2))/seperate_second[-1] #quotient
                seperate_second[0] = str(seperate_second[0])
                seperate_second[-1] = str(seperate_second[-1])
                if (int(seperate_second[1]) == 3) and (int(seperate_second[-1]) == 2): #sqrt(3)/2
                    answer_first = '(+/-)pi/6'
                elif (int(seperate_second[1]) == 2) and (int(seperate_second[-1]) == 2):#sqrt(2)/2
                    answer_first = '(+/-)pi/4'
                elif (seperate_second_cos_four > -1) and (seperate_second_cos_four < 1):
                    # didn’t come up with anything smarter than how to create a second list, and make all the elements string
                    # then we simply connect them together
                    strange_thing = []
                    for elem in seperate_second:
                        strange_thing.append(str(elem))
                    answer_first = '(+/-)arccos(' + ''.join(strange_thing) + ')'
                else:
                    answer_first = 'There is no answer.'
            else:
                if seperate_second[0] == 'sqrt':
                    #for sqrt
                    seperate_second[1] = int(seperate_second[1])
                    if (seperate_second[1]**(1/2) < 1) and (seperate_second[1]**(1/2) > -1):
                        strange_thing = []
                        for elem in seperate_second:
                            strange_thing.append(str(elem))
                        answer_first = '(+/-)arccos(' + ''.join(strange_thing) + ')'
                    else:
                        answer_first = 'There is no answer.'
            if answer_first != 'There is no answer.':
                if len(str(multiplicator)) > 0:
                    if len(str(answer_first)) > 0:
                        answer_xm = 'x = (' + answer_first + ')' + str(multiplicator) + ' + (2*pi*n)' + str(multiplicator)
                    else:
                        if '/' in str(multiplicator):
                            answer_xm = 'x = ' + '(2*pi*n)' + str(multiplicator)
                        else:
                            answer_xm = 'x = ' + '(2*pi*n)' + str(multiplicator)
                else:
                    if len(str(answer_first)) > 0:
                        answer_xm = 'x = ' + answer_first + ' + 2*pi*n'
                    else:
                        answer_xm = 'x = (2*pi*n)'
            else:
                answer_xm = answer_first
#-----------------------------for sin----------------------------
            #complete analogy to cosine
        elif seperate_first[0] == 'sin':
            answer_second = 0
            if len(seperate_second) == 1:
                seperate_second[-1] = int(seperate_second[-1])
                if seperate_second[-1] == 1:
                    answer_first = 'pi/2'
                    answer_second = '3pi/2'
                elif seperate_second[-1] == 0:
                    answer_first = 'pi'
                else:
                    answer_first = 'There is no answer.'
            elif len(seperate_second) == 3:
                seperate_second[0] = int(seperate_second[0])
                seperate_second[-1] = int(seperate_second[-1])
                seperate_second_cos_three = seperate_second[0] / seperate_second[-1]  #quotient
                seperate_second[0] = str(seperate_second[0])
                seperate_second[-1] = str(seperate_second[-1])
                if seperate_second_cos_three == 0.5:
                    answer_first = 'pi/6'
                    answer_second = '5*pi/6'
                elif (seperate_second_cos_three > -1) and (seperate_second_cos_three < 1):
                    answer_first = 'arcsin(' + ''.join(seperate_second) + ')'
                    answer_second = 'pi-arcsin(' + ''.join(seperate_second) + ')'
                else:
                    answer_first = 'There is no answer.'
                    answer_second = ''
            elif len(seperate_second) == 4:
                seperate_second[1] = int(seperate_second[1])
                seperate_second[-1] = int(seperate_second[-1])
                seperate_second_cos_four = (seperate_second[1] ** (1 / 2)) / seperate_second[-1]  #quotient
                seperate_second[0] = str(seperate_second[0])
                seperate_second[-1] = str(seperate_second[-1])
                if (int(seperate_second[1]) == 3) and (int(seperate_second[-1]) == 2):
                    answer_first = 'pi/3'
                    answer_second = '2*pi/3'
                elif (int(seperate_second[1]) == 2) and (int(seperate_second[-1]) == 2):
                    answer_first = 'pi/4'
                    answer_second = '3*pi/4'
                elif (seperate_second_cos_four > -1) and (seperate_second_cos_four < 1):
                    strange_thing = []
                    for elem in seperate_second:
                        strange_thing.append(str(elem))
                    answer_first = 'arcsin(' + ''.join(strange_thing) + ')'
                    answer_second = 'pi-arcsin(' + ''.join(strange_thing) + ')'
                else:
                    answer_first = 'There is no answer.'
            else:
                if seperate_second[0] == 'sqrt':
                    seperate_second[1] = int(seperate_second[1])
                    if (seperate_second[1] ** (1 / 2) < 1) and (seperate_second[1] ** (1 / 2) > -1):
                        strange_thing = []
                        for elem in seperate_second:
                            strange_thing.append(str(elem))
                        answer_first = 'arcsin(' + ''.join(strange_thing) + ')'
                        answer_second = 'pi-arcsin(' + ''.join(strange_thing) + ')'
                    else:
                        answer_first = 'There is no answer.'
            if answer_first != 'There is no answer.':
                if len(str(multiplicator)) > 0:
                    answer_xm = 'x1 = (' + answer_first + ')' + str(multiplicator) + ' + (2*pi*n)' + str(
                            multiplicator)
                    answer_xmm = 'x2 = (' + answer_second + ')' + str(multiplicator) + ' + (2*pi*n)' + str(
                            multiplicator)
                else:
                    answer_xm = 'x1 = ' + answer_first + ' + 2*pi*n'
                    answer_xmm = 'x2 = ' + answer_second + ' + 2*pi*n'
            else:
                answer_xm = answer_first
                answer_xmm = ''
#-------------------for tg------------------------------
            #complete analogy to cosine
        elif seperate_first[0] == 'tg':
            if len(seperate_second) == 1:
                seperate_second[-1] = int(seperate_second[-1])
                if seperate_second[-1] == 1:
                    answer_first = 'pi/4'
                elif seperate_second[-1] == 0:
                    answer_first = ''
                else:
                    answer_first = 'There is no answer.'
            elif len(seperate_second) == 3:
                seperate_second[0] = int(seperate_second[0])
                seperate_second[-1] = int(seperate_second[-1])
                seperate_second_cos_three = seperate_second[0] / seperate_second[-1] #quotient
                seperate_second[0] = str(seperate_second[0])
                seperate_second[-1] = str(seperate_second[-1])
                if (seperate_second_cos_three > -1) and (seperate_second_cos_three < 1):
                    answer_first = 'arctg(' + ''.join(seperate_second) + ')'
                else:
                    answer_first = 'There is no answer.'
            elif len(seperate_second) == 4:
                seperate_second[1] = int(seperate_second[1])
                seperate_second[-1] = int(seperate_second[-1])
                seperate_second_cos_four = (seperate_second[1] ** (1 / 2)) / seperate_second[-1]  #quotient
                if (seperate_second[1] == 3) and (seperate_second[-1] == 3):
                    answer_first = 'pi/6'
                elif (seperate_second_cos_four > -1) and (seperate_second_cos_four < 1):
                    answer_first = 'arctg(' + seperate_second + ')'
                else:
                    answer_first = 'There is no answer.'
            else:
                if seperate_second[0] == 'sqrt':
                    seperate_second[1] = int(seperate_second[1])
                    if int(seperate_second[1]) == 3:
                        answer_first = 'pi/3'
                    elif (seperate_second[1] ** (1 / 2) < 1) and (seperate_second[1] ** (1 / 2) > -1):
                        strange_thing = []
                        for elem in seperate_second:
                            strange_thing.append(str(elem))
                        answer_first = 'arctg(' + ''.join(strange_thing) + ')'
                    else:
                        answer_first = 'There is no answer.'
            if answer_first != 'There is no answer.':
                if len(str(multiplicator)) > 0:
                    if len(str(answer_first)) > 0:
                        answer_xm = 'x = (' + answer_first + ')' + str(multiplicator) + ' + (pi*n)' + str(
                            multiplicator)
                    else:
                        answer_xm = 'x = (pi*n)' + str(multiplicator)
                else:
                    answer_xm = 'x = ' + answer_first + ' + pi*n'
            else:
                answer_xm = answer_first
#-------------------------for ctg--------------------------------------
            #complete analogy to cotangent
        elif seperate_first[0] == 'ctg':
            if len(seperate_second) == 1:
                seperate_second[-1] = int(seperate_second[-1])
                if seperate_second[-1] == 1:
                    answer_first = 'pi/4'
                elif seperate_second[-1] == 0:
                    answer_first = 'pi/2'
                else:
                    answer_first = 'There is no answer.'
            elif len(seperate_second) == 3:
                seperate_second[0] = int(seperate_second[0])
                seperate_second[-1] = int(seperate_second[-1])
                seperate_second_cos_three = seperate_second[0] / seperate_second[-1] #quotient
                seperate_second[0] = str(seperate_second[0])
                seperate_second[-1] = str(seperate_second[-1])
                if (seperate_second_cos_three > -1) and (seperate_second_cos_three < 1):
                    answer_first = 'arcctg(' + ''.join(seperate_second) + ')'
                else:
                    answer_first = 'There is no answer.'
            elif len(seperate_second) == 4:
                seperate_second[1] = int(seperate_second[1])
                seperate_second[-1] = int(seperate_second[-1])
                seperate_second_cos_four = (seperate_second[1] ** (1 / 2)) / seperate_second[-1]  #quotient
                if (seperate_second[1] == 3) and (seperate_second[-1] == 3):
                    answer_first = 'pi/3'
                elif (seperate_second_cos_four > -1) and (seperate_second_cos_four < 1):
                    strange_thing = []
                    for elem in seperate_second:
                        strange_thing.append(str(elem))
                    answer_first = 'arcctg(' + ''.join(strange_thing) + ')'
                else:
                    answer_first = 'There is no answer.'
            else:
                if seperate_second[0] == 'sqrt':
                    seperate_second[1] = int(seperate_second[1])
                    if int(seperate_second[1] == 3):
                        answer_first = 'pi/6'
                    elif (seperate_second[1] ** (1 / 2) < 1) and (seperate_second[1] ** (1 / 2) > -1):
                        strange_thing = []
                        for elem in seperate_second:
                            strange_thing.append(str(elem))
                        answer_first = 'arcctg(' + ''.join(strange_thing) + ')'
                    else:
                        answer_first = 'There is no answer.'
            if answer_first != 'There is no answer.':
                if len(str(multiplicator)) > 0:
                    if len(str(answer_first)) > 0:
                        if '/' in multiplicator:
                            answer_xm = 'x = (' + answer_first + ')' + str(multiplicator) + ' + (pi*n)' + str(
                                multiplicator)
                        else:
                            answer_xm = 'x = (' + answer_first + ')' + str(multiplicator) + ' + (pi*n)' + str(
                            multiplicator)
                    else:
                        answer_xm = 'x = 1/' + str(multiplicator) + ' + pi*n'
                else:
                    answer_xm = 'x = ' + answer_first + ' + pi*n'
            else:
                answer_xm = answer_first
    else:
        answer_xm = 'At the moment, the program does not know how to solve this. I am sorry.'
        answer_xmm = ''
    return answer_xm, answer_xmm


#main code block
while True:
    input_start = input('To start, type start, to exit type exit: ')
    if input_start == 'start':
        print('''
         Be sure to follow the input pattern.
        The program can process all trigonometric equations
        Extra spaces at the end are forbidden. Will be considered an incorrect entry.
        Equations must fit the standard. cos (x) + sin ^ 2 (t) = y
        Where under t and x can be 1x/3, 412x/5, x. Moreover, x is mandatory before division
        Under y can be sqrt(2), sqrt(5)/3,24123 and all kinds of numbers
        Instead of cosine and sine, you can also use all tangent and cotangent.
        However, I could not write an algorithm to solve any addition, multiplication
        The program will give the answer only for simple trigonometric expressions of the form:
                    cos(12x) = 1
                    sin(3x/4) = 1/2
                    ctg(50x/21) = sqrt(3/3)
                    tg(x) = sqrt(2)/2
        ''')

        #The main block starts here
        while True:
            input_string = str(input('Enter your expression or exit to stop: '))
            if input_string == 'exit':
                break
            else:
                list_main = main_separation(input_string) #entered begin to share
                if list_main:
                    first_word_main = list_main[0] #left part
                    second_word_main = list_main[-1] #right part
                    bool_true_left = conditional_check_left(first_word_main) #check the left side for input
                    bool_true_right = conditional_check_right(second_word_main) #check the right side for input
                    if bool_true_left and bool_true_right:
                        print(first_word_main, second_word_main)
                        answer_x = solve_main(first_word_main, second_word_main) #solve these parts
                        if len(answer_x[1]) > 0: #if an answer has only 1 line
                            print(answer_x[0])
                            print(answer_x[1])
                        else:                    #if an answer has 2 lines
                            print(answer_x[0])
                    else:
                        print('You have entered impossible arguments.')
                else:
                    print('Does not match input format.')
        break
    elif input_start == 'exit':
        break
    else:
        continue