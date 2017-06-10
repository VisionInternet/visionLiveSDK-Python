# visionLiveSDK-Python

The Python SDK project for visionLive API

API Explorer: http://api.visioninternet.com/

API Document: http://api.visioninternet.com/Document

Install:
```
# pip install -e git+https://github.com/VisionInternet/visionLiveSDK-Python.git#egg=visionLiveSDK
```

Uninstall
```
# pip uninstall visionLiveSDK
```

Python Example
```
from visionLiveSDK import apiClient
from visionLiveSDK.apiClient import ApiClient

appSecret = '{Your App Secret}'
appKey='{Your App Key}'
client = ApiClient('http://www.city.gov/API',appKey, appSecret)

# vision.cms.calendarcomponent.event.get is the API Name
eventResult = client.vision.cms.calendarcomponent.event.get(Fields=1, ID=3754)
dictEventResult = apiClient._O(dict(eventResult))
print(dictEventResult.Event.StartDate)

# vision.cms.core.system.content.get is the API Name
eventResult = client.vision.cms.core.system.content.get(Fields=1, ID=3754, ContentTypeName='Event')
dictEventResult = apiClient._O(dict(eventResult))
print(dictEventResult.Content.StartDate)
```

