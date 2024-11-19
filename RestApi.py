from flask import Flask, request, jsonify 
import json 

app=Flask(__name__)

def load_config():
    with open ('config,json','r') as file:
        return json.load(file)

        config= load_config()

        @app.route('/info', methods=['GET'])
        def get_info():
            lang = request.args.get('lang', 'em')
            return jsonify(response)

            if __name__=='__main__':
                app.rum(debug=True)