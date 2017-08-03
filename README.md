# mf_client

A python library for media framework client devices

## Installation

```PIP install mf_client```

## Usage

**Create a new media framework client:**
The URL is the base URL of the websocket server, by default this runs on port 80.
```python
mf_client = MF_API_Client('url', 80, 'password')
```

#### General Commands
These are generic commands not targeted at a specific room

**Get a list of all available scenes:**
Scenes will be returned to the specified callback
```python
def scenes_callback(scenes):
    print(scenes)

mf_client.getScenes(scenes_callback)
```

**Get the content of a scene from it's ID:**
Returns the full content of a single scene
```python
def scene_callback(scene):
    print(scene)

mf_client.getSceneByID(testSceneID, scene_callback)
```

#### Playback Commands

These commands are targeted at a specific playback room

**Send a scene to a room for playback**

```python
mf_client.sendScene('room', 'sceneID')
```

**Send a list of scenes  themes for playback:**
There must be at least one scene, any other combination of scenes and themes is valid
```python
mf_client.sendScenesAndThemes('room', ['sceneID','sceneID'], ['theme','theme'])
```

## Contributing

Read [CONTRIBUTING](CONTRIBUTING.md).
