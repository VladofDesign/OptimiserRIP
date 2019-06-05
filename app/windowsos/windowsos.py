import os, socket, multiprocessing, datetime, ctypes
now = datetime.datetime.now()
boucle=0
def windowsos():
    while boucle==0:
        os.system('cls')
        print("\n                        [1;34m____________________________________________________[0m")
        print("                       [1;34m|[33m   _ _ _ _ _  _ ___  ____ _ _ _ ____    ____ ____   [1;34m|[0m")
        print("                       [1;34m|[33m   | | | | |\ | |  \ |  | | | | [__     |  | [__    [1;34m|[0m")
        print("                       [1;34m|[33m   |_|_| | | \| |__/ |__| |_|_| ___]    |__| ___]   [1;34m|[0m")
        print("                       [1;34m|____________________________________________________[1;34m|[0m \n")                
        print("                                  [[7;33m Scanning system - Please wait [0m]")
        print("\n \n            PC-Name             =  [[102;97m", socket.gethostname(),"[0m]          SystemDrive         =  [[102;97m",os.environ['SYSTEMDRIVE'],"[0m]") 
        print("            Date                =  [[102;97m",now.strftime("%Y-%m-%d"),"[0m]       Processeurs         =  [[102;97m",multiprocessing.cpu_count(),"[0m]   \n \n")
        print("                               [ [102;97m - [0m ] Press A to check TCPOptimiser.\n")                                                                                     
        print("                               [ [106;97m - [0m ] Press B to check Network Share.\n")                                                                                     
        print("                               [ [43;97m - [0m ] Press C to check Wake.\n")                                                                                    
        print("                               [ [102;97m - [0m ] Press D to return to the menu.\n")                                                                                   
        choix2 = input("                <-> Press any key to apply [33mOptimiserRIP[0m to your computer: ")
        if choix2=="A" or choix2=="a":
            os.system("pause")
        if choix2=="B" or choix2=="b":
            os.system("pause")
        if choix2=="C" or choix2=="c":
            os.system("pause")
        if choix2=="D" or choix2=="d":
            break