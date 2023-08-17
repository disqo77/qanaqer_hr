from flask import Flask, render_template, request, redirect

class User:
     def __init__(self, username, password, isAdmin, skills):
          self.username = username
          self.password = password
          self.isAdmin = isAdmin
          self.skills = skills

app = Flask(__name__, static_url_path='', static_folder='static')

currentUser = None
userDic = { 'admin': User('admin', 'admin', True, []), 'test': User('test', 'test', True, []) }


@app.route('/')
def index():
     if currentUser != None:
          return redirect('/profile')
     else:
          return render_template('login.html')

@app.route('/signup')
def getSignup():
          return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def postSignup():
    global currentUser
    global userDic
    username = request.form['username']
    password = request.form['password']

    if username in userDic:
         return render_template("signup.html", error_message1="Username already in use")
    else:
         newUser = User(username, password, False, [])
         currentUser = newUser
         userDic[username] = newUser
         return render_template("profile.html", username=username, password=password)

@app.route('/login')
def getLogin():
          return render_template('login.html')

@app.route('/login', methods=['POST'])
def postLogin():
    global currentUser
    global userDic
    username = request.form['login']
    password = request.form['password']

    if username in userDic and userDic[username].password == password:
        return redirect('/profile')
    else:
        return render_template("login.html", error_message="Duq mutqagrel eq sxal gaxtnabar kam nman account arka che")
    
@app.route('/profile')
def profile():
    global currentUser
    global userDic
    if currentUser == None:
        return redirect('/')
    else:
        return render_template('profile.html', username=userDic[currentUser.username], skills = userDic[currentUser.skills]) 
       

@app.route('/addSkill', methods=['POST'])
def addSkill():
    global currentUser
    global userDic
    currentUser = User(username, password, False, [])
    skill = request.form['skill']
    s = userDic[currentUser.skills]
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

@app.route('/logout', methods=['POST'])
def logout():
    global currentUser
    global userDic
    currentUser = None
    return redirect('/')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80)
