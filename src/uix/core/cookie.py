from urllib.parse import urlencode

def extract_cookie_settings_from_request_args(request_args):
    """
    Extracts cookie settings from Flask's request.args for potential server-side usage.
    Handles type conversions, provides default values, and performs validation.

    Args:
        request_args (Dict[str, Union[str, int, bool]]): Flask's request.args dictionary.

    Returns:
        Dict[str, Union[str, int, bool, None]]: A dictionary containing potential cookie settings.

    Examples:
        >>> extract_cookie_settings_from_request_args({'key': 'my_cookie', 'value': 'my_value'})
        {'key': 'my_cookie', 'value': 'my_value', ...}  # Other defaults applied

        >>> extract_cookie_settings_from_request_args({'key': 'my_cookie', 'value': 'my_value', 'max_age': '3600'})
        {'key': 'my_cookie', 'value': 'my_value', 'max_age': 3600, ...}

        >>> extract_cookie_settings_from_request_args({'key': 'my_cookie', 'value': 'my_value', 'path': '/'})
        {'key': 'my_cookie', 'value': 'my_value', 'path': '/', ...}

        >>> extract_cookie_settings_from_request_args({'key': 'my_cookie', 'value': 'my_value', 'domain': '127.0.0.1'})
        {'key': 'my_cookie', 'value': 'my_value', 'domain': '127.0.0.1', ...}

        >>> extract_cookie_settings_from_request_args({'key': 'my_cookie', 'value': 'my_value', 'expires': '1711877452', 'secure': 'true', 'httponly': 'true', 'samesite': 'strict'})
        {'key': 'my_cookie', 'value': 'my_value', 'expires': 1711877452, 'secure': True, 'httponly': True, 'samesite': 'strict', ...}
    """
    cookie_settings = {
        'key': request_args.get('key'),
        'value': request_args.get('value'),
        'max_age': int(request_args.get('max_age')) if request_args.get('max_age') else None,
        'expires': int(request_args.get('expires')) if request_args.get('expires') else None,
        'path': request_args.get('path', '/'),
        'domain': request_args.get('domain'),
        'secure': request_args.get('secure', 'False').lower() == 'true',
        'httponly': request_args.get('httponly', 'False').lower() == 'true',
        'samesite': request_args.get('samesite', 'Lax').lower() 
    }

    # Validation: Check for valid 'samesite' value
    if cookie_settings['samesite'] not in ['lax', 'strict', 'none']:
        cookie_settings['samesite'] = 'Lax'  # Set to a safe default
        print(f"Warning: Invalid SameSite value: {cookie_settings['samesite']}. Using 'Lax'")

    return cookie_settings

def build_cookie_url(route_path, cookie_name, cookie_params, cookie_name_key='key'):
    """
    Generates a URL with query parameters based on cookie settings.

    Args:
        route_path (str): The path of the route that sets the cookie (e.g., "/set-cookie").
        cookie_name (str): The name of the cookie.
        cookie_params (dict): A dictionary containing cookie settings.
        cookie_name_key (str, optional): The key to use for the cookie name in the URL. 
                                         Defaults to 'key' for Flask compatibility.

    Returns:
        str: The generated URL with query parameters.

    Examples:
        # For Flask:
        >>> build_cookie_url('/set-cookie', 'my_cookie', {'value': 'my_value'})
        '/set-cookie?key=my_cookie&value=my_value'

        # For a cookie jar (potentially):
        >>> build_cookie_url('/set-cookie', 'session_id', {'value': '12345'}, cookie_name_key='name')
        '/set-cookie?name=session_id&value=12345'
    """

    query_params = {cookie_name_key: cookie_name}  # Start with the cookie name
    query_params.update(cookie_params)

    # Handle special cases (if needed)
    if 'expires' in query_params:
        query_params['expires'] = str(query_params['expires'])  

    query_string = urlencode(query_params)
    return route_path + '?' + query_string

from requests.cookies import cookiejar_from_dict as build_cookieJar_from_dict