import json
import uuid
import random
import datetime
import time
from string import ascii_letters



methods = ['GET','POST']
urls = ['post', 'profiles', 'feed']
statuses = [200, 400, 404, 500, 200, 200, 200]
users = ["user_1", "user_2", "user_3" ]

def make_ok():

    ok = {
        "text": 'text',
        'record': { "exception": 'null',
                    'extra': {'request_id':str(uuid.uuid4()), 
                                'method': random.choice(methods), 
                                "url": f"/api/content/{random.choice(urls)}", 
                                "status_code": random.choice(statuses), 
                                "profile_id": random.choice(users) , 
                                "duration": random.uniform(0.02, 1.5)
                            },
                    "time": {"repr":str(datetime.datetime.now()) + '+00:00', "timestamp": datetime.datetime.now().timestamp()}} 
        }
    return ok 

def make_ex():
    ok = make_ok()
    errors = ["USER NOT FOUND", "SERVER IS DOWN", "AUTH FAILED"]
    time_ = ok['record']['time']
   
    ex =  {'record': {'exception': {"type": None, "value": None, "traceback": False}}}
    ok.update(ex)

    er = random.choice(errors)
    extra = {"extra" : 
    {"err": er, 
    "request_id": str(uuid.uuid4()), 
    "method": random.choice(methods), 
    "url": f"/api/profile/{random.choice(urls)}", 
    "exception_info": 
        {"type": er,
        "filename": f"/app/./core/api/api_v1/endpoints/profile/{''.join(random.choices(ascii_letters, k=4))}.py", 
                        "line": f"raise {er}", "func": f"get_profile_settings"}
        }
    }

    ok.update(extra)
    ok['time'] = time_
    return ok


for e in range(100):
    fn = random.choice([make_ok, make_ex, make_ok, make_ok])
    log = json.dumps(fn()) 
    time.sleep(1)
    print('осталось ',100 - e)
    with open('log.json', 'a') as f:
        f.write(f'{log}\n')
