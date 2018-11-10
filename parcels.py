from flask import Flask, jsonify, request
app = Flask(__name__)
client_parcels = [
    {'name': 'groceries','id':1, 'first name' : 'francis', 'Location' : 'masaka', 'Destination' :'kampala'},
    {'name': 'chairs', 'first name' : 'kamanzi', 'location' : 'entebbe', 'destination' : 'arua'},
    {'name': 'posho', 'first name' : 'franchesco', 'location' : 'pakwach', 'destination' : 'gulu'},
    {'name': 'milk', 'first name' : 'musasizi', 'location' : 'mbarara', 'destination' : 'luweero'}
  ]
  
  
@app.route('/')
def test():
	return 'Welcome to Our Parcel Delivery Order'
	
@app.route('/parcels/api/v1/client_parcels', methods=['GET'])
def returnAll():
    return jsonify({'client_parcels' : client_parcels}), 200
    
@app.route('/parcels/api/v1/client_parcels/<string:name>', methods=['GET'])
def returnOne(name):
    parcels = [client_parcel for client_parcel in client_parcels if client_parcel['name'] == name] 
    return jsonify({'client_parcel' : parcels}), 200
    
@app.route('/parcels/api/v1/client_parcels', methods=['POST'])
def addOne():
    client_parcel = [{'name' : request.json['name']}] 
    client_parcels.append(client_parcel)
    return jsonify({'client_parcels' : client_parcels})


@app.route('/parcels/api/v1/client_parcels/<string:name>', methods=['PUT'])
def editOne(name):
     parcels = [client_parcel for client_parcel in client_parcels if client_parcel['name'] == name]#returns all the parcels that match the name
     parcels[0]['name'] = request.json['name'] #update the name whatever that is in the json
     return jsonify({'parcel' : parcels[0]})
       
    

    
    
#@app.route('/users/api/v1/user_id/<string:name>', methods=['GET'])
#def returnOne(user_id):
	#users = [users for users in users if users['user_id'] == user == user_id]
	#return jsonify({'users' : user_id})
	    
    
        
	
#@app.route('/parcels/api/v1/my_parcels/<string:name>', methods=['GET'])
#def returnOne(name):
	#Items = [My_Item for My_Item in My_Items if My_Item['name'] == name] 
    #return jsonify({'My_Item' : Items})	


if __name__ == '__main__':
	app.run(debug=True)
