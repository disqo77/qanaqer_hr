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
         userDic[username] = newUser
         currentUser = userDic[username]
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
        currentUser = userDic[username]
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
        return render_template('profile.html', username=currentUser.username, skills = currentUser.skills) 
       

@app.route('/addSkill', methods=['POST'])
def addSkill():
    global currentUser
    global userDic
    skill = request.form['skill']
    s = currentUser.skills
    s.append(skill)
    return redirect('/profile')

@app.route('/settings')
def getsettings():
          return render_template('settings.html')

@app.route('/settings', methods=['POST'])
def settings():
    global currentUser
    global userDic
    return redirect('/settings')

@app.route('/passreset', methods=['POST'])
def passreset():
    global currentUser
    global userDic
    currpass = request.form['currpass']
    newpass = request.form['newpass']
    confnewpass = request.form['confnewpass']
    if currentUser.password == currpass and newpass == confnewpass and currpass != newpass:
         currentUser.password = confnewpass
         return render_template('settings.html', pass_message= "Password changed succesfully")
    else:
         return render_template('settings.html', passerror_message= "Please retry") 
    
app.route('/admin')
def getadmmin():
     if currentUser.isAdmin == True:
          return redirect('/admin')
     else:
          return redirect('/profile')

app.route('/admin', methods=['POST'])
def admmin():
    global currentUser
    global userDic
    currusername = request.form['currusername']
    currpass = request.form['currpass']
    newpass = request.form['newpass']
    confnewpass = request.form['confnewpass']
    if currentUser.isAdmin == True:
         return render_template('admin.html', pass_message= "Password changed succesfully")
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
