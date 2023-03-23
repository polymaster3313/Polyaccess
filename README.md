# PolyC2

<small>low-profile C2 and malware made in python</small>

***for educational purposes only***



*only capable on windows*

Features:

```
>Remote Access through shell
>keglogging
>grab chrome passwords
>registry persistence
>upload and download files
>undetectable
>screenshot
>checkprivilege
>checkporn
>block website
>gets system information
>encrypt and decrypt files 
>privilege escalation
``` 

Update
```
Privilege escalation:
  weak service path
  Check Always install elevated
```

Upcoming features:
```
play sound in background
AES encryption tunneling
```

**How to use?**

```
1. edit the host and the port in the config.py



2. install the requirements.txt using "pip3 install -r requirements.txt"


3. and then "build" the backdoor.py using pyinstaller or nuitka
NOTE: if you are building on windows 11, windows 11 defender might detect and prevent the building process, so it is adviced that you stop windows defender, however the payload generated will still be undetectable



4. start the C2.py on your machine and execute the payload on the target machine
```

python to exe detection (nuitka):
![image](https://user-images.githubusercontent.com/93959737/222945408-82b23489-eda3-4b32-b3cd-4f3498683d22.png)


Evading Bitdefender example:

https://www.youtube.com/watch?v=iqlV4gZxqIw&t=2s

PolyC2 demonstration:
https://www.youtube.com/watch?v=Duf53TVVqrg


Discord server for enquiries:
https://discord.gg/3R3BaDrTPK
