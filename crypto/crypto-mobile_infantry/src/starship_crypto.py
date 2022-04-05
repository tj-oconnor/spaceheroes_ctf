import string
import inspect
import sys


def logo():
    print("                                                                                                                        ")
    print("                                                        #######                                                         ")
    print("                                               ####&&&&&&&@&&&&&&&####                                                  ")
    print("                                        ###&&&&&&@@@&&&&@@@@@@@@@@@@@@@&&&##                                            ")
    print("                                    #&&@@@&&@@@@@@@@@@@@@@@@@@@@$$$$$$$$$$$$@@&##                                       ")
    print("                                #&@@@@@$$$$@$$$$$@@@@@@@&&&&&&&@@@@$$$$$$$$$$$$$$@@&#                                   ")
    print("                             #&@@@$$$@$$$$$$$@@&##   BBBBBBBBBBBB    #&&@@$$$$$$$$%$$@&#                                ")
    print("                          #&@@@@@$$$$@$@@&#  BBBBBBBBBBBBBBBBBBBBBBBBBBBBB ##&@@$$$$$$$$$@#                             ")
    print("                        #@@@@@$$$$$$@&# BBBBBBBBBB                       BBBBBB #&@@$$$$$$$@&                           ")
    print("                      #@@@@$$$$$$@&# BBBBBBB                                   BBB  &@@$$$$%$$@#                        ")
    print("                    #@$$$$$$$$$@# BBBBBB                                           BBB &@$$$%%%$@#                      ")
    print("                  #@$$$$$$$$@& BBBBBB                                                 BB #@$%%%%%%@#                    ")
    print("                #@$$$%%%%%$& BBBBB                 #@&&&&&&&&&&&&&#                      BB#@%%%%%%$@#                  ")
    print("               &$%$%%%%%$& BBBBB                   &$@$$$$%$$%%$$$&                        B #@%%%%%$$&                 ")
    print("              @%%%%%%%%@ BBBB                @@&&&&$%%%%%%%%%%%%%%@ BB                         &$%%$$$$@#B              ")
    print("            #$%$%%%%%$&BBBBB                @%@$$$$$%%%%%%%$%%%%%%$#BB                          #@$$$$$$$#              ")
    print("           #$$$%%%%%@#BBBB                  %$$%%%%%%%%%%%%%%%%%%%$&BB                            &$%%$$$$@             ")
    print("          #$$$$%%%$& BBB                   @%$%%%%%%%%%%%%%%%%%%%%%&BB                             #$%%%%%%@ B          ")
    print("         #$$$$$$%$&BBBB                    $@$$%%%%%%%%%%%%%%%%%%%%@ B                              #@%%%%%%@ B         ")
    print("        #$%%%%%%$#BBBB                            #$%%%%%%%%%%%%%%$@ B                               #@$$%%%%@ B        ")
    print("       #$%%%%%%$#BBB                          BBBB&%%%*%%%%%%%%%%$$$#BB                               #@$$%%%%@ B       ")
    print("       $%%%**%%#BBB   #&##                        @$%%*%%%%%%%%%%%$$#BB                   ####&#       #@$%$%%%&        ")
    print("      &%%****%@BBBB   %$@$@@@&&&&####             @$%%%%%%%%%%%%%%$$&BBB      #####&&&&@@@@$$$$$#       &$$%%%*%#B      ")
    print("     #%%%%%*%$ BBB   @*$%%%%%%%%%%%$$@@@&&&###    @%%**%%%%%%%%%%%$$@ ##&&&@@@@@$$$$%%%%%%%%%%%%$#B     #@$%****$ B     ")
    print("     @%%*%%%%&BBB   #%$%%%****************%%$$$$@@%%%***%*%%%%%%%%%%$$$$$$$$%$%%%%%%********%%%%%@ B     &$%****%&BB    ")
    print("    #%%***%%$ BB    $%$%%*****************************************%%%%%%%%%%%%%%***%*************%&B      @%%****$ B    ")
    print("    @%%***%%&BBB   &$$%******************%%%%%%********************%**********%******************%$ B     &$%***%%#BB   ")
    print("    $%*****$ BB       #@%*******%%**%%%%**%%%%%%%*********%********%%******%**********%**%%%%%%$&# BB     #$$*****@ B   ")
    print("   #%%****%@BBB       BB #$***********%%**%%%*%*********************%**************%**%%*%%%$# BBBBB       @$*****$ B   ")
    print("   &%%****%#BB            $%%*****%*%**%***%%**************************************%*******%@BBBBB         &$%****%#BB  ")
    print("   @%*****%#BB            $%%%**%@ ##&@%%%%%*************************%***********$@###%*****@BBB           &$%*****&BB  ")
    print("   $%*****$ BB            %$%%%*$ BBBB&%%%%%**%*********************************@BBBBB@%****@BB            #%%*****@BB  ")
    print("   %%*!*!*$ BB            %$%%%%&BBB  @$%%***@  #&@$***************%$&&&#&%*****@BBB  #$****@BB            #%%*****@ B  ")
    print("   %%*!!!*$ BB            %%%%%$ BB   @$%***$#BBBBB&%**************$ BBBB $%****&BB    @%***@BB            #%%*****@ B  ")
    print("   $%*!!!!$ BB            %%%%%&BB    $$%**%&BBB   &$%*************&BBBB  #$%***&BB    #$**%@BB            #%%*****@BB  ")
    print("   &%*!!!!%#BB            # ##& BB    $%%**$ BB    #$%************%#BB     &$%*%&BB     &##  BB            &%%*****&BB  ")
    print("   #$*!!!!*&BB              BBBBB     &@$%$#BB     #$%************$ BB      @$$@#BB      BBBBB             @%%*!!*%#BB  ")
    print("   #$*!!!!*@ B                         B   BBB      @%*!**********$ BB      #  BBB                         %%%****$ BB  ")
    print("    @%!!!!*%#B                           BBB        @%*!**********&BB          BB                         &*%***!*@ BB  ")
    print("    &%*!!!!*@BB                                     &%*!**********&BB                                     $*%**!!%&BB   ")
    print("     $*!!!!*%#B                                     #$**!!**!!!!*%#BB                                    #*%*****$ BB   ")
    print("     &%*!!!!*@ B                                     $*!****!!!**$ BB                                    %*%****%&BBB   ")
    print("      $**!**!%#B                                     @%!!********@BBB                                   @*%*****% BB    ")
    print("      #%****!*$ B                                    &%*!*******%&BB                                   &%%*****%&BBB    ")
    print("       &%***!!*@ B                                   &$*********%#BB                                  #%%*!****@BBB     ")
    print("        &%*!!!!*& B                                  #$%********$ BB                                 #$%**!!!*@ BB      ")
    print("         &%!!!!!*&                                    $%********@ BB                                #%%**!!!*@ BBB      ")
    print("          &%!!!!!*@                                   $%%*******@BB                                &%%%*!!!*@ BBB       ")
    print("           &%*!!!!*$#                              #&$%*********%& B                              @*%%***!*@ BBB        ")
    print("            &%*!!!!*%&                            #$%*%********!!!%@                            #$*$%%****@ BBB         ")
    print("             #$******%@#                          #$%***********!!*%#B                         @%%%%%%**%@ BBB          ")
    print("              #@%******$&                          &@%*********!!*$& B                       &%%$%%%%**$#BBBB           ")
    print("                &$*******$#                           &$*******%& BBBB                     &%*%%%****%@ BBB             ")
    print("                  @%*******$#                         B@**!!!**@BBBB                     &$*%*******$#BBBB              ")
    print("                   #@%*****!*$&#                       &@@$$$@@#BBB                   #@$%%*******%& BBB                ")
    print("                     #@%***!!!*%@&#                      BBBBBBBBB                 #&$%%%******%%& BBBB                 ")
    print("                        @%*!***!**$@&##                                        #&@$%%%*******%$# BBBB                   ")
    print("                        B &$*!*!*****%$@&##                                #&@$$%%%%*******%@#BBBBB                     ")
    print("                          B #@%**!***!***%$@@&&####                ###&@@$$%%%%%%%****!*%$& BBBBB                       ")
    print("                            BB #@%***!********%$$$$@@@@@@@@@@@@@@$$$$%%%%%%%%********%$& BBBBB                          ")
    print("                               BB #&@%***************%%%%%%%%%%%%%%%*************%$@# BBBBBB                            ")
    print("                                  BBB #&@$%*********************************%%$&# BBBBBBB                               ")
    print("                                      BBB  ##&@$$%%****************%%%%$$@&#  BBBBBBB                                   ")
    print("                                          BBBBBB   ###&&&&&@@@&&&###   BBBBBBBBBB                                       ")
    print("                                                BBBBBBBBBBBBBBBBBBBBBBBBBB                                              ")
    print("                                                                                                                        ")


def throw_pad_fail(fail):
    print("\n[!]- Failed pad strength validation. Please use a stronger pad to keep the mobile infantry safe.\n")
    print("------------------------------------------")
    print(fail)
    print("------------------------------------------")
    sys.exit(-1)


def len_check(pad):
    if len(pad) != 38:
        return False
    return True


def check0(pad):
    for char in pad:
        if char not in string.printable:
            return False
    return True


def check1(pad):
    for i in range(0, int(len(pad)/2)+1):
        if not pad[i].isupper():
            return False
    return True


def check2(pad):
    for i in range(int(len(pad)/2)+1, len(pad)):
        if not pad[i].islower():
            return False
    return True


def check3(pad):
    for i in range(0, int(len(pad)/2)):
        if ord(pad[i]) != ord(pad[i+1])-1:
            return False
    return True


def check4(pad):
    for i in range(int(len(pad)/2)+1, len(pad)-1):
        if ord(pad[i]) != ord(pad[i+1])+1:
            return False
    return True


def validate_pad(pad):

    if (not len_check(pad)):
        throw_pad_fail(inspect.getsource(len_check))
    elif (not check0(pad)):
        throw_pad_fail(inspect.getsource(check0))
    elif (not check1(pad)):
        throw_pad_fail(inspect.getsource(check1))
    elif (not check2(pad)):
        throw_pad_fail(inspect.getsource(check2))
    elif (not check3(pad)):
        throw_pad_fail(inspect.getsource(check3))
    elif (not check4(pad)):
        throw_pad_fail(inspect.getsource(check4))
    return True


def otp(flag, pad):
    #pad = pad[0:len(flag)]
    if validate_pad(pad):
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(flag, pad))
    else:
        raise("Failed pad strength validation check")


def main():
    flag = "shctf{Th3-On1Y-G00d-BUg-I$-A-deAd-BuG}"
    secret_pad = "EFGHIJKLMNOPQRSTUVWXxwvutsrqponmlkjihg"
    secret = otp(flag, secret_pad)

    logo()
    print("\nWelcome to Ricos Roughnecks. We use 1-time-pads to keep all our secrets safe from the Arachnids.")
    print("Here in the mobile infantry, we also implement some stronger roughneck checks.\n")

    pad = input("Enter pad > ")
    result = otp(secret, pad)
    if (result == flag):
        print("[+] The fight is over, here is your flag: %s" % result)
    else:
        print("[+] Welcome the mobile infantry, keep fighting.")


main()
