from flask import Flask
from flask_restful import Api,Resource
import requests

app =Flask(__name__)
api=Api(app)

class getSensor(Resource):
	def get(self,SV):
		if SV>400 and SV<650 :
			return {"Light": "on"}
		else :
			return {"Light": "off"}

api.add_resource(getSensor,"/testing/<int:SV>")

if __name__=="__main__":
	app.run(debug=True)


port = "http://127.0.0.1:5000/"

print('Enter the value:')
x = input()
response = requests.get(port+"testing/"+x)
print(response.json())
