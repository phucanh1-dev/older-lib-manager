from flask import redirect, request, url_for
from model.sinhvien_model import getsinhvien

def listsinhvien():
    listsinhviens = getsinhvien()
    return listsinhviens

