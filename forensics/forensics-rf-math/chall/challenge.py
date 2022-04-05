import argparse


def challenge( flag , keyfile ):
    print("Enter authenticator key:")
    user_key = input()
    #
    f = open( keyfile ,'rt')
    key_lines = f.readlines()
    correct_key = key_lines[2] # its the second line in the file
    f.close()
    #
    if( user_key == correct_key ):
        print("Access granted!!!")
        print("Thanks for keeping your keys secure ^^")
        print("Here is the flag:")
        print( flag )
    else:
        print("ACCESS DENIED!!!!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--keyfile", required=True)
    parser.add_argument("--flag", required=True )
    args = parser.parse_args()
    challenge( args.flag , args.keyfile )