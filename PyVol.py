from sys import argv
from subprocess import call

def main():
    if len(argv)==3:
        while True:
            volume=argv[2]
            try:
                volume=int(volume[:-1])
                if volume>=0 and volume<=100:
                    call(["amixer","-D","pulse","sset","Master",str(volume)+"%"])
                else:
                    print("Invalid Volume Value! Run Again!")
                break

            except ValueError:
                print("Invalid Value! Run again!")
                break
    elif argv[1][2:]=="present":
        call(["amixer","-D","pulse","get","Master"])
    elif argv[1][2:]=="mute":
        call(["amixer", "-D", "pulse", "sset", "Master", "0%"])
    elif argv[1][2:]=="max":
        call(["amixer","-D","pulse","sset","Master","100%"])
    else:
        print("Invalid Argument!")


if __name__=="__main__":
    main()
