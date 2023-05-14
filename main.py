from flask import Flask
from get_month_listeners import get_month_listeners

app = Flask(__name__)


@app.route('/artist/<artistId>')
def month_listeners(artistId):
    
    month_listeners = get_month_listeners(artistId)
    print(month_listeners)
    response = {
        "artistId": artistId, 
        "monthListeners": month_listeners["listeners"],
        "artistName": month_listeners["artistName"],
        "artistImage": month_listeners["artistImage"]
    }
    
    return response

if __name__ == '__main__':
    app.run()