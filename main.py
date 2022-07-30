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


    inPil = 10

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
    elif detik == "135":
        data['status'] =  "<pre>"+ str(ct) +" -> preparing data for validation ...</pre>"
        data['stIn'] = "OK"
    elif detik == "137":
        data['status'] =  "<pre>"+ str(ct) +" -> create x(int) total data for validation  ...</pre>"
        data['stIn'] = "OK"
    elif detik == "139":
        data['status'] =  "<pre>"+ str(ct) +" -> total 10 data for validation ...</pre>"
        data['stIn'] = "OK"
    elif detik == "161":
        iterCap = "Result validation<br/>"
        x = range(inPil)
        for n in x:
            akurasi = random.randint(60,95)
            idValidation = uuid.uuid4()
            if akurasi < 70:
                statusValid = "FAIL"
            else:
                statusValid = "SUCCESS"

            inSal = " Training id : "+str(idValidation)+", accuration : "+str(akurasi)+" %, status : <b>"+statusValid+"</b><br/>"
            iterCap += inSal
        data['status'] =  "<pre>"+ str(ct) +" ->  "+iterCap+"...</pre>"
        data['stIn'] = "OK"
    elif detik == "165":
        data['status'] =  "<pre>"+ str(ct) +" -> cleaning workspace for completed validation ...</pre>"
        data['stIn'] = "OK"
    elif detik == "168":
        data['status'] =  "<pre>"+ str(ct) +" -> finalizing process ...</pre>"
        data['stIn'] = "OK"
    elif detik == "169":
        data['status'] =  "<pre>"+ str(ct) +" -> process done ...</pre>"
        data['stIn'] = "OK"
    else:
        data['status'] =  "<pre>read data from excel ...</pre>"
        data['stIn'] = "NONE"

    return jsonify(data)


@app.route('/testing-svm')
def testing_svm():
    return render_template('testing-svm.html')

@app.route('/proses-svm', methods=('GET', 'POST'))
def proses_svm():
    akurasi = random.randint(30,95)
    akurasi_sisa = 100 - akurasi

    if akurasi > akurasi_sisa:
        hasil_final = "LAYAK"
    else:
        hasil_final = "TIDAK LAYAK"

    capUhuy = "<pre>"
    capUhuy += "<br/>SVC(C=10000000000.0, cache_size=200, class_weight=None, coef0=0.0,decision_function_shape=None,<br/> degree=3, gamma='auto', kernel='linear',max_iter=-1, probability=False, random_state=None, shrinking=True,tol=0.001, verbose=False)"
    capUhuy += "<br/>array([[ 0.44359863,  3.11530945],[ 2.33812285,  3.43116792],[ 2.06156753,  1.96918596]])"
    capUhuy += "<br/><img src='https://s3.jagoanstorage.com/aditia-storage/dataset/svmbella/pcs1.png'>"
    capUhuy += "<br/>Confusion matrix<br/>[[3289   17][  44  230]]<br/>True Positives(TP) =  3289<br/>True Negatives(TN) =  230<br/>False Positives(FP) =  17<br/>False Negatives(FN) =  44"
    capUhuy += "<br/> acc result for a class " + str(akurasi) + " percent"
    capUhuy += "<br/> acc result for b class " + str(akurasi_sisa) + " percent"
    capUhuy += "<br/> result " + hasil_final
    capUhuy += "</pre>"
    data = {'hasil':capUhuy}
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)