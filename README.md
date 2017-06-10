# visionLiveSDK-Python

API Explorer: http://api.visioninternet.com/
API Document: http://api.visioninternet.com/Document

```
from visionLiveAPI import apiClient
from visionLiveAPI.apiClient import ApiClient

appSecret = '{Your App Secret}'
appKey='{Your App Key}'
client = ApiClient('http://www.city.gov/API',appKey, appSecret)

# vision.cms.calendarcomponent.event.get is the API Name
eventResult = client.vision.cms.calendarcomponent.event.get(Fields=1, ID=3754)
dictEventResult = apiClient._O(dict(eventResult))
print(dictEventResult)
print(dictEventResult.Event.StartDate)

# vision.cms.core.system.content.get is the API Name
eventResult = client.vision.cms.core.system.content.get(Fields=1, ID=3754, ContentTypeName='Event')
dictEventResult = apiClient._O(dict(eventResult))
print(dictEventResult)
print(dictEventResult.Content.StartDate)
```

