alphabhets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', ':', "'", '+',
    '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`',
    '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', " "
]

## get user message
## get encode shift number
## encode the message
## get decode shift number
## decode message


def get_shift_number():
    return int(input("enter shift number: "))


def shift_the_letters(msg, s_number):
    shifted_words = ""
    length_of_chars = len(alphabhets)
    for l in msg:
        index_of_l = alphabhets.index(l)
        print(index_of_l)
        if (index_of_l + s_number >= length_of_chars):
            last_chars_len = length_of_chars - index_of_l
            index_of_l = 0 + s_number - last_chars_len
        else:
            index_of_l = index_of_l + s_number
        shifted_words = shifted_words + alphabhets[index_of_l]
    return shifted_words


def encode_message(msg):
    print("Encoding message")
    s_number = get_shift_number()

    e_message = shift_the_letters(msg, s_number)
    return e_message


def decode_messsage(msg):
    print("Decoding message")
    s_number = get_shift_number()
    d_message = shift_the_letters(msg, -s_number)
    return d_message


message = input("enter your message: ")
encoded_message = encode_message(message)
print(encoded_message)
decoded_message = decode_messsage(encoded_message)
print(decoded_message)
