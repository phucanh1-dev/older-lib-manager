from flask import redirect, request, url_for
from model.tacgia_model import gettacgia

def listtacgia():
    listtacgias = gettacgia()
    return listtacgias

