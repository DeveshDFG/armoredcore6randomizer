import math
import sys
import os
import urllib.parse
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame, QGridLayout, \
    QAction, QMenuBar, QComboBox, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import random

# The python dictionary for each part (thanks ChatGPT lol)
parts = {
    'RArm': {
        'MA-J-200 RANSETSU-RF': {
            'Image': '',
            'Weight': 4210,
            'EN Load': 158
        },
        'WR-0555 ATTACHE': {
            'Image': '',
            'Weight': 5110,
            'EN Load': 303
        },
        'LR-036 CURTIS': {
            'Image': '',
            'Weight': 4150,
            'EN Load': 289
        },
        'LR-037 HARRIS': {
            'Image': '',
            'Weight': 4840,
            'EN Load': 441
        },
        'RF-024 TURNER': {
            'Image': '',
            'Weight': 3560,
            'EN Load': 102
        },
        'RF-025 SCUDDER': {
            'Image': '',
            'Weight': 3830,
            'EN Load': 153
        },
        'MA-J-201 RANSETSU-AR': {
            'Image': '',
            'Weight': 3620,
            'EN Load': 132
        },
        'MG-014 LUDLOW': {
            'Image': '',
            'Weight': 2450,
            'EN Load': 82
        },
        'DF-MG-02 CHANG-CHEN': {
            'Image': '',
            'Weight': 3280,
            'EN Load': 143
        },
        'MA-E-210 ETSUJIN': {
            'Image': '',
            'Weight': 2810,
            'EN Load': 98
        },
        'DF-GA-08 HU-BEN': {
            'Image': '',
            'Weight': 5800,
            'EN Load': 425
        },
        'SG-026 HALDEMAN': {
            'Image': '',
            'Weight': 3660,
            'EN Load': 185
        },
        'SG-027 ZIMMERMAN': {
            'Image': '',
            'Weight': 4400,
            'EN Load': 242
        },
        'WR-0777 SWEET SIXTEEN': {
            'Image': '',
            'Weight': 1640,
            'EN Load': 268
        },
        'HG-003 COQUILLETT': {
            'Image': '',
            'Weight': 1200,
            'EN Load': 122
        },
        'HG-004 DUCKETT': {
            'Image': '',
            'Weight': 1650,
            'EN Load': 158
        },
        'MA-E-211 SAMPU': {
            'Image': '',
            'Weight': 960,
            'EN Load': 62
        },
        'EL-PW-00 VIENTO': {
            'Image': '',
            'Weight': 1180,
            'EN Load': 215
        },
        'VP-66EG': {
            'Image': '',
            'Weight': 980,
            'EN Load': 247
        },
        'DF-BA-06 XUAN-GE': {
            'Image': '',
            'Weight': 5480,
            'EN Load': 240
        },
        'MAJESTIC': {
            'Image': '',
            'Weight': 4660,
            'EN Load': 178
        },
        'LITTLE GEM': {
            'Image': '',
            'Weight': 3100,
            'EN Load': 192
        },
        '44-141 JVLN ALPHA': {
            'Image': '',
            'Weight': 7420,
            'EN Load': 99
        },
        'DF-GR-07 GOU-CHEN': {
            'Image': '',
            'Weight': 5460,
            'EN Load': 385
        },
        'DIZZY': {
            'Image': '',
            'Weight': 6420,
            'EN Load': 455
        },
        'IRIDIUM': {
            'Image': '',
            'Weight': 2020,
            'EN Load': 290
        },
        'MA-T-222 KYORAI': {
            'Image': '',
            'Weight': 2890,
            'EN Load': 60
        },
        'WS-1200 THERAPIST': {
            'Image': '',
            'Weight': 3180,
            'EN Load': 82
        },
        'WB-0000 BAD COOK': {
            'Image': '',
            'Weight': 6210,
            'EN Load': 403
        },
        'VP-66LR': {
            'Image': '',
            'Weight': 3560,
            'EN Load': 480
        },
        'VE-66LRA': {
            'Image': '',
            'Weight': 4940,
            'EN Load': 532
        },
        'VE-66LRB': {
            'Image': '',
            'Weight': 7760,
            'EN Load': 604
        },
        'WUERGER/66E': {
            'Image': '',
            'Weight': 2880,
            'EN Load': 440
        },
        'VP-66LS': {
            'Image': '',
            'Weight': 3540,
            'EN Load': 510
        },
        'VP-66LH': {
            'Image': '',
            'Weight': 2800,
            'EN Load': 395
        },
        'Vvc-760PR': {
            'Image': '',
            'Weight': 3330,
            'EN Load': 490
        },
        'IA-C01W1: NEBULA': {
            'Image': '',
            'Weight': 3890,
            'EN Load': 609
        },
        'IA-C01W6: NB-REDSHIFT': {
            'Image': '',
            'Weight': 4040,
            'EN Load': 667
        },
        'IB-C03W1: WLT 011': {
            'Image': '',
            'Weight': 9030,
            'EN Load': 850
        },
        '44-142 KRSV': {
            'Image': '',
            'Weight': 10120,
            'EN Load': 707
        },
        'HI-16: GU-Q1': {
            'Image': '',
            'Weight': 2110,
            'EN Load': 368
        },
        'HI-18: GU-A2': {
            'Image': '',
            'Weight': 2650,
            'EN Load': 448
        },
        'HML-G2/P19MLT-04': {
            'Image': '',
            'Weight': 3250,
            'EN Load': 165
        },
        'HML-G3/P08SPL-06': {
            'Image': '',
            'Weight': 4630,
            'EN Load': 180
        },
        'WS-5000 APERITIF': {
            'Image': '',
            'Weight': 4600,
            'EN Load': 165
        }
    },
    'LArm': {
        'PB-033M ASHMEAD': {
            'Image': '',
            'Weight': 4150,
            'EN Load': 225
        },
        'DF-ET-09 TAI-YANG-SHOU': {
            'Image': '',
            'Weight': 3790,
            'EN Load': 160
        },
        'WB-0010 DOUBLE TROUBLE': {
            'Image': '',
            'Weight': 5090,
            'EN Load': 108
        },
        'VP-67EB': {
            'Image': '',
            'Weight': 1720,
            'EN Load': 198
        },
        'VP-67LD': {
            'Image': '',
            'Weight': 1350,
            'EN Load': 150
        },
        'Vvc-770LB': {
            'Image': '',
            'Weight': 2060,
            'EN Load': 245
        },
        'Vvc-774LS': {
            'Image': '',
            'Weight': 3260,
            'EN Load': 328
        },
        'VE-67LLA': {
            'Image': '',
            'Weight': 4520,
            'EN Load': 460
        },
        '44-143 HMMR': {
            'Image': '',
            'Weight': 2410,
            'EN Load': 311
        },
        'HI-32: BU-TT/A': {
            'Image': '',
            'Weight': 1800,
            'EN Load': 213
        },
        'IA-C01W2: MOONLIGHT': {
            'Image': '',
            'Weight': 2200,
            'EN Load': 544
        },
        'IA-C01W7: ML-REDSHIFT': {
            'Image': '',
            'Weight': 2200,
            'EN Load': 544
        },
        'IB-C03W2: WLT 101': {
            'Image': '',
            'Weight': 2030,
            'EN Load': 642
        },
        'MA-J-200 RANSETSU-RF': {
            'Image': '',
            'Weight': 4210,
            'EN Load': 158
        },
        'WR-0555 ATTACHE': {
            'Image': '',
            'Weight': 5110,
            'EN Load': 303
        },
        'LR-036 CURTIS': {
            'Image': '',
            'Weight': 4150,
            'EN Load': 289
        },
        'LR-037 HARRIS': {
            'Image': '',
            'Weight': 4840,
            'EN Load': 441
        },
        'RF-024 TURNER': {
            'Image': '',
            'Weight': 3560,
            'EN Load': 102
        },
        'RF-025 SCUDDER': {
            'Image': '',
            'Weight': 3830,
            'EN Load': 153
        },
        'MA-J-201 RANSETSU-AR': {
            'Image': '',
            'Weight': 3620,
            'EN Load': 132
        },
        'MG-014 LUDLOW': {
            'Image': '',
            'Weight': 2450,
            'EN Load': 82
        },
        'DF-MG-02 CHANG-CHEN': {
            'Image': '',
            'Weight': 3280,
            'EN Load': 143
        },
        'MA-E-210 ETSUJIN': {
            'Image': '',
            'Weight': 2810,
            'EN Load': 98
        },
        'DF-GA-08 HU-BEN': {
            'Image': '',
            'Weight': 5800,
            'EN Load': 425
        },
        'SG-026 HALDEMAN': {
            'Image': '',
            'Weight': 3660,
            'EN Load': 185
        },
        'SG-027 ZIMMERMAN': {
            'Image': '',
            'Weight': 4400,
            'EN Load': 242
        },
        'WR-0777 SWEET SIXTEEN': {
            'Image': '',
            'Weight': 1640,
            'EN Load': 268
        },
        'HG-003 COQUILLETT': {
            'Image': '',
            'Weight': 1200,
            'EN Load': 122
        },
        'HG-004 DUCKETT': {
            'Image': '',
            'Weight': 1650,
            'EN Load': 158
        },
        'MA-E-211 SAMPU': {
            'Image': '',
            'Weight': 960,
            'EN Load': 62
        },
        'EL-PW-00 VIENTO': {
            'Image': '',
            'Weight': 1180,
            'EN Load': 215
        },
        'VP-66EG': {
            'Image': '',
            'Weight': 980,
            'EN Load': 247
        },
        'DF-BA-06 XUAN-GE': {
            'Image': '',
            'Weight': 5480,
            'EN Load': 240
        },
        'MAJESTIC': {
            'Image': '',
            'Weight': 4660,
            'EN Load': 178
        },
        'LITTLE GEM': {
            'Image': '',
            'Weight': 3100,
            'EN Load': 192
        },
        '44-141 JVLN ALPHA': {
            'Image': '',
            'Weight': 7420,
            'EN Load': 99
        },
        'DF-GR-07 GOU-CHEN': {
            'Image': '',
            'Weight': 5460,
            'EN Load': 385
        },
        'DIZZY': {
            'Image': '',
            'Weight': 6420,
            'EN Load': 455
        },
        'IRIDIUM': {
            'Image': '',
            'Weight': 2020,
            'EN Load': 290
        },
        'MA-T-222 KYORAI': {
            'Image': '',
            'Weight': 2890,
            'EN Load': 60
        },
        'WS-1200 THERAPIST': {
            'Image': '',
            'Weight': 3180,
            'EN Load': 82
        },
        'WB-0000 BAD COOK': {
            'Image': '',
            'Weight': 6210,
            'EN Load': 403
        },
        'VP-66LR': {
            'Image': '',
            'Weight': 3560,
            'EN Load': 480
        },
        'VE-66LRA': {
            'Image': '',
            'Weight': 4940,
            'EN Load': 532
        },
        'VE-66LRB': {
            'Image': '',
            'Weight': 7760,
            'EN Load': 604
        },
        'WUERGER/66E': {
            'Image': '',
            'Weight': 2880,
            'EN Load': 440
        },
        'VP-66LS': {
            'Image': '',
            'Weight': 3540,
            'EN Load': 510
        },
        'VP-66LH': {
            'Image': '',
            'Weight': 2800,
            'EN Load': 395
        },
        'Vvc-760PR': {
            'Image': '',
            'Weight': 3330,
            'EN Load': 490
        },
        'IA-C01W1: NEBULA': {
            'Image': '',
            'Weight': 3890,
            'EN Load': 609
        },
        'IA-C01W6: NB-REDSHIFT': {
            'Image': '',
            'Weight': 4040,
            'EN Load': 667
        },
        'IB-C03W1: WLT 011': {
            'Image': '',
            'Weight': 9030,
            'EN Load': 850
        },
        '44-142 KRSV': {
            'Image': '',
            'Weight': 10120,
            'EN Load': 707
        },
        'HI-16: GU-Q1': {
            'Image': '',
            'Weight': 2110,
            'EN Load': 368
        },
        'HI-18: GU-A2': {
            'Image': '',
            'Weight': 2650,
            'EN Load': 448
        },
        'HML-G2/P19MLT-04': {
            'Image': '',
            'Weight': 3250,
            'EN Load': 165
        },
        'HML-G3/P08SPL-06': {
            'Image': '',
            'Weight': 4630,
            'EN Load': 180
        },
        'WS-5000 APERITIF': {
            'Image': '',
            'Weight': 4600,
            'EN Load': 165
        }
    },
    'RBack': {
        'SB-033M MORLEY': {
            'Image': '',
            'Weight': 5420,
            'EN Load': 455
        },
        'EARSHOT': {
            'Image': '',
            'Weight': 7230,
            'EN Load': 388
        },
        'SONGBIRDS': {
            'Image': '',
            'Weight': 5500,
            'EN Load': 285
        },
        'VE-60SNA': {
            'Image': '',
            'Weight': 6150,
            'EN Load': 826
        },
        'VP-60LCS': {
            'Image': '',
            'Weight': 5190,
            'EN Load': 683
        },
        'VE-60LCA': {
            'Image': '',
            'Weight': 14820,
            'EN Load': 1200
        },
        'VP-60LCD': {
            'Image': '',
            'Weight': 7620,
            'EN Load': 784
        },
        'FASAN/60E': {
            'Image': '',
            'Weight': 6270,
            'EN Load': 882
        },
        'KRANICH/60Z': {
            'Image': '',
            'Weight': 2100,
            'EN Load': 652
        },
        'EULE/60D': {
            'Image': '',
            'Weight': 3060,
            'EN Load': 620
        },
        'IA-C01W3: AURORA': {
            'Image': '',
            'Weight': 3330,
            'EN Load': 522
        },
        'BML-G1/P20MLT-04': {
            'Image': '',
            'Weight': 2120,
            'EN Load': 154
        },
        'BML-G2/P03MLT-06': {
            'Image': '',
            'Weight': 3840,
            'EN Load': 241
        },
        'BML-G2/P05MLT-10': {
            'Image': '',
            'Weight': 5220,
            'EN Load': 320
        },
        'BML-G2/P19SPL-12': {
            'Image': '',
            'Weight': 3630,
            'EN Load': 325
        },
        'BML-G2/P16SPL-08': {
            'Image': '',
            'Weight': 2800,
            'EN Load': 228
        },
        'BML-G2/P17SPL-16': {
            'Image': '',
            'Weight': 5010,
            'EN Load': 510
        },
        'BML-G1/P31DUO-02': {
            'Image': '',
            'Weight': 1900,
            'EN Load': 182
        },
        'BML-G1/P32DUO-03': {
            'Image': '',
            'Weight': 3450,
            'EN Load': 262
        },
        'BML-G2/P08DUO-03': {
            'Image': '',
            'Weight': 4020,
            'EN Load': 332
        },
        'BML-G1/P01VTC-04': {
            'Image': '',
            'Weight': 2240,
            'EN Load': 258
        },
        'BML-G1/P03VTC-08': {
            'Image': '',
            'Weight': 3520,
            'EN Load': 380
        },
        'BML-G1/P07VTC-12': {
            'Image': '',
            'Weight': 5010,
            'EN Load': 525
        },
        'BML-G3/P04ACT-01': {
            'Image': '',
            'Weight': 2680,
            'EN Load': 213
        },
        'BML-G3/P05ACT-02': {
            'Image': '',
            'Weight': 4320,
            'EN Load': 424
        },
        'BML-G1/P29CNT': {
            'Image': '',
            'Weight': 6370,
            'EN Load': 150
        },
        'WR-0999 DELIVERY BOY': {
            'Image': '',
            'Weight': 6890,
            'EN Load': 499
        },
        'WS-5001 SOUP': {
            'Image': '',
            'Weight': 5620,
            'EN Load': 685
        },
        '45-091 JVLN BETA': {
            'Image': '',
            'Weight': 4250,
            'EN Load': 425
        },
        'EL-PW-01 TRUENO': {
            'Image': '',
            'Weight': 3100,
            'EN Load': 420
        },
        'Vvc-703PM': {
            'Image': '',
            'Weight': 2720,
            'EN Load': 245
        },
        'Vvc-706PM': {
            'Image': '',
            'Weight': 4800,
            'EN Load': 342
        },
        'Vvc-70VPM': {
            'Image': '',
            'Weight': 3760,
            'EN Load': 268
        },
        'IB-C03W3: NGI 006': {
            'Image': '',
            'Weight': 4200,
            'EN Load': 783
        },
        'BO-044 HUXLEY': {
            'Image': '',
            'Weight': 2230,
            'EN Load': 435
        },
        '45-091 ORBT': {
            'Image': '',
            'Weight': 2010,
            'EN Load': 446
        },
        'VP-60LT': {
            'Image': '',
            'Weight': 2800,
            'EN Load': 560
        },
        'Vvc-700LD': {
            'Image': '',
            'Weight': 3800,
            'EN Load': 570
        },
        'DF-GA-09 SHAO-WEI': {
            'Image': '',
            'Weight': 3960,
            'EN Load': 404
        }
    },
    'LBack': {
        'VP-61PS': {
            'Image': '',
            'Weight': 2700,
            'EN Load': 310
        },
        'SI-24: SU-Q5': {
            'Image': '',
            'Weight': 2010,
            'EN Load': 220
        },
        'SI-27: SU-R8': {
            'Image': '',
            'Weight': 3150,
            'EN Load': 323
        },
        'VP-61PB': {
            'Image': '',
            'Weight': 1920,
            'EN Load': 285
        },
        'SI-29: SU-TT/C': {
            'Image': '',
            'Weight': 3360,
            'EN Load': 385
        },
        'VE-61PSA': {
            'Image': '',
            'Weight': 4100,
            'EN Load': 450
        },
        'IB-C03W4: NGI 028': {
            'Image': '',
            'Weight': 2170,
            'EN Load': 800
        },
        'SB-033M MORLEY': {
            'Image': '',
            'Weight': 5420,
            'EN Load': 455
        },
        'EARSHOT': {
            'Image': '',
            'Weight': 7230,
            'EN Load': 388
        },
        'SONGBIRDS': {
            'Image': '',
            'Weight': 5500,
            'EN Load': 285
        },
        'VE-60SNA': {
            'Image': '',
            'Weight': 6150,
            'EN Load': 826
        },
        'VP-60LCS': {
            'Image': '',
            'Weight': 5190,
            'EN Load': 683
        },
        'VE-60LCA': {
            'Image': '',
            'Weight': 14820,
            'EN Load': 1200
        },
        'VP-60LCD': {
            'Image': '',
            'Weight': 7620,
            'EN Load': 784
        },
        'FASAN/60E': {
            'Image': '',
            'Weight': 6270,
            'EN Load': 882
        },
        'KRANICH/60Z': {
            'Image': '',
            'Weight': 2100,
            'EN Load': 652
        },
        'EULE/60D': {
            'Image': '',
            'Weight': 3060,
            'EN Load': 620
        },
        'IA-C01W3: AURORA': {
            'Image': '',
            'Weight': 3330,
            'EN Load': 522
        },
        'BML-G1/P20MLT-04': {
            'Image': '',
            'Weight': 2240,
            'EN Load': 258
        },
        'BML-G2/P03MLT-06': {
            'Image': '',
            'Weight': 3840,
            'EN Load': 241
        },
        'BML-G2/P05MLT-10': {
            'Image': '',
            'Weight': 5220,
            'EN Load': 320
        },
        'BML-G2/P19SPL-12': {
            'Image': '',
            'Weight': 3630,
            'EN Load': 325
        },
        'BML-G2/P16SPL-08': {
            'Image': '',
            'Weight': 2800,
            'EN Load': 228
        },
        'BML-G2/P17SPL-16': {
            'Image': '',
            'Weight': 5010,
            'EN Load': 510
        },
        'BML-G1/P31DUO-02': {
            'Image': '',
            'Weight': 1900,
            'EN Load': 182
        },
        'BML-G1/P32DUO-03': {
            'Image': '',
            'Weight': 3450,
            'EN Load': 262
        },
        'BML-G2/P08DUO-03': {
            'Image': '',
            'Weight': 4020,
            'EN Load': 332
        },
        'BML-G1/P01VTC-04': {
            'Image': '',
            'Weight': 2240,
            'EN Load': 258
        },
        'BML-G1/P03VTC-08': {
            'Image': '',
            'Weight': 3520,
            'EN Load': 380
        },
        'BML-G1/P07VTC-12': {
            'Image': '',
            'Weight': 5010,
            'EN Load': 525
        },
        'BML-G3/P04ACT-01': {
            'Image': '',
            'Weight': 2680,
            'EN Load': 213
        },
        'BML-G3/P05ACT-02': {
            'Image': '',
            'Weight': 4320,
            'EN Load': 424
        },
        'BML-G1/P29CNT': {
            'Image': '',
            'Weight': 6370,
            'EN Load': 150
        },
        'WR-0999 DELIVERY BOY': {
            'Image': '',
            'Weight': 6890,
            'EN Load': 499
        },
        'WS-5001 SOUP': {
            'Image': '',
            'Weight': 5620,
            'EN Load': 685
        },
        '45-091 JVLN BETA': {
            'Image': '',
            'Weight': 4250,
            'EN Load': 425
        },
        'EL-PW-01 TRUENO': {
            'Image': '',
            'Weight': 3100,
            'EN Load': 420
        },
        'Vvc-703PM': {
            'Image': '',
            'Weight': 2720,
            'EN Load': 245
        },
        'Vvc-706PM': {
            'Image': '',
            'Weight': 4800,
            'EN Load': 342
        },
        'Vvc-70VPM': {
            'Image': '',
            'Weight': 3760,
            'EN Load': 268
        },
        'IB-C03W3: NGI 006': {
            'Image': '',
            'Weight': 4200,
            'EN Load': 783
        },
        'BO-044 HUXLEY': {
            'Image': '',
            'Weight': 2230,
            'EN Load': 435
        },
        '45-091 ORBT': {
            'Image': '',
            'Weight': 2010,
            'EN Load': 446
        },
        'VP-60LT': {
            'Image': '',
            'Weight': 2800,
            'EN Load': 560
        },
        'Vvc-700LD': {
            'Image': '',
            'Weight': 3800,
            'EN Load': 570
        },
        'DF-GA-09 SHAO-WEI': {
            'Image': '',
            'Weight': 3960,
            'EN Load': 404
        }
    },
    'Head': {
        'AH-J-124 BASHO': {
            'Image': '',
            'Weight': 4600,
            'EN Load': 95
        },
        'AH-J-124/RC JAILBREAK': {
            'Image': '',
            'Weight': 4250,
            'EN Load': 95
        },
        'HD-011 MELANDER': {
            'Image': '',
            'Weight': 3160,
            'EN Load': 135
        },
        'HD-033M VERRILL': {
            'Image': '',
            'Weight': 3830,
            'EN Load': 240
        },
        'HD-012 MELANDER C3': {
            'Image': '',
            'Weight': 3300,
            'EN Load': 165
        },
        'DF-HD-08 TIAN-QIANG': {
            'Image': '',
            'Weight': 1230,
            'EN Load': 88
        },
        'VP-44S': {
            'Image': '',
            'Weight': 3080,
            'EN Load': 148
        },
        'VP-44D': {
            'Image': '',
            'Weight': 3260,
            'EN Load': 177
        },
        'NACHTREIHER/44E': {
            'Image': '',
            'Weight': 2320,
            'EN Load': 210
        },
        'KASUAR/44Z': {
            'Image': '',
            'Weight': 2590,
            'EN Load': 254
        },
        'VE-44A': {
            'Image': '',
            'Weight': 3640,
            'EN Load': 182
        },
        'VE-44B': {
            'Image': '',
            'Weight': 4320,
            'EN Load': 265
        },
        'HC-2000 FINDER EYE': {
            'Image': '',
            'Weight': 2670,
            'EN Load': 125
        },
        'HC-2000/BC SHADE EYE': {
            'Image': '',
            'Weight': 3090,
            'EN Load': 163
        },
        'HC-3000 WRECKER': {
            'Image': '',
            'Weight': 3800,
            'EN Load': 102
        },
        'HS-5000 APPETIZER': {
            'Image': '',
            'Weight': 3000,
            'EN Load': 103
        },
        'EL-TH-10 FIRMEZA': {
            'Image': '',
            'Weight': 2570,
            'EN Load': 134
        },
        'EL-PH-00 ALBA': {
            'Image': '',
            'Weight': 2800,
            'EN Load': 205
        },
        '20-081 MIND ALPHA': {
            'Image': '',
            'Weight': 3350,
            'EN Load': 142
        },
        '20-082 MIND BETA': {
            'Image': '',
            'Weight': 3460,
            'EN Load': 128
        },
        'IA-C01H: EPHEMERA': {
            'Image': '',
            'Weight': 4330,
            'EN Load': 233
        },
        'IB-C03H: HAL 826': {
            'Image': '',
            'Weight': 3760,
            'EN Load': 215
        },
        'LAMMERGEIER/44F': {
            'Image': '',
            'Weight': 1050,
            'EN Load': 220
        }
    },
    'Core': {
        'AC-J-120 BASHO': {
            'Image': '',
            'Weight': 16100,
            'EN Load': 300,
            'Generator Output Adj.': 83
        },
        'AC-J-120/RC JAILBREAK': {
            'Image': '',
            'Weight': 12350,
            'EN Load': 300,
            'Generator Output Adj.': 83
        },
        'BD-011 MELANDER': {
            'Image': '',
            'Weight': 15800,
            'EN Load': 304,
            'Generator Output Adj.': 105
        },
        'BD-012 MELANDER C3': {
            'Image': '',
            'Weight': 14050,
            'EN Load': 322,
            'Generator Output Adj.': 102
        },
        'DF-BD-08 TIAN-QIANG': {
            'Image': '',
            'Weight': 20650,
            'EN Load': 388,
            'Generator Output Adj.': 114
        },
        'VP-40S': {
            'Image': '',
            'Weight': 15030,
            'EN Load': 337,
            'Generator Output Adj.': 106
        },
        'NACHTREIHER/40E': {
            'Image': '',
            'Weight': 9820,
            'EN Load': 330,
            'Generator Output Adj.': 84
        },
        'VE-40A': {
            'Image': '',
            'Weight': 21100,
            'EN Load': 432,
            'Generator Output Adj.': 122
        },
        'CC-2000 ORBITER': {
            'Image': '',
            'Weight': 12650,
            'EN Load': 267,
            'Generator Output Adj.': 103
        },
        'CC-3000 WRECKER': {
            'Image': '',
            'Weight': 19000,
            'EN Load': 310,
            'Generator Output Adj.': 96
        },
        'CS-5000 MAIN DISH': {
            'Image': '',
            'Weight': 23600,
            'EN Load': 413,
            'Generator Output Adj.': 97
        },
        'EL-TC-10 FIRMEZA': {
            'Image': '',
            'Weight': 10890,
            'EN Load': 351,
            'Generator Output Adj.': 104
        },
        'EL-PC-00 ALBA': {
            'Image': '',
            'Weight': 12000,
            'EN Load': 315,
            'Generator Output Adj.': 101
        },
        '07-061 MIND ALPHA': {
            'Image': '',
            'Weight': 16510,
            'EN Load': 364,
            'Generator Output Adj.': 112
        },
        'IA-C01C: EPHEMERA': {
            'Image': '',
            'Weight': 13200,
            'EN Load': 412,
            'Generator Output Adj.': 126
        },
        'IB-C03C: HAL 826': {
            'Image': '',
            'Weight': 18520,
            'EN Load': 366,
            'Generator Output Adj.': 120
        },
        'LAMMERGEIER/40F': {
            'Image': '',
            'Weight': 9700,
            'EN Load': 341,
            'Generator Output Adj.': 117
        }
    },
    'Arms': {
        'AA-J-123 BASHO': {
            'Image': '',
            'Weight': 10480,
            'EN Load': 210,
            'Arms Load Limit': 10520
        },
        'AA-J-123/RC JAILBREAK': {
            'Image': '',
            'Weight': 8480,
            'EN Load': 210,
            'Arms Load Limit': 10520
        },
        'AR-011 MELANDER': {
            'Image': '',
            'Weight': 13650,
            'EN Load': 265,
            'Arms Load Limit': 15100
        },
        'AR-012 MELANDER C3': {
            'Image': '',
            'Weight': 12300,
            'EN Load': 232,
            'Arms Load Limit': 12000
        },
        'DF-AR-08 TIAN-QIANG': {
            'Image': '',
            'Weight': 20020,
            'EN Load': 295,
            'Arms Load Limit': 19500
        },
        'DF-AR-09 TIAN-LAO': {
            'Image': '',
            'Weight': 26740,
            'EN Load': 266,
            'Arms Load Limit': 17200
        },
        'VP-46S': {
            'Image': '',
            'Weight': 14020,
            'EN Load': 278,
            'Arms Load Limit': 14520
        },
        'VP-46D': {
            'Image': '',
            'Weight': 10990,
            'EN Load': 248,
            'Arms Load Limit': 11800
        },
        'NACHTREIHER/46E': {
            'Image': '',
            'Weight': 11420,
            'EN Load': 302,
            'Arms Load Limit': 12730
        },
        'VE-46A': {
            'Image': '',
            'Weight': 22210,
            'EN Load': 380,
            'Arms Load Limit': 21300
        },
        'AC-2000 TOOL ARM': {
            'Image': '',
            'Weight': 11300,
            'EN Load': 216,
            'Arms Load Limit': 13300
        },
        'AC-3000 WRECKER': {
            'Image': '',
            'Weight': 14650,
            'EN Load': 220,
            'Arms Load Limit': 15800
        },
        'AS-5000 SALAD': {
            'Image': '',
            'Weight': 20940,
            'EN Load': 324,
            'Arms Load Limit': 18700
        },
        'EL-TA-10 FIRMEZA': {
            'Image': '',
            'Weight': 11220,
            'EN Load': 270,
            'Arms Load Limit': 13540
        },
        'EL-PA-00 ALBA': {
            'Image': '',
            'Weight': 9810,
            'EN Load': 315,
            'Arms Load Limit': 11350
        },
        '04-101 MIND ALPHA': {
            'Image': '',
            'Weight': 16960,
            'EN Load': 358,
            'Arms Load Limit': 15550
        },
        'IA-C01A: EPHEMERA': {
            'Image': '',
            'Weight': 12700,
            'EN Load': 312,
            'Arms Load Limit': 12680
        },
        'IB-C03A: HAL 826': {
            'Image': '',
            'Weight': 14160,
            'EN Load': 300,
            'Arms Load Limit': 14000
        },
        'LAMMERGEIER/46F': {
            'Image': '',
            'Weight': 9700,
            'EN Load': 328,
            'Arms Load Limit': 11970
        }
    },
    'Legs': {
        'AL-J-121 BASHO': {
            'Image': '',
            'Weight': 20520,
            'EN Load': 300,
            'Load Limit': 62600,
            'Type': "Non-Tank"
        },
        'AL-J-121/RC JAILBREAK': {
            'Image': '',
            'Weight': 18560,
            'EN Load': 300,
            'Load Limit': 62600,
            'Type': "Non-Tank"
        },
        'LG-011 MELANDER': {
            'Image': '',
            'Weight': 18700,
            'EN Load': 365,
            'Load Limit': 60520,
            'Type': "Non-Tank"
        },
        'LG-012 MELANDER C3': {
            'Image': '',
            'Weight': 17210,
            'EN Load': 355,
            'Load Limit': 55440,
            'Type': "Non-Tank"
        },
        'DF-LG-08 TIAN-QIANG': {
            'Image': '',
            'Weight': 23600,
            'EN Load': 400,
            'Load Limit': 82600,
            'Type': "Non-Tank"
        },
        'VP-422': {
            'Image': '',
            'Weight': 17900,
            'EN Load': 387,
            'Load Limit': 58620,
            'Type': "Non-Tank"
        },
        'NACHTREIHER/42E': {
            'Image': '',
            'Weight': 14030,
            'EN Load': 462,
            'Load Limit': 48650,
            'Type': "Non-Tank"
        },
        'VE-42A': {
            'Image': '',
            'Weight': 28950,
            'EN Load': 465,
            'Load Limit': 85700,
            'Type': "Non-Tank"
        },
        '2C-2000 CRAWLER': {
            'Image': '',
            'Weight': 16300,
            'EN Load': 280,
            'Load Limit': 51200,
            'Type': "Non-Tank"
        },
        '2C-3000 WRECKER': {
            'Image': '',
            'Weight': 21680,
            'EN Load': 680,
            'Load Limit': 68900,
            'Type': "Non-Tank"
        },
        '2S-5000 DESSERT': {
            'Image': '',
            'Weight': 25880,
            'EN Load': 420,
            'Load Limit': 77100,
            'Type': "Non-Tank"
        },
        'EL-TL-10 FIRMEZA': {
            'Image': '',
            'Weight': 11200,
            'EN Load': 378,
            'Load Limit': 52100,
            'Type': "Non-Tank"
        },
        'EL-PL-00 ALBA': {
            'Image': '',
            'Weight': 13150,
            'EN Load': 360,
            'Load Limit': 50100,
            'Type': "Non-Tank"
        },
        '06-041 MIND ALPHA': {
            'Image': '',
            'Weight': 22110,
            'EN Load': 432,
            'Load Limit': 63810,
            'Type': "Non-Tank"
        },
        'IA-C01L: EPHEMERA': {
            'Image': '',
            'Weight': 15200,
            'EN Load': 398,
            'Load Limit': 55050,
            'Type': "Non-Tank"
        },
        'IB-C03L: HAL 826': {
            'Image': '',
            'Weight': 20890,
            'EN Load': 385,
            'Load Limit': 64900,
            'Type': "Non-Tank"
        },
        'KASUAR/42Z': {
            'Image': '',
            'Weight': 19060,
            'EN Load': 388,
            'Load Limit': 47820,
            'Type': "Non-Tank"
        },
        '06-042 MIND BETA': {
            'Image': '',
            'Weight': 22200,
            'EN Load': 426,
            'Load Limit': 61600,
            'Type': "Non-Tank"
        },
        'RC-2000 SPRING CHICKEN': {
            'Image': '',
            'Weight': 25890,
            'EN Load': 402,
            'Load Limit': 68360,
            'Type': "Non-Tank"
        },
        'LG-033M VERRILL': {
            'Image': '',
            'Weight': 36200,
            'EN Load': 675,
            'Load Limit': 76200,
            'Type': "Non-Tank"
        },
        'VP-424': {
            'Image': '',
            'Weight': 31600,
            'EN Load': 760,
            'Load Limit': 69800,
            'Type': "Non-Tank"
        },
        'LAMMERGEIER/42F': {
            'Image': '',
            'Weight': 22430,
            'EN Load': 790,
            'Load Limit': 52460,
            'Type': "Non-Tank"
        },
        'LG-022T BORNEMISSZA': {
            'Image': '',
            'Weight': 49800,
            'EN Load': 455,
            'Load Limit': 100300,
            'Type': "Tank"
        },
        'VE-42B': {
            'Image': '',
            'Weight': 46600,
            'EN Load': 824,
            'Load Limit': 91000,
            'Type': "Tank"
        },
        'EL-TL-11 FORTALEZA': {
            'Image': '',
            'Weight': 24650,
            'EN Load': 620,
            'Load Limit': 69300,
            'Type': "Tank"
        }
    },
    'Booster': {
        'AB-J-137 KIKAKU': {
            'Image': '',
            'Weight': 1820,
            'EN Load': 266
        },
        'BST-G2/P04': {
            'Image': '',
            'Weight': 1710,
            'EN Load': 250
        },
        'BST-G1/P10': {
            'Image': '',
            'Weight': 1300,
            'EN Load': 130
        },
        'BST-G2/P06SPD': {
            'Image': '',
            'Weight': 1420,
            'EN Load': 390
        },
        'ALULA/21E': {
            'Image': '',
            'Weight': 1900,
            'EN Load': 410
        },
        'FLUEGEL/21Z': {
            'Image': '',
            'Weight': 1980,
            'EN Load': 282
        },
        'BUERZEL/21D': {
            'Image': '',
            'Weight': 2240,
            'EN Load': 480
        },
        'BC-0600 12345': {
            'Image': '',
            'Weight': 1360,
            'EN Load': 180
        },
        'BC-0400 MULE': {
            'Image': '',
            'Weight': 970,
            'EN Load': 200
        },
        'BC-0200 GRIDWALKER': {
            'Image': '',
            'Weight': 2010,
            'EN Load': 244
        },
        'IA-C01B: GILLS': {
            'Image': '',
            'Weight': 1590,
            'EN Load': 400
        },
        'IB-C03B: NGI 001': {
            'Image': '',
            'Weight': 1830,
            'EN Load': 342
        }
    },
    'FCS': {
        'FCS-G1/P01': {
            'Image': '',
            'Weight': 80,
            'EN Load': 198
        },
        'FCS-G2/P05': {
            'Image': '',
            'Weight': 100,
            'EN Load': 232
        },
        'FCS-G2/P10SLT': {
            'Image': '',
            'Weight': 100,
            'EN Load': 209
        },
        'FCS-G2/P12SML': {
            'Image': '',
            'Weight': 130,
            'EN Load': 278
        },
        'FC-006 ABBOT': {
            'Image': '',
            'Weight': 90,
            'EN Load': 266
        },
        'FC-008 TALBOT': {
            'Image': '',
            'Weight': 140,
            'EN Load': 312
        },
        'VE-21A': {
            'Image': '',
            'Weight': 85,
            'EN Load': 364
        },
        'VE-21B': {
            'Image': '',
            'Weight': 160,
            'EN Load': 388
        },
        'IA-C01F: OCELLUS': {
            'Image': '',
            'Weight': 130,
            'EN Load': 292
        },
        'IB-C03F: WLT 001': {
            'Image': '',
            'Weight': 150,
            'EN Load': 486
        }
    },
    'Generator': {
        'AG-J-098 JOSO': {
            'Image': '',
            'Weight': 3420,
            'EN Output': 2600
        },
        'AG-E-013 YABA': {
            'Image': '',
            'Weight': 5080,
            'EN Output': 3000
        },
        'AG-T-005 HOKUSHI': {
            'Image': '',
            'Weight': 7080,
            'EN Output': 3810
        },
        'DF-GN-02 LING-TAI': {
            'Image': '',
            'Weight': 3860,
            'EN Output': 2340
        },
        'DF-GN-06 MING-TANG': {
            'Image': '',
            'Weight': 6320,
            'EN Output': 3160
        },
        'DF-GN-08 SAN-TAI': {
            'Image': '',
            'Weight': 10060,
            'EN Output': 3210
        },
        'VP-20S': {
            'Image': '',
            'Weight': 3800,
            'EN Output': 3200
        },
        'VP-20C': {
            'Image': '',
            'Weight': 5320,
            'EN Output': 3670
        },
        'VP-20D': {
            'Image': '',
            'Weight': 11030,
            'EN Output': 4430
        },
        'VE-20A': {
            'Image': '',
            'Weight': 3590,
            'EN Output': 3120
        },
        'VE-20B': {
            'Image': '',
            'Weight': 5860,
            'EN Output': 2890
        },
        'VE-20C': {
            'Image': '',
            'Weight': 10130,
            'EN Output': 4090
        },
        'IA-C01G: AORTA': {
            'Image': '',
            'Weight': 4330,
            'EN Output': 3500
        },
        'IB-C03G: NGI 000': {
            'Image': '',
            'Weight': 8950,
            'EN Output': 4340
        }
    },
    'Expansion': {
        'ASSAULT ARMOR': {
            'Image': '',
            'Weight': 0,
            'EN Output': 0
        },
        'PULSE ARMOR': {
            'Image': '',
            'Weight': 0,
            'EN Output': 0
        },
        'PULSE PROTECTION': {
            'Image': '',
            'Weight': 0,
            'EN Output': 0
        },
        'TERMINAL ARMOR': {
            'Image': '',
            'Weight': 0,
            'EN Output': 0
        }
    }
}
# Instead of gathering images form url, all the images are downloaded onto the images folder so that the randomizer is instant
# folder name is exactly spelled (case sensitivity does not matter)
images_folder = 'images'
for filename in os.listdir(images_folder):
    for part_type, parts_dict in parts.items():
        for part_name, part_info in parts_dict.items():
            encoded_part_name = urllib.parse.quote(part_name, safe='')
            if encoded_part_name + '.png' == filename:
                parts[part_type][part_name]['Image'] = os.path.join(images_folder, filename)

Build = {}

# Selects a random part from a category, the backbone I suppose
def random_part_selection(category):
    part_keys = list(parts[category].keys())
    selected_key = random.choice(part_keys)
    part_info = parts[category][selected_key]
    print(f"Selected {category}: {selected_key} with info {part_info}")
    return selected_key, part_info

# Function to calculate the actual total EN limit, uses the core's adjusted output and generator's En Output to calculate
def calculate_adjusted_generator_output(core_info, generator_info):
    generator_output_adj = core_info['Generator Output Adj.']
    adjusted_output = math.floor(generator_info['EN Output'] * (generator_output_adj * 0.01))
    print(f"Adjusted generator output: {adjusted_output} (Base {generator_info['EN Output']}, Adj {generator_output_adj}%)")
    return adjusted_output

# Function to generate the build itself. Selects legs first for the load limit, then the core for the adjusted output stat, and then the generator for its EN Output
# For the rest of the parts, they just randomly get added and their stats get added to the AC's weight and EN Load
# If the generation has to be retried because of EN Load, then it will keep the generator (more diversity)
# max is 50 because the software will almost never hit that
def generate_build(parts, retry=False, previous_generator_info=None, previous_leg_info=None, previous_arm_info=None, max_retries=50):
    build = {}
    retries = 0  # Initialize retry counter

    while retries < max_retries:
        build.clear()
        total_weight = 0
        total_arm_weight = 0
        total_en_load = 0

        # Selection of core
        core_category = 'Core'
        selected_core, core_info = random_part_selection(core_category)
        build[core_category] = (selected_core, core_info)
        total_weight += core_info['Weight']
        total_en_load += core_info['EN Load']
        print(f"Selected {core_category}: {selected_core} with EN Load: {core_info['EN Load']}")

        # Define generator, legs, and arms category outside the if-else block (so that we do not default to heavier legs/arms/generators overall)
        generator_category = 'Generator'
        legs_category = 'Legs'
        arms_category = 'Arms'

        if retry and (previous_generator_info or previous_leg_info or previous_arm_info):
            # Reuse the previously selected generator and legs if retrying
            selected_generator, generator_info = previous_generator_info
            selected_legs, legs_info = previous_leg_info
            selected_arms, arms_info = previous_arm_info
            print(f"Reusing {generator_category}: {selected_generator} with EN Output: {generator_info['EN Output']}")
            print(f"Reusing {legs_category}: {selected_legs} with Load Limit: {legs_info['Load Limit']}")
            print(f"Reusing {arms_category}: {selected_arms} with Weapon Load Limit: {arms_info['Arms Load Limit']}")
        else:
            # Selection of generator and legs
            selected_generator, generator_info = random_part_selection(generator_category)
            selected_legs, legs_info = random_part_selection(legs_category)
            selected_arms, arms_info = random_part_selection(arms_category)
            print(f"Selected {generator_category}: {selected_generator} with EN Output: {generator_info['EN Output']}")
            print(f"Selected {legs_category}: {selected_legs} with Load Limit: {legs_info['Load Limit']}")
            print(f"Selected {arms_category}: {selected_arms} with Weapon Load Limit: {arms_info['Arms Load Limit']}")

        build[generator_category] = (selected_generator, generator_info)
        build[legs_category] = (selected_legs, legs_info)
        build[arms_category] = (selected_arms, arms_info)
        load_limit = legs_info['Load Limit']
        arms_load_limit = arms_info['Arms Load Limit']
        total_en_load += legs_info['EN Load']
        total_en_load += arms_info['EN Load']
        total_weight += generator_info['Weight']
        total_weight += arms_info['Weight']
        adjusted_output = calculate_adjusted_generator_output(core_info, generator_info)
        leg_type = legs_info['Type']
        print(f"Leg type: {leg_type}")

        # Configurable exclusion rules for arms and backs
        optional_categories = {
            'RArm': 0.1,  # 10% chance to not include RArm
            'LArm': 0.1,  # 10% chance to not include LArm
            'RBack': 0.1,  # 10% chance to not include RBack
            'LBack': 0.1,  # 10% chance to not include LBack
        }

        # Other mandatory categories
        mandatory_categories = ['FCS', 'Head', 'Expansion']
        if "Non-Tank" in leg_type:
            mandatory_categories.append('Booster')
        else:
            build['Booster'] = ('N/A', {'Image': 'N/A', 'Weight': 0, 'EN Load': 0})
            print("Boosters excluded due to Tank type legs.")

        for category in optional_categories.keys():
            if random.random() > optional_categories[category]:  # Randomly decide based on the assigned chance
                selected_part, part_info = random_part_selection(category)
                build[category] = (selected_part, part_info)
                if 'Weight' in part_info:
                    total_weight += part_info['Weight']
                    total_arm_weight += part_info['Weight']
                if 'EN Load' in part_info:
                    total_en_load += part_info['EN Load']
                if 'Image' in part_info:
                    load_image(part_info['Image'])  # This will cache the image
                print(f"Added {category}: {selected_part} with Weight: {part_info['Weight']}, EN Load: {part_info['EN Load']}")

        for category in mandatory_categories:
            selected_part, part_info = random_part_selection(category)
            build[category] = (selected_part, part_info)
            if 'Weight' in part_info:
                total_weight += part_info['Weight']
            if 'EN Load' in part_info:
                total_en_load += part_info['EN Load']
            if 'Image' in part_info:
                load_image(part_info['Image'])  # This will cache the image
            print(f"Added {category}: {selected_part} with Weight: {part_info['Weight']}, EN Load: {part_info.get('EN Load', 'N/A')}")

        print(f"Total weight (excluding legs): {total_weight}")
        print(f"Total energy load: {total_en_load} / {adjusted_output}")

        if total_en_load <= adjusted_output and total_weight <= load_limit and total_arm_weight <= arms_load_limit:
            return build, total_weight, total_en_load, legs_info['Load Limit'], adjusted_output

        retries += 1
        print(f"Retrying build generation... ({retries}/{max_retries})")

    # If maximum retries reached, return None to indicate failure
    return None

# Global cache dictionary
image_cache = {}

# Downloads all images to ram (takes a bit), so it is faster to switch between builds
# Need to download all images onto disk for fastest response
def load_image(file_path):
    if file_path == 'N/A':
        # Return a placeholder QPixmap for 'N/A' or handle it according to the UI design
        return QPixmap()  # Returns an empty pixmap
    if file_path in image_cache:
        return image_cache[file_path]  # Return the cached pixmap if available
    else:
        pixmap = QPixmap(file_path)
        image_cache[file_path] = pixmap
        return pixmap

#This is the GUI setup
class PartSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.builds = []  # Initialize the builds list here
        self.initUI()

    def initUI(self):
        self.setLayout(QVBoxLayout())  # Set a vertical box layout for the main widget

        # Main Menu Bar for application-level options
        self.mainMenuBar = QMenuBar()
        self.buildMenu = self.mainMenuBar.addMenu('Switch Build')
        self.layout().addWidget(self.mainMenuBar)  # Add the main menu bar to the vertical layout

        # Grid layout for the main content
        self.grid = QGridLayout()
        self.layout().addLayout(self.grid)  # Add grid layout to the main vertical layout

        # Controls for randomization and build selection
        self.setupControlPanel()

        # Generate initial build
        global parts
        self.addBuild(generate_build(parts))

        self.setWindowTitle('Armored Core 6 Randomizer')
        self.setGeometry(100, 100, 1200, 800)
        self.show()

        # Display the first build
        self.displayBuild(0)

    # ok this is actual GUI shenanigans
    def setupControlPanel(self):
        # Randomize button and ComboBox for selecting the number of builds
        self.randomizeButton = QPushButton('Randomize Builds', self)
        self.randomizeButton.clicked.connect(self.randomizeBuilds)

        # ComboBox for selecting the number of builds
        self.buildNumComboBox = QComboBox(self)
        self.buildNumComboBox.addItem("Randomize Build Amt.")
        self.buildNumComboBox.insertSeparator(1)
        for i in range(1, 21): # If you want to change number of builds past 20, here is the line
            self.buildNumComboBox.addItem(str(i))

        # Layout for control elements
        controlsLayout = QHBoxLayout()
        controlsLayout.addWidget(self.randomizeButton)
        controlsLayout.addWidget(self.buildNumComboBox)
        self.layout().addLayout(controlsLayout)  # Add control layout to the main vertical layout

    def addBuild(self, build_data):
        self.builds.append(build_data)
        self.updateBuildMenu()

    def displayBuild(self, index):
        if 0 <= index < len(self.builds):
            self.current_build_index = index
            self.parts, self.total_weight, self.total_en_load, self.legs_load_limit, self.adjusted_generator_output = self.builds[index]
            self.setWindowTitle(f'Armored Core 6 Randomizer - Build {self.current_build_index + 1}')
            self.addPartsToGrid()

    def randomizeBuilds(self):
        try:
            current_text = self.buildNumComboBox.currentText()
            if current_text == "Randomize Build Amt.":
                raise ValueError("No valid number selected")

            num_builds = int(current_text)
            self.builds = []
            for num in range(num_builds):
                build = generate_build(parts)
                if build is None:
                    raise RuntimeError("Maximum retries reached. Unable to generate a valid build.")
                self.builds.append(build)

            self.updateBuildMenu()
            self.displayBuild(0)
        except ValueError as ve:
            QMessageBox.critical(self, "Error", str(ve))
        except RuntimeError as re:
            QMessageBox.critical(self, "Error", str(re))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")




    def updateBuildMenu(self):
        self.buildMenu.clear()
        for i in range(len(self.builds)):
            action = QAction(f'Build #{i + 1}', self)
            action.triggered.connect(lambda _, x=i: self.displayBuild(x))
            self.buildMenu.addAction(action)

    def addPartsToGrid(self):
        for i in reversed(range(self.grid.count())):
            widget = self.grid.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        layout_positions = {
            'Legs': (2, 0), 'Generator': (2, 1), 'Core': (2, 2),
            'Arms': (3, 0), 'LArm': (3, 1), 'RArm': (3, 2),
            'LBack': (4, 0), 'RBack': (4, 1), 'Booster': (4, 2),
            'FCS': (5, 0), 'Head': (5, 1), 'Expansion': (5, 2)
        }

        for category, position in layout_positions.items():
            row, col = position
            frame = QFrame(self)
            frame.setFrameShape(QFrame.StyledPanel)
            vbox = QVBoxLayout()
            cat_label = QLabel(category)
            cat_label.setAlignment(Qt.AlignCenter)
            vbox.addWidget(cat_label)

            if category in self.parts:
                part_name, details = self.parts[category]
                img_label = QLabel(self)
                pixmap = load_image(details['Image'])
                pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
                img_label.setPixmap(pixmap)
                img_label.setAlignment(Qt.AlignCenter)
                name_label = QLabel(part_name)
                name_label.setAlignment(Qt.AlignCenter)
                vbox.addWidget(img_label)
                vbox.addWidget(name_label)
            else:
                error_label = QLabel("N/A")
                error_label.setAlignment(Qt.AlignCenter)
                vbox.addWidget(error_label)

            frame.setLayout(vbox)
            self.grid.addWidget(frame, row, col)

        info_label = QLabel(f"Total Load: {self.total_weight} / {self.legs_load_limit}, "
                            f"Total Energy: {self.total_en_load} / {self.adjusted_generator_output}")
        info_label.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(info_label, 8, 0, 1, 3)  # Information row

if __name__ == '__main__':
    app = QApplication([])
    ex = PartSelector()
    sys.exit(app.exec_())
