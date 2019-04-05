import ai2thor.controller
controller = ai2thor.controller.Controller()
controller.start()

controller.reset('FloorPlan28')
controller.step(dict(action='Initialize', gridSize=0.1))
event = controller.step(dict(action='RotateLeft'))

event = controller.step(dict(action='LookDown'))
event = controller.step(dict(action='MoveAhead'))
event = controller.step(dict(action='MoveAhead'))
event = controller.step(dict(action='MoveAhead'))

for o in event.metadata['objects']:
  if o['visible'] and o['pickupable'] and o['objectType'] == 'Egg':
     event = controller.step(dict(action='PickupObject',objectId=o['objectId']), raise_for_failure=True) 
     egg_object_id = o['objectId']
     break
event = controller.step(dict(action='LookUp'))
event = controller.step(dict(action='MoveLeft'))
event = controller.step(dict(action='MoveLeft'))
event = controller.step(dict(action='MoveBack'))
event = controller.step(dict(action='MoveBack'))
event = controller.step(dict(action='MoveLeft'))
event = controller.step(dict(action='MoveLeft'))
event = controller.step(dict(action='MoveBack'))
for o in event.metadata['objects']:
    if o['visible'] and o['openable'] and o['objectType'] == 'Fridge':
        event = controller.step(dict(action='OpenObject', objectId=o['objectId']), raise_for_failure=True)
        receptacle_object_id = o['objectId']
        break

event = controller.step(dict(
    action='PutObject',
    receptacleObjectId=receptacle_object_id,
    objectId=egg_object_id), raise_for_failure=True)

# close the microwave
event = controller.step(dict(
    action='CloseObject',
    objectId=receptacle_object_id), raise_for_failure=True)
event = controller.step(dict(action='MoveBack'))
event = controller.step(dict(action='MoveBack'))
event = controller.step(dict(action='MoveBack'))
event = controller.step(dict(action='MoveBack'))


