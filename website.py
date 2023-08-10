from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_url_path='', static_folder='static')

#barev dzez

ifloggedin = False
currentLogin = " "
username = " "
passwordsDic= { }
skillsDic = { }
#testSkills=[]
#adminSkills=[]
#userSkills=[]

@app.route('/')
def index():
     global ifloggedin
     if ifloggedin:
          return redirect('/profile')
     else:
          return render_template('login.html')

@app.route('/signup')
def getSignup():
          return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def postSignup():
    global ifloggedin
    global passwordsDic
    global currentLogin

    userSignup = request.form['username']
    userPass = request.form['password']

    if userSignup in passwordsDic:
         return render_template("signup.html", error_message1="Username already in use")
    else:
         passwordsDic[userSignup] = userPass
         ifloggedin = True
         currentLogin = userSignup
         skillsDic[currentLogin] = []
         return render_template("profile.html", username=currentLogin)

@app.route('/login')
def getLogin():
          return render_template('login.html')

@app.route('/login', methods=['POST'])
def postLogin():
    global ifloggedin
    global currentLogin
    userLogin = request.form['login']
    userPass = request.form['password']

    if userLogin in passwordsDic and passwordsDic[userLogin] == userPass:
        ifloggedin = True
        currentLogin = userLogin
        return redirect('/profile')
    else:
        return render_template("login.html", error_message="Duq mutqagrel eq sxal gaxtnabar kam nman account arka che")
    
@app.route('/profile')
def profile():
    global ifloggedin
    global currentLogin
    if not ifloggedin:
        return redirect('/')
    else:
        skillsDic[currentLogin] = [skills]
        return render_template('profile.html', username=currentLogin, skills=skills) 
       

@app.route('/addSkill', methods=['POST'])
def addSkill():
    global currentLogin
    skill = request.form['skill']
    s = skillsDic[currentLogin]
    s.append(skill)
    return redirect('/profile')

@app.route('/logout', methods=['POST'])
def logout():
    global ifloggedin

    ifloggedin = False
    return redirect('/')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80)
