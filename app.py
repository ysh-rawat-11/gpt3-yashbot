from flask import Flask, request, session
from twilio.twiml.messaing_response import MessagingResponse
from jabebot import ask, append_interaction_to_chat_log

app = Flask(_name_)
app.config['SECRET_KEY']= '89djhf9lhkd93'

@app.route('/bot',method = ['POST'])
def HE():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg,chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg,answer,chat_log)

    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)

if __name__ == '__main__':
    app.run(debug = true)