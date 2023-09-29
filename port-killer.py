import os
import platform
import subprocess
import requests
import re
import time
from colorama import just_fix_windows_console,Fore,Back,Style

if(platform.system()=="Linux"):
    os.system('clear')
if(platform.system()=="Windows"):
    os.system('cls')
    just_fix_windows_console()

ascii_art='''
    ██████╗░░█████╗░██████╗░████████╗░░░░░░██╗░░██╗██╗██╗░░░░░██╗░░░░░███████╗██████╗░
    ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝░░░░░░██║░██╔╝██║██║░░░░░██║░░░░░██╔════╝██╔══██╗
    ██████╔╝██║░░██║██████╔╝░░░██║░░░█████╗█████═╝░██║██║░░░░░██║░░░░░█████╗░░██████╔╝
    ██╔═══╝░██║░░██║██╔══██╗░░░██║░░░╚════╝██╔═██╗░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
    ██║░░░░░╚█████╔╝██║░░██║░░░██║░░░░░░░░░██║░╚██╗██║███████╗███████╗███████╗██║░░██║
    ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░░░░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝
    '''
author_sign=''' 
    PORT KILLER FOR DISABLING YOUR PORTS
    @author  - leurk
    @version - 0.1'''

tip='''
    TIP:- If USB Ports Are Not Working After Enabling, Just Reboot
'''
print(Fore.RED+Style.BRIGHT+ascii_art+Style.RESET_ALL)
time.sleep(0.3)
print(Fore.GREEN+Style.BRIGHT+author_sign+Style.RESET_ALL)
print(Fore.BLUE+Style.BRIGHT+tip+Style.RESET_ALL)

try:
    if(platform.system()=="Linux"):
        print(Fore.GREEN+Style.NORMAL+"[+] Menu Of USB Killer :-")
        print("[+] 1 - Disable All USB Ports")
        print("[+] 0 - Enable All USB Ports"+Style.RESET_ALL)
        while True:
            user_input1=input(Fore.BLUE+Style.BRIGHT+"\n[-] Enter Your Choice - "+Style.RESET_ALL)
            if(user_input1=="1"):
                os.system('rmmod ohci_hcd 2>/dev/null')
                os.system('rmmod uhci_hcd 2>/dev/null')
                os.system('rmmod ehci_pci 2>/dev/null')
                os.system('rmmod ehci_hcd 2>/dev/null')
                os.system('rmmod xhci_hcd 2>/dev/null')
                print(Fore.GREEN+Style.BRIGHT+"[=] ALL PORTS DISABLED."+Style.RESET_ALL)
                break
            elif(user_input1=="0"):
                os.system('modprobe ohci_hcd 2>/dev/null')
                os.system('modprobe uhci_hcd 2>/dev/null')
                os.system('modprobe ehci_pci 2>/dev/null')
                os.system('modprobe ehci_hcd 2>/dev/null')
                os.system('modprobe xhci_hcd 2>/dev/null')
                print(Fore.GREEN+Style.BRIGHT+"[=] ALL PORTS ENABLED"+Style.RESET_ALL)
                break
            else:
                print(Fore.RED+Style.BRIGHT+"[!] You Can Enter Only 0,1 Try Again"+Style.RESET_ALL)

    if(platform.system()=="Windows"):
        print(Fore.GREEN+Style.NORMAL+"[+] Setting Up The System")
        time.sleep(1)
        is_installed=os.system('.\devcon.exe help 1>temp_output.txt 2>&1')
        os.system("del -Force temp_output.txt")
        if(is_installed==0):
            print("[+] Setup Completed"+Style.RESET_ALL)
        if(is_installed!=0):
            print("\n[+] One File Missing. Installing .."+Style.RESET_ALL)
            if platform.architecture()[0]=="32bit":
                url="https://dl.dropboxusercontent.com/scl/fi/kt77ziditzh18npsxjfvf/devcon_x86.exe?rlkey=3bww2esk3yue07m2i8a68y695&dl=0"
            if platform.architecture()[0]=="64bit":
                url="https://dl.dropboxusercontent.com/scl/fi/da5mo5qqmvzk5ixvzuc0j/devcon_x64.exe?rlkey=okaunpowov9nev2jnw84g2zvc&dl=0"
            response=requests.get(url)
            if response.status_code == 200:
                with open('.\devcon.exe','wb') as file:
                    file.write(response.content)
            else:
                print(Fore.RED+Style.BRIGHT+f"[!] Failed To Download File. Status Code: {response.status_code}"+Style.RESET_ALL)

        command = r".\devcon.exe listclass USB"
        result = subprocess.check_output(command,text=True)
        usb_root_hub_lines=[line for line in result.splitlines() if "USB Root Hub" in line]
        device_ids=[re.search(r'USB\\[^:]+',line).group() for line in usb_root_hub_lines]
        count=0
        for i in device_ids:
            device_ids[count]=i.strip()
            count+=1
        print(Fore.GREEN+Style.NORMAL+"\n[+] Menu Of Port Killer :-")
        print("[+] L - List All USB Ports")
        print("[+] 1 - Disable All USB Ports")
        print("[+] 0 - Enable All USB Ports")
        #print("[+] D - Disable a Single Port")
        #print("[+] E - Enable a Single Port")
        print("[+] Q - Quit the Program"+Style.RESET_ALL)

        while True:
            user_input2=input(Fore.BLUE+Style.BRIGHT+"\n[-] Enter Your Choice - "+Style.RESET_ALL)
            user_input2=user_input2.lower()
            if(user_input2 ==  "l"):
                for i in device_ids:
                    print(i)

            if(user_input2 == "1"):
                for device_id in device_ids:
                    os.system(f'.\devcon.exe remove "@{device_id}"')
                break

            if(user_input2 == "0"):
                os.system(".\devcon.exe rescan")
                break

            #if(user_input2 == "d"):
             #   pass
              #  break

            #if(user_input2 == "e"):
             #   pass
              #  break

            if(user_input2 == "q"):
                print(Fore.RED+Style.BRIGHT+"\n\n[!] EXITING THE PROGRAM."+Style.RESET_ALL)
                break

except KeyboardInterrupt:
    print(Fore.RED+Style.BRIGHT+"\n\n[!] EXITING THE PROGRAM .",end="")
    time.sleep(0.2)
    print(".",end="\n"+Style.RESET_ALL)
except Exception as e:
    print(Fore.RED+Style.BRIGHT+f"\n[!] Unexpected Error Occured -> {e}. Try Again"+Style.RESET_ALL)
