from flask import Flask, render_template, request, url_for
import qrcode
import random


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def main():
    # The below code works if form in index.html called 
    if request.method == 'POST':
        string = request.form['string'] #The input is named as string in index.html
        code_name = str(string) 
        QR_code = qrcode.make(code_name)
        code_file_name = str(random.randint(10000,99999)) + '.png' #file name will be a random number from 10000 to 99999 save in .png format 
        file_path = 'static/qrcodes/' + code_file_name
        QR_code.save(file_path) # saves the qrcode image file in 'static/qrcode/filename.png' file path
        url_path = 'qrcodes/' + code_file_name

        url = url_for('static',filename=url_path)
        return render_template('index.html', image_url=url)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
