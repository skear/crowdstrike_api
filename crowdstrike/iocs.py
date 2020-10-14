import json
import urllib.parse
from loguru import logger
from .utilities import validate_kwargs

def iocs_create(self, **kwargs):
    """ Create a new IOC
    Type (string) - Valid types include: (sha256, md5, domain: A domain name, ipv4, ipv6)
    Value (string) - The string representation of the indicator
    Policy (string) - detect (Enable detections) none: (Disable detections)
    """

    args_validation = {
        'policy': str,
        'type' : str,
        'value' : str,
    }
    validate_kwargs(args_validation, kwargs, required=args_validation.keys())

    uri = '/indicators/entities/iocs/v1'
    method = 'post'

    response = self.request(uri=uri,
                            request_method=method,
                            data=[kwargs],
                            )
    logger.debug(f"Request body: {response.request.body}")
    logger.debug(response)
    return response.json()


def iocs_get(self, **kwargs):
    ''' Get an IOC by providing a type and value

    Type (string) - Valid types include: (sha256, md5, domain: A domain name, ipv4, ipv6)
    Value (string) - The string representation of the indicator

    '''

    args_validation = {
        'type' : str,
        'value' : str,
    }
    validate_kwargs(args_validation, kwargs)
    uri = '/indicators/entities/iocs/v1'
    method = 'get'

    response = self.request(uri=uri,
                            request_method=method,
                            data="",
                            )
    logger.debug(f"Request body: {response.request.body}")
    logger.debug(response)
    return response.json()

def iocs_delete(self, **kwargs):
    '''Delete an IOC by providing a type and value

     Type (string) - Valid types include: (sha256, md5, domain: A domain name, ipv4, ipv6)
     Value (string) - The string representation of the indicator

    '''
    
    args_validation = {
        'type' : str,
        'value' : str,
    }
    validate_kwargs(args_validation, kwargs)
    uri = '/indicators/entities/iocs/v1?'

    # Add arguments as additional parameters to the base URI
    uri = uri + urllib.parse.urlencode(kwargs)

    method = 'delete'

    response = self.request(uri=uri,
                            request_method=method,
                            data="",
                            )
    logger.debug(f"Request body: {response.request.body}")
    logger.debug(response)
    return response.json()
