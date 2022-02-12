from asyncio import tasks
from distutils.log import debug
from flask import Flask,jsonify,request
app=Flask(__name__)

tasks=[
    {
        'id': 1, 
        'name': u'Raju', 
        'contacts': u'9987644456',
        'done': False
    },
    {
        'id': 2, 
        'name': u'Rahul', 
        'contacts': u'9876543222',
        'done': False
    }
    ]

@app.route('/add-data',methods=["POST"])
def add_task():
    if not request.json:
        return jsonify
        ({
        "status":"error",
        "message":"please provide data"
    },400)

    task={
        'id': tasks[-1]['id']+1, 
        'name': request.json['name'], 
        'contacts': request.json.get('contacts',""), 
        'done': False
    }

    tasks.append(task)
    return jsonify({
            "status":"success",
            "message":"task added successfully"
        })

@app.route('/get-data')
def get_task():
    return jsonify({
        "data":tasks
    })
    

if (__name__=='__main__'):
    app.run(debug=True)
    #hyper text transfer protocol(http)