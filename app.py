from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


# Configurazioni per invio Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)


@app.route('/')
def homePage():
    return render_template('homePage.html')


@app.route('/scenario')
def scenario():
    return render_template('scenario.html')


@app.route('/prodotto')
def prodotto():
    return render_template('prodotto.html')


@app.route('/sicurezza')
def sicurezza():
    return render_template('sicurezza.html')


@app.route('/benefici')
def benefici():
    return render_template('benefici.html')


# Rotta per invio email
@app.route('/invia-richiesta', methods=['POST'])
def invia_richiesta():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email_utente = request.form.get('email')
        azienda = request.form.get('azienda')
        
        
        # EMAIL PER ADMIN
        msg_admin = Message(
            subject = f"EVENTIZE: Nuova richiesta Demo da {azienda}",
            
            recipients = [os.getenv('MAIL_RECIPIENT')],
            
            reply_to = email_utente,
            
            html = render_template('emails/adminNotification.html', nome = nome, email = email_utente, azienda = azienda)
        )
        
        
        # EMAIL DI CONFERMA PER CLIENTE
        msg_user = Message(
            subject = "Abbiamo ricevuto la tua richiesta - Eventize",
            
            recipients = [email_utente],
            
            html = render_template('emails/userConfirmation.html', nome = nome, azienda = azienda)
        )
        
        
        try:
            mail.send(msg_admin)
            mail.send(msg_user)
            flash('Richiesta inviata con successo | Controlla la tua email.', 'success')
        except Exception as e:
            flash(f"Errore nell'invio: {str(e)}", 'error')
            
        return redirect(request.referrer)


if __name__ == '__main__':
    app.run(debug = True)