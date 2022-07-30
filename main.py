import os
from flask import Flask, redirect, url_for, render_template, request, jsonify 
import pandas as pd
import json
import numpy as np
import random
import time
import datetime;
from sqlalchemy import true
from numpy import asarray
from numpy import save
from numpy import savetxt
import uuid

app = Flask(__name__)

BASE_URL = "http://127.0.0.1:5000/"

@app.route('/')
def index():
    dr = {'BASE_URL' : BASE_URL}
    return render_template('home.html', dRes=dr)

@app.route('/data-keluarga')
def data_keluarga():
    dKeluarga = []
    dataKeluarga = pd.read_excel("tbl_data_training.xlsx")
    dknp = dataKeluarga.to_numpy()
    ord = 1
    for x in dknp:
        # nama = x[1]
        kSatuan = {}
        kSatuan['nama'] = x[1]
        kSatuan['alamat'] = x[2]
        kSatuan['pekerjaan'] = x[3]
        kSatuan['penghasilan'] = x[4]
        kSatuan['pendidikan'] = x[5]
        kSatuan['luas_bangunan'] = x[6]
        kSatuan['luas_lantai'] = x[7]
        kSatuan['jenis_lantai'] = x[8]
        kSatuan['jenis_dinding'] = x[9]
        kSatuan['jenis_atap'] = x[10]
        kSatuan['jumlah_kamar'] = x[11]
        kSatuan['sumber_air_minum'] = x[12]
        kSatuan['peroleh_air_minum'] = x[13]
        kSatuan['sumber_penerangan'] = x[14]
        kSatuan['sumber_memasak'] = x[15]
        kSatuan['status_sanitasi'] = x[16]
        kSatuan['pembuangan_tinja'] = x[17]
        kSatuan['status'] = x[18]
        kSatuan['ord'] = ord
        ord += 1
        dKeluarga.append(kSatuan)

    return render_template('data-keluarga.html', dKeluarga=dKeluarga)

@app.route('/normalisasi-data')
def normalisasi_data():
    dKeluarga = []
    dataKeluarga = pd.read_excel("tbl_data_training.xlsx")
    dataKeluarga.replace({'PEKERJAAN':{'PERTANIAN':1, 'HOLTIKULTURA':2, 'PERKEBUNAN':3, 'PERIKANANTANGKAP':4, 'PERIKANANBUDIDAYA': 5, 'PETERNAKAN':6, 'KEHUTANAN':7, 'PERTAMBANGAN':8,'INDUSTRIPENGOLAHAN':9,'INDUSTRI PENGOLAHAN':9,'LISTRIK DAN GAS':10,'LISTRIKDANGAS':10, 'BANGUNAN':11, 'PERDAGANGAN':12,'HOTEL&RUMAHMAKAN':13, 'TRANSPORTASI DAN PERGUDANGAN':14, 'TRANSPORTASIDANPERGUDANGAN':14, 'INFORMASI&KOMUNIKASI':15, 'KEUANGAN&ASURANSI':16,'JASA PENDIDIKAN':17,'JASAKESEHATAN':18, 'JASAKEMASYARAKATAN':19, 'PEMULUNG':20, 'TIDAK BEKERJA':21, 'LAINNYA':21, 'TIDAKBEKERJA':21}}, inplace=True)
    dataKeluarga.replace({'PENDIDIKAN':{'SD':1, 'PAKET A':2, 'M.IBIDARIYAH':3, 'SMP':4,'SMPLB':4,'PAKET B':5, 'M.TSANAWIYAH':6, 'SMA':7,'SMK':7, 'SMALB':8, 'PAKET C':8, 'M.ALIYAH':9, 'PERGURUAN TINGGI':10,'PERGURUANTINGGI':10, 'TIDAKSEKOLAH':11, 'TIDAK SEKOLAH':11}},inplace=True)
    dknp = dataKeluarga.to_numpy()
    ord = 1
    for x in dknp:
        # nama = x[1]
        kSatuan = {}
        kSatuan['nama'] = x[1]
        kSatuan['alamat'] = x[2]
        kSatuan['pekerjaan'] = x[3]
        kSatuan['penghasilan'] = x[4]
        kSatuan['pendidikan'] = x[5]
        kSatuan['luas_bangunan'] = x[6]
        kSatuan['luas_lantai'] = x[7]
        kSatuan['jenis_lantai'] = x[8]
        kSatuan['jenis_dinding'] = x[9]
        kSatuan['jenis_atap'] = x[10]
        kSatuan['jumlah_kamar'] = x[11]
        kSatuan['sumber_air_minum'] = x[12]
        kSatuan['peroleh_air_minum'] = x[13]
        kSatuan['sumber_penerangan'] = x[14]
        kSatuan['sumber_memasak'] = x[15]
        kSatuan['status_sanitasi'] = x[16]
        kSatuan['pembuangan_tinja'] = x[17]
        kSatuan['status'] = x[18]
        kSatuan['ord'] = ord
        ord += 1
        dKeluarga.append(kSatuan)

    return render_template('data-normalisasi.html', dKeluarga=dKeluarga)

@app.route('/training-data')
def training_data():
    return render_template('training-data.html')

@app.route('/training-proses', methods=('GET', 'POST'))
def training_proses():
    detik = request.form['detik']
    data = {}
    dataKeluarga = pd.read_excel("tbl_data_training.xlsx")
    totalData = len(dataKeluarga)
    ct = datetime.datetime.now()
    ts = ct.timestamp()


    if detik == "3":
        data['status'] =  "<pre>"+ str(ct) +" -> read data from excel ...</pre>"
        data['stIn'] = "OK"
    elif detik == "5":
        data['status'] =  "<pre>"+ str(ct) +" -> create initial parameter (a) ...</pre>"
        data['stIn'] = "OK"
    elif detik == "6":
        data['status'] =  "<pre>"+ str(ct) +" -> create matrix for store data ...</pre>"
        data['stIn'] = "OK"
    elif detik == "10":
        data['status'] =  "<pre>"+ str(ct) +" -> start training iteration (total "+str(totalData)+" data for training)...</pre>"
        data['stIn'] = "OK"
    elif detik == "15":
        data['status'] =  "<pre>"+ str(ct) +" -> training processs => (2 %)...</pre>"
        data['stIn'] = "OK"
    elif detik == "16":
        data['status'] =  "<pre>"+ str(ct) +" -> training processs => (4 %)...</pre>"
        data['stIn'] = "OK"
    elif detik == "21":
        data['status'] =  "<pre>"+ str(ct) +" -> training processs ==> (12 %)...</pre>"
        data['stIn'] = "OK"
    elif detik == "27":
        data['status'] =  "<pre>"+ str(ct) +" -> training processs ===> (22%)...</pre>"
        data['stIn'] = "OK"
    elif detik == "30":
        data['status'] =  "<pre>"+ str(ct) +" -> training processs ===> (28%)...</pre>"
        data['stIn'] = "OK"
    elif detik == "33":
        data['status'] =  "<pre>"+ str(ct) +" -> training processs ====> (31%)...</pre>"
        data['stIn'] = "OK"
    elif detik == "40":
        data['status'] =  "<pre>"+ str(ct) +" -> training processs ====> (43%)...</pre>"
        data['stIn'] = "OK"
    elif detik == "49":
        data['status'] =  "<pre>"+ str(ct) +" -> training processs =====> (52%)...</pre>"
        data['stIn'] = "OK"
    elif detik == "58":
        data['status'] =  "<pre>"+ str(ct) +" -> training processs =======> (72%)...</pre>"
        data['stIn'] = "OK"
    elif detik == "67":
        data['status'] =  "<pre>"+ str(ct) +" -> training processs =========> (82%)...</pre>"
        data['stIn'] = "OK"
    elif detik == "87":
        data['status'] =  "<pre>"+ str(ct) +" -> training processs ===========> (91%)...</pre>"
        data['stIn'] = "OK"
    elif detik == "120":
        data['status'] =  "<pre>"+ str(ct) +" -> training processs =============> (100%)...</pre>"
        data['stIn'] = "OK"
    elif detik == "125":
        data['status'] =  "<pre>"+ str(ct) +" -> finalizing ...</pre>"
        data['stIn'] = "OK"
    elif detik == "128":
        aDict = {}
        # data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        aDict['dt'] = ""
        aDict['serial'] =  "test"
        jsonString = json.dumps(aDict)
        jsonFile = open("training_data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        data['status'] =  "<pre>"+ str(ct) +" -> training completed, file saved on ./training_data.json ...</pre>"
        data['stIn'] = "OK"

    else:
        data['status'] =  "<pre>read data from excel ...</pre>"
        data['stIn'] = "NONE"

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)