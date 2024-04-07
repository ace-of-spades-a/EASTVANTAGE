first you need to install requirment.txt
which will install the all requirments
{
    if pydentic[email] module not found install it manually 
    pip3 install pydentic[email]
}
then run the command -
uvicorn main:app --reload

go to the http://127.0.0.1:8000/docs/ on to the browser.
you will see two section in that 
1. User
2. Address

1. user have two apis:
    1. Sign IN
    2. Log IN

    Signin:- will register a user.
    Login:- Will validate user and  return authentication token.

For access address you need to validate user (Login ) and valid acceess token.
