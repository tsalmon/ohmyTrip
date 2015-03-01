from django.http import HttpResponse
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter

from config import CONFIG

authomatic = Authomatic(CONFIG, 'a super secret random string')

def home(request):
    # Create links and OpenID form to the Login handler.
    return HttpResponse('''
        Login with <a href="fb">Facebook</a>.<br />
    ''')

#source : https://github.com/peterhudec/authomatic/blob/master/examples/django/example/simple/views.py
def login(request, provider_name):
    response = HttpResponse()
    result = authomatic.login(DjangoAdapter(request, response), provider_name)
    if result:
        response.write('<a href="..">Home</a>')
        
        if result.error:
            response.write('<h2>Damn that error: {0}</h2>'.format(result.error.message))
        
        elif result.user:
            if not (result.user.name and result.user.id):
                result.user.update()
            response.write(u'<h1>Hi {0}</h1>'.format(result.user.name))
            response.write(u'<h2>Your id is: {0}</h2>'.format(result.user.id))
            response.write(u'<h2>Your email is: {0}</h2>'.format(result.user.email))
            if result.user.credentials:
                if result.provider.name == 'fb':
                    response.write('Your are logged in with Facebook.<br />')
                    url = 'https://graph.facebook.com/{0}?fields=feed.limit(5)'
                    url = url.format(result.user.id)
                    
                    # Access user's protected resource.
                    access_response = result.provider.access(url)
                    
                    if access_response.status == 200:
                        # Parse response.
                        response.write("OK!")
                        """
                        error = access_response.data.get('error')
                        statuses = access_response.data.get('feed').get('data')
                        
                        if error:
                            response.write(u'Damn that error: {0}!'.format(error))
                        elif statuses:
                            response.write('Your 5 most recent statuses:<br />')
                            for message in statuses:
                                
                                text = message.get('message')
                                date = message.get('created_time')
                                
                                response.write(u'<h3>{0}</h3>'.format(text))
                                response.write(u'Posted on: {0}'.format(date))
                        """
                    else:
                        response.write('Damn that unknown error!<br />')
                        response.write(u'Status: {0}'.format(response.status))                   
    return response
