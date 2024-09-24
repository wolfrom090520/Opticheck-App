from firebase import firebase


#initialize Firebase
firebase = firebase.FirebaseApplication('https://opticheck-62567-default-rtdb.firebaseio.com/', None)


#importing data
data = {
    'email': 'valenciagelo09@gmail.com',
    'password': 'angelo090520'

}

#post data
#Database Name/Table Name
firebase.post('opticheck-62567-default-rtdb/Users', data)
#Because async is keyword in python

#get data
result = firebase.post('opticheck-62567-default-rtdb/Users', data)

