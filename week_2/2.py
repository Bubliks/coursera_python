import json
import functools

def to_json(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        return json.dumps(f(*args, **kwargs))
    return wrapped

@to_json
def get_data(data):
    return {
     'data': data
}

value = 42
print(get_data(value))