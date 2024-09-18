from flask import Flask, render_template

app = Flask(__name__)

#ホーム画面
@app.route("/home", methods=['GET'])
def home():
    return render_template("home.html")

#ファイルデータ(pdf,csv)登録画面
@app.route("/home/filedata_register", methods=['GET'])
def filedata_register():
    return render_template("filedata_register.html")

#学生情報一覧画面
@app.route("/home/all_student", methods=['GET'])
def all_student():
    return render_template("all_student.html")

#学生情報(手動入力)登録画面
@app.route("/home/all_student/add_student", methods=['GET'])
def add_student():
    return render_template("add_student.html")

#学生情報更新画面
@app.route("/home/all_student/update_student", methods=['GET'])
def update_student():
    return render_template("update_student.html")

#学生プロフィール画面
@app.route("/home/detail_student", methods=['GET'])
def all_student():
    return render_template("detail_student.html")

#テスト結果一覧画面
@app.route("/home/all_testresult", methods=['GET'])
def all_testresult():
    return render_template("all_testresult.html")

#テスト結果(手動入力)登録画面
@app.route("/home/all_testresult/add_testresult", methods=['GET'])
def add_testresult():
    return render_template("add_testresult.html")

#テスト結果更新画面
@app.route("/home/all_testresult/update_testresult", methods=['GET'])
def update_testresult():
    return render_template("update_testresult.html")

#テスト結果詳細画面
@app.route("/home/all_testresult/detail_testresult", methods=['GET'])
def detail_testresult():
    return render_template("detail_testresult.html")

#テスト過去問一覧画面
@app.route("/home/all_pasttest", methods=['GET'])
def all_pasttest():
    return render_template("all_pasttest.html")

#テスト過去問詳細画面
@app.route("/home/all_pasttest/detail_pasttest", methods=['GET'])
def detail_pasttest():
    return render_template("detail_pasttest.html")

#学習教材一覧画面
@app.route("/home/all_learningtext", methods=['GET'])
def all_learningtext():
    return render_template("all_learningtext.html")

#学習教材詳細画面
@app.route("/home/all_pasttest/detail_learningtext", methods=['GET'])
def detail_learningtext():
    return render_template("detail_learningtext.html")

#レポート一覧画面
@app.route("/home/all_report", methods=['GET'])
def all_report():
    return render_template("all_report.html")

#レポート作成画面
@app.route("/home/all_report/add_report", methods=['GET'])
def add_report():
    return render_template("add_report.html")

#レポート詳細画面
@app.route("/home/all_report/detail_report", methods=['GET'])
def detail_report():
    return render_template("detail_report.html")

#レポート更新画面
@app.route("/home/all_report/update_report", methods=['GET'])
def update_report():
    return render_template("update_report.html")


if __name__=="__main__":
    app.run()