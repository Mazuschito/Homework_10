import json
from flask import Flask

app = Flask(__name__)


def json_load():
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
    return candidates


@app.route("/")
def index():
    page = ""
    for candidate in json_load():
        page += 'Имя кандидата - ' + candidate['name'] + '\n'
        page += "Позиция кандидата - " + candidate["position"] + "\n"
        page += "Навыки через запятую - " + candidate["skills"] + "\n"
        page += "\n"
    return f"<pre>{page} <pre>"


@app.route("/candidates/<name>")
def candidates(name):
    page = ""
    for candidate in json_load():
        if name == candidate['name']:
            link = candidate['picture']
            page += 'Имя кандидата - ' + candidate['name'] + '\n'
            page += "Позиция кандидата - " + candidate["position"] + "\n"
            page += "Навыки через запятую - " + candidate["skills"] + "\n"
    return f"<Img src='{link}' Width='200' Height='150'> <pre>{page} <pre>"


@app.route("/skills/<skill>")
def skills(skill):
    page = ""
    for candidate in json_load():
        lower_string = candidate["skills"].lower()
        skills_list = lower_string.split(", ")
        if skill in skills_list:
            page += 'Имя кандидата - ' + candidate['name'] + '\n'
            page += "Позиция кандидата - " + candidate["position"] + "\n"
            page += "Навыки через запятую - " + candidate["skills"] + "\n"
            page += "\n"
    return f"<pre>{page} <pre>"


if __name__ == "__main__":
    app.run()
