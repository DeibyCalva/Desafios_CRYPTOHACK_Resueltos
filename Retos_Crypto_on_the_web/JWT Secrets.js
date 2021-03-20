
import jwt
encoded = jwt.encode({'username':'PatoNinja','admin':'true'},'secret',algorithm='HS256')
print(encoded)





