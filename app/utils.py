import os
import base64
import time
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('env.cfg')


def get_base_url():
    base_url = config.get('URL', 'LOCAL_URL')
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
    new_wd = file_wd + '\\' + new_file_name

    # create a writable image and write the decoding result
    wav_64_decode = base64.decodestring(file_data)
    wav_result = open(new_wd, 'wb')
    wav_result.write(wav_64_decode)
    return new_wd


def create_user_directory(username):
    cwd = os.getcwd()
    new_wd = cwd + '\\app\\static\\wav_files\\' + username
    exist = os.path.isdir(new_wd)
    if exist is True:
        return new_wd
    else:
        os.makedirs(new_wd)
        return new_wd
