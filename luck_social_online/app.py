from flask import Flask
app=Flask(__name__)
@app.route('/')
def ok(): return 'Luck online'
if __name__=='__main__': app.run()
