import random, string

def random_generate_alpha_numberic(length = 16):
    ui_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    # print(ui_string)
    return ui_string