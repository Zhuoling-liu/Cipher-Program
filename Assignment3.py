def is_not_valid(message):
    '''
    (str) -> bol
    Return if one of the characters is not a letter (lowercase or uppercase) or is not a space character

    >>> is_not_valid('asfg123 asdf')
    True
    >>> is_not_valid('asdf sdh')
    False
    >>> is_not_valid('sdwewed')
    False
    '''
    message = message.lower()

    # traverse the message to check if it is vaild
    for i in message:
        if (i > 'z' or i < 'a') and i != ' ':
            return True
    return False


def is_not_square(message):
    '''
    (str) -> bol
    Verify whether the length of the string forms a square number

    >>> is_not_square('abc')
    True
    >>> is_not_square('asdsdfds')
    True
    >>> is_not_square('b')
    False
    '''
    message_len = len(message)
    index = 1

    # Iterate while the square of index is less than or equal to the string
    # length
    while message_len >= index * index:
        # If the length matches the square of index, it's a perfect square
        if message_len == index * index:
            return False
        index += 1
    return True


def string2list(message):
    '''
    (str) -> list
    Convert the string into a 2D square list
    >>> string2list("Hello Bye")
    [['H', 'e', 'l'], ['l', 'o', ' '], ['B', 'y', 'e']]
    >>> string2list("sd")
    []
    >>> string2list("wertsidj sihihgd")
    [['w', 'e', 'r', 't'], ['s', 'i', 'd', 'j'], [' ', 's', 'i', 'h'], ['i', 'h', 'g', 'd']]
    '''
    if is_not_valid(message) or is_not_square(message):
        return []

    one_list = []
    square_list = []
    i = 0  # index in square_list

    # find the square root of the length of the message
    def find_squareroot(message):
        length = 0  # initial number used to get the square root
        while len(message) >= length * length:
            if len(message) == length * length:
                return length
            length += 1

    length = find_squareroot(message)

    while i < length:
        for j in range(len(message)):
            # Collect characters for a sublist
            one_list.append(message[j])

            # Check if sublist is complete，
            if (j + 1) % length == 0:
                # Add sublist to the main list
                square_list.append(one_list)
                one_list = []
                i += 1

    return square_list


def add_space(message):
    '''
    (str) -> str
    Retrun a new string after adding a space before the upper case

    >>> add_space('HelloEveryone')
    'Hello Everyone'
    >>> add_space('IamPretty')
    'Iam Pretty'
    >>> add_space('HelloHelloNing')
    HelloHelloNing
    '''
    for i in range(len(message)):
        # Check if the current and two characters ahead are lowercase, and the
        # middle is uppercase (not a space)
        if ('a' < message[i] < 'z' and 'a' < message[i + 2] <
                'z') and message[i + 1] < 'a' and message[i + 1] != ' ':
            # Insert space before the uppercase letter
            message = message[0:i + 1] + ' ' + message[i + 1:len(message) + 1]
        if i == len(message) - 3:
            return message


def list2string(list1):
    '''
    (list[list[str]]) -> str
    Convert a 2D square list to a string.

    >>> list2string([['H', 'e', 'l'], ['l', 'o', 'o'], ['B', 'y', 'e']])
    'Helloo Bye'
    >> list2string([['w', 'e', 'r', 't'], ['s', 'i', 'd', 'j'], [' ', 's', 'i', 'h'], ['i', 'h', 'g', 'd']])
    'wertsidj sihihgd'
    >>> list2string([['H', 'e', 'l'], ['l', 'o', ' '], ['B', 'y', 'e']])
    'Hello Bye'
    '''
    list2 = []
    # Flatten the 2D list into a single list
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            list2.append(list1[i][j])

    # Join the list into a single string and add spaces before uppercase
    # letters
    message = ''.join(list2)
    message = add_space(message)

    return message


def horizontal_flip(input_list):
    '''
    (list[list[str]]) -> None
    Flips the list horizontally
    >>> input_list = [[ '1','2'],['3','4']]
    >>> horizontal_flip(input_list)
    >>> input_list
    [['2', '1'], ['4', '3']]

    >>> input_list = [[ '1','2','3'],['4','5','6'],['7','8','9']]
    >>> horizontal_flip(input_list)
    >>> input_list
    [['3', '2', '1'], ['6', '5', '4'], ['9', '8', '7']]

    >>> input_list=[['H', 'e', 'l'], ['l', 'o', ' '], ['B', 'y', 'e']]
    >>> horizontal_flip(input_list)
    >>> input_list
    [['l', 'e', 'H'], [' ', 'o', 'l'], ['e', 'y', 'B']]
    '''

    list_inter = []

    # Reverse each row in the list
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            for k in range(len(input_list[i]) - j - 1):
                list_inter = input_list[i][k + 1]
                input_list[i][k + 1] = input_list[i][k]
                input_list[i][k] = list_inter


def transpose(input_list):
    '''
    (list[list[str]]) -> None
    Transposing the list will flip itover its diagonal
    >>> input_list=[[ '1','2','3'],['4','5','6'],['7','8','9']]
    >>> transpose(input_list)
    >>> input_list
    [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]

    >>> input_list=[['H', 'e', 'l'], ['l', 'o', ' '], ['B', 'y', 'e']]
    >>> transpose(input_list)
    >>> input_list
    [['H', 'l', 'B'], ['e', 'o', 'y'], ['l', ' ', 'e']]

    >>> input_list = [[ '1','2'],['3','4']]
    >>> transpose(input_list)
    >>> input_list
    [['1', '3'], ['2', '4']]
    '''
    # Iterate through each element in the upper triangle of the matrix
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list[i])):
            # Use a temporary variable to swap the values
            temp = input_list[j][i]
            input_list[j][i] = input_list[i][j]
            input_list[i][j] = temp


def flip_list(input_list):
    '''
    (list[list[str]]) -> None
    Transforms the 2D list by changing the position of its items
    >>> input_list=[['B','I','H'],['y','o','e'],['e',' ','l']]
    >>> flip_list(input_list)
    >>> input_list
    [['H', 'e', 'l'], ['I', 'o', ' '], ['B', 'y', 'e']]

    >>> input_list = [[ '1','2','3'],['4','5','6'],['7','8','9']]
    >>> flip_list(input_list)
    >>> input_list
    [['3', '6', '9'], ['2', '5', '8'], ['1', '4', '7']]
    >>> input_list=[['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','16']]
    >>> flip_list(input_list)
    >>> input_list
    [['4', '8', '12', '16'], ['3', '7', '11', '15'], ['2', '6', '10', '14'], ['1', '5', '9', '13']]
    '''
    horizontal_flip(input_list)

    transpose(input_list)


def decipher_code(message):
    '''
    (str) -> str
    Return all the deciphered sentences into one single string

    >>> decipher_code('BlHyoee l')
    'Hello Bye'
    >>>message = 'd  WoYahioranuet'
    >>> decipher_code(message)
    'What are Youdoin'
    >>> message = 'sdfgdjfhskdj'
    >>> decipher_code(message)
    '''
    # Convert the input string to a 2D list
    list_receive = string2list(message)

    # Flip the 2D list horizontally, then transpose it
    flip_list(list_receive)

    # Convert the flipped list back to a string
    decryp_message = list2string(list_receive)

    return(decryp_message)
    
    
