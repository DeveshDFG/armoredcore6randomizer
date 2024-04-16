import math
import sys
import urllib3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame, QGridLayout, \
    QAction, QMenuBar, QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import random

# The python dictionary for each part (thanks ChatGPT lol)
parts = {
    'RArm': {
        'MA-J-200 RANSETSU-RF': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/29/01_-_MA-J-200_RANSETSU-RF.png',
            'Weight': 4210,
            'EN Load': 158
        },
        'LR-036 CURTIS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b5/02_-_LR-036_CURTIS.png',
            'Weight': 4150,
            'EN Load': 289
        },
        'LR-037 HARRIS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b5/03_-_LR-037_HARRIS.png',
            'Weight': 4840,
            'EN Load': 441
        },
        'RF-024 TURNER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/ea/04_-_RF-024_TURNER.png',
            'Weight': 3560,
            'EN Load': 102
        },
        'RF-025 SCUDDER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/ca/05_-_RF-025_SCUDDER.png',
            'Weight': 3830,
            'EN Load': 153
        },
        'MA-J-201 RANSETSU-AR': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/a2/06_-_MA-J-201_RANSETSU-AR.png',
            'Weight': 3620,
            'EN Load': 132
        },
        'MG-014 LUDLOW': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9b/07_-_MG-014_LUDLOW.png',
            'Weight': 2450,
            'EN Load': 82
        },
        'DF-MG-02 CHANG-CHEN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/f2/08_-_DF-MG-02_CHANG-CHEN.png',
            'Weight': 3280,
            'EN Load': 143
        },
        'MA-E-210 ETSUJIN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/1a/09_-_MA-E-210_ETSUJIN.png',
            'Weight': 2810,
            'EN Load': 98
        },
        'DF-GA-08 HU-BEN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9b/10_-_DF-GA-08_HU-BEN.png',
            'Weight': 5800,
            'EN Load': 425
        },
        'SG-026 HALDEMAN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/8a/11_-_SG-026_HALDEMAN.png',
            'Weight': 3660,
            'EN Load': 185
        },
        'SG-027 ZIMMERMAN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c0/12_-_SG-027_ZIMMERMAN.png',
            'Weight': 4400,
            'EN Load': 242
        },
        'WR-0777 SWEET SIXTEEN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/01/13_-_WR-0777_SWEET_SIXTEEN.png',
            'Weight': 1640,
            'EN Load': 268
        },
        'HG-003 COQUILLETT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/90/14_-_HG-003_COQUILLETT.png',
            'Weight': 1200,
            'EN Load': 122
        },
        'HG-004 DUCKETT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/aa/15_-_HG-004_DUCKETT.png',
            'Weight': 1650,
            'EN Load': 158
        },
        'MA-E-211 SAMPU': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/36/16_-_MA-E-211_Sampu.png',
            'Weight': 960,
            'EN Load': 62
        },
        'EL-PW-00 VIENTO': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9d/17_-_EL-PW-00_VIENTO.png',
            'Weight': 1180,
            'EN Load': 215
        },
        'VP-66EG': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/dd/Vp-66eg.jpg',
            'Weight': 980,
            'EN Load': 247
        },
        'DF-BA-06 XUAN-GE': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0b/19_-_DF-BA-06_XUAN-GE.png',
            'Weight': 5480,
            'EN Load': 240
        },
        'MAJESTIC': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/dc/20_-_MAJESTIC.png',
            'Weight': 4660,
            'EN Load': 178
        },
        'LITTLE GEM': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/71/21_-_LITTLE_GEM.png',
            'Weight': 3100,
            'EN Load': 192
        },
        '44-141 JVLN ALPHA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b0/22_-_44-141_JVLN_ALPHA.png',
            'Weight': 7420,
            'EN Load': 99
        },
        'DF-GR-07 GOU-CHEN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/43/23_-_DF-GR-07_GOU-CHEN.png',
            'Weight': 5460,
            'EN Load': 385
        },
        'DIZZY': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/3c/24_-_DIZZY.png',
            'Weight': 6420,
            'EN Load': 455
        },
        'IRIDIUM': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/93/25_-_IRIDIUM.png',
            'Weight': 2020,
            'EN Load': 290
        },
        'MA-T-222 KYORAI': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/f0/26_-_MA-T-222_KYORAI.png',
            'Weight': 2890,
            'EN Load': 60
        },
        'WS-1200 THERAPIST': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/bb/28_-_WS-1200_THERAPIST.png',
            'Weight': 3180,
            'EN Load': 82
        },
        'WB-0000 BAD COOK': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/29/29_-_WB-0000_BAD_COOK.png',
            'Weight': 6210,
            'EN Load': 403
        },
        'VP-66LR': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/5c/30_-_VP-66LR.png',
            'Weight': 3560,
            'EN Load': 480
        },
        'VE-66LRA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b7/31_-_VE-66LRA.png',
            'Weight': 4940,
            'EN Load': 532
        },
        'VE-66LRB': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/7e/32_-_VE-66LRB.png',
            'Weight': 7760,
            'EN Load': 604
        },
        'WUERGER/66E': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/bd/33_-_WUERGER-66E.png',
            'Weight': 2880,
            'EN Load': 440
        },
        'VP-66LS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/e2/34_-_VP-66LS.png',
            'Weight': 3540,
            'EN Load': 510
        },
        'VP-66LH': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/4d/35_-_VP-66LH.png',
            'Weight': 2800,
            'EN Load': 395
        },
        'Vvc-760PR': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b5/36_-_Vvc-760PR.png',
            'Weight': 3330,
            'EN Load': 490
        },
        'IA-C01W1: NEBULA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/76/37_-_IA-C01W1_NEBULA.png',
            'Weight': 3890,
            'EN Load': 609
        },
        'IA-C01W6: NB-REDSHIFT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c2/38_-_IA-C01W6_NB-REDSHIFT.png',
            'Weight': 4040,
            'EN Load': 667
        },
        'IB-C03W1: WLT 011': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/98/39_-_IB-C03W1_WLT_011.png',
            'Weight': 9030,
            'EN Load': 850
        },
        '44-142 KRSV': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/56/40_-_44-142_KRSV.png',
            'Weight': 10120,
            'EN Load': 707
        },
        'HI-16: GU-Q1': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9f/41_-_HI-16_GU-Q1.png',
            'Weight': 2110,
            'EN Load': 368
        },
        'HI-18: GU-A2': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/fa/42_-_HI-18_GU-A2.png',
            'Weight': 2650,
            'EN Load': 448
        },
        'HML-G2/P19MLT-04': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/69/43_-_HML-G2-P19MLT-04.png',
            'Weight': 3250,
            'EN Load': 165
        },
        'HML-G3/P08SPL-06': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/d6/44_-_HML-G3-P08SPL-06.png',
            'Weight': 4630,
            'EN Load': 180
        },
        'WS-5000 APERITIF': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/22/45_-_WS-5000_APERITIF.png',
            'Weight': 4600,
            'EN Load': 165
        }
    },
    'LArm': {
        'PB-033M ASHMEAD': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c7/01_-_PB-033M_ASHMEAD.png',
            'Weight': 4150,
            'EN Load': 225
        },
        'DF-ET-09 TAI-YANG-SHOU': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/df/02_-_DF-ET-09_TAI-YANG-SHOU.png',
            'Weight': 3790,
            'EN Load': 160
        },
        'WB-0010 DOUBLE TROUBLE': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/26/03_-_WB-0010_DOUBLE_TROUBLE.png',
            'Weight': 5090,
            'EN Load': 108
        },
        'VP-67EB': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/92/04_-_VP-67EB.png',
            'Weight': 1720,
            'EN Load': 198
        },
        'VP-67LD': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/75/05_-_VP-67LD.png',
            'Weight': 1350,
            'EN Load': 150
        },
        'Vvc-770LB': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/02/06_-_Vvc-770LB.png',
            'Weight': 2060,
            'EN Load': 245
        },
        'Vvc-774LS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/3d/07_-_Vvc-774LS.png',
            'Weight': 3260,
            'EN Load': 328
        },
        'VE-67LLA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/63/08_-_VE-67LLA.png',
            'Weight': 4520,
            'EN Load': 460
        },
        '44-143 HMMR': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/25/09_-_44-143_HMMR.png',
            'Weight': 2410,
            'EN Load': 311
        },
        'HI-32: BU-TT/A': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/41/10_-_HI-32_BU-TT_A.png',
            'Weight': 1800,
            'EN Load': 213
        },
        'IA-C01W2: MOONLIGHT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/00/11_-_IA-C01W2_MOONLIGHT.png',
            'Weight': 2200,
            'EN Load': 544
        },
        'IA-C01W7: ML-REDSHIFT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/00/11_-_IA-C01W2_MOONLIGHT.png',
            'Weight': 2200,
            'EN Load': 544
        },
        'IB-C03W2: WLT 101': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/ca/13_-_IB-C03W2_WLT_101.png',
            'Weight': 2030,
            'EN Load': 642
        },
        'MA-J-200 RANSETSU-RF': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/29/01_-_MA-J-200_RANSETSU-RF.png',
            'Weight': 4210,
            'EN Load': 158
        },
        'LR-036 CURTIS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b5/02_-_LR-036_CURTIS.png',
            'Weight': 4150,
            'EN Load': 289
        },
        'LR-037 HARRIS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b5/03_-_LR-037_HARRIS.png',
            'Weight': 4840,
            'EN Load': 441
        },
        'RF-024 TURNER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/ea/04_-_RF-024_TURNER.png',
            'Weight': 3560,
            'EN Load': 102
        },
        'RF-025 SCUDDER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/ca/05_-_RF-025_SCUDDER.png',
            'Weight': 3830,
            'EN Load': 153
        },
        'MA-J-201 RANSETSU-AR': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/a2/06_-_MA-J-201_RANSETSU-AR.png',
            'Weight': 3620,
            'EN Load': 132
        },
        'MG-014 LUDLOW': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9b/07_-_MG-014_LUDLOW.png',
            'Weight': 2450,
            'EN Load': 82
        },
        'DF-MG-02 CHANG-CHEN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/f2/08_-_DF-MG-02_CHANG-CHEN.png',
            'Weight': 3280,
            'EN Load': 143
        },
        'MA-E-210 ETSUJIN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/1a/09_-_MA-E-210_ETSUJIN.png',
            'Weight': 2810,
            'EN Load': 98
        },
        'DF-GA-08 HU-BEN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9b/10_-_DF-GA-08_HU-BEN.png',
            'Weight': 5800,
            'EN Load': 425
        },
        'SG-026 HALDEMAN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/8a/11_-_SG-026_HALDEMAN.png',
            'Weight': 3660,
            'EN Load': 185
        },
        'SG-027 ZIMMERMAN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c0/12_-_SG-027_ZIMMERMAN.png',
            'Weight': 4400,
            'EN Load': 242
        },
        'WR-0777 SWEET SIXTEEN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/01/13_-_WR-0777_SWEET_SIXTEEN.png',
            'Weight': 1640,
            'EN Load': 268
        },
        'HG-003 COQUILLETT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/90/14_-_HG-003_COQUILLETT.png',
            'Weight': 1200,
            'EN Load': 122
        },
        'HG-004 DUCKETT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/aa/15_-_HG-004_DUCKETT.png',
            'Weight': 1650,
            'EN Load': 158
        },
        'MA-E-211 SAMPU': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/36/16_-_MA-E-211_Sampu.png',
            'Weight': 960,
            'EN Load': 62
        },
        'EL-PW-00 VIENTO': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9d/17_-_EL-PW-00_VIENTO.png',
            'Weight': 1180,
            'EN Load': 215
        },
        'VP-66EG': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/dd/Vp-66eg.jpg',
            'Weight': 980,
            'EN Load': 247
        },
        'DF-BA-06 XUAN-GE': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0b/19_-_DF-BA-06_XUAN-GE.png',
            'Weight': 5480,
            'EN Load': 240
        },
        'MAJESTIC': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/dc/20_-_MAJESTIC.png',
            'Weight': 4660,
            'EN Load': 178
        },
        'LITTLE GEM': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/71/21_-_LITTLE_GEM.png',
            'Weight': 3100,
            'EN Load': 192
        },
        '44-141 JVLN ALPHA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b0/22_-_44-141_JVLN_ALPHA.png',
            'Weight': 7420,
            'EN Load': 99
        },
        'DF-GR-07 GOU-CHEN': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/43/23_-_DF-GR-07_GOU-CHEN.png',
            'Weight': 5460,
            'EN Load': 385
        },
        'DIZZY': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/3c/24_-_DIZZY.png',
            'Weight': 6420,
            'EN Load': 455
        },
        'IRIDIUM': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/93/25_-_IRIDIUM.png',
            'Weight': 2020,
            'EN Load': 290
        },
        'MA-T-222 KYORAI': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/f0/26_-_MA-T-222_KYORAI.png',
            'Weight': 2890,
            'EN Load': 60
        },
        'WS-1200 THERAPIST': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/bb/28_-_WS-1200_THERAPIST.png',
            'Weight': 3180,
            'EN Load': 82
        },
        'WB-0000 BAD COOK': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/29/29_-_WB-0000_BAD_COOK.png',
            'Weight': 6210,
            'EN Load': 403
        },
        'VP-66LR': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/5c/30_-_VP-66LR.png',
            'Weight': 3560,
            'EN Load': 480
        },
        'VE-66LRA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b7/31_-_VE-66LRA.png',
            'Weight': 4940,
            'EN Load': 532
        },
        'VE-66LRB': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/7e/32_-_VE-66LRB.png',
            'Weight': 7760,
            'EN Load': 604
        },
        'WUERGER/66E': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/bd/33_-_WUERGER-66E.png',
            'Weight': 2880,
            'EN Load': 440
        },
        'VP-66LS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/e2/34_-_VP-66LS.png',
            'Weight': 3540,
            'EN Load': 510
        },
        'VP-66LH': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/4d/35_-_VP-66LH.png',
            'Weight': 2800,
            'EN Load': 395
        },
        'Vvc-760PR': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b5/36_-_Vvc-760PR.png',
            'Weight': 3330,
            'EN Load': 490
        },
        'IA-C01W1: NEBULA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/76/37_-_IA-C01W1_NEBULA.png',
            'Weight': 3890,
            'EN Load': 609
        },
        'IA-C01W6: NB-REDSHIFT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c2/38_-_IA-C01W6_NB-REDSHIFT.png',
            'Weight': 4040,
            'EN Load': 667
        },
        'IB-C03W1: WLT 011': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/98/39_-_IB-C03W1_WLT_011.png',
            'Weight': 9030,
            'EN Load': 850
        },
        '44-142 KRSV': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/56/40_-_44-142_KRSV.png',
            'Weight': 10120,
            'EN Load': 707
        },
        'HI-16: GU-Q1': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9f/41_-_HI-16_GU-Q1.png',
            'Weight': 2110,
            'EN Load': 368
        },
        'HI-18: GU-A2': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/fa/42_-_HI-18_GU-A2.png',
            'Weight': 2650,
            'EN Load': 448
        },
        'HML-G2/P19MLT-04': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/69/43_-_HML-G2-P19MLT-04.png',
            'Weight': 3250,
            'EN Load': 165
        },
        'HML-G3/P08SPL-06': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/d6/44_-_HML-G3-P08SPL-06.png',
            'Weight': 4630,
            'EN Load': 180
        },
        'WS-5000 APERITIF': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/22/45_-_WS-5000_APERITIF.png',
            'Weight': 4600,
            'EN Load': 165
        }
    },
    'RBack': {
        'SB-033M MORLEY': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/33/01_-_SB-033M_MORLEY.png',
            'Weight': 5420,
            'EN Load': 455
        },
        'EARSHOT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9c/02_-_EARSHOT.png',
            'Weight': 7230,
            'EN Load': 388
        },
        'SONGBIRDS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0a/03_-_SONGBIRDS.png',
            'Weight': 5500,
            'EN Load': 285
        },
        'VE-60SNA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/35/04_-_VE-60SNA.png',
            'Weight': 6150,
            'EN Load': 826
        },
        'VP-60LCS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/3a/05_-_VP-60LCS.png',
            'Weight': 5190,
            'EN Load': 683
        },
        'VE-60LCA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/88/06_-_VE-60LCA.png',
            'Weight': 14820,
            'EN Load': 1200
        },
        'VP-60LCD': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/95/07_-_VP-60LCD.png',
            'Weight': 7620,
            'EN Load': 784
        },
        'FASAN/60E': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0b/08_-_FASAN_60E.png',
            'Weight': 6270,
            'EN Load': 882
        },
        'KRANICH/60Z': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/10/09_-_KRANICH_60Z.png',
            'Weight': 2100,
            'EN Load': 652
        },
        'EULE/60D': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c8/10_-_EULE_60D.png',
            'Weight': 3060,
            'EN Load': 620
        },
        'IA-C01W3: AURORA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/e6/11_-_IA-C01W3_AURORA.png',
            'Weight': 3330,
            'EN Load': 522
        },
        'BML-G1/P20MLT-04': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/83/12_-_BML-G1_P20MLT-04.png',
            'Weight': 2240,
            'EN Load': 258
        },
        'BML-G2/P03MLT-06': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/eb/13_-_BML-G2_P03MLT-06.png',
            'Weight': 3840,
            'EN Load': 241
        },
        'BML-G2/P05MLT-10': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/08/14_-_BML-G2_P05MLT-10.png',
            'Weight': 5220,
            'EN Load': 320
        },
        'BML-G2/P19SPL-12': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/74/15_-_BML-G2_P19SPL-12.png',
            'Weight': 3630,
            'EN Load': 325
        },
        'BML-G2/P16SPL-08': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/ff/16_-_BML-G2_P16SPL-08.png',
            'Weight': 2800,
            'EN Load': 228
        },
        'BML-G2/P17SPL-16': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/68/17_-_BML-G2_P17SPL-16.png',
            'Weight': 5010,
            'EN Load': 510
        },
        'BML-G1/P31DUO-02': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/d0/18_-_BML-G1_P31DUO-02.png',
            'Weight': 1900,
            'EN Load': 182
        },
        'BML-G1/P32DUO-03': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/e0/19_-_BML-G1_P32DUO-03.png',
            'Weight': 3450,
            'EN Load': 262
        },
        'BML-G2/P08DUO-03': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c6/20_-_BML-G2_P08DUO-03.png',
            'Weight': 4020,
            'EN Load': 332
        },
        'BML-G1/P01VTC-04': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/1b/21_-_BML-G1_P01VTC-04.png',
            'Weight': 2240,
            'EN Load': 258
        },
        'BML-G1/P03VTC-08': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/83/22_-_BML-G1_P03VTC-08.png',
            'Weight': 3520,
            'EN Load': 380
        },
        'BML-G1/P07VTC-12': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/7d/23_-_BML-G1_P07VTC-12.png',
            'Weight': 5010,
            'EN Load': 525
        },
        'BML-G3/P04ACT-01': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/5e/24_-_BML-G3_P04ACT-01.png',
            'Weight': 2680,
            'EN Load': 213
        },
        'BML-G3/P05ACT-02': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/71/25_-_BML-G3_P05ACT-02.png',
            'Weight': 4320,
            'EN Load': 424
        },
        'BML-G1/P29CNT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/a1/26_-_BML-G1_P29CNT.png',
            'Weight': 6370,
            'EN Load': 150
        },
        'WR-0999 DELIVERY BOY': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/86/27_-_WR-0999_DELIVERY_BOY.png',
            'Weight': 6890,
            'EN Load': 499
        },
        'WS-5001 SOUP': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/79/28_-_WS-5001_SOUP.png',
            'Weight': 5620,
            'EN Load': 685
        },
        '45-091 JVLN BETA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/21/29_-_45-091_JVLN_BETA.png',
            'Weight': 4250,
            'EN Load': 425
        },
        'EL-PW-01 TRUENO': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/ae/30_-_EL-PW-01_TRUENO.png',
            'Weight': 3100,
            'EN Load': 420
        },
        'Vvc-703PM': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/5e/31_-_Vvc-703PM.png',
            'Weight': 2720,
            'EN Load': 245
        },
        'Vvc-706PM': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/6e/32_-_Vvc-706PM.png',
            'Weight': 4800,
            'EN Load': 342
        },
        'Vvc-70VPM': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/ed/33_-_Vvc-70VMP.png',
            'Weight': 3760,
            'EN Load': 268
        },
        'IB-C03W3: NGI 006': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/15/34_-_IB-C03W3_NGI_006.png',
            'Weight': 4200,
            'EN Load': 783
        },
        'BO-044 HUXLEY': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0d/35_-_BO-044_HUXLEY.png',
            'Weight': 2230,
            'EN Load': 435
        },
        '45-091 ORBT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c0/36_-_45-091_ORBT.png',
            'Weight': 2010,
            'EN Load': 446
        },
        'VP-60LT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/4b/37_-_VP-60LT.png',
            'Weight': 2800,
            'EN Load': 560
        },
        'Vvc-700LD': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c2/38_-_Vvc-700LD.png',
            'Weight': 3800,
            'EN Load': 570
        },
        'DF-GA-09 SHAO-WEI': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9a/DF-GA-09_SHAO-WEI.png   ',
            'Weight': 3960,
            'EN Load': 404
        }
    },
    'LBack': {
        'VP-61PS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c3/01_-_VP-61PS.png',
            'Weight': 2700,
            'EN Load': 310
        },
        'SI-24: SU-Q5': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9b/02_-_SI-24_SU-Q5.png',
            'Weight': 2010,
            'EN Load': 220
        },
        'SI-27: SU-R8': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b8/03_-_SI-27_SU-R8.png',
            'Weight': 3150,
            'EN Load': 323
        },
        'VP-61PB': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/99/04_-_VP-61PB.png',
            'Weight': 1920,
            'EN Load': 285
        },
        'SI-29: SU-TT/C': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/cf/05_-_SI-29_SU-TT_C.png',
            'Weight': 3360,
            'EN Load': 385
        },
        'VE-61PSA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/52/06_-_VE-61PSA.png',
            'Weight': 4100,
            'EN Load': 450
        },
        'IB-C03W4: NGI 028': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0d/07_-_IB-C03W4_NGI_028.png',
            'Weight': 2170,
            'EN Load': 800
        },
        'SB-033M MORLEY': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/33/01_-_SB-033M_MORLEY.png',
            'Weight': 5420,
            'EN Load': 455
        },
        'EARSHOT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9c/02_-_EARSHOT.png',
            'Weight': 7230,
            'EN Load': 388
        },
        'SONGBIRDS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0a/03_-_SONGBIRDS.png',
            'Weight': 5500,
            'EN Load': 285
        },
        'VE-60SNA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/35/04_-_VE-60SNA.png',
            'Weight': 6150,
            'EN Load': 826
        },
        'VP-60LCS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/3a/05_-_VP-60LCS.png',
            'Weight': 5190,
            'EN Load': 683
        },
        'VE-60LCA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/88/06_-_VE-60LCA.png',
            'Weight': 14820,
            'EN Load': 1200
        },
        'VP-60LCD': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/95/07_-_VP-60LCD.png',
            'Weight': 7620,
            'EN Load': 784
        },
        'FASAN/60E': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0b/08_-_FASAN_60E.png',
            'Weight': 6270,
            'EN Load': 882
        },
        'KRANICH/60Z': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/10/09_-_KRANICH_60Z.png',
            'Weight': 2100,
            'EN Load': 652
        },
        'EULE/60D': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c8/10_-_EULE_60D.png',
            'Weight': 3060,
            'EN Load': 620
        },
        'IA-C01W3: AURORA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/e6/11_-_IA-C01W3_AURORA.png',
            'Weight': 3330,
            'EN Load': 522
        },
        'BML-G1/P20MLT-04': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/83/12_-_BML-G1_P20MLT-04.png',
            'Weight': 2240,
            'EN Load': 258
        },
        'BML-G2/P03MLT-06': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/eb/13_-_BML-G2_P03MLT-06.png',
            'Weight': 3840,
            'EN Load': 241
        },
        'BML-G2/P05MLT-10': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/08/14_-_BML-G2_P05MLT-10.png',
            'Weight': 5220,
            'EN Load': 320
        },
        'BML-G2/P19SPL-12': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/74/15_-_BML-G2_P19SPL-12.png',
            'Weight': 3630,
            'EN Load': 325
        },
        'BML-G2/P16SPL-08': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/ff/16_-_BML-G2_P16SPL-08.png',
            'Weight': 2800,
            'EN Load': 228
        },
        'BML-G2/P17SPL-16': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/68/17_-_BML-G2_P17SPL-16.png',
            'Weight': 5010,
            'EN Load': 510
        },
        'BML-G1/P31DUO-02': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/d0/18_-_BML-G1_P31DUO-02.png',
            'Weight': 1900,
            'EN Load': 182
        },
        'BML-G1/P32DUO-03': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/e0/19_-_BML-G1_P32DUO-03.png',
            'Weight': 3450,
            'EN Load': 262
        },
        'BML-G2/P08DUO-03': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c6/20_-_BML-G2_P08DUO-03.png',
            'Weight': 4020,
            'EN Load': 332
        },
        'BML-G1/P01VTC-04': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/1b/21_-_BML-G1_P01VTC-04.png',
            'Weight': 2240,
            'EN Load': 258
        },
        'BML-G1/P03VTC-08': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/83/22_-_BML-G1_P03VTC-08.png',
            'Weight': 3520,
            'EN Load': 380
        },
        'BML-G1/P07VTC-12': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/7d/23_-_BML-G1_P07VTC-12.png',
            'Weight': 5010,
            'EN Load': 525
        },
        'BML-G3/P04ACT-01': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/5e/24_-_BML-G3_P04ACT-01.png',
            'Weight': 2680,
            'EN Load': 213
        },
        'BML-G3/P05ACT-02': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/71/25_-_BML-G3_P05ACT-02.png',
            'Weight': 4320,
            'EN Load': 424
        },
        'BML-G1/P29CNT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/a1/26_-_BML-G1_P29CNT.png',
            'Weight': 6370,
            'EN Load': 150
        },
        'WR-0999 DELIVERY BOY': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/86/27_-_WR-0999_DELIVERY_BOY.png',
            'Weight': 6890,
            'EN Load': 499
        },
        'WS-5001 SOUP': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/79/28_-_WS-5001_SOUP.png',
            'Weight': 5620,
            'EN Load': 685
        },
        '45-091 JVLN BETA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/21/29_-_45-091_JVLN_BETA.png',
            'Weight': 4250,
            'EN Load': 425
        },
        'EL-PW-01 TRUENO': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/ae/30_-_EL-PW-01_TRUENO.png',
            'Weight': 3100,
            'EN Load': 420
        },
        'Vvc-703PM': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/5e/31_-_Vvc-703PM.png',
            'Weight': 2720,
            'EN Load': 245
        },
        'Vvc-706PM': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/6e/32_-_Vvc-706PM.png',
            'Weight': 4800,
            'EN Load': 342
        },
        'Vvc-70VPM': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/ed/33_-_Vvc-70VMP.png',
            'Weight': 3760,
            'EN Load': 268
        },
        'IB-C03W3: NGI 006': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/15/34_-_IB-C03W3_NGI_006.png',
            'Weight': 4200,
            'EN Load': 783
        },
        'BO-044 HUXLEY': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0d/35_-_BO-044_HUXLEY.png',
            'Weight': 2230,
            'EN Load': 435
        },
        '45-091 ORBT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c0/36_-_45-091_ORBT.png',
            'Weight': 2010,
            'EN Load': 446
        },
        'VP-60LT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/4b/37_-_VP-60LT.png',
            'Weight': 2800,
            'EN Load': 560
        },
        'Vvc-700LD': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c2/38_-_Vvc-700LD.png',
            'Weight': 3800,
            'EN Load': 570
        },
        'DF-GA-09 SHAO-WEI': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9a/DF-GA-09_SHAO-WEI.png   ',
            'Weight': 3960,
            'EN Load': 404
        }
    },
    'Head': {
        'AH-J-124 BASHO': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/46/Part_icon_ACVI_AH-J-124_BASHO.png',
            'Weight': 4600,
            'EN Load': 95
        },
        'AH-J-124/RC JAILBREAK': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/8c/Part_icon_ACVI_AH-J-124_RC_JAILBREAK.png',
            'Weight': 4250,
            'EN Load': 95
        },
        'HD-011 MELANDER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/77/Part_icon_ACVI_HD-011_MELANDER.png',
            'Weight': 3160,
            'EN Load': 135
        },
        'HD-033M VERRILL': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/7e/Part_icon_ACVI_HD-033M_VERRILL.png',
            'Weight': 3830,
            'EN Load': 240
        },
        'HD-012 MELANDER C3': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/4e/Part_icon_ACVI_HD-012_MELANDER_C3.png',
            'Weight': 3300,
            'EN Load': 165
        },
        'DF-HD-08 TIAN-QIANG': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/e2/Part_icon_ACVI_DF-HD-08_TIAN-QIANG.png',
            'Weight': 1230,
            'EN Load': 88
        },
        'VP-44S': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/ab/Part_icon_ACVI_VP-44S.png',
            'Weight': 3080,
            'EN Load': 148
        },
        'VP-44D': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/44/Part_icon_ACVI_VP-44D.png',
            'Weight': 3260,
            'EN Load': 177
        },
        'NACHTREIHER/44E': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/a6/Part_icon_ACVI_NACHTREIHER_44E.png',
            'Weight': 2320,
            'EN Load': 210
        },
        'KASUAR/44Z': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/ca/Part_icon_ACVI_KASUAR_44Z.png',
            'Weight': 2590,
            'EN Load': 254
        },
        'VE-44A': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/52/Part_icon_ACVI_VE-44A.png',
            'Weight': 3640,
            'EN Load': 182
        },
        'VE-44B': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/cc/Part_icon_ACVI_VE-44B.png',
            'Weight': 4320,
            'EN Load': 265
        },
        'HC-2000 FINDER EYE': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/e6/Part_icon_ACVI_HC-2000_FINDER_EYE.png',
            'Weight': 2670,
            'EN Load': 125
        },
        'HC-2000/BC SHADE EYE': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/04/Part_icon_ACVI_HC-2000_BC_SHADE_EYE.png',
            'Weight': 3090,
            'EN Load': 163
        },
        'HC-3000 WRECKER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/2c/Part_icon_ACVI_HC-3000_WRECKER.png',
            'Weight': 3800,
            'EN Load': 102
        },
        'HS-5000 APPETIZER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/8f/Part_icon_ACVI_HS-5000_APPETIZER.png',
            'Weight': 3000,
            'EN Load': 103
        },
        'EL-TH-10 FIRMEZA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/8e/Part_icon_ACVI_EL-TH-10_FIRMEZA.png',
            'Weight': 2570,
            'EN Load': 134
        },
        'EL-PH-00 ALBA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/d5/Part_icon_ACVI_EL-PH-00_ALBA.png',
            'Weight': 2800,
            'EN Load': 205
        },
        '20-081 MIND ALPHA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/cb/Part_icon_ACVI_20-081_MIND_ALPHA.png',
            'Weight': 3350,
            'EN Load': 142
        },
        '20-082 MIND BETA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/a0/Part_icon_ACVI_20-082_MIND_BETA.png',
            'Weight': 3460,
            'EN Load': 128
        },
        'IA-C01H: EPHEMERA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/6f/Part_icon_ACVI_IA-C01H_EPHEMERA.png',
            'Weight': 4330,
            'EN Load': 233
        },
        'IB-C03H: HAL 826': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/2f/Part_icon_ACVI_IB-C03H_HAL_826.png',
            'Weight': 3760,
            'EN Load': 215
        },
        'LAMMERGEIER/44F': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/ee/LAMMERGEIER-44F.png',
            'Weight': 1050,
            'EN Load': 220
        }
    },
    'Core': {
        'AC-J-120 BASHO': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/1c/Part_icon_ACVI_AC-J-120_BASHO.png',
            'Weight': 16100,
            'EN Load': 300,
            'Generator Output Adj.': 83
        },
        'AC-J-120/RC JAILBREAK': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/05/Part_icon_ACVI_AC-J-120_RC_JAILBREAK.png',
            'Weight': 12350,
            'EN Load': 300,
            'Generator Output Adj.': 83
        },
        'BD-011 MELANDER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/40/Part_icon_ACVI_BD-011_MELANDER.png',
            'Weight': 15800,
            'EN Load': 304,
            'Generator Output Adj.': 105
        },
        'BD-012 MELANDER C3': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/f6/Part_icon_ACVI_BD-012_MELANDER_C3.png',
            'Weight': 14050,
            'EN Load': 322,
            'Generator Output Adj.': 102
        },
        'DF-BD-08 TIAN-QIANG': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b5/Part_icon_ACVI_DF-BD-08_TIAN-QIANG.png',
            'Weight': 20650,
            'EN Load': 388,
            'Generator Output Adj.': 114
        },
        'VP-40S': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/69/Part_icon_ACVI_VP-40S.png',
            'Weight': 15030,
            'EN Load': 337,
            'Generator Output Adj.': 106
        },
        'NACHTREIHER/40E': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b6/Part_icon_ACVI_NACHTREIHER_40E.png',
            'Weight': 9820,
            'EN Load': 330,
            'Generator Output Adj.': 84
        },
        'VE-40A': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/99/Part_icon_ACVI_VE-40A.png',
            'Weight': 21100,
            'EN Load': 432,
            'Generator Output Adj.': 122
        },
        'CC-2000 ORBITER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/50/Part_icon_ACVI_CC-2000_ORBITER.png',
            'Weight': 12650,
            'EN Load': 267,
            'Generator Output Adj.': 103
        },
        'CC-3000 WRECKER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/1a/Part_icon_ACVI_CC-3000_WRECKER.png',
            'Weight': 19000,
            'EN Load': 310,
            'Generator Output Adj.': 96
        },
        'CS-5000 MAIN DISH': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/65/Part_icon_ACVI_CS-5000_MAIN_DISH.png',
            'Weight': 23600,
            'EN Load': 413,
            'Generator Output Adj.': 97
        },
        'EL-TC-10 FIRMEZA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/da/Part_icon_ACVI_EL-TC-10_FIRMEZA.png',
            'Weight': 10890,
            'EN Load': 351,
            'Generator Output Adj.': 104
        },
        'EL-PC-00 ALBA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/fc/Part_icon_ACVI_EL-PC-00_ALBA.png',
            'Weight': 12000,
            'EN Load': 315,
            'Generator Output Adj.': 101
        },
        '07-061 MIND ALPHA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/37/Part_icon_ACVI_ACVI_07-061_MIND_ALPHA.png',
            'Weight': 16510,
            'EN Load': 364,
            'Generator Output Adj.': 112
        },
        'IA-C01C: EPHEMERA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/6d/Part_icon_ACVI_IA-C01C_EPHEMERA.png',
            'Weight': 13200,
            'EN Load': 412,
            'Generator Output Adj.': 126
        },
        'IB-C03C: HAL 826': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/98/Part_icon_ACVI_IB-C03C_HAL_826.png',
            'Weight': 18520,
            'EN Load': 366,
            'Generator Output Adj.': 120
        },
        'LAMMERGEIER/40F': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/4a/LAMMERGEIER-40F.png',
            'Weight': 9700,
            'EN Load': 341,
            'Generator Output Adj.': 117
        }
    },
    'Arms': {
        'AA-J-123 BASHO': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/e0/Part_icon_ACVI_AA-J-123_BASHO.png',
            'Weight': 10480,
            'EN Load': 210,
            'Arms Load Limit': 10520
        },
        'AA-J-123/RC JAILBREAK': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/dd/Part_icon_ACVI_AA-J-123_RC_JAILBREAK.png',
            'Weight': 8480,
            'EN Load': 210,
            'Arms Load Limit': 10520
        },
        'AR-011 MELANDER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/23/Part_icon_ACVI_AR-011_MELANDER.png',
            'Weight': 13650,
            'EN Load': 265,
            'Arms Load Limit': 15100
        },
        'AR-012 MELANDER C3': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/f5/Part_icon_ACVI_AR-012_MELANDER_C3.png',
            'Weight': 12300,
            'EN Load': 232,
            'Arms Load Limit': 12000
        },
        'DF-AR-08 TIAN-QIANG': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/66/Part_icon_ACVI_DF-AR-08_TIAN-QIANG.png',
            'Weight': 20020,
            'EN Load': 295,
            'Arms Load Limit': 19500
        },
        'DF-AR-09 TIAN-LAO': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/52/Part_icon_ACVI_DF-AR-09_TIAN-LAO.png',
            'Weight': 26740,
            'EN Load': 266,
            'Arms Load Limit': 17200
        },
        'VP-46S': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/ca/Part_icon_ACVI_VP-46S.png',
            'Weight': 14020,
            'EN Load': 278,
            'Arms Load Limit': 14520
        },
        'VP-46D': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/f5/Part_icon_ACVI_VP-46D.png',
            'Weight': 10990,
            'EN Load': 248,
            'Arms Load Limit': 11800
        },
        'NACHTREIHER/46E': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/be/Part_icon_ACVI_NACHTREIHER_46E.png',
            'Weight': 11420,
            'EN Load': 302,
            'Arms Load Limit': 12730
        },
        'VE-46A': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/a2/Part_icon_ACVI_VE-46A.png',
            'Weight': 22210,
            'EN Load': 380,
            'Arms Load Limit': 21300
        },
        'AC-2000 TOOL ARM': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/e2/Part_icon_ACVI_AC-2000_TOOL_ARM.png',
            'Weight': 11300,
            'EN Load': 216,
            'Arms Load Limit': 13300
        },
        'AC-3000 WRECKER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/d1/Part_icon_ACVI_AC-3000_WRECKER.png',
            'Weight': 14650,
            'EN Load': 220,
            'Arms Load Limit': 15800
        },
        'AS-5000 SALAD': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/87/Part_icon_ACVI_AS-5000_SALAD.png',
            'Weight': 20940,
            'EN Load': 324,
            'Arms Load Limit': 18700
        },
        'EL-TA-10 FIRMEZA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/d8/Part_icon_ACVI_EL-TA-10_FIRMEZA.png',
            'Weight': 11220,
            'EN Load': 270,
            'Arms Load Limit': 13540
        },
        'EL-PA-00 ALBA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/7b/Part_icon_ACVI_EL-PA-00_ALBA.png',
            'Weight': 9810,
            'EN Load': 315,
            'Arms Load Limit': 11350
        },
        '04-101 MIND ALPHA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0a/Part_icon_ACVI_04-101_MIND_ALPHA.png',
            'Weight': 16960,
            'EN Load': 358,
            'Arms Load Limit': 15550
        },
        'IA-C01A: EPHEMERA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/88/Part_icon_ACVI_IA-C01A_EPHEMERA.png',
            'Weight': 12700,
            'EN Load': 312,
            'Arms Load Limit': 12680
        },
        'IB-C03A: HAL 826': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/c4/Part_icon_ACVI_IB-C03A_HAL_826.png',
            'Weight': 14160,
            'EN Load': 300,
            'Arms Load Limit': 14000
        },
        'LAMMERGEIER/46F': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/a8/LAMMERGEIER-46F.png',
            'Weight': 9700,
            'EN Load': 328,
            'Arms Load Limit': 11970
        }
    },
    'Legs': {
        'Bipedal': {
            'AL-J-121 BASHO': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/6e/Part_icon_ACVI_AL-J-121_BASHO.png',
                'Weight': 20520,
                'EN Load': 300,
                'Load Limit': 62600
            },
            'AL-J-121/RC JAILBREAK': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/51/Part_icon_ACVI_AL-J-121_RC_JAILBREAK.png',
                'Weight': 18560,
                'EN Load': 300,
                'Load Limit': 62600
            },
            'LG-011 MELANDER': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/09/Part_icon_ACVI_LG-011_MELANDER.png',
                'Weight': 18700,
                'EN Load': 365,
                'Load Limit': 60520
            },
            'LG-012 MELANDER C3': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9e/Part_icon_LG-012_MELANDER_C3.png',
                'Weight': 17210,
                'EN Load': 355,
                'Load Limit': 55440
            },
            'DF-LG-08 TIAN-QIANG': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/34/Part_icon_ACVI_DF-LG-08_TIAN-QIANG.png',
                'Weight': 23600,
                'EN Load': 400,
                'Load Limit': 82600
            },
            'VP-422': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/13/Part_icon_ACVI_VP-422.png',
                'Weight': 17900,
                'EN Load': 387,
                'Load Limit': 58620
            },
            'NACHTREIHER/42E': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/11/Part_icon_ACVI_NACHTREIHER_42E.png',
                'Weight': 14030,
                'EN Load': 462,
                'Load Limit': 48650
            },
            'VE-42A': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/ee/Part_icon_ACVI_VE-42A.png',
                'Weight': 28950,
                'EN Load': 465,
                'Load Limit': 85700
            },
            '2C-2000 CRAWLER': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/5b/Part_icon_ACVI_2C-2000_CRAWLER.png',
                'Weight': 16300,
                'EN Load': 280,
                'Load Limit': 51200
            },
            '2C-3000 WRECKER': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/29/Part_icon_ACVI_2C-3000_WRECKER.png',
                'Weight': 21680,
                'EN Load': 680,
                'Load Limit': 68900
            },
            '2S-5000 DESSERT': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/7f/Part_icon_ACVI_2S-5000_DESSERT.png',
                'Weight': 25880,
                'EN Load': 420,
                'Load Limit': 77100
            },
            'EL-TL-10 FIRMEZA': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/9b/Part_icon_ACVI_EL-TL-10_FIRMEZA.png',
                'Weight': 11200,
                'EN Load': 378,
                'Load Limit': 52100
            },
            'EL-PL-00 ALBA': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0d/Part_icon_ACVI_EL-PL-00_ALBA.png',
                'Weight': 13150,
                'EN Load': 360,
                'Load Limit': 50100
            },
            '06-041 MIND ALPHA': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/40/Part_icon_ACVI_06-041_MIND_ALPHA.png',
                'Weight': 22110,
                'EN Load': 432,
                'Load Limit': 63810
            },
            'IA-C01L: EPHEMERA': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/20/Part_icon_ACVI_IA-C01L_EPHEMERA.png',
                'Weight': 15200,
                'EN Load': 398,
                'Load Limit': 55050
            },
            'IB-C03L: HAL 826': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/54/Part_icon_ACVI_IB-C03L_HAL_826.png',
                'Weight': 20890,
                'EN Load': 385,
                'Load Limit': 64900
            }
        },
        'Tetrapod': {
            'LG-033M VERRILL': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/ae/Part_icon_ACVI_LG-033M_VERRILL.png',
                'Weight': 36200,
                'EN Load': 675,
                'Load Limit': 76200
            },
            'VP-424': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/95/Part_icon_ACVI_VP-424.png',
                'Weight': 31600,
                'EN Load': 760,
                'Load Limit': 69800
            },
            'LAMMERGEIER/42F': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/09/LAMMERGEIER-42F.png',
                'Weight': 22430,
                'EN Load': 790,
                'Load Limit': 52460
            }
        },
        'Reverse-Joint': {
            'KASUAR/42Z': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/97/Part_icon_ACVI_KASUAR_42Z.png',
                'Weight': 19060,
                'EN Load': 388,
                'Load Limit': 47820
            },
            '06-042 MIND BETA': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/35/Part_icon_ACVI_06-042_MIND_BETA.png',
                'Weight': 22200,
                'EN Load': 426,
                'Load Limit': 61600
            },
            'RC-2000 SPRING CHICKEN': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/f7/Part_icon_ACVI_RC-2000_SPRING_CHICKEN.png',
                'Weight': 25890,
                'EN Load': 402,
                'Load Limit': 68360
            }
        },
        'Tank': {
            'LG-022T BORNEMISSZA': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/d7/Part_icon_ACVI_LG-022T_BORNEMISSZA.png',
                'Weight': 49800,
                'EN Load': 455,
                'Load Limit': 100300
            },
            'VE-42B': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/c/ca/Part_icon_ACVI_VE-42B.png',
                'Weight': 46600,
                'EN Load': 824,
                'Load Limit': 91000
            },
            'EL-TL-11 FORTALEZA': {
                'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/67/Part_icon_ACVI_EL-TL-11_FORTALEZA.png',
                'Weight': 24650,
                'EN Load': 620,
                'Load Limit': 69300
            }
        }
    },
    'Booster': {
        'AB-J-137 KIKAKU': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/e9/Part_icon_ACVI_AB-J-137_KIKAKU.png',
            'Weight': 1820,
            'EN Load': 266
        },
        'BST-G2/P04': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/30/Part_icon_ACVI_BST-G2_P04.png',
            'Weight': 1710,
            'EN Load': 250
        },
        'BST-G1/P10': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/6b/Part_icon_ACVI_BST-G1_P10.png',
            'Weight': 1300,
            'EN Load': 130
        },
        'BST-G2/P06SPD': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/d/d2/Part_icon_ACVI_BST-G2_P06SPD.png',
            'Weight': 1420,
            'EN Load': 390
        },
        'ALULA/21E': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/7e/Part_icon_ACVI_ALULA_21E.png',
            'Weight': 1900,
            'EN Load': 410
        },
        'FLUEGEL/21Z': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/eb/Part_icon_ACVI_FLUEGEL_21Z.png',
            'Weight': 1980,
            'EN Load': 282
        },
        'BUERZEL/21D': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/22/Part_icon_ACVI_BUERZEL_21D.png',
            'Weight': 2240,
            'EN Load': 480
        },
        'BC-0600 12345': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/81/Part_icon_ACVI_BC-0600_12345.png',
            'Weight': 1360,
            'EN Load': 180
        },
        'BC-0400 MULE': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/36/Part_icon_ACVI_BC-0400_MULE.png',
            'Weight': 970,
            'EN Load': 200
        },
        'BC-0200 GRIDWALKER': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b7/Part_icon_ACVI_BC-0200_GRIDWALKER.png',
            'Weight': 2010,
            'EN Load': 244
        },
        'IA-C01B: GILLS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/b9/Part_icon_ACVI_IA-C01B_GILLS.png',
            'Weight': 1590,
            'EN Load': 400
        },
        'IB-C03B: NGI 001': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/07/Part_icon_ACVI_IB-C03B_NGI_001.png',
            'Weight': 1830,
            'EN Load': 342
        }
    },
    'FCS': {
        'FCS-G1/P01': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/7a/01_-_FCS-G1_P01.png',
            'Weight': 80,
            'EN Load': 198
        },
        'FCS-G2/P05': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/ef/02_-_FCS-G2_P05.png',
            'Weight': 100,
            'EN Load': 232
        },
        'FCS-G2/P10SLT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/b/bf/03_-_FCS-G2_P10SLT.png',
            'Weight': 100,
            'EN Load': 209
        },
        'FCS-G2/P12SML': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/3e/04_-_FCS-G2_P12SML.png',
            'Weight': 130,
            'EN Load': 278
        },
        'FC-006 ABBOT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/29/05_-_FC-006_ABBOT.png',
            'Weight': 90,
            'EN Load': 266
        },
        'FC-008 TALBOT': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/32/06_-_FC-008_TALBOT.png',
            'Weight': 140,
            'EN Load': 312
        },
        'VE-21A': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/7a/07_-_VE-21A.png',
            'Weight': 85,
            'EN Load': 364
        },
        'VE-21B': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/4f/08_-_VE-21B.png',
            'Weight': 160,
            'EN Load': 388
        },
        'IA-C01F: OCELLUS': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/8/81/09_-_IA-C01F_OCELLUS.png',
            'Weight': 130,
            'EN Load': 292
        },
        'IB-C03F: WLT 001': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/e5/10_-_IB-C03F_WLT_001.png',
            'Weight': 150,
            'EN Load': 486
        }
    },
    'Generator': {
        'AG-J-098 JOSO': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/e/ec/01_-_AG-J-098_JOSO.png',
            'Weight': 3420,
            'EN Output': 2600
        },
        'AG-E-013 YABA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/f/f6/02_-_AG-E-013_YABA.png',
            'Weight': 5080,
            'EN Output': 3000
        },
        'AG-T-005 HOKUSHI': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/34/03_-_AG-T-005_HOKUSHI.png',
            'Weight': 7080,
            'EN Output': 3810
        },
        'DF-GN-02 LING-TAI': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/4e/04_-_DF-GN-02_LING-TAI.png',
            'Weight': 3860,
            'EN Output': 2340
        },
        'DF-GN-06 MING-TANG': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/1/1a/05_-_DF-GN-06_MING-TANG.png',
            'Weight': 6320,
            'EN Output': 3160
        },
        'DF-GN-08 SAN-TAI': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0c/06_-_DF-GN-08_SAN-TAI.png',
            'Weight': 10060,
            'EN Output': 3210
        },
        'VP-20S': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/a/a5/07_-_VP-20S.png',
            'Weight': 3800,
            'EN Output': 3200
        },
        'VP-20C': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/4/46/08_-_VP-20C.png',
            'Weight': 5320,
            'EN Output': 3670
        },
        'VP-20D': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/2/2f/09_-_VP-20D.png',
            'Weight': 11030,
            'EN Output': 4430
        },
        'VE-20A': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/77/10_-_VE-20A.png',
            'Weight': 3590,
            'EN Output': 3120
        },
        'VE-20B': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/5/51/11_-_VE-20B.png',
            'Weight': 5860,
            'EN Output': 2890
        },
        'VE-20C': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/6/6b/12_-_VE-20C.png',
            'Weight': 10130,
            'EN Output': 4090
        },
        'IA-C01G: AORTA': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/99/13_-_IA-C01G_AORTA.png',
            'Weight': 4330,
            'EN Output': 3500
        },
        'IB-C03G: NGI 000': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/0/0f/14_-_IB-C03G_NGI_000.png',
            'Weight': 8950,
            'EN Output': 4340
        }
    },
    'Expansion': {
        'ASSAULT ARMOR': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/93/01_-_ASSAULT_ARMOR.png',
            'Weight': 0,
            'EN Output': 0
        },
        'PULSE ARMOR': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/3/3e/02_-_PULSE_ARMOR.png',
            'Weight': 0,
            'EN Output': 0
        },
        'PULSE PROTECTION': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/9/93/03_-_PULSE_PROTECTION.png',
            'Weight': 0,
            'EN Output': 0
        },
        'TERMINAL ARMOR': {
            'Image': 'https://static.wikia.nocookie.net/armoredcore/images/7/7b/04_-_TERMINAL_ARMOR.png',
            'Weight': 0,
            'EN Output': 0
        }
    }
}

Build = {}

# Selects a random part from a category, the backbone I suppose
def random_part_selection(category):
    if category == 'Legs':
        leg_types = list(parts[category].keys())
        selected_type = random.choice(leg_types)
        leg_options = list(parts[category][selected_type].keys())
        selected_leg = random.choice(leg_options)
        part_info = parts[category][selected_type][selected_leg]
        print(f"Selected {category} ({selected_type}): {selected_leg} with info {part_info}")
        return f"{selected_type} - {selected_leg}", part_info
    else:
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
def generate_build(parts, retry=False, previous_generator_info=None):
    build = {}
    total_weight = 0
    total_en_load = 0

    # Selection of legs
    legs_category = 'Legs'
    selected_legs, legs_info = random_part_selection(legs_category)
    build[legs_category] = (selected_legs, legs_info)
    total_en_load += legs_info.get('EN Load', 0)
    print(f"Selected {legs_category}: {selected_legs} with EN Load: {legs_info['EN Load']}")

    # Selection of core
    core_category = 'Core'
    selected_core, core_info = random_part_selection(core_category)
    build[core_category] = (selected_core, core_info)
    total_weight += core_info['Weight']
    total_en_load += core_info.get('EN Load', 0)
    print(f"Selected {core_category}: {selected_core} with EN Load: {core_info.get('EN Load', 'N/A')}")

    # Define generator category outside the if-else block
    generator_category = 'Generator'

    if retry and previous_generator_info:
        # Reuse the previously selected generator if retrying
        selected_generator, generator_info = previous_generator_info
        print(f"Reusing {generator_category}: {selected_generator} with EN Output: {generator_info['EN Output']}")
    else:
        # Selection of generator
        selected_generator, generator_info = random_part_selection(generator_category)
        print(f"Selected {generator_category}: {selected_generator} with EN Output: {generator_info['EN Output']}")

    build[generator_category] = (selected_generator, generator_info)
    total_weight += generator_info['Weight']
    adjusted_output = calculate_adjusted_generator_output(core_info, generator_info)

    # Configurable exclusion rules for arms and backs
    optional_categories = {
        'RArm': 0.2,  # 20% chance to not include RArm
        'LArm': 0.2,  # 20% chance to not include LArm
        'RBack': 0.2,  # 20% chance to not include RBack
        'LBack': 0.2,  # 20% chance to not include LBack
    }

    # Other mandatory categories
    mandatory_categories = ['FCS', 'Head', 'Arms', 'Expansion']
    if 'Tank' not in selected_legs:
        mandatory_categories.append('Booster')
    else:
        build['Booster'] = ('N/A', {'Image': 'N/A', 'Weight': 0, 'EN Load': 0})
        print("Boosters excluded due to Tank type legs.")

    for category in optional_categories.keys():
        if random.random() > optional_categories[category]:  # Randomly decide based on the assigned chance
            selected_part, part_info = random_part_selection(category)
            build[category] = (selected_part, part_info)
            if 'Weight' in part_info:
                total_weight += part_info.get('Weight', 0)
            if 'EN Load' in part_info:
                total_en_load += part_info.get('EN Load', 0)
            if 'Image' in part_info:
                load_image(part_info['Image'])  # This will cache the image
            print(f"Added {category}: {selected_part} with Weight: {part_info.get('Weight', 'N/A')}, EN Load: {part_info.get('EN Load', 'N/A')}")

    for category in mandatory_categories:
        selected_part, part_info = random_part_selection(category)
        build[category] = (selected_part, part_info)
        if 'Weight' in part_info:
            total_weight += part_info.get('Weight', 0)
        if 'EN Load' in part_info:
            total_en_load += part_info.get('EN Load', 0)
        if 'Image' in part_info:
            load_image(part_info['Image'])  # This will cache the image
        print(f"Added {category}: {selected_part} with Weight: {part_info.get('Weight', 'N/A')}, EN Load: {part_info.get('EN Load', 'N/A')}")

    print(f"Total weight (excluding legs): {total_weight}")
    print(f"Total energy load: {total_en_load} / {adjusted_output}")

    if total_en_load > adjusted_output:
        print("Energy load exceeds output, trying again...")
        return generate_build(parts, retry=True, previous_generator_info=(selected_generator, generator_info))

    return build, total_weight, total_en_load, legs_info['Load Limit'], adjusted_output

# Global cache dictionary
image_cache = {}

# Downloads all images to ram (takes a bit), so it is faster to switch between builds
# Need to download all images onto disk for fastest response
def load_image(url):
    if url == 'N/A':
        # Return a placeholder QPixmap for 'N/A' or handle it according to the UI design
        return QPixmap()  # Returns an empty pixmap
    if url in image_cache:
        return image_cache[url]  # Return the cached pixmap if available
    else:
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        data = response.data
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        image_cache[url] = pixmap
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
        self.buildMenu = self.mainMenuBar.addMenu('Builds')
        self.layout().addWidget(self.mainMenuBar)  # Add the main menu bar to the vertical layout

        # Build Switcher Menu Bar
        self.switcherMenuBar = QMenuBar()
        self.switcherMenu = self.switcherMenuBar.addMenu('Switch Build')
        self.layout().addWidget(self.switcherMenuBar)  # Add the switcher menu bar below the main menu bar

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
        for i in range(1, 11): # If you want to change number of builds past 20, here is the line
            self.buildNumComboBox.addItem(str(i))

        # Layout for control elements
        controlsLayout = QHBoxLayout()
        controlsLayout.addWidget(self.randomizeButton)
        controlsLayout.addWidget(self.buildNumComboBox)
        self.layout().addLayout(controlsLayout)  # Add control layout to the main vertical layout

    def addBuild(self, build_data):
        self.builds.append(build_data)
        self.updateBuildMenu()
        self.updateSwitcherMenu()

    def displayBuild(self, index):
        if 0 <= index < len(self.builds):
            self.current_build_index = index
            self.parts, self.total_weight, self.total_en_load, self.legs_load_limit, self.adjusted_generator_output = self.builds[index]
            self.setWindowTitle(f'Mech Part Selector - Build {self.current_build_index + 1}')
            self.addPartsToGrid()

    def randomizeBuilds(self):
        num_builds = int(self.buildNumComboBox.currentText()) # This allows players to choose how much builds they want randomized through combobox (click select number)
        self.builds = [generate_build(parts) for _ in range(num_builds)]
        self.updateBuildMenu()
        self.updateSwitcherMenu()
        self.displayBuild(0)

    def updateBuildMenu(self):
        self.buildMenu.clear()
        for i in range(len(self.builds)):
            action = QAction(f'Build #{i + 1}', self)
            action.triggered.connect(lambda _, x=i: self.displayBuild(x))
            self.buildMenu.addAction(action)

    def updateSwitcherMenu(self):
        self.switcherMenu.clear()
        for i in range(len(self.builds)):
            action = QAction(f'Switch to Build #{i + 1}', self)
            action.triggered.connect(lambda _, x=i: self.displayBuild(x))
            self.switcherMenu.addAction(action)

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