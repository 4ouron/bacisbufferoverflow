# Buffer overflow Learning 


## Lab setting up

Download:
- Window 10 VM: https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/
- Vulnserver: https://github.com/stephenbradshaw/vulnserver
- Immunity Debugger: https://www.immunityinc.com/products/debugger/
- Kali linux VM: https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/
- Corelan Mona: https://github.com/corelan/mona




## Preparation step: 
  On Windows 10: 
  - Turn off all firewall, windows defender vulnserver will be buggy if they are on.
  - Install Immunity Debugger, it's very simple and straight forward, just next.
  - Copy mona.py into Immunity Debugger' Folder "C:\Program Files (x86)\Immunity INc\Immunity Debugger\PyCommands"
  
  On Kali linux:
  - Install Netcap, metasploit, vim
  
  
 ## Let's start hacking into vuln server:
 
 
### 1.Find vulnerabilities
On Vuln server:
- Run immunity debugger as admin.
- Run vulnserver.exe as admin
- Attach vulnserver process to immunity debugger.
- Hit the button PLAY on immunity debugger to RUN, status will be at the boton right conner
