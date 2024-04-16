from file_reader import File_reader
from graham import Graham


def main():
    fr = File_reader('./dane/przyklad1.txt')
    data = fr.read()
    graham = Graham(data)
    print(graham.getOtoczka())
    graham.draw()

if __name__ == '__main__':
    main()