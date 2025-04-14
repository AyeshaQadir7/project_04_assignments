import os


def main():
    i = 0
    path = "C:/Users/Soft Hands/Documents/File Renamer Python/"

    for filename in os.listdir(path):
        my_dest = "image" + str(i) + ".png"
        my_source = os.path.join(path, filename)
        my_dest = os.path.join(path, my_dest)
        os.rename(my_source, my_dest)
        i += 1


if __name__ == "__main__":
    main()
