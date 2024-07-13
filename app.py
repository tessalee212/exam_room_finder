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
    # Use the room_data_text defined in another cell
    global room_data_text  # Ensure this variable is accessible in this cell
    uniqname = input("Enter the uniqname to find: ")

    room_data = []

    lines = room_data_text.strip().split('\n')

    # Iterate through lines in pairs (name/start and end)
    for i in range(0, len(lines), 2):
        if i + 1 < len(lines):  # Ensure there's a corresponding end line
            r_name = lines[i].strip()
            u_start, u_end = lines[i + 1].strip().split(' - ')
            room_data.append(Room(r_name, u_start, u_end))
  
    uniqname = make_uppercase(uniqname)

    for room in room_data:
        if uniqname >= room.uniq_start and uniqname <= room.uniq_end:
            print(room.room_name) 
            return

    print("No room found for the given uniqname")

if __name__ == '__main__':
    app.run(debug=True)
