import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path
        self.all_path = os.path.join(tempfile.gettempdir(), path)

        if not os.path.exists(self.all_path):
            open(self.all_path, 'w').close()

    def __str__(self):
        return self.path

    """ 
    //////////////ALTERNATIVE ITERATOR
    def __iter__(self):
        return self
    
    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.current_position)

            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')

            self.current_position = f.tell()
            return line
    """

    def __iter__(self):
        self.f = open(self.all_path, 'r')
        return self

    def __next__(self):
        line = self.f.readline()
        if not line:
            self.f.close()
            raise StopIteration
        return line

    def write(self, string):
        with open(self.all_path, 'w') as f:
            f.write(string)

    def read(self):
        with open(self.all_path, 'r') as f:
            return f.read()

    def __add__(self, other):
        f1_text = self.read()
        f2_text = other.read()

        obj = File('file.txt')
        obj.write(f1_text + f2_text)
        return obj


def main():
    f1 = File('first.txt')
    print(f1)
    for line in f1:
        print(line)

    for line in f1:
        print(line)


if __name__ == '__main__':
    main()