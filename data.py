from flask import Flask,jsonify,request
import csv
all_score_data=[]
with open("movies.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_score_data=data[1:]
    
liked_score=[]
not_liked_score=[]
did_not_score=[]

app=Flask(__name__)
@app.route("/get-score")
def get_score():
    return jsonify({
        "data":all_score_data[0],
        "status":"success"
    }),201
    
@app.route("/liked-score",methods=["POST"])
def liked_score():
    score=all_score_data[0]
    all_score_data = all_score_data[1:]
    liked_score.append(score)
    return jsonify({
        "status":"success"
    }),201
    
@app.route("/not-liked-score",methods=["POST"])
def not_liked_score():
    score=all_score_data[0]
    all_score_data=all_score_data[1:]
    not_liked_score.append(score)
    return jsonify({
        "status":"success"
    }),201

@app.route("/did-not-score",methods=["POST"])
def did_not_score():
    score=all_score_data[0]
    all_score_data=all_score_data[1:]
    did_not_score.append(score)
    return jsonify({
        "status":"success"
    }),201
    
if __name__ == "__main__":
    app.run()