from flask import Flask, redirect, render_template, url_for, request, flash, session
from DB_handler import DBModule #백엔드에서 처리해주는 파일이고, 데이터베이스와 연동되는 py파일
#from learn import learn

app = Flask(__name__)

DB = DBModule()
app.secret_key = "adminmaster"


@app.route("/")
def index():
#세션 uid를 html에서 사용할 수 있도록 변수에 넣어준다.
    if "uid" in session:
        user = session["uid"]
    else:
        user = "주소가 입력되지 않았습니다."
    return render_template("index.html", user=user)



################
@app.route("/csv")
def csv():
   # return render_template("d.html")
    return render_template("mokposobang.html")
#############


###########################################################################

    

    
@app.route("/fire_2016")
def fire_2016():
    return render_template("test.html")
######################################################

    



#html의 돌아가기 버튼을 구현하였다
@app.route("/logout")
def logout():
    if "uid" in session:
        session.pop("uid")
        return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))


#html의 주소 검색창을 구현하였다
@app.route("/login")
def login():
    if "uid" in session:
        return redirect(url_for("index"))
    return render_template("login.html")



#검색한 주소가 데이터베이스 안에 있는지 검증한다.
#검증하는 이유는 머신러닝으로 넘기기전, 사용할 수 있는 주소데이터인지 확인하기 위함.
@app.route("/login_done", methods=["get"])
def login_done():
    uid = request.args.get("id") #html에서 입력창을 통해"id"를 받아온다(읍면동)
    if DB.login(uid): #db모듈의 login섹터 참조
        #DBpy의 로그인함수에 uid를 넣는다.
        session["uid"] = uid
        return redirect(url_for("index"))
    else:
        flash("존재하지 않는 주소입니다.")
        logout()
        return redirect(url_for("index"))

    
    
    
#@app.route("/kakao", methods=["get"])
#def kakao():
    #html to flask
 #   uid = request.args.get("id")
    #flask to html
  #  return render_template('kakao.html', "name"=uid)

    
    
@app.route("/signin")
def signin():
    return render_template("signin.html")


@app.route("/signin_done", methods=["get"])
def signin_done():
    uid = request.args.get("id")
 #   pwd = request.args.get("pwd")
    # signin에서 넣은 정보가 여기로 온다.
    # 데이터베이스로 이제 넘겨줘야 함
   # if DB.signin(_id_=uid, pwd=pwd): #등록된 읍면동을 검색 했다면
    if DB.signin(uid):
        return redirect(url_for("index")) #해당 읍면동으로 보내야하는데 아직 데이터 없어서 인덱스로 보냄
    else:
        flash("이미 존재하는 아이디입니다")
        return redirect(url_for("signin")) #검색한 읍면동의 정보가 없을때 사인인으로 보냄


# return redirect(url_for("index"))  #데이터가 왔는지 확인하는 코드. 오류나서 검증할때 사용


@app.route("/write")
def write():
    if "uid" in session:
        return render_template("write_post.html")
    else:
        return redirect(url_for("login"))



@app.route("/write_done", methods = ["get"])
def write_done():
    title = request.args.get("title")
    contents = request.args.get("contents")
    uid = session.get("uid")
    DB.write_post(title, contents, uid)
    return redirect(url_for("index"))




@app.route("/post/<string:pid>")
def post(pid):
    post = DB.post_detail(pid)
    return render_template("post_detail.html", post=post)


@app.route("/list")
def post_list():
    post_list = DB.post_list()
    if post_list == None:
        length = 0
    else:
        length = len(post_list)
    return render_template("post_list.html", post_list=post_list.items(), length=length)



@app.route("/user/<string:uid>")
def user_posts(uid):
    u_post = DB.get_user(uid)
    if u_post == None:
        length = 0
    else:
        length = len(u_post)
    return render_template("user_detail.html", post_list = u_post, length = length, uid=uid)


@app.route("/firefight/<string:uid>")
def firefight(uid):
    uid = session.get("uid")
    userinfo = DB.firefight(uid)
    try:
        
        if userinfo == "목포소방":
            return render_template("mokposobang.html")
        if userinfo == "연산":
            return render_template("yeonsan.html")
        if userinfo == "호남":
            return render_template("honam.html")
        if userinfo == "삼학":
            return render_template("samhak.html")
        if userinfo == "경동":
            return render_template("gyeongdong.html")
        if userinfo == None:
            flash("주소를 입력하지 않았거나 해당 주소의 데이터가 없습니다!")
        return redirect(url_for("index"))
    except:
        flash("주소를 입력하지 않았거나 해당 주소의 데이터가 없습니다!")
        return redirect(url_for("index"))




if __name__=="__main__":
    app.run(host='0.0.0.0', debug=False)

    

    
    
    
    
