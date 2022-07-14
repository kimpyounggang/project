import pyrebase
import json
import uuid

class DBModule:
    def __init__(self):
        with open("./auth/firebaseAuth.json") as f:
            config = json.load(f)

        firebase = pyrebase.initialize_app(config)
        # 파이어베이스 시작
        self.db = firebase.database()
        # 파이어베이스와 db핸들러를 연결



    def login(self, uid): #app에서 작성한 uid변수를 넣는다.
        users = self.db.child("users").get().val()
        #DB에서 "users"의 정보를 얻어와 users 에 넣는다(리스트임)
        try:
            userinfo = users[uid]
            #users의 리스트중 유저가 입력한uid가 있는지 확인한다.
            if userinfo["uid"] == uid:
                return True
            else:
                return False
        except:
            return False


    def signin_verification(self, uid):  # uid = 유저가 적은 정보
        users = self.db.child("users").get().val()
        print(users)

    # 해당 코드는 데이터베이스에 정보를 넣는 코드
    def signin(self, _id_):
        infomation = {
            "uid":_id_
        }
        self.signin_verification(_id_)
        self.db.child("users").child(_id_).set(infomation)
           

#        if self.signin_verification(_id_):
 #           self.db.child("users").child(_id_).set(infomation)
  #          return True
   #     else:
    #        return False


    def write_post(self, title, contents, uid):
        pid = str(uuid.uuid4())[:12]
        information = {
            "title":title,
            "contents":contents,
            "id":uid
        }
        self.db.child("posts").child(pid).set(information)


    def post_list(self):
        post_lists = self.db.child("posts").get().val()
        return post_lists

    def post_detail(self, pid):
        post = self.db.child("posts").get().val()[pid]
        return post



    def get_user(self, uid):
        post_list = []
        user_post = self.db.child("posts").get().val()
        for post in user_post.items():
            if post[1]["id"] == uid:
                #리스트로된 db의 데이터에서, post의 리스트1번항목 즉 id항목이
                #uid와 같을경우 postlist(리스트)의 마지막에 post를 추가해준다.
                post_list.append(post)
        return post_list

    def firefight(self, uid):  # uid = 유저가 적은 정보
        firewhich = self.db.child("users").child(uid).child("which").get().val()
        #DB에서 "users.uid.which"의 정보를 얻어와 users 에 넣는다(리스트임)
        userinfo = firewhich
            #firewhich의 리스트중 which에 따라 다른 결과값을 출력한다.
        return firewhich

## if self.db.child(_id_).set(infomation): 임시저장

  ##      information = { }
   ##     if self.signin_verification(_id_):
    ##       return True
        # self.db.child(사용자가 적는정보-html변수명을 넣음-).set(information) #데이터베이스에 정보를 넣음
      #  else:
       #    return False #(데이터베이스에 있다)


