# main.py

from flask import Flask, flash, render_template, request, send_from_directory, redirect, url_for
from controllers.sach_controller import listsach
from controllers.tacgia_controller import listtacgia
from controllers.sinhvien_controller import listsinhvien
from controllers.loaisach_controller import listloaisach
from model.loaisach_model import sua_loai_sach, them_loai_sach, xoa_loai_sach

app = Flask(__name__)
app.secret_key = 'your_unique_secret_key_here'
@app.route('/')
def index():
    return render_template('trangchu.html')

@app.route('/home')
def home():
    return render_template('trangchu.html')

@app.route('/quanlysach')
def quanlysach():
    sachs = listsach()
    return render_template('sach.html', sachs=sachs)

@app.route('/quanlysinhvien')
def quanlysinhvien():
    sinhviens = listsinhvien()
    return render_template('quanlysinhvien.html', sinhviens=sinhviens)

@app.route('/quanlymuontrasach')
def quanlymuontrasach():
    return render_template('quanlymuontrasach.html')

@app.route('/quanlynhanvien')
def quanlynhanvien():
    return render_template('quanlynhanvien.html')

@app.route('/baocaothongke')
def baocaothongke():
    return render_template('baocaothongke.html')

@app.route('/sach')
def sach():
    sachs = listsach()
    return render_template('sach.html', sachs=sachs)

@app.route('/loaisach')
def loaisach():
    loaisachs = listloaisach()
    return render_template('loaisach.html',  loaisachs = loaisachs)

@app.route('/tacgia')
def tacgia():
    tacgias = listtacgia()
    return render_template('tacgia.html', tacgias=tacgias)



@app.route('/themloaisach', methods=['POST'])
def them_loaisach():
    maLoai = request.form.get('maLoai')
    loaiSach = request.form.get('loaiSach')
    ghiChu = request.form.get('ghiChu')

    # Check if maLoai is empty
    if not maLoai:
        flash('Bạn vui lòng nhập mã loại sách', 'danger')
        return redirect(url_for('loaisach'))
    
    # Check if loaiSach is empty
    if not loaiSach:
        flash('Bạn vui lòng nhập tên loại sách', 'danger')
        return redirect(url_for('loaisach'))
    
    # Check for duplicate maLoai
    existing_loaisachs = listloaisach()
    if any(loaisach[0] == maLoai for loaisach in existing_loaisachs):
        flash('Mã loại sách đã tồn tại', 'danger')
        return redirect(url_for('loaisach'))

    # If all checks pass, add the new record
    them_loai_sach(maLoai, loaiSach, ghiChu)
    flash('Thêm thành công', 'success')
    return redirect(url_for('loaisach'))

@app.route('/sualoaisach', methods=['POST'])
def sua_loaisach():
    txtMaLoai = request.form.get('maLoai')
    txtLoaiSach = request.form.get('loaiSach')
    txtGhiChu = request.form.get('ghiChu')

    if not txtMaLoai:
        flash('Bạn vui lòng nhập mã loại sách', 'danger')
        return redirect(url_for('loaisach'))
    
    if not txtLoaiSach:
        flash('Bạn vui lòng nhập tên loại sách', 'danger')
        return redirect(url_for('loaisach'))

    sua_loai_sach(txtMaLoai, txtLoaiSach, txtGhiChu)
    flash('Sửa thành công', 'success')
    return redirect(url_for('loaisach'))

@app.route('/xoaloaisach/<maLoai>', methods=['POST'])
def xoa_loaisach(maLoai):
    xoa_loai_sach(maLoai)
    flash('Xóa thành công', 'success')
    return redirect(url_for('loaisach'))
    

@app.route('/anh/<filename>')
def duongdan_picture(filename):
    return send_from_directory('picture', filename)

if __name__ == '__main__':
    app.run(debug=True)
