import json
from app import app
from flask import render_template, redirect, request, url_for, flash


FLASH_SUCCES_MESSAGE = 'Сообщение отправлено'


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/send', methods=['POST'])
def sending_email():
    """ Контроллер контактной формы на сайте """
    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        form_data_writer(email=email, subject=subject, message=message)

        flash(FLASH_SUCCES_MESSAGE)

        return redirect(url_for('index') + '#contact')


def form_data_writer(email: str, subject: str, message: str) -> None:
    """ Запись данных формы в файл """
    with open('form_data.json', 'a') as file:
        data = {
            'Email': email,
            'Subject': subject,
            'Message': message,
        }
        json.dump(data, file, indent=4, ensure_ascii=False)
        
