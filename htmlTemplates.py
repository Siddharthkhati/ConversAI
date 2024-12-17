css = '''
<style>
body {
    background: linear-gradient(to bottom right, #0f0f1a, #1c1c2e);
    color: #dcdcdc; /* Light gray font color */
}
.chat-container {
    background-color: #161625; 
    padding: 1rem;
    border-radius: 10px;
}
.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex; 
    align-items: center;
}
.chat-message.user {
    background-color: #252542; 
    color: #fff;
}
.chat-message.bot {
    background-color: #fff;
}
.chat-message.bot .message {
    color: #454580; 
}
.chat-message .avatar {
    width: 10%; 
    margin-right: 1rem;
}
.chat-message .avatar img {
    max-width: 50px;
    max-height: 50px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: 90%;
    font-family: Arial, sans-serif; 
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://thumbs.dreamstime.com/b/chatbot-red-speech-bubble-concept-ui-media-soft-dialogue-script-popup-spam-profile-software-communication-contact-flat-style-104052623.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://media.istockphoto.com/id/1445426863/vector/chat-bot-vector-logo-design-concept.jpg?s=612x612&w=0&k=20&c=XDdfzS4lNW9yxQ0BQGZq9KMLL4bJ8ywXlYdAhBSuoCA=">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
