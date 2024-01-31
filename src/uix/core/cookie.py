from typing import Dict, Union

def cookie_builder_from_query_string(query: Dict[str, Union[str, int, bool]]) -> Dict[str, Union[str, int, None, bool]]:
    """
    Build a cookie dictionary from query string parameters.

    Args:
        query (dict): Query string parameters.

    Returns:
        dict: Cookie dictionary.

    Examples:
        cookie_builder_from_query_string({'key': 'my_cookie', 'value': 'my_value'})
        cookie_builder_from_query_string({'key': 'my_cookie', 'value': 'my_value', 'max_age': 3600})
        cookie_builder_from_query_string({'key': 'my_cookie', 'value': 'my_value', 'path': '/'})
        cookie_builder_from_query_string({'key': 'my_cookie', 'value': 'my_value', 'domain': '127.0.0.1'})
        cookie_builder_from_query_string({'key': 'my_cookie', 'value': 'my_value', 'expires': 1711877452, 'secure': True, 'httponly': True, 'samesite': 'strict'})

      Example URLs:
        http://127.0.0.1:5000/set-cookie?key=my_cookie&value=my_value
        http://127.0.0.1:5000/set-cookie?key=my_cookie&value=my_value&max_age=3600
        http://127.0.0.1:5000/set-cookie?key=my_cookie&value=my_value&path=/
        http://127.0.0.1:5000/set-cookie?key=my_cookie&value=my_value&domain=127.0.0.1
        http://127.0.0.1:5000/set-cookie?key=my_cookie&value=my_value&expires=1711877452
        http://127.0.0.1:5000/set-cookie?key=my_cookie&value=my_value&expires=1711877452&secure=true&httponly=true&samesite=strict
    """

    cookie = {}
    cookie["key"] = query.get("key", default=None)
    cookie["value"] = query.get("value", default=None)
    
    max_age = query.get("max_age", default=None)
    cookie["max_age"] = int(max_age) if max_age and max_age.isdigit() else None
    
    expires = query.get("expires", default=None)
    cookie["expires"] = int(expires) if expires is not None else None
    
    cookie["path"] = query.get("path", default=None)
    cookie["domain"] = query.get("domain", default=None)
    
    secure = query.get("secure", default="false").lower()
    cookie["secure"] = secure == "true"
    
    httponly = query.get("httponly", default="false").lower()
    cookie["httponly"] = httponly == "true"
    
    cookie["samesite"] = query.get("samesite", default=None)
    
    return cookie

def build_cookie_url(base_url: str, cookie_params: dict) -> str:
    """
    Build a URL with cookie parameters.

    Args:
        base_url (str): The base URL.
        cookie_params (dict): Cookie parameters.

    Returns:
        str: The complete URL.
    """
    query_string = '&'.join(f"{key}={value}" for key, value in cookie_params.items() if value is not None)
    url = f"{base_url}?{query_string}" if query_string else base_url
    return url