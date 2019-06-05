import os, socket, multiprocessing, datetime, ctypes, sys
from app.network import networks
from app.drivers import drivers
from app.services import services
from app.telemetry import telemetry
from app.windowsos import windowsos
from app.sound import sound
from app.latency import latency
from app.nvidia import nvidia
from app.processor import processor
from app.hardware import hardware
from app.overclocking import overclocking
from app.games import games
from app.bios import bios
from app.tools import tools

now = datetime.datetime.now()
dir_path = '%s\\VlaDoF\\' %  os.environ['APPDATA'] 
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
boucle=0
while boucle==0:
    os.system("mode con: cols=100 lines=32")
    ctypes.windll.kernel32.SetConsoleTitleW("[Administrateur] VlaDoF")
    os.system('cls')
    print("\n                        [1;34m____________________________________________________[0m")
    print("                       [1;34m|[33m ____ ___  ___ _  _ _ ____ ____ ____    ____ _ ___  [1;34m|[0m")
    print("                       [1;34m|[33m |  | |__]  |  |\/| | [__  |___ |__/ __ |__/ | |__] [1;34m|[0m")
    print("                       [1;34m|[33m |__| |     |  |  | | ___] |___ |  \    |  \ | |    [1;34m|[0m")
    print("                       [1;34m|____________________________________________________|[0m \n")
    print("                                  [[7;33m Scanning system - Please wait [0m]")
    print("\n \n            PC-Name             =  [[102;97m", socket.gethostname(),"[0m]          SystemDrive         =  [[102;97m",os.environ['SYSTEMDRIVE'],"[0m]") 
    print("            Date                =  [[102;97m",now.strftime("%Y-%m-%d"),"[0m]       Processeurs         =  [[102;97m",multiprocessing.cpu_count(),"[0m]   \n \n")
    print("         [ [102;97m - [0m ] Press A to check Drivers.            [ [102;97m - [0m ] Press H to check NVIDIA.\n")                                                                    
    print("         [ [106;97m - [0m ] Press B to check Network.            [ [106;97m - [0m ] Press I to check Processeur.\n")                                                                   
    print("         [ [43;97m - [0m ] Press C to check Services.           [ [43;97m - [0m ] Press J to check Hardware.\n")                                                                    
    print("         [ [102;97m - [0m ] Press D to check Telemetry.          [ [102;97m - [0m ] Press K to check Overclocking.\n")                                                                    
    print("         [ [106;97m - [0m ] Press E to check Windows OS.         [ [106;97m - [0m ] Press L to check Games Settings.\n")                                                                    
    print("         [ [43;97m - [0m ] Press F to check Sound.              [ [43;97m - [0m ] Press M to check BIOS.\n")                                                                    
    print("         [ [102;97m - [0m ] Press G to check Latency.            [ [102;97m - [0m ] Press N to check Tools.\n \n")
    choix = input("                <-> Press any key to apply [33mOptimiserRIP[0m to your computer: ")

    #=================================================================
    # ------------------------- Drivers ----------------------------
    #=================================================================

    if choix=="A" or choix=="a":
        drivers.drivers()

    #=================================================================
    # ------------------------- Network ----------------------------
    #=================================================================

    if choix=="B" or choix=="b":
        networks.networks()

    #=================================================================
    # ------------------------- Services ----------------------------
    #=================================================================

    if choix=="C" or choix=="c":
        services.services()

    #=================================================================
    # ------------------------- Telemetry  ----------------------------
    #=================================================================

    if choix=="D" or choix=="d":
        telemetry.telemetry()

    #=================================================================
    # ------------------------- Windows OS  -------------------------
    #=================================================================

    if choix=="E" or choix=="e":
        windowsos.windowsos()

    #=================================================================
    # ------------------------- Sound ------------------------------
    #=================================================================

    if choix=="F" or choix=="f":
        sound.sound()

    #=================================================================
    # ------------------------- Latency ----------------------------
    #=================================================================

    if choix=="G" or choix=="g":
        latency.latency()

    #=================================================================
    # ------------------------- NVIDIA ----------------------------
    #=================================================================

    if choix=="H" or choix=="h":
        nvidia.nvidia()

    #=================================================================
    # ------------------------- Processeur ----------------------------
    #=================================================================

    if choix=="I" or choix=="i":
        processor.processor()

    #=================================================================
    # ------------------------- Hardware ----------------------------
    #=================================================================

    if choix=="J" or choix=="j":
        hardware.hardware()

    #=================================================================
    # ------------------------- Overclock -----------------------
    #=================================================================

    if choix=="K" or choix=="k":
        overclocking.overclocking()

    #=================================================================
    # ------------------------- Games ------------------------
    #=================================================================

    if choix=="L" or choix=="l":
        games.games()

    #=================================================================
    # ------------------------- BIOS ------------------------
    #=================================================================

    if choix=="M" or choix=="m":
        bios.bios()

    #=================================================================
    # ------------------------- Tools ----------------------------
    #=================================================================

    if choix=="N" or choix=="n":
        tools.tools()

    #=================================================================
    # ------------------------- Exit ----------------------------
    #=================================================================

    if choix=="O" or choix=="o":
         sys.exit(0)