from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_url_path='', static_folder='static')

ifloggedin = False
currentLogin = " "
username = " "
currentPass = " "
passwordsDic= { }
skillsDic = { }


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
    global skillsDic
    global currentLogin
    global currentPass

    userSignup = request.form['username']
    userPass = request.form['password']

    if userSignup in passwordsDic:
         return render_template("signup.html", error_message1="Username already in use")
    else:
         passwordsDic[userSignup] = userPass
         ifloggedin = True
         currentLogin = userSignup
         currentPass = userPass
         skillsDic[currentLogin] = []
         return render_template("profile.html", username=currentLogin, password=userPass)

@app.route('/login')
def getLogin():
          return render_template('login.html')

@app.route('/login', methods=['POST'])
def postLogin():
    global ifloggedin
    global currentLogin
    global currentPass
    userLogin = request.form['login']
    userPass = request.form['password']

    if userLogin in passwordsDic and passwordsDic[userLogin] == userPass:
        ifloggedin = True
        currentLogin = userLogin
        currentPass = userPass
        return redirect('/profile')
    else:
        return render_template("login.html", error_message="Duq mutqagrel eq sxal gaxtnabar kam nman account arka che")
    
@app.route('/profile')
def profile():
    global ifloggedin
    global skillsDic
    global currentLogin
    if not ifloggedin:
        return redirect('/')
    else:
        return render_template('profile.html', username=currentLogin, skills = skillsDic[currentLogin]) 
       

@app.route('/addSkill', methods=['POST'])
def addSkill():
    global currentLogin
    global skillsDic
    skill = request.form['skill']
    s = skillsDic[currentLogin]
    s.append(skill)
    return redirect('/profile')

@app.route('/settings')
def getsettings():
          return render_template('settings.html')

@app.route('/settings', methods=['POST'])
def settings():
    global currentLogin
    global skillsDic
    global passwordsDic
    
    return redirect('/settings')

@app.route('/passreset', methods=['POST'])
def passreset():
    global currentLogin
    global skillsDic
    global passwordsDic
    global currentPass
    currpass = request.form['currpass']
    newpass = request.form['newpass']
    confnewpass = request.form['confnewpass']
    if passwordsDic[currentLogin] == currpass and newpass == confnewpass and currpass != newpass:
         passwordsDic[currentLogin] = confnewpass
         return render_template('settings.html', pass_message= "Password changed succesfully")
    else:
         return render_template('settings.html', passerror_message= "Please retry") 

@app.route('/back', methods=['POST'])
def back():
     return redirect('/profile')

@app.route('/logout', methods=['POST'])
def logout():
    global ifloggedin

    ifloggedin = False
    return redirect('/')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80)
