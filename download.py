#######################
# video_download 
#######################

import pyrebase
#파이어베이스 연결을 위한 환경설정
config ={
    "apiKey": "AIzaSyCeBKEfSHlTVHojwDJmPOyXkSPA8XgVIu4",
    "authDomain": "videoex-52fd4.firebaseapp.com",
    "databaseURL": "https://videoex-52fd4.firebaseio.com",
    "projectId": "videoex-52fd4",
    "storageBucket": "videoex-52fd4.appspot.com",
    "messagingSenderId": "804606110787",
    "appId": "1:804606110787:web:1513ec0deff69ee1e5f8f6"
}
#firebase config of app initialize
firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

#db에 연결
db = firebase.database()
#userlist내의 정보를 받아옴
company = db.child("UserList").get()
# company.val()['email']
dict = {}

dict = company.val()
print(dict.keys())

for i in dict.keys():
    print(dict[i])
    if i =='0102345679':#동영상을 다운 받을 조건을 설정
        storage.child("videos/"+"2020-09-22 17:24:330102345679").download("./videos/"+i+".mp4")
        


