from flask import Flask
from routes.home import home_route
from routes.ganhos import ganhos_route
from routes.despesas import despesas_route
from routes.login import login_route

app=Flask(__name__); 
app.secret_key = 'your_secret_key'  
app.register_blueprint(home_route)
app.register_blueprint(ganhos_route, url_prefix='/ganhos')
app.register_blueprint(despesas_route, url_prefix='/despesas')
app.register_blueprint(login_route, url_prefix='/login')


app.run(debug=True)