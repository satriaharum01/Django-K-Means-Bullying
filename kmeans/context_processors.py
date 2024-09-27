import os 

def export_vars(request):
    data = {}
    data['APP_NAME'] = os.environ['APP_NAME']
    data['APP_DETAIL'] = os.environ['APP_DETAIL']
    return data