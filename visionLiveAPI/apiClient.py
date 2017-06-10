import hashlib
import base64
import datetime
import urllib2
import urllib
import json
import apiConstant
import apiException

# some ideas are from https://github.com/dingyuliang/python-taobao/tree/master/taobao

class ApiClient(object):
    """
    Base API Client class for executing API
    """
    API_VERSION = '1.0'
    FORMAT = 'json' #'xml'
    
    def __init__(self, serverUrl = None, app_key = None, app_secret = None):
        if not (app_key and app_secret and serverUrl):
            raise AttributeError("serverUrl and app_key and app_secret can not be None.")
        
        self.serverUrl = serverUrl
        self.app_key = app_key
        self.app_secret = app_secret

    def decode_params(self, api_parameters):
        params = {}
        param_string = base64.b64decode(api_parameters)
        for p in param_string.split('&') :
            key, value = p.split('=')
            params[key] = value
        return params

    def _get_timestamp(self):
        utcTime = datetime.datetime.utcnow()
        strtime = utcTime.strftime(apiConstant.DATE_TIME_FORMAT)
        return strtime

    def _sign(self, params):
        # Step 1: order parameters by name alphabetically
        keys = self._sortedByCSharp(params.keys())

        # Step 2: contact all parameters name and parameter value 
        query = self.app_secret
        for key in keys:
            if key and params.get(key):
                query = query + key + str(params.get(key))

        # Step 3: encrypt with MD5
        m = hashlib.md5()
        m.update(query)

        # Step 4: convert the binary to uppercase hexadecimal    
        sign = m.hexdigest().upper()

        return sign
    
    def execute(self, method_name, **kwargs):
        params = self._generate_params(method_name, **kwargs)
        urlopen = urllib2.urlopen(self.serverUrl, urllib.urlencode(params))
        rsp = urlopen.read()
        rsp = json.loads(rsp, strict=False, object_hook=lambda x:_O(x))

        if rsp.has_key('ErrorCode'):
            error_code = rsp['ErrorCode']
            error_msg = rsp['ErrorMessage']
            raise apiException.ApiException(error_code,error_msg)
        else:
            #rsp = rsp[method_name.replace('.','_')[7:] + '_response']
            return rsp

    def __request(self, method_name, *args, **kwargs):
        return self.execute(method_name, **kwargs)

    def _sortedByCSharp(self, keys):
        # C# SortedDictionary is different from Python sorted.
        # assume we only have parameters with starting  with _ and letter.
        dictOfKeys = {}
        for key in keys:
            dictOfKeys[key.lower()] = key
        
        result = []
        for key in sorted(dictOfKeys.keys()):
            result.append(dictOfKeys.get(key))
        
        return result

    def __getattr__(self, name):
        return _Method(self.__request, name)

    def _generate_params(self, method_name, **kwargs):
        params = {}
        for k, v in kwargs.iteritems():
            if v: 
                params[k] = v

        params[apiConstant.PARAM_METHOD_KEY] = method_name
        params[apiConstant.PARAM_VERSION_KEY] = self.API_VERSION
        params[apiConstant.PARAM_APP_KEY_KEY] = self.app_key
        params[apiConstant.PARAM_FORMAT_KEY] = self.FORMAT
        params[apiConstant.PARAM_TIMESTAMP_KEY] = self._get_timestamp()
        
        params[apiConstant.PARAM_SIGN_KEY] = self._sign(params)

        return params

class _O(dict):
    """Makes a dictionary behave like an object."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value

class _Method:
    def __init__(self, send, name):
        self.__send = send
        self.__name = name

    def __getattr__(self, name):
        return _Method(self.__send, "%s.%s" % (self.__name, name))

    def __call__(self, *args, **kwargs):
        return self.__send(self.__name, args, **kwargs)