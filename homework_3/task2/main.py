text = "Создайте виртуальное окружение для проекта, используя модуль venv. В этом окружении установите несколько модулей, таких как requests и BeautifulSoup4, с помощью pip. После установки модулей напишите скрипт, который будет использовать эти модули для выполнения следующих задач"

import re
from collections import Counter

def func(string):
    words = (re.split(";|, |\n| ", string))
    print(Counter(words))

func(text)