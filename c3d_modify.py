# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 01:15:30 2021

@author: JAEWOO
"""


from ezc3d import c3d
import pdb

name = 'STSXXXXXX_sample.c3d' 

c3d_CH = c3d(name)
# c3d_CH = c3d(name, extract_forceplat_data=True)

from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt
import numpy as np

# analog 첫번째 데이터 삭제
ana = c3d_CH['data']._storage['analogs']
ana_del = np.delete(ana, 1 , axis = 1)
c3d_CH['data']._storage['analogs'] = []
c3d_CH['data']._storage['analogs'] = ana_del

ana_check = c3d_CH['data']._storage['analogs']

label = c3d_CH['parameters']['ANALOG']['LABELS']['value']
del label[1]
c3d_CH['parameters']['ANALOG']['LABELS']['value'] = label
label_chcek = label = c3d_CH['parameters']['ANALOG']['LABELS']['value']

c3d_CH.write("STS_sample_del.c3d")


# fz1_CH = c3d_CH["data"]["platform"][0]._storage["force"][2] # FP1
# fz2_CH = c3d_CH["data"]["platform"][1]._storage["force"][2] # FP2
# plt.plot(fz1_CH)
# plt.plot(fz2_CH)
# plt.show()

# parameters = c3d_CH['parameters']['POINT']
# label = c3d_CH['parameters']['POINT']['LABELS']['value']
# rate = c3d_CH['parameters']['POINT']['RATE']['value']

# data = c3d_CH["data"]._storage
# analog_data_CH = c3d_CH['data']._storage['analogs']
# f1_CH =c3d_CH["data"]["platform"][0]._storage["force"] # X,Y,Z 데이터
# f2_CH =c3d_CH["data"]["platform"][1]._storage["force"]

# point_data_x = c3d_CH['data']['points'][0] # 마커 좌표
# point_data_y = c3d_CH['data']['points'][1]
# point_data_z = c3d_CH['data']['points'][2]



###



name = 'LOSD03_127_label.c3d' #force data

c3d_SD = c3d(name, extract_forceplat_data=True)

fz1_SD = c3d_SD["data"]["platform"][0]._storage["force"][2]
fz2_SD = c3d_SD["data"]["platform"][1]._storage["force"][2]
plt.plot(fz1_SD)
plt.plot(fz2_SD)
plt.show()

f1_SD =c3d_SD["data"]["platform"][0]._storage["force"] # X,Y,Z 데이터
f2_SD =c3d_SD["data"]["platform"][1]._storage["force"]
analog_data_SD = c3d_SD['data']._storage['analogs']


### CH force data를 SD force data로 변경

# c3d_CH['data']['platform'][0]._storage['force'] = []
# c3d_CH['data']['platform'][1]._storage['force'] = []

# c3d_CH['data']['platform'][0]._storage['force'] = f1_SD
# c3d_CH['data']['platform'][1]._storage['force'] = f2_SD

# fz1_CH = c3d_CH["data"]["platform"][0]._storage["force"][2] # FP1
# fz2_CH = c3d_CH["data"]["platform"][1]._storage["force"][2] # FP2

# plt.plot(fz1_CH)
# plt.plot(fz2_CH)
# plt.show()


### 아예 더 상위폴더인 'platform'을 변경
# c3d_CH["data"]._storage['platform'] = []
# c3d_CH["data"]._storage['platform'] = c3d_SD["data"]._storage['platform']


### analogs 데이터 변경

# import numpy as np

# len_CH = len(c3d_CH['data']._storage['analogs'][0][0]) # analogs 프레임 수
# len_SD = len(c3d_SD['data']._storage['analogs'][0][0]) # analogs 프레임 수
# len_dlff = len_CH - len_SD

# c3d_CH['data']._storage['analogs'] = c3d_SD['data']._storage['analogs']

# if len_dlff > 0: # 마커 데이터의 길이가 길면
#     add = abs(len_dlff) 
#     # 차이나는 만큼 뒤에 데이터 추가해주기
#     insert_matrix = np.zeros((1, 16, add))
#     c3d_CH['data']._storage['analogs'] = np.concatenate((c3d_CH['data']._storage['analogs'], insert_matrix),axis=2)
       
# if len_dlff < 0: # 마커 데이터의 길이가 더 짧으면
#    subtr = abs(len_dlff)
   
#    for i in range(subtr):
#    # 차이나는 만큼 뒤에 데이터 삭제해주기
#    c3d_CH['data']._storage['analogs'] = np.delete((c3d_CH['data']._storage['analogs']),-1, axis=2)
     
         
                                                     

          
           

analog_data_CH = c3d_CH['data']._storage['analogs'] #확인 

c3d_CH.write("TEST_analogs.c3d")

