import wikipediaapi
from src import language
from src import find

def main():
    value = ''
    lang = wikipediaapi.Wikipedia(language.select_language(input('Select language: \nRussian\nEnglish\n')))
    page = lang.page(input('input page from wiki : '))

    print(page.text, '\n\n\n did you want find something ? y/n')
    value = input()
    if (value == 'y'): print(find.find(input('input key'), page))
    return 0;
main()
