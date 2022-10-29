
from .db import base

def get_session(request):
    #jwt = request.session.get('jwt',None)
    try:
        jwt  = request.cookies.get('jwt',None)
        if  "?access_token=" in str(jwt):
            try:
                session_object = base.auth.get_session_from_url(url=jwt)
                session = base.auth.current_session = session_object
                return session
            except :
                return None    
        else:
            session = base.auth.session()
            return session
               
    except Exception as e:
        raise  
    #return base.auth.user()
         