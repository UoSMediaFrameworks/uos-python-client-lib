import sys
sys.path.insert(0,'../mf_client') #lib location

from MF_API_Client import *
from pprint import *
import time

testRoom = "presentation"
test_scenes = []

#these variables would be pulled from a config in a real client
mf_client = MF_API_Client('url', 80, 'password')
print("Connected to MF as a client")

#callbacks----------------------------------------------------------------------
def scenes_callback(scenes):
    global test_scenes
    test_scenes = scenes
    pprint(test_scenes)

def scene_callback(scene):
    pprint(scene)

#generic requests----------------------------------------------------------------

print "Getting all scenes"
mf_client.getSceneList(scenes_callback)

time.sleep(5) #wait to make sure scenes have been recived

#get a specific scenes data
testSceneID = test_scenes[1].get('_id')
testSceneName = test_scenes[1].get('name')
print "Getting scene: " + testSceneName + " with ID: " + testSceneID
mf_client.getSceneByID(testSceneID, scene_callback)

time.sleep(5)
print "Sending a single scene"
mf_client.sendScene('5797309781a29c700e9ddf41')

time.sleep(5)
print("Sending scenes and themes")
mf_client.sendScenesAndThemes(testRoom, ['5797309781a29c700e9ddf41'], ['theme'])

time.sleep(5)
print("Sending scene with empty themes")
mf_client.sendScenesAndThemes(testRoom,['5797309781a29c700e9ddf41'], [])

time.sleep(5)
print("Sending Scene with no themes")
mf_client.sendScenesAndThemes(testRoom, ['5797309781a29c700e9ddf41'])

time.sleep(5)
print("Attempt to send empty scene list")
try:
    mf_client.sendScenesAndThemes(testRoom, [])
    #should throw error
except Exception as e:
    print e

print "done"

exit()
