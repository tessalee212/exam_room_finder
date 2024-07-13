from flask import Flask, render_template, request

app = Flask(__name__)

class Room:
    def __init__(self, room_name, uniq_start, uniq_end):
        self.room_name = room_name
        self.uniq_start = uniq_start
        self.uniq_end = uniq_end

def make_uppercase(lowercase):
    return lowercase.upper()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # get data from html 
    room_data_text = request.form['room_data_text']
    uniqname = request.form['uniqname']

    room_data = []

    # Your Python processing logic here
    lines = room_data_text.strip().split('\n')
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 4:
            r_name, u_start, _, u_end = parts
            room_data.append(Room(r_name, u_start, u_end))

    uniqname = make_uppercase(uniqname)

    for room in room_data:
        if uniqname >= room.uniq_start and uniqname <= room.uniq_end:
            return f"Room found: {room.room_name}"

    return "No room found for the given uniqname"


if __name__ == '__main__':
    app.run(debug=True)
