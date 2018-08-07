def say_hello(): 
  print("Hello")
  
# say_hello() Output: Hello
say_hello2 = say_hello

print(say_hello2()) # Output: Hello 


def authenticate(func):
    def authenticate_and_call(*args, **kwargs):
        if not Account.is_authentic(request): 
            raise Exception('Authentication Failed.')
        return func(*args, **kwargs)
    return authenticate_and_call


def authorize(role):
    def wrapper(func):
        def authorize_and_call(*args, **kwargs):
            if not current_user.has(role): 
                raise Exception('Unauthorized Access!')
            return func(*args, **kwargs)
        return authorize_and_call
    return wrapper