# PolyAccess



Malware and listener created with python

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

``` 
**How to use?**

```
1. edit the host and the port for the listener.py and the backdoor.py
2. install the requirements.txt using "pip3 install -r requirements.txt"
3. and then "compile" the backdoor.py and the keylogger.py using pyinstaller or nuitka to create the payload
4. start the listener.py on your target machine and execute the payload on your target machine
```

unobfscated python detection:
![image](https://user-images.githubusercontent.com/93959737/206857718-b6397dd8-22d7-4634-8bad-d143a0377639.png)

obfuscated python detection:
![image](https://user-images.githubusercontent.com/93959737/206237397-bc30953a-4062-448f-9664-4bf230d1a2e9.png)

***Note: For those braindead people , the plain obfuscated python file is non detectable , however depending on how you convert the python code to an exe, the exe may not be fully undetectable***

python to exe detection (nuitka):
![image](https://user-images.githubusercontent.com/93959737/206857089-22a2608a-4d88-4217-af74-958e080dfb56.png)


Evading Bitdefender example:


https://user-images.githubusercontent.com/93959737/206185600-5bd25ab3-97e6-4434-a735-d2735476a24d.mp4





.


.

.
***join my discord for more enquiries***
https://discord.gg/3R3BaDrTPK
