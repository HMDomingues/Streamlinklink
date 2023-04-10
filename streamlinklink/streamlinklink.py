import sys
import json
import subprocess
import struct



def getMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    return json.loads(message)


def launchStreamlink(url):
    p = subprocess.Popen(['streamlink.exe', url, '720p60', '--player-passthrough=hls', '--twitch-disable-ads'], creationflags = 0x01000000 | subprocess.CREATE_NEW_CONSOLE)




def main():
    url = getMessage()
    launchStreamlink(url)


main()

    


