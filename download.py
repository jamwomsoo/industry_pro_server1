#######################
# video_download 
#######################



import pyrebase
from firebase import firebase

# Import database module.
from firebase_admin import db



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

#firebase_update = firebase.firebasApplication("https://videoex-52fd4.firebaseio.com/",None)


dict = {}

dict = company.val()

for i in range(len(dict)):#list(dict.values()):
    print(i)
    print(list(dict.values())[i]['approval'])
    print(list(dict.keys())[i])
    if list(dict.values())[i]['approval'] == 'T':#동영상을 다운 받을 조건을 설정
        #수정할 부분
        storage.child("videos/"+list(dict.keys())[i]).download("./videos/"+list(dict.keys())[i]+".mp4")
        #동영상 받아주고 승인여부를 T로 바꿔줌.....//이 부분을 학습 후에 적용해야 할 듯? 
        db.child("UserList").child(list(dict.keys())[i]).update({'approval':'F'})
        
        


