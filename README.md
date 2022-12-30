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
>undetectable 
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
C2 listener
```

**How to use?**

```
1. edit the host and the port for the listener.py and the backdoor.py
optional: put your webhook in the discord.py file to recieve discord token



2. install the requirements.txt using "pip3 install -r requirements.txt"


3. and then "build" the backdoor.py and the keylogger.py using pyinstaller or nuitka to create the payload
NOTE: if you are building on windows 11, windows 11 defender might detect and prevent the building process, so it is adviced that you stop windows defender, however the payload generated will still be undetectable



4. start the listener.py on your machine and execute the payload on the target machine
```

unobfscated python detection:
![image](https://user-images.githubusercontent.com/93959737/206857718-b6397dd8-22d7-4634-8bad-d143a0377639.png)

obfuscated python detection:
![image](https://user-images.githubusercontent.com/93959737/206237397-bc30953a-4062-448f-9664-4bf230d1a2e9.png)

***Note:the plain obfuscated python file is non detectable , however depending on how you convert the python code to an exe, the exe may not be fully undetectable***

python to exe detection (nuitka):
![image](https://user-images.githubusercontent.com/93959737/206857089-22a2608a-4d88-4217-af74-958e080dfb56.png)


Evading Bitdefender example:


https://user-images.githubusercontent.com/93959737/206185600-5bd25ab3-97e6-4434-a735-d2735476a24d.mp


