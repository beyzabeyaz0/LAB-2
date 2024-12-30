import pandas as pd

import numpy as np


def tablo2Create():
    data = {
    "Ders Çıktı": [1, 2, 3, 4, 5],
    "Ödev1": [np.nan, np.nan, np.nan, np.nan, np.nan],
    "Ödev2": [np.nan, np.nan, np.nan, np.nan, np.nan],
    "Quiz": [np.nan, np.nan, np.nan, np.nan, np.nan],
    "Vize": [np.nan, np.nan, np.nan, np.nan, np.nan],
    "Final": [np.nan, np.nan, np.nan, np.nan, np.nan]
}

    df = pd.DataFrame(data)


    extra_row = ["TABLO 2/ORAN","YÜZDELİK ÖDEV1" , "YÜZDELİK ÖDEV2", "YÜZDELİK QUİZ", "YÜZDELİK VİZE","YÜZDELİK FİNAL"]


    df_with_extra_row = pd.DataFrame([extra_row], columns=df.columns)._append(df, ignore_index=True)

    # Excel dosyasına kaydet
    df_with_extra_row.to_excel("tablo2.xlsx", index=False)


def tablo1Create():
    

    data={
            "Prg Çıktı":[1,2,3,4,5,6,7,8,9,10],
            1.0:[np.nan, np.nan, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan, np.nan, np.nan],
            2.0:[np.nan, np.nan, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan, np.nan, np.nan],
            3.0:[np.nan, np.nan, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan, np.nan, np.nan],
            4.0:[np.nan, np.nan, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan, np.nan, np.nan],
            5.0:[np.nan, np.nan, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan, np.nan, np.nan],
  "İlişki Değ.":[np.nan, np.nan, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan, np.nan, np.nan]

    


    }

    df=pd.DataFrame(data)

    df.to_excel("tablo1.xlsx",index=False)


tablo1Create()
tablo2Create()