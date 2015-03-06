#from authomatic.providers import oauth2, oauth1#, gaeopenid

#CONFIG = {
    
    #'tw': { # Your internal provider name
        
        # Provider class
    #    'class_': oauth1.Twitter,
        
        # Twitter is an AuthorizationProvider so we need to set several other properties too:
    #    'consumer_key': '########################',
    #    'consumer_secret': '########################',
    #},
    
    # 'fb': {
           
    #     'class_': oauth2.Facebook,
        
    #     # Facebook is an AuthorizationProvider too.
    #     'consumer_key': '633714880107939',
    #     'consumer_secret': 'f8d8cf8f4b51cf96fadba2ae51577a3f',
        
    #     # But it is also an OAuth 2.0 provider and it needs scope.
    #     'scope': ['user_about_me', 'email', 'publish_stream'],
    # }
    
    #'oi': {
           
        # OpenID provider dependent on the python-openid package.
    #    'class_': openid.OpenID,
    #}
#s}