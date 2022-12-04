import os

#useful commands
# python manage.py makemigrations members
# python manage.py migrate
# python manage.py runserver


def start_app():

    os.system('python myworld/manage.py runserver')
    # Use a breakpoint in the code line below to debug your script.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_app()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
