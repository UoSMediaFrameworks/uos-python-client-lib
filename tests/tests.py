import sys
sys.path.insert(0,'../src')

from mf_client.MF_API_Client import *
import time


#these variables would be pulled from a config in a real client
room = MF_API_Client('url', 80, 'password', 'room')
print("Connected to room")

time.sleep(1)
print("Sending scenes and themes")
room.sendScenesAndThemes(['5797309781a29c700e9ddf41'], ['theme'])

time.sleep(10)
print("Sending scene with empty themes")
room.sendScenesAndThemes(['5797309781a29c700e9ddf41'], [])

time.sleep(10)
print("Sending Scene with no themes")
room.sendScenesAndThemes(['5797309781a29c700e9ddf41'])

time.sleep(10)
print("Attempt to send empty scene list")
room.sendScenesAndThemes([])

#should throw error
