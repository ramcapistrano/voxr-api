import os
import base64
import time
import ConfigParser
from random import randint
from mailer import Mailer
from mailer import Message

config = ConfigParser.RawConfigParser()
config.read('/var/www/html/python/env.cfg')


def get_base_url():
    base_url = config.get('URL', 'LIVE_URL')
    return base_url


def get_wav_dir():
    wav_dir = config.get('WavFile', 'WAV_PATH')
    return wav_dir


def generate_new_file_path(username, file_path):
    fp = os.path.basename(file_path)
    new_file_path = get_base_url() + get_wav_dir() + username + "/" + fp
    return new_file_path


def get_vokaturi_lib():
    vokaturi_lib = config.get('VokaturiLib', 'VOKATURI_LIB')
    return vokaturi_lib


def get_file_name(file_path):
    file_name = os.path.basename(file_path)
    return file_name


def upload_wav_file(file_data, username):
    timestamp = int(time.time())
    new_file_name = str(timestamp) + ".wav"
    file_wd = create_user_directory(username)
    new_wd = file_wd + '/' + new_file_name

    # create a writable image and write the decoding result
    wav_64_decode = base64.decodestring(file_data)
    wav_result = open(new_wd, 'wb')
    wav_result.write(wav_64_decode)
    return new_wd


def create_user_directory(username):
    cwd = os.getcwd()
    print cwd + 'app/static/wav_files/'
    new_wd = '/var/www/html/python/app/static/wav_files/' + username
    exist = os.path.isdir(new_wd)
    if exist is True:
        return new_wd
    else:
	print new_wd
        os.makedirs(new_wd)
        return new_wd


def generate_random_number(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def get_mail_username():
    usr = config.get('Gmail', 'USERNAME')
    return usr


def get_mail_password():
    pwd = config.get('Gmail', 'PASSWORD')
    return pwd


def generate_email_code(first_name, receiver):
    sender = get_mail_username()
    pwd = get_mail_password()
    generated_code = generate_random_number(4)

    message = Message(From=sender, To=receiver)
    message.Subject = "Password Reset"
    message.Html = """Dear """ + first_name + """,<br><br>
           Here is your verification code to reset your account password:<br>
           <b>""" + str(generated_code) + """</b><br><br>
           Best Regards,<br>Voxr App Team"""

    sender = Mailer('smtp.gmail.com', port=587, use_tls=True, usr=sender, pwd=pwd)
    sender.send(message)

    return generated_code

