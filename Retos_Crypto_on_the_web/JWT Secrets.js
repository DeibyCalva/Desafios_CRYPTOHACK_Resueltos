
import jwt
encoded = jwt.encode({'username':'mario','admin':'true'},'secret',algorithm='HS256')
print(encoded)





