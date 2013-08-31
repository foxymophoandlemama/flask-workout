from views import app
from database import init_db

app.run(debug=True)
init_db()