import random
import string


def randon_roll_number():
    roll_number_text_file_read = open("roll_number.txt", "r")
    random_roll_list = list(roll_number_text_file_read)
    roll_number_text_file_read.close()
    random_list = list(string.ascii_uppercase)
    random_roll = random.choice(random_list) + random.choice(random_list) + str(random.randrange(0, 10)) + str(random.randrange(0, 10)) + "\n"
    with open("roll_number.txt", "a") as roll_number_text_file_append:
        for i in reversed(random_roll_list):
            if random_roll == i:
                randon_roll_number()
            roll_number_text_file_append.write(random_roll)
            roll_number_text_file_append.close()
            break
    return random_roll