from visionLiveSDK import apiClient
from visionLiveSDK.apiClient import ApiClient

appSecret = '{Your App Secret}'
appKey='{Your App Key}'
client = ApiClient('https://www.city.gov/API',appKey, appSecret)


eventResult = client.vision.cms.calendarcomponent.event.get(Fields=1, ID=3754)
dictEventResult = apiClient._O(dict(eventResult))
print(dictEventResult)
print(dictEventResult.Event.StartDate)


eventResult = client.vision.cms.core.system.content.get(Fields=1, ID=3754, ContentTypeName='Event')
dictEventResult = apiClient._O(dict(eventResult))
print(dictEventResult)
print(dictEventResult.Content.StartDate)

