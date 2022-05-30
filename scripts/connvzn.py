from asyncio import subprocess
import re
import pandas as pd
import subprocess
# import socket
import zipfile
import os
from zipfile import ZipFile

cmpl_pat_0 = re.compile(r'(,){2,}')
cmpl_pat_1 = re.compile(r'\d\/.*$')
cmpl_pat_2 = re.compile(r'\b(?:[1-2]?[0-9]{1,2}\.){3}[1-2]?[0-9]{1,2}\b')

try:
    os.remove("incoming.txt")
    os.remove("outgoing.txt")
    os.remove("inprocess.txt")
    os.remove("outprocess.txt")
    os.remove("twowayprocess.html")
    os.remove("prc_fl_stat_znl.txt")
    os.remove("prc_fl_stat_znl.csv")
    os.remove("download.zip")
    # cmd = "sh starter.sh"
    # subprocess.Popen(cmd,shell=True)
except:
    pass
dr = "/var/www/html/scripts"
with open(dr+'/onlo_fl_n.txt') as onlo_fl_n:
    onlo_fl_n_ls = onlo_fl_n.readlines()

onlo_fl_n_las = set() 
onlo_fl_n_hl = "Active Internet connections (w/o servers)"

with open(dr+"/prc_fl_stat_znl.txt","w") as lde_fle_ot:    
    for onlo_fl_n_l in onlo_fl_n_ls:
        if onlo_fl_n_l not in onlo_fl_n_las: 
            if onlo_fl_n_hl not in onlo_fl_n_l:
                lde_fle_ot.write(onlo_fl_n_l)
                onlo_fl_n_las.add(onlo_fl_n_l)

with open(dr+"/prc_fl_stat_znl.txt") as exc_l_fi_let:
    onlo_fl_n_pr_lns = exc_l_fi_let.readlines()
    
headers_original = "Proto,Recv-Q,Send-Q,Local,Address,Foreign,Address,State,PID/Program,name"
headers_modified = "Con,In,Out,Local,Foreign,State,PID/Program"

with open(dr+"/prc_fl_stat_znl.csv","w") as execoutfile:
    for onlo_fl_nprc_ln in onlo_fl_n_pr_lns:
        onlo_fl_n_tres_metl_crs_l_0 = cmpl_pat_1.findall(onlo_fl_nprc_ln)
        if onlo_fl_n_tres_metl_crs_l_0:
            onlo_fl_n_on_tr_mtl_opn_l_1 = onlo_fl_n_tres_metl_crs_l_0[0].replace(" ","")
        else:
            onlo_fl_n_on_tr_mtl_opn_l_1 = onlo_fl_nprc_ln
        onlo_fl_n_ores_mtl_opn_l_2 = re.sub(cmpl_pat_1,onlo_fl_n_on_tr_mtl_opn_l_1,onlo_fl_nprc_ln)
        onlo_fl_n_eon_ores_mtl_opn_l_3 = onlo_fl_n_ores_mtl_opn_l_2.replace(" ",",")
        onlo_fl_n_tmp_ex_crs_l_4 = re.sub(cmpl_pat_0,',', onlo_fl_n_eon_ores_mtl_opn_l_3)
        onlo_fl_n_nvs_pois_l_5 = onlo_fl_n_tmp_ex_crs_l_4.replace(headers_original,headers_modified)

        execoutfile.write(onlo_fl_n_nvs_pois_l_5)

n_df_nod_ref = pd.read_csv(dr+'/prc_fl_stat_znl.csv')
n_df_nod_ref_incoming = n_df_nod_ref[['Foreign']] [n_df_nod_ref['In'] != 0]
n_df_nod_ref_outgoing = n_df_nod_ref[['Foreign']] [n_df_nod_ref['Out'] != 0]
n_df_nod_ref_twoway = n_df_nod_ref[['Local','Foreign','PID/Program']] [(n_df_nod_ref.In == 0) & (n_df_nod_ref.Out == 0)]


n_df_nod_ref_twoway_html = r'<link rel="stylesheet" type="text/css" href="hetro-frame-slide.css" />' + '\n'
n_df_nod_ref_twoway_html += n_df_nod_ref_twoway.to_html(index=False)

n_df_nod_ref_incoming.to_csv(dr+'/inprocess.txt',header=None, index=None,mode='a')
n_df_nod_ref_outgoing.to_csv(dr+'/outprocess.txt',header=None, index=None,mode='a')

with open(dr+'/twowayprocess.html','w') as twowyfile:
    twowyfile.write(n_df_nod_ref_twoway_html)


myip = subprocess.getstatusoutput('hostname -I')
myip1 = str(myip[1])
# myip = socket.gethostbyname(socket.gethostname())
with open(dr+'/myip.txt','w') as output_file:
    output_file.write(myip1)

with open(dr+'/onlo_fl_n_0.txt') as onlod_sec_nfl:
    onlod_sec_nfl_ls = onlod_sec_nfl.readlines()

with open(dr+"/incoming.txt", "w") as output_file:
    for onlod_sec_nfl_l in onlod_sec_nfl_ls:
        onlod_sec_nfl_ip_list = cmpl_pat_2.findall(onlod_sec_nfl_l)
        if not onlod_sec_nfl_ip_list[1] == myip1:
            output_file.write(onlod_sec_nfl_ip_list[1]+'\n')
with open(dr+"/outgoing.txt", "w") as output_file:
    for onlod_sec_nfl_l in onlod_sec_nfl_ls:
        onlod_sec_nfl_ip_list = cmpl_pat_2.findall(onlod_sec_nfl_l)
        if not onlod_sec_nfl_ip_list[0] == myip1:
            output_file.write(onlod_sec_nfl_ip_list[0]+'\n')

with ZipFile(dr+'/download.zip','w') as dn_load_fl:
    dn_load_fl.write('twowayprocess.html')
    dn_load_fl.write('incoming.txt')
    dn_load_fl.write('inprocess.txt')
    dn_load_fl.write('outgoing.txt')
    dn_load_fl.write('outprocess.txt')

