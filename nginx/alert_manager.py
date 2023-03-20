import smtplib
import sys

def send_email(sender_email, sender_password, receiver_email, message):
    try:
        # Set up SMTP connection
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        # Create message object
        subject = 'Test email'
        body = message
        msg = f'Subject: {subject}\n\n{body}'

        # Send message
        smtp_server.sendmail(sender_email, receiver_email, msg)
        print('Email sent successfully!')

    except Exception as e:
        print(f'Error: {e}')
    
    finally:
        # Close SMTP connection
        smtp_server.quit()

# Replace the following values with your own information
sender_email = 'sender@gmail.com'
sender_password = 'APP_PASSWORD'
receiver_email = 'reciver@example.com'
message = 'This is a test Fuck you Bitch.'

def send_telegram(message):
    pass

if __name__ == "__main__":
    msg = sys.stdin.readline()
    if msg.__contains__("505"):
        send_email(sender_email, sender_password, receiver_email, msg)
    elif msg.__contains__('404'):
        send_telegram(msg)
