
def file_read():
    file = 'referat.txt'

    with open(file, encoding='utf-8') as f:
        content = f.read()
    print(f'Line length is: {len(content)}.')
    words = content.split()
    print(f'Amount of words is: {len(words)}.')


def file_rewrite():
    file = 'referat.txt'

    with open(file, encoding='utf-8') as f:
        content = f.read()
    content_replace = content.replace('.', '!')
    with open('referat_2.txt', 'w', encoding='utf-8') as f:
        f.write(content_replace)


if __name__ == '__main__':
    file_read()
    file_rewrite()
