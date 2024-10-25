from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Data biodata yang akan ditampilkan
    members = [
        {
            'name': 'Khoirul Umar Rizki',
            'nim': '22.83.0902',
            'education': 'Amikom Yogyakarta',
            'about': 'Mahasiswa biasa.',
            'image': 'profile1.jpg'
        },
        {
            'name': 'Jesen Tanamas',
            'nim': '22.83.0920',
            'education': 'Amikom Yogyakarta',
            'about': 'Mahasiswa keturunan China dari Bangka',
            'image': 'profile2.jpg'
        },
        {
            'name': 'Bayu Rosdianko Kurniawan',
            'nim': '22.83.0945',
            'education': 'Amikom Yogyakarta',
            'about': 'Ketua orma.',
            'image': 'profile3.jpg'
        }
    ]
    return render_template('index.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)
