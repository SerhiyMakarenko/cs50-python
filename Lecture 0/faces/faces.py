def convert(face):
    return face.replace(':)', '😊').replace(':(', '🙁')

def main():
    print(convert(input()))

main()