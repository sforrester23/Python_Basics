## Stupid School Teacher
#Create a program to have a conversation with your teacher. This is how he reacts to your responses
# if you responde to your school teacher:
    # Go back to school!
# if you ask a questions
    # HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!
# if your respond with something ending with !
    # YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!
# if your response is 'I'm a doctor'
    # WELLL DONE! YOU can now talk to me
    # Exits


while True:
    response = input('What do you have to say to me, insolent pupil? ').lower().capitalize()
    if '?' in response:
        print('HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!')
    elif '!' in response:
        print('YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!')
    elif response == 'I\'m a doctor':
        print('WELLL DONE! YOU can now talk to me.')
        break
    else:
        print('Go back to school!')