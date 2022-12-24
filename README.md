# automated-email-sender
A python program for automatically sending email to multiple recipients
The program extracts text from two .docx files. 
The first file must contain the emails that the user wants to send the email to
The second file must contain the content of the email. The subject of the mail should be on the first line, while the the body should be on the next lines.

The repo consists of two python files: 'email_sender.py' and 'word_test.py'
'word_test' extracts information from the .docx files
'email_sender' interacts with the user and prompts the user for the name of .docx files that'll be used by 'word_test'
