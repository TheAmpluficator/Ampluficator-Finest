import argparse

book = {}

parser = argparse.ArgumentParser(description='Telephon book')
parser.add_argument('-a', '--add', dest='param1')
parser.add_argument('-d', '--delete', dest='param2')
parser.add_argument('-s', '--show', dest='param3', default='all')

args = parser.parse_args()

if args.param1:
    name, tele = args.param1.split(':')
    if name in book:
        book[name] = [book.get(name), int(tele)]
        print('Контакт с именем', name, 'обновлен')
        print(name, ':', book[name])
    else:
        book[name] = int(tele)
        print('Контакт с именем', name, 'создан')
        print(name, ':', book[name])
        
elif args.param2:
    name = args.param2
    if name in book:
        book.pop(name)
        print('Удалён')
    else:
        print('Нету тут таких')
        
#elif args.param3:
