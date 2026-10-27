from flask import Flask, jsonify

app = Flask(__name__)

# 新增一个接口，返回 JSON 数据
@app.route('/api/user')
def get_user_info():
    # 这是一个 Python 字典
    user_data = {
        "name": "杨东杰",
        "role": "Python后端开发助理",
        "skills": ["Python", "Flask", "HTML/CSS"],
        "is_learning": True
    }
    # 使用 jsonify 把 Python 字典转换成浏览器认识的 JSON 格式
    return jsonify(user_data)

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)