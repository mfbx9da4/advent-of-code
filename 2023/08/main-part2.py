import math
import itertools


input = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

input = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

# Leandro input
input = """
LRRLRRLRRLRRRLRRLRRRLRRLRRRLRLRLLRLRLRRLLLRLRLRRRLRRLRLRRRLRRLRRLRRLLLRRLRRRLRRRLRLLRRLRLLRRLRRRLRRLRLRRRLRLRLRRLRLRRRLLRRRLLRRRLRLRRRLRRLLRRLRRRLRRLRRLLRRLRRLRRRLLLRRRLRRLRRLRRLRLRRRLRRLLLLRLRRLRRRLRLLRRLRLLRRLRRRLRRRLRRRLLRRLRRLRRLRRRLRRLRRRLLRLRRRLRRRLRRRLLRRRLRRLRRRR

LRL = (MCG, TRC)
TNJ = (LMV, PMP)
GQK = (MGD, DBP)
KVK = (LHC, NMM)
PQX = (SLC, LSD)
GRR = (XCR, BJT)
RBF = (VDM, BFG)
TKN = (VDH, HGQ)
MMJ = (LTR, CNQ)
CCX = (FJJ, FKD)
VHD = (JFQ, DDH)
NRL = (CTM, XTJ)
SNH = (QDH, PSQ)
JTM = (VFH, QBR)
BJT = (GJL, JXD)
LBJ = (JFQ, DDH)
FPN = (PBT, SJR)
CGR = (NJC, CNF)
RCM = (GTQ, BBT)
BQQ = (FNS, KPL)
NSF = (SLD, SJV)
QFQ = (XNX, GHT)
QCZ = (JPG, NLJ)
RJD = (QDT, NSG)
CNK = (SKK, NFL)
CBR = (QDT, NSG)
QMV = (HXG, FHS)
DNL = (XLX, RDT)
XRS = (DHT, RDP)
GHV = (FHS, HXG)
MJM = (GQB, XCC)
GQC = (NKG, NSF)
RKH = (KVG, JCQ)
DKT = (LTN, LTN)
THR = (PHF, VKN)
BQV = (BTS, SCG)
BJJ = (GQC, QRR)
CQL = (LHK, BCD)
LXX = (LCX, FJV)
NSG = (VSX, DFN)
LSD = (JRL, KXC)
QKB = (NLJ, JPG)
HSK = (CFN, NTM)
BLL = (JJQ, MSN)
SQD = (BLK, LBK)
KVP = (DBB, RHN)
MLJ = (QQR, HDH)
QVB = (GMN, TDP)
HJB = (GPG, XDT)
NBX = (NVT, SNB)
CLL = (PLG, LHS)
AAA = (JXS, MFQ)
CHN = (RNL, FHV)
JHT = (JQF, JQX)
KSB = (VDL, VBD)
HBT = (CKB, CCX)
JXH = (MQH, PRD)
DBB = (XHL, CHN)
PBD = (RDB, VHH)
SDV = (VMG, NTV)
BJS = (NNG, RQH)
SLM = (BRB, FLG)
VDH = (QPG, GKG)
KNS = (VQX, HFR)
HBF = (RQC, MXC)
JSF = (KPL, FNS)
HLS = (TJQ, TKM)
TRV = (BVN, GKF)
NLJ = (GBH, JCT)
SVM = (DKT, XLG)
THK = (NTM, CFN)
MDK = (DNL, VXV)
MHV = (DQQ, MQX)
CNF = (QQH, SLN)
XJK = (VFH, QBR)
FNT = (HXR, HXR)
KCT = (CPX, FXC)
BDB = (NMP, JGG)
LRZ = (JXC, TNJ)
JBQ = (NDL, KSJ)
LJQ = (GHT, XNX)
HKD = (HFH, VHJ)
VDM = (GTD, HRP)
QQH = (THC, THR)
PRD = (KFR, TJK)
KKH = (VTJ, LSR)
LQS = (SJQ, RHD)
RLF = (LCR, SGG)
JHK = (PDJ, TRV)
QHG = (VMS, PKS)
JRL = (GVJ, SKL)
XDV = (PJL, JRN)
TSV = (KCR, QJP)
JSN = (QFQ, LJQ)
RLA = (JSN, JVD)
KPD = (RDK, NSS)
HXP = (RQT, QTS)
DDB = (SFH, RHV)
JGG = (BJG, JTS)
VBD = (SGD, FRJ)
HRP = (RJD, CBR)
RRT = (MLJ, MLJ)
NVD = (KHM, RBF)
TNK = (QSX, KVD)
NST = (CDL, VGL)
FLF = (SNF, KRN)
LHS = (BSD, DTD)
NCV = (KSB, PTG)
FMX = (QKX, XFP)
KMB = (FDM, BSX)
CRH = (CVV, DDS)
VGL = (JLS, CPK)
DBF = (KGB, PXQ)
RNM = (HTP, LVL)
HKC = (XML, RTK)
JLC = (TKN, VSV)
FLB = (NNG, RQH)
QKH = (GQM, LSB)
DTD = (FTJ, HCK)
BXS = (HKD, FDK)
TKV = (RHN, DBB)
QBJ = (KNS, DXQ)
LBS = (BHT, SFM)
VMS = (CTJ, DDC)
FQJ = (FVQ, GKR)
RQC = (LRF, HCM)
SSG = (GQK, HDV)
KPL = (GQS, MDK)
GJN = (PNN, CPB)
LHK = (QPD, GSV)
KFR = (KPD, DTV)
QXC = (QVM, BHJ)
XRH = (PKM, FPN)
CKL = (BBT, GTQ)
FPK = (CRV, MGR)
LTK = (LVT, HXF)
BLK = (BRT, BQN)
BSX = (XMS, XJN)
MMR = (JCG, HHX)
DVM = (LHK, BCD)
RCJ = (BDB, CFK)
QLN = (DDB, LDQ)
GKF = (QLV, FNP)
BXQ = (NKT, FFN)
HCM = (FPK, KQB)
HKG = (GQK, HDV)
FNS = (GQS, MDK)
CTJ = (NST, HDJ)
QQS = (GQB, XCC)
ZZZ = (MFQ, JXS)
MGK = (CRH, BRV)
LCR = (FRD, KMK)
BKD = (BNR, BKM)
LDB = (KLM, SCC)
PLS = (PBL, CRG)
FQR = (PNR, NCV)
TNL = (CDT, MKC)
KVH = (FJQ, SHJ)
KPT = (KGB, PXQ)
GQM = (BXQ, VLP)
FDR = (GLC, KGF)
DDC = (NST, HDJ)
MTJ = (TMT, TMB)
PBJ = (LTK, VFB)
JXS = (SBL, CQB)
XML = (BMK, QBL)
XSK = (KSN, KSN)
TKM = (TKQ, NTX)
XFP = (HBX, RMX)
DXQ = (VQX, HFR)
KRN = (CNK, JDM)
TJQ = (TKQ, NTX)
VQX = (LBJ, VHD)
TGX = (HLK, LDJ)
MCX = (GDH, BNS)
DKM = (TVC, LPB)
VXD = (GCF, SVD)
FGB = (BKM, BNR)
VNN = (VCS, BSR)
FXX = (LHC, NMM)
JKR = (TQN, GXV)
FRJ = (TDK, PKQ)
MMQ = (SCC, KLM)
XGL = (MSN, JJQ)
GTQ = (DMV, LLK)
KML = (MCX, CTT)
LBH = (LSR, VTJ)
BDS = (XJK, JTM)
FVH = (TSV, HHC)
KXN = (LRL, QKK)
HND = (HNQ, FSG)
JQS = (QLL, RKH)
CKD = (TBT, HBT)
PXP = (NXC, TTK)
VHP = (QJC, QKH)
KQL = (BQV, RJR)
FSG = (JBH, GPH)
BVN = (QLV, FNP)
HNV = (XFH, BKL)
CNJ = (MNT, DCG)
VSV = (HGQ, VDH)
PXB = (RRT, RRT)
FNK = (TKC, LTM)
VTX = (LDJ, HLK)
KKG = (QDL, SNT)
CTT = (GDH, BNS)
FJJ = (FNT, FNT)
JCS = (DDB, LDQ)
GDH = (TPG, DND)
FMF = (XHB, BNH)
QLL = (JCQ, KVG)
NJK = (RDB, VHH)
LHC = (QDS, SXP)
QHS = (KQL, SXQ)
BJQ = (BXB, HQT)
GJL = (BTX, GJC)
BNR = (NJK, PBD)
NFL = (NSC, FTL)
SKK = (FTL, NSC)
MQN = (FMF, KPC)
XHB = (DCS, SQD)
MDT = (TDP, GMN)
XBL = (TMT, TMB)
HFH = (XDV, DMD)
BSR = (VTX, TGX)
LDH = (BJQ, XJJ)
GXX = (KKL, RCJ)
PQZ = (HDH, QQR)
CXH = (VXD, SGC)
HPB = (VHR, FNQ)
LLF = (QVM, BHJ)
VQQ = (FQD, MQN)
GSV = (NDT, SLM)
GLR = (HVD, DMF)
SLC = (JRL, KXC)
RHV = (HBC, TFR)
PVX = (PLS, SJS)
LLK = (BDC, PNK)
SLL = (FJQ, SHJ)
LKT = (VPF, SSC)
MXC = (LRF, HCM)
FTL = (QSR, SVH)
GCF = (JTF, HJB)
VHZ = (RRN, TSH)
LNB = (DQQ, MQX)
DRQ = (XML, RTK)
XLG = (LTN, VLD)
LBL = (VVF, SPR)
MBB = (NFG, NFG)
QJC = (GQM, LSB)
LSR = (BJS, FLB)
MQH = (TJK, KFR)
DFN = (LXG, LLL)
MSN = (KXN, MPV)
JCT = (MHV, LNB)
TPG = (CJJ, RRD)
GCV = (NVT, SNB)
LNL = (GXX, DJM)
XFT = (TSH, RRN)
FSS = (SLC, LSD)
TKT = (TVC, LPB)
XBN = (NBX, GCV)
RQT = (QKF, XRS)
XCC = (MXL, RLF)
RTH = (QVB, MDT)
DBP = (HNV, XCG)
QQB = (JMF, PBJ)
KSJ = (NCS, RNM)
GNQ = (CPX, FXC)
HHX = (JKT, SVM)
SGG = (KMK, FRD)
SMM = (SJS, PLS)
VPK = (LTM, TKC)
VLD = (QKB, QCZ)
LTR = (TFX, FVN)
VCL = (DKM, TKT)
HXG = (MTG, SNM)
KGB = (MRV, LFD)
JGK = (CNJ, RXF)
FMV = (FRT, MNF)
SLD = (KVH, SLL)
VVL = (TNJ, JXC)
GDP = (RBF, KHM)
XDT = (RML, JHK)
JKP = (NDL, KSJ)
BNH = (SQD, DCS)
LFD = (LQC, HLS)
NHC = (JHT, SSM)
VPF = (NRN, LBL)
BHT = (LQS, MCP)
SNT = (RHL, BDS)
BQN = (XGL, BLL)
FVN = (HGP, QKM)
NXC = (KQJ, FMV)
NKG = (SJV, SLD)
HSF = (HPB, NFR)
QKM = (RRR, PMK)
PJL = (XBN, PFX)
MRP = (LCX, FJV)
XSQ = (FDK, HKD)
TVC = (GHN, QQC)
XLX = (DKJ, NNT)
VSX = (LLL, LXG)
FQD = (FMF, KPC)
PNJ = (XCR, BJT)
QDV = (QRJ, BFS)
QVG = (GLC, KGF)
BMK = (RJS, FLF)
SXQ = (BQV, RJR)
BGL = (CSB, SBH)
BJG = (CNH, PQJ)
RSG = (QFT, VPD)
VVF = (DRQ, HKC)
BBT = (LLK, DMV)
HGQ = (GKG, QPG)
HMD = (PHT, PCD)
PPL = (CKL, RCM)
QLA = (TSH, RRN)
KBG = (HBT, TBT)
RHD = (HKG, SSG)
GQB = (RLF, MXL)
QFA = (QQR, HDH)
KPC = (BNH, XHB)
XNX = (FVH, MNH)
HBX = (NFD, VJF)
SVD = (HJB, JTF)
DMD = (JRN, PJL)
PKJ = (BJQ, XJJ)
TFX = (HGP, QKM)
MCH = (PKD, PFF)
SGD = (PKQ, TDK)
RRJ = (KCT, GNQ)
PJD = (VLM, JJZ)
PHF = (PQX, FSS)
PKQ = (NTP, MMR)
VPD = (QHB, NHC)
FRD = (GDP, NVD)
SFH = (HBC, TFR)
JRN = (XBN, PFX)
HSB = (MRP, LXX)
RMX = (NFD, VJF)
SBH = (JXH, TSQ)
NTP = (JCG, HHX)
PSX = (FMX, PCR)
LCQ = (PKS, VMS)
LKV = (SMM, PVX)
SGC = (SVD, GCF)
CQB = (LDD, QDV)
FRT = (XCV, HSF)
KGT = (SGC, VXD)
TRC = (PSX, NQC)
BSG = (PKD, PFF)
CKB = (FJJ, FKD)
SSM = (JQF, JQX)
DKJ = (BKD, FGB)
TKC = (TXS, FQJ)
JQX = (DVQ, NLN)
BDC = (KNL, DSV)
FJV = (MTJ, XBL)
DND = (CJJ, RRD)
PPH = (MMQ, LDB)
FTJ = (LKT, GNX)
JKV = (RFM, MGK)
KCR = (LLF, QXC)
RFN = (LJL, CFX)
HCF = (NFG, HSR)
NTV = (JXG, VHP)
QQR = (DTX, HND)
BTX = (QVG, FDR)
JQK = (SXQ, KQL)
NJC = (SLN, QQH)
RML = (PDJ, TRV)
SNF = (JDM, CNK)
KMK = (GDP, NVD)
XSH = (DXQ, KNS)
DTX = (HNQ, FSG)
BNS = (TPG, DND)
KHM = (BFG, VDM)
SBF = (MGK, RFM)
NFD = (PKJ, LDH)
BHJ = (VNN, CGL)
TXS = (FVQ, GKR)
CRV = (NTQ, SDV)
GHT = (FVH, MNH)
RBN = (RQC, MXC)
KKL = (BDB, CFK)
NLN = (RBN, HBF)
QFT = (NHC, QHB)
QBL = (FLF, RJS)
RHG = (PNN, CPB)
MNF = (XCV, HSF)
SJS = (CRG, PBL)
FDK = (VHJ, HFH)
HXM = (JJD, JJD)
PNN = (QDK, MMJ)
GCS = (TTK, NXC)
VJF = (LDH, PKJ)
GTD = (CBR, RJD)
RRD = (TPL, XVR)
JXC = (LMV, PMP)
NXH = (MKC, CDT)
HCK = (GNX, LKT)
BRC = (QLL, RKH)
KQB = (CRV, MGR)
TMB = (MCH, BSG)
XJN = (RSX, JGK)
HQP = (SFM, BHT)
HQT = (MBB, HCF)
THC = (VKN, PHF)
TPL = (NGD, QQB)
NGD = (PBJ, JMF)
GVJ = (RNT, LKV)
QDK = (LTR, CNQ)
JXG = (QKH, QJC)
TQN = (KRL, QCV)
RDB = (JQS, BRC)
MPV = (LRL, QKK)
SJQ = (HKG, SSG)
XHL = (RNL, FHV)
LRF = (KQB, FPK)
GNX = (SSC, VPF)
VXV = (XLX, RDT)
MTG = (CCR, CRR)
NFG = (BHH, BHH)
DSV = (PXB, PJN)
CVT = (KPT, DBF)
RHL = (JTM, XJK)
CBQ = (GXL, PQB)
BHH = (JXS, MFQ)
DMV = (BDC, PNK)
NSS = (HQP, LBS)
FVM = (PRP, RFN)
NCS = (HTP, LVL)
QPD = (NDT, SLM)
GJC = (FDR, QVG)
CFK = (JGG, NMP)
HDV = (MGD, DBP)
PNB = (PQB, GXL)
RXA = (NLJ, JPG)
CNH = (JSF, BQQ)
VXL = (HXR, XQQ)
QKF = (RDP, DHT)
QTS = (QKF, XRS)
VDL = (SGD, FRJ)
FCM = (TQN, GXV)
BHQ = (GQC, QRR)
BSD = (FTJ, HCK)
CJJ = (TPL, XVR)
PLG = (DTD, BSD)
LQC = (TKM, TJQ)
NTM = (KLG, PPL)
SHJ = (NRL, NMS)
QDL = (BDS, RHL)
PCR = (XFP, QKX)
XCG = (XFH, BKL)
LMV = (GCS, PXP)
JJD = (QQV, QQV)
HGP = (PMK, RRR)
TNF = (RQT, QTS)
SFM = (MCP, LQS)
MNR = (RFN, PRP)
LLL = (CBQ, PNB)
RJS = (SNF, KRN)
BRV = (CVV, DDS)
GGK = (LHS, PLG)
HVD = (GBJ, VQQ)
KQJ = (FRT, MNF)
PMK = (CGR, PQR)
MFB = (GGK, CLL)
HLK = (NTG, KMB)
BKL = (CQL, DVM)
SVT = (CSB, SBH)
FGD = (PNR, NCV)
LVT = (VCL, XTQ)
MFQ = (SBL, CQB)
SCC = (KKH, LBH)
JMF = (VFB, LTK)
GLC = (FBS, DNB)
HFT = (MMQ, LDB)
PNR = (PTG, KSB)
SNM = (CRR, CCR)
TJK = (DTV, KPD)
PQR = (NJC, CNF)
VPM = (QDL, SNT)
DHT = (KGT, CXH)
RPK = (KML, XRL)
VFH = (HSB, QBV)
FNP = (JBQ, JKP)
JLS = (QLN, JCS)
XMS = (JGK, RSX)
FRK = (GGK, CLL)
PDJ = (GKF, BVN)
QDH = (JLC, QTG)
PFX = (GCV, NBX)
BXB = (MBB, MBB)
TTK = (KQJ, FMV)
PKS = (DDC, CTJ)
KLG = (RCM, CKL)
CSV = (QVB, MDT)
NNG = (DXR, BPD)
HHC = (KCR, QJP)
LVL = (CSQ, TKJ)
QHB = (JHT, SSM)
JDM = (SKK, NFL)
JCQ = (TNK, LPJ)
TSQ = (MQH, PRD)
JTS = (PQJ, CNH)
RCR = (KCT, GNQ)
LXG = (CBQ, PNB)
TKQ = (HXP, TNF)
PKM = (PBT, SJR)
GXV = (QCV, KRL)
HJS = (BBX, RPK)
CPX = (XSK, XSK)
JXD = (BTX, GJC)
CVV = (HXM, VDB)
SBL = (LDD, QDV)
HBC = (VPM, KKG)
DXR = (CVT, KKS)
VDB = (JJD, BVS)
XQQ = (VVL, LRZ)
PQB = (BXS, XSQ)
NTX = (HXP, TNF)
SCG = (VMQ, HJS)
GHN = (SBF, JKV)
VXR = (SGL, LMC)
NQF = (VPD, QFT)
DDS = (HXM, VDB)
KLM = (LBH, KKH)
SGL = (QRL, KLQ)
GKR = (CSV, RTH)
QDT = (DFN, VSX)
MNT = (SNH, FPP)
TDP = (TKV, KVP)
KNL = (PXB, PXB)
GMN = (KVP, TKV)
MXL = (SGG, LCR)
PKD = (FXX, KVK)
SXP = (FNK, VPK)
NTG = (BSX, FDM)
QSR = (KBG, CKD)
FHV = (XCL, MBP)
RDT = (NNT, DKJ)
SPR = (HKC, DRQ)
FFN = (JHD, GLR)
FBS = (QXL, FTF)
VLP = (FFN, NKT)
KXC = (SKL, GVJ)
TKJ = (FQR, FGD)
LHH = (PHT, PCD)
CTM = (GHV, QMV)
VHH = (JQS, BRC)
MQX = (MJM, QQS)
BBX = (XRL, KML)
LKK = (PKM, FPN)
RNT = (PVX, SMM)
JSA = (TNJ, JXC)
RDK = (LBS, HQP)
RXF = (MNT, DCG)
HDH = (HND, DTX)
VKN = (FSS, PQX)
LSB = (VLP, BXQ)
BPD = (CVT, KKS)
TMT = (BSG, MCH)
QLV = (JBQ, JKP)
LPJ = (KVD, QSX)
QDS = (VPK, FNK)
GQS = (VXV, DNL)
DTV = (NSS, RDK)
SNB = (JLB, LLV)
NMM = (SXP, QDS)
CSB = (TSQ, JXH)
PFF = (FXX, KVK)
VHJ = (XDV, DMD)
XFX = (KSN, THB)
CCR = (NQF, RSG)
VMQ = (BBX, RPK)
HXR = (VVL, VVL)
SJV = (KVH, SLL)
CFN = (KLG, PPL)
DDH = (RHG, GJN)
FLG = (HMD, LHH)
FVQ = (RTH, CSV)
RTK = (BMK, QBL)
NSC = (SVH, QSR)
MKC = (FCM, JKR)
XTJ = (GHV, QMV)
CNQ = (FVN, TFX)
SJR = (BJJ, BHQ)
MGR = (NTQ, SDV)
XFH = (DVM, CQL)
QSX = (GRR, PNJ)
QKX = (HBX, RMX)
LBK = (BQN, BRT)
PXQ = (MRV, LFD)
LDQ = (SFH, RHV)
MNH = (HHC, TSV)
XCV = (HPB, NFR)
KLQ = (QBJ, XSH)
FTF = (SCQ, RGC)
JJQ = (MPV, KXN)
LJL = (VDV, SJJ)
DNB = (FTF, QXL)
CFX = (VDV, SJJ)
JKT = (DKT, DKT)
SJJ = (THK, HSK)
CDL = (JLS, CPK)
QCV = (XRH, LKK)
XCR = (GJL, JXD)
KMJ = (MLJ, PQZ)
MPS = (DJM, GXX)
GBJ = (MQN, FQD)
PNK = (KNL, DSV)
BRB = (HMD, LHH)
PBT = (BJJ, BHQ)
JPG = (JCT, GBH)
HSR = (BHH, ZZZ)
DQQ = (QQS, MJM)
MCP = (SJQ, RHD)
LTM = (TXS, FQJ)
KKS = (KPT, DBF)
DCG = (FPP, SNH)
TDK = (MMR, NTP)
QJP = (LLF, QXC)
NFR = (FNQ, VHR)
FKD = (FNT, VXL)
LMC = (KLQ, QRL)
PBL = (FVM, MNR)
JHD = (DMF, HVD)
CRR = (RSG, NQF)
JJZ = (JVD, JSN)
RQH = (DXR, BPD)
HXF = (VCL, XTQ)
CRG = (MNR, FVM)
VHR = (QHG, LCQ)
VCS = (VTX, TGX)
FPP = (QDH, PSQ)
KSN = (XFT, XFT)
BVS = (QQV, PJD)
RSX = (RXF, CNJ)
FXC = (XSK, XFX)
HDJ = (CDL, VGL)
QQC = (SBF, JKV)
LPB = (GHN, QQC)
LRJ = (QHS, JQK)
SCQ = (RCR, RRJ)
PQJ = (JSF, BQQ)
GKG = (VMJ, LRJ)
SSC = (NRN, LBL)
NVT = (JLB, LLV)
KVD = (GRR, PNJ)
XRL = (CTT, MCX)
BTS = (VMQ, HJS)
KRL = (XRH, LKK)
RRN = (BGL, SVT)
FHS = (SNM, MTG)
QPG = (VMJ, LRJ)
QKK = (TRC, MCG)
VDV = (THK, HSK)
GPH = (VXR, GKQ)
RNL = (XCL, MBP)
SLN = (THC, THR)
CPB = (MMJ, QDK)
NMS = (XTJ, CTM)
RJR = (BTS, SCG)
CGL = (VCS, BSR)
MBP = (MFB, FRK)
NNT = (FGB, BKD)
HTP = (CSQ, TKJ)
GPG = (RML, JHK)
QRL = (QBJ, XSH)
BCD = (GSV, QPD)
QQV = (VLM, VLM)
PRP = (CFX, LJL)
TFR = (KKG, VPM)
LDD = (QRJ, BFS)
QVM = (VNN, CGL)
KGF = (FBS, DNB)
GBH = (MHV, LNB)
JCG = (JKT, SVM)
FJQ = (NMS, NRL)
QXL = (RGC, SCQ)
NRN = (SPR, VVF)
FDM = (XMS, XJN)
RFM = (BRV, CRH)
NKT = (GLR, JHD)
HFR = (VHD, LBJ)
THB = (XFT, VHZ)
XJJ = (BXB, HQT)
QTG = (VSV, TKN)
NQC = (PCR, FMX)
JLB = (HFT, PPH)
GXL = (BXS, XSQ)
PSQ = (QTG, JLC)
NDT = (BRB, FLG)
PJN = (RRT, KMJ)
TBT = (CKB, CCX)
JBH = (GKQ, VXR)
XVR = (QQB, NGD)
BRT = (XGL, BLL)
PCD = (MPS, LNL)
SKL = (RNT, LKV)
TSH = (BGL, SVT)
JQF = (DVQ, NLN)
DVQ = (RBN, HBF)
RGC = (RCR, RRJ)
QRJ = (TNL, NXH)
XCL = (MFB, FRK)
VLM = (JSN, JVD)
RDP = (KGT, CXH)
VTJ = (FLB, BJS)
LCX = (XBL, MTJ)
JVD = (QFQ, LJQ)
BKM = (NJK, PBD)
VMJ = (QHS, JQK)
DMF = (VQQ, GBJ)
CDT = (FCM, JKR)
NTQ = (NTV, VMG)
QRR = (NSF, NKG)
NDL = (RNM, NCS)
KVG = (LPJ, TNK)
DCS = (BLK, LBK)
JFQ = (RHG, GJN)
GKQ = (SGL, LMC)
JTF = (GPG, XDT)
SVH = (CKD, KBG)
RRR = (PQR, CGR)
RHN = (CHN, XHL)
HNQ = (GPH, JBH)
BFG = (GTD, HRP)
LLV = (PPH, HFT)
NMP = (BJG, JTS)
CSQ = (FQR, FGD)
MRV = (HLS, LQC)
LDJ = (KMB, NTG)
PHT = (LNL, MPS)
DJM = (RCJ, KKL)
PTG = (VBD, VDL)
PMP = (PXP, GCS)
LTN = (QKB, QKB)
BFS = (NXH, TNL)
MGD = (XCG, HNV)
QBV = (MRP, LXX)
VFB = (LVT, HXF)
XTQ = (TKT, DKM)
QBR = (QBV, HSB)
CPK = (QLN, JCS)
MCG = (NQC, PSX)
VMG = (VHP, JXG)
FNQ = (LCQ, QHG)
"""

# david input
input = """
LLRRRLRLLRLRRLRLRLRRRLLRRLRRRLRRRLRRRLRRRLRRRLRRLRLLRRRLRRLLRLRLLLRRLRRLRLRLRLRRRLRLRRRLRRLLLRRRLLRRLLRRLLRRRLLLLRLRLRRRLRLRRRLRLLLRLRRLRRRLRRRLRRRLRRRLLRRLLLLRRLLRRLLRRLRLRRRLRRRLRRRLRRLRRRLRRLRRLRRLRLRRRLRRLRRRLRRRLRRLRLRRRLRRLLRLRRLRRRLRLRRLRRRLRRLRRLRRRLLRRRR

GXF = (XQB, GFH)
QQC = (HQF, BNK)
TPP = (XNG, FDD)
LQD = (MGR, GJN)
XNG = (RCM, BJG)
NQC = (KNT, DQF)
DGJ = (PGM, LSB)
RBF = (RCH, RCH)
DNH = (RTL, MLF)
VKF = (SRV, TQR)
MPT = (FVV, TVP)
TKX = (VRN, KNV)
XLQ = (MCF, MCF)
MNJ = (FRT, QGV)
STF = (LFQ, QDS)
FFH = (JVM, TCJ)
KRT = (GFC, HRX)
FVG = (QFS, RSJ)
DBH = (GXF, DJL)
RKP = (VNL, MSC)
VQX = (GGG, RPB)
FCM = (VMC, MGV)
SRL = (LVV, JQN)
HHM = (BDM, FRV)
GMN = (LPK, FHT)
QCF = (RCH, NJM)
PCB = (MDJ, KDM)
VMR = (THX, HHB)
XQK = (BJQ, LST)
FCS = (KPT, RSC)
XTG = (XTL, SVX)
FVF = (KXB, VVV)
NNR = (SBM, TPP)
NPH = (RHN, FRR)
GJF = (FXG, MLP)
TRR = (LVC, RMR)
NBS = (SFH, JGT)
SSH = (KTK, DDM)
CJH = (QJK, XHB)
DQF = (NSR, MJB)
FHT = (PFK, GPS)
GTJ = (QXC, XBR)
KQB = (JXT, KGR)
JLL = (GTJ, CBN)
QPH = (LTX, BDJ)
BSP = (MRH, BXJ)
QBX = (GPR, SHJ)
SPJ = (SLD, XQK)
PML = (TTV, BHX)
FQN = (TPJ, BTV)
GTK = (NBS, VNP)
DSQ = (RFN, QGB)
KTK = (JHR, FCM)
FXV = (BBN, VPK)
LJC = (VKH, PPQ)
NBA = (JBL, LSR)
RKK = (VTL, SNM)
FVV = (DQS, CSM)
MGJ = (QHP, DPL)
RND = (JRQ, XGJ)
DVP = (RBF, RBF)
JXR = (TJN, CVC)
FMV = (CVJ, BVZ)
XBL = (KFC, HHT)
GDR = (KCV, KCV)
NGN = (VKH, PPQ)
NJB = (VTH, FSQ)
MBD = (JKS, SFQ)
TGC = (PXP, TTF)
VMT = (XJN, CCH)
LBF = (QRB, SKN)
DGH = (CSD, RND)
SFH = (XHH, GSC)
QQD = (VTT, NLX)
BLB = (GHJ, KQD)
LFG = (TLH, XJT)
CQS = (FRR, RHN)
XRS = (QLF, KLC)
DJL = (GFH, XQB)
LJM = (RPM, HPF)
HHT = (LBF, VCS)
GFL = (LFG, MGQ)
TNX = (TSJ, HCK)
HPR = (MTG, TJX)
LKP = (BXL, BHG)
KRC = (DCT, CTS)
PSJ = (QPF, MQT)
CXG = (NPG, JQP)
QTK = (XBL, DSM)
SVP = (MLF, RTL)
NDT = (NLC, MLK)
TDR = (DJR, CJQ)
RHS = (HXN, PSZ)
PSZ = (VNG, NNK)
KKL = (GLH, SPJ)
RSB = (SFQ, JKS)
PQS = (XVK, LMV)
TTV = (MLG, FRH)
CJQ = (CTM, KCC)
VTT = (QSQ, TVV)
TCJ = (MTD, KKX)
CNM = (SXQ, RGK)
XCC = (DNP, FQN)
CXD = (TJX, MTG)
VTL = (JFV, DHN)
BJG = (FHB, QVJ)
MJR = (HDL, LSF)
CSV = (CTS, DCT)
LFQ = (LNX, RHQ)
MNL = (XBL, DSM)
NDR = (PGT, TPC)
CKS = (CDQ, GLT)
VVV = (BVL, QQC)
GGG = (JGS, VRC)
QRT = (SQJ, VSJ)
HQF = (NJK, NJK)
JGK = (FJK, PXJ)
RXG = (CLT, GTK)
TNH = (SJM, QNX)
HLX = (QJX, PGN)
FRR = (CKP, NHC)
QMK = (QVH, QLH)
FRT = (TMB, VRX)
KJD = (GBS, QMT)
RCH = (TGC, TGC)
JGF = (DKD, CHG)
TSM = (TDR, XHJ)
MTG = (DRP, KRR)
DCF = (NQC, KNM)
VPQ = (HRB, MGG)
XVK = (MPC, XMX)
NNK = (FKT, CMD)
TBF = (JDV, LQD)
TTH = (SJM, QNX)
NLX = (TVV, QSQ)
HGT = (LSF, HDL)
FCB = (KLC, QLF)
GBH = (HTJ, LXL)
BJQ = (XDH, RGV)
FLH = (FXV, SMJ)
XGN = (CHN, BLJ)
RGV = (QCB, TCC)
BCV = (NHF, NDH)
GQD = (LDC, TVB)
BCT = (KGS, QCH)
NGC = (MGJ, RPT)
LSL = (QVH, QLH)
SQJ = (TTH, TNH)
VNL = (RLV, CRK)
XCQ = (KQB, BLP)
CDL = (DJL, GXF)
MJB = (CRR, HHM)
GSP = (DQJ, FLV)
NCM = (SQN, VPJ)
JRQ = (RJM, CXG)
SXA = (QPH, CFB)
LBT = (GPL, NDJ)
QNX = (PJT, PQC)
PBV = (RRP, TSM)
CSD = (XGJ, JRQ)
MLK = (GLG, SKB)
CFB = (LTX, BDJ)
BCH = (HPQ, JBR)
BBN = (RHR, VMT)
KCV = (RHL, RHL)
SGG = (SMP, QSP)
GFB = (KCF, KJR)
TSD = (NSD, NDL)
CXL = (FVG, JCJ)
FSQ = (FQG, GXQ)
BQF = (HRB, MGG)
LRK = (JPG, BHR)
LBB = (BHX, TTV)
CXR = (BXX, STP)
MGV = (RLK, FDX)
FHB = (LCN, KSX)
JDQ = (GFK, BHD)
FJL = (GDR, GDR)
TSN = (RKJ, GLN)
VPK = (RHR, VMT)
VCS = (SKN, QRB)
BKG = (RSC, KPT)
LQB = (MMQ, BCT)
KJK = (SMF, VPM)
XMV = (PQS, RCX)
TCC = (GPP, KRT)
BFS = (DDP, VJJ)
FDD = (RCM, BJG)
BHG = (MKG, BSM)
GQP = (PRR, FFH)
GXQ = (BLH, FMB)
XBV = (NSH, GCB)
MCF = (QPH, CFB)
BTD = (BCH, GFM)
JQD = (VPQ, BQF)
JGT = (XHH, GSC)
KGS = (MGB, QQS)
JMF = (PSK, GDD)
VTZ = (NNR, NVQ)
JGS = (KHM, DTS)
CBF = (NDJ, GPL)
XPM = (MCF, VGZ)
RSJ = (VCC, MGS)
BLQ = (HJP, MPP)
HHB = (NKX, PXK)
JKS = (DKV, GMN)
GFH = (RXG, VGP)
MSC = (RLV, CRK)
KJR = (SLQ, FLH)
KFC = (VCS, LBF)
GGM = (KJK, QJF)
QDS = (RHQ, LNX)
TPC = (PFD, DJN)
DSM = (HHT, KFC)
BPJ = (RKK, GGV)
MLG = (PDG, SGF)
HTJ = (RBJ, PKL)
HJR = (MRH, BXJ)
JVA = (NVQ, NNR)
PXK = (CRV, RHB)
NJK = (CVJ, CVJ)
XPR = (PGT, TPC)
DTS = (FCS, BKG)
XJN = (TFT, LKP)
SNV = (DDT, LBL)
BXX = (KKQ, GBH)
PQM = (MXJ, FTT)
NSX = (HLX, GVH)
CVJ = (JBL, LSR)
HKQ = (VMR, DSR)
RQJ = (QFV, XMV)
CMQ = (KKL, QDL)
PGM = (VBL, KFF)
LST = (RGV, XDH)
CMD = (HKQ, SPB)
XSV = (LBB, PML)
JHB = (SSB, CXR)
LVC = (JHB, TVH)
QNT = (RBB, NDT)
QPF = (FJG, TKX)
NDH = (RRT, PQM)
TSJ = (LGH, FBN)
KDM = (GJJ, NVX)
HMJ = (HPF, RPM)
STP = (GBH, KKQ)
LDC = (LBT, CBF)
RCB = (BPN, JXR)
MSN = (PDF, JHF)
KKX = (HVX, BKX)
GLT = (VHR, GGM)
MRH = (LCD, CKD)
VGP = (CLT, GTK)
LLV = (MRN, PBV)
PDL = (DGH, LNK)
PFD = (RCB, VRH)
CRK = (NGC, KQR)
TVP = (CSM, DQS)
VTH = (GXQ, FQG)
RHJ = (SHN, PNR)
MMQ = (QCH, KGS)
GFK = (VDV, XCC)
PQC = (SRF, KML)
SHJ = (CHD, DCB)
QJF = (SMF, VPM)
QLF = (NGX, RKP)
LTX = (RNS, VHH)
RQB = (MGQ, LFG)
BHD = (XCC, VDV)
FQG = (BLH, FMB)
SNM = (JFV, DHN)
LRQ = (JDL, QBX)
SHP = (FRT, QGV)
DDP = (CRJ, SXV)
LMV = (XMX, MPC)
KMP = (HQB, SSK)
GXM = (SRV, TQR)
SMP = (JGK, GST)
KRH = (PBV, MRN)
RDM = (FKN, MSN)
FNF = (VJJ, DDP)
VKH = (CJX, PDB)
NHF = (PQM, RRT)
PBJ = (RMR, LVC)
FRG = (QJC, BPL)
RHG = (BGQ, XCQ)
RPB = (VRC, JGS)
KQD = (VBS, MBN)
LSR = (SRH, CSS)
KFF = (MFT, NSX)
TJX = (KRR, DRP)
GPL = (FPQ, SSH)
XNM = (BCH, GFM)
MPP = (RLX, FVF)
HQB = (DJJ, SPV)
SSK = (SPV, DJJ)
XVA = (SHP, MNJ)
TMT = (VRS, JHH)
NGX = (MSC, VNL)
SMF = (HFP, JMF)
SFQ = (DKV, GMN)
GBM = (NDH, NHF)
DKV = (FHT, LPK)
PTN = (FCD, SRL)
GPB = (CVS, GFD)
QFR = (BLQ, LCT)
TLH = (KMP, LFS)
TVG = (BHD, GFK)
RRT = (MXJ, FTT)
DCB = (BPC, GJF)
VRN = (CVH, PLG)
MGG = (RGR, DDB)
XND = (LGX, FCN)
HDC = (DJP, BPJ)
TCV = (NNV, MDV)
JQP = (LSL, QMK)
KLC = (NGX, RKP)
DPL = (VSL, GQP)
BHX = (MLG, FRH)
HNK = (LFQ, QDS)
RHR = (CCH, XJN)
RCM = (FHB, QVJ)
JVN = (RHL, VTZ)
HSS = (LXF, LXF)
XQB = (RXG, VGP)
XJQ = (NLN, XLD)
HFP = (PSK, GDD)
HCK = (FBN, LGH)
VHR = (KJK, QJF)
MLF = (MPT, SGJ)
TPS = (PGM, LSB)
HJJ = (CQS, NPH)
LMQ = (JQD, VPR)
GPR = (CHD, DCB)
QFS = (MGS, VCC)
SKB = (SMG, STS)
CKT = (CCJ, RJH)
SDV = (NGN, LJC)
DJB = (DVP, SHV)
CDR = (RQJ, BPH)
QHP = (VSL, GQP)
PFK = (HQJ, XSV)
PNM = (NRQ, JGF)
SQN = (LJM, HMJ)
KXB = (BVL, QQC)
NHX = (XDQ, PTN)
TFT = (BHG, BXL)
XDH = (TCC, QCB)
XFN = (QGB, RFN)
BLJ = (QRV, GGH)
QLH = (SGG, QHQ)
KPT = (LQB, TNG)
VBS = (PDL, PJH)
RFN = (GFL, RQB)
JDL = (GPR, SHJ)
NNV = (VSN, BRN)
JNV = (KDM, MDJ)
SLK = (FLV, DQJ)
JPG = (XRS, FCB)
DQJ = (NGR, XKM)
LMT = (GJC, BKT)
GFD = (DMP, XND)
RJM = (NPG, JQP)
GLH = (XQK, SLD)
SPB = (DSR, VMR)
MGQ = (TLH, XJT)
SNL = (MLR, VTM)
KNT = (MJB, NSR)
DDM = (FCM, JHR)
TDD = (GLN, RKJ)
RRX = (XLQ, XPM)
SGF = (SNL, FJF)
BTV = (GFB, SMX)
BPH = (XMV, QFV)
VSJ = (TNH, TTH)
DSD = (DVP, SHV)
JXT = (DGJ, TPS)
DDV = (NNV, MDV)
DRP = (KDS, TNJ)
MTD = (HVX, BKX)
CVH = (FFD, RDM)
LCD = (CMJ, CMJ)
NLC = (SKB, GLG)
XJT = (LFS, KMP)
CHG = (DHF, FVX)
MFT = (HLX, GVH)
HRX = (HPM, XGN)
KGR = (TPS, DGJ)
GLJ = (NSH, GCB)
GPP = (GFC, HRX)
TVV = (NFR, QNT)
QJK = (QKQ, KDV)
XHH = (NJB, PVR)
BHR = (FCB, XRS)
CKD = (CMJ, RRX)
XKM = (VQX, RDL)
PXJ = (GBM, BCV)
DCT = (HDC, BFG)
HXN = (NNK, VNG)
QGG = (BPH, RQJ)
DQS = (FKL, NCM)
STL = (DDT, LBL)
PDB = (FNF, BFS)
ZZZ = (TTF, PXP)
SHV = (RBF, QCF)
NGL = (GDR, XRQ)
QVH = (QHQ, SGG)
CBN = (XBR, QXC)
RNT = (KRC, CSV)
GCB = (DDF, LMQ)
NDL = (DDV, TCV)
SRV = (CDR, QGG)
DMP = (LGX, LGX)
RKJ = (KFG, FRG)
SKG = (KBH, LRQ)
QGB = (RQB, GFL)
XBR = (GQD, QJV)
DHN = (LMT, NBB)
LPK = (PFK, GPS)
QVS = (HJJ, TQJ)
MSV = (RJH, CCJ)
CCK = (SQJ, VSJ)
QHQ = (SMP, QSP)
PKL = (RVD, BDX)
JDV = (MGR, GJN)
FDX = (JFT, TNX)
DJN = (RCB, VRH)
XGJ = (CXG, RJM)
DJJ = (VKF, GXM)
VPR = (VPQ, BQF)
PGT = (PFD, DJN)
RGR = (RPS, NBT)
BRK = (BSP, HJR)
KKQ = (LXL, HTJ)
VRC = (DTS, KHM)
GST = (FJK, PXJ)
SLD = (BJQ, LST)
GHL = (NRQ, JGF)
HQJ = (PML, LBB)
BLH = (RNT, JFC)
SPV = (GXM, VKF)
VPM = (JMF, HFP)
RBB = (MLK, NLC)
FTT = (PVF, DVS)
XRQ = (KCV, JVN)
LSB = (VBL, KFF)
QMT = (CCK, QRT)
FBN = (XNM, BTD)
JFT = (TSJ, HCK)
HDL = (QHL, XNP)
BPC = (FXG, MLP)
TVB = (LBT, CBF)
KNM = (KNT, DQF)
CHN = (QRV, GGH)
SRH = (XQN, NNC)
LXF = (HXN, HXN)
VCC = (SKG, QQR)
VMM = (RGK, SXQ)
FCD = (LVV, JQN)
FMB = (RNT, JFC)
CNC = (PTN, XDQ)
KCC = (JLL, VFC)
CDQ = (VHR, GGM)
QFV = (RCX, PQS)
XQN = (RHG, TKF)
SMJ = (VPK, BBN)
SRF = (JDQ, TVG)
SKN = (RLS, RHJ)
KXX = (KHL, LFJ)
GJN = (BRK, FPX)
QGV = (VRX, TMB)
SXV = (GQM, KJD)
VGZ = (CFB, QPH)
JQN = (XFN, DSQ)
BKT = (CBT, PVD)
QJC = (PBJ, TRR)
BLP = (JXT, KGR)
TTF = (MMV, MFK)
PXP = (MMV, MFK)
PSK = (KMJ, QQD)
VPJ = (HMJ, LJM)
RPQ = (CDL, DBH)
RPS = (NDR, XPR)
QQS = (VDG, XJP)
GGH = (PCB, JNV)
KHL = (MLT, PSJ)
NPG = (QMK, LSL)
XDQ = (SRL, FCD)
MXJ = (PVF, DVS)
VGG = (XLD, NLN)
DNP = (TPJ, BTV)
XRN = (LRK, QXS)
XTS = (NQC, KNM)
FJF = (MLR, VTM)
MVL = (THG, GPB)
TPJ = (GFB, SMX)
FJG = (VRN, KNV)
NDX = (JDV, LQD)
JHR = (MGV, VMC)
KNV = (CVH, PLG)
NSH = (LMQ, DDF)
THG = (CVS, GFD)
RDL = (RPB, GGG)
BNK = (NJK, FMV)
FHG = (THG, GPB)
NKX = (RHB, CRV)
MMV = (CKS, FRS)
RHB = (GSP, SLK)
GVH = (QJX, PGN)
LFS = (HQB, SSK)
SJM = (PQC, PJT)
TVH = (CXR, SSB)
FKN = (JHF, PDF)
KRR = (TNJ, KDS)
HPQ = (FJL, NGL)
PDG = (FJF, SNL)
RRP = (TDR, XHJ)
LGX = (XVV, XVV)
QKQ = (TDD, TSN)
GQM = (GBS, QMT)
MQT = (FJG, TKX)
HRB = (RGR, DDB)
HQS = (DJB, DSD)
XMX = (MNL, QTK)
LGH = (XNM, BTD)
QJX = (PPC, KXX)
JBR = (FJL, NGL)
FRV = (HGT, MJR)
BXN = (QXS, LRK)
GFM = (HPQ, JBR)
MDV = (VSN, BRN)
PPQ = (PDB, CJX)
FRH = (PDG, SGF)
KBH = (QBX, JDL)
LNX = (XTG, MJV)
PHD = (XJQ, VGG)
DJR = (KCC, CTM)
LNK = (RND, CSD)
SVX = (HRJ, RPQ)
BVZ = (LSR, JBL)
STS = (CMQ, MGX)
DDF = (VPR, JQD)
GHJ = (MBN, VBS)
HVX = (CXD, HPR)
JBL = (CSS, SRH)
HPF = (BNS, QFR)
DSR = (THX, HHB)
KMJ = (VTT, NLX)
GFC = (XGN, HPM)
CJX = (FNF, BFS)
FKT = (SPB, HKQ)
MBN = (PDL, PJH)
NLN = (CXL, KNR)
GSC = (PVR, NJB)
LFJ = (MLT, PSJ)
NBT = (NDR, XPR)
RLK = (TNX, JFT)
SSB = (BXX, STP)
FJK = (GBM, BCV)
VRX = (CJH, KXH)
DJP = (RKK, GGV)
HRJ = (CDL, DBH)
XHB = (QKQ, KDV)
BVL = (HQF, HQF)
PVF = (VMM, CNM)
GLN = (KFG, FRG)
KHM = (BKG, FCS)
VHH = (MBJ, PHD)
XPV = (DJB, DSD)
MJV = (XTL, SVX)
BDJ = (VHH, RNS)
RLS = (SHN, PNR)
CBT = (RQM, JJX)
PRR = (JVM, TCJ)
DVS = (VMM, CNM)
KXH = (QJK, XHB)
SHD = (LXF, RHS)
GPS = (XSV, HQJ)
MGR = (BRK, FPX)
BXJ = (LCD, CKD)
RBJ = (RVD, BDX)
JFC = (KRC, CSV)
GDD = (QQD, KMJ)
KDS = (TBF, NDX)
BRN = (HSS, SHD)
QXC = (QJV, GQD)
GLG = (STS, SMG)
MGX = (QDL, KKL)
MLT = (MQT, QPF)
HPM = (BLJ, CHN)
CKP = (CNC, NHX)
KML = (TVG, JDQ)
AAA = (PXP, TTF)
BPZ = (MNJ, SHP)
FPQ = (DDM, KTK)
NSR = (CRR, HHM)
XLD = (CXL, KNR)
PLG = (FFD, RDM)
RPM = (BNS, QFR)
SGJ = (FVV, TVP)
BPL = (PBJ, TRR)
RHN = (NHC, CKP)
MGB = (XJP, VDG)
RJH = (BTK, FBK)
VNP = (JGT, SFH)
BDX = (SNV, STL)
VSN = (HSS, HSS)
LCT = (MPP, HJP)
NBB = (GJC, BKT)
VRS = (GHL, PNM)
JJX = (BLB, FBQ)
TMB = (KXH, CJH)
RLX = (KXB, VVV)
NJM = (TGC, ZZZ)
VNG = (CMD, FKT)
GJJ = (MSV, CKT)
CVC = (SNH, TMT)
CVS = (DMP, DMP)
MFK = (CKS, FRS)
XHJ = (DJR, CJQ)
FCN = (XVV, BPZ)
JVM = (KKX, MTD)
RQM = (FBQ, BLB)
SLQ = (FXV, SMJ)
BNS = (LCT, BLQ)
DKD = (FVX, DHF)
JHF = (MBD, RSB)
FBQ = (GHJ, KQD)
KDV = (TSN, TDD)
FVL = (HJJ, TQJ)
LXL = (PKL, RBJ)
VDV = (FQN, DNP)
BDM = (HGT, MJR)
VDG = (KHJ, SDV)
BFG = (DJP, BPJ)
PNR = (XPV, HQS)
XTL = (RPQ, HRJ)
PGN = (PPC, KXX)
XNP = (LLV, KRH)
VTM = (DNH, SVP)
VJJ = (CRJ, SXV)
NVQ = (SBM, TPP)
RLV = (NGC, KQR)
THX = (NKX, PXK)
MLP = (GLJ, XBV)
MPC = (MNL, QTK)
FPX = (BSP, HJR)
NHC = (NHX, CNC)
CRV = (SLK, GSP)
NNC = (RHG, TKF)
SNH = (JHH, VRS)
KNR = (FVG, JCJ)
CRJ = (GQM, KJD)
PJT = (SRF, KML)
XJP = (KHJ, SDV)
BXL = (BSM, MKG)
QRB = (RHJ, RLS)
SMX = (KCF, KJR)
CSM = (FKL, NCM)
MGS = (QQR, SKG)
RTL = (SGJ, MPT)
CND = (NDL, NSD)
BTK = (QVS, FVL)
TNJ = (TBF, NDX)
JFV = (LMT, NBB)
CMJ = (XLQ, XLQ)
CCJ = (BTK, FBK)
SXQ = (FHG, MVL)
MLR = (DNH, SVP)
PJH = (LNK, DGH)
KFG = (QJC, BPL)
MRN = (RRP, TSM)
LBL = (HNK, STF)
NFR = (RBB, NDT)
NGR = (RDL, VQX)
PVR = (VTH, FSQ)
LVV = (XFN, DSQ)
RCX = (XVK, LMV)
FLV = (NGR, XKM)
CRR = (FRV, BDM)
BSM = (CND, TSD)
FVX = (XRN, BXN)
TKF = (XCQ, BGQ)
QSQ = (NFR, QNT)
XVV = (SHP, MNJ)
RVD = (SNV, STL)
MKG = (TSD, CND)
QCB = (GPP, KRT)
NVX = (MSV, CKT)
GGV = (VTL, SNM)
GJC = (PVD, CBT)
QSP = (JGK, GST)
VBL = (MFT, NSX)
DDB = (RPS, NBT)
BKX = (HPR, CXD)
FKL = (VPJ, SQN)
VRH = (BPN, JXR)
QQR = (KBH, LRQ)
RSC = (LQB, TNG)
NRQ = (DKD, CHG)
RHL = (NVQ, NNR)
QCH = (MGB, QQS)
CTS = (BFG, HDC)
KHJ = (NGN, LJC)
RGK = (MVL, FHG)
CCH = (LKP, TFT)
VSL = (FFH, PRR)
KQR = (RPT, MGJ)
LCN = (XTS, DCF)
TJN = (TMT, SNH)
CLT = (NBS, VNP)
JCJ = (QFS, RSJ)
BPN = (TJN, CVC)
FXG = (GLJ, XBV)
BGQ = (KQB, BLP)
RMR = (TVH, JHB)
CTM = (JLL, VFC)
KCF = (SLQ, FLH)
DHF = (XRN, BXN)
NDJ = (SSH, FPQ)
KSX = (XTS, DCF)
RPT = (DPL, QHP)
QJV = (TVB, LDC)
TNG = (BCT, MMQ)
FBK = (FVL, QVS)
MBJ = (XJQ, VGG)
CHD = (GJF, BPC)
LSF = (QHL, XNP)
SHN = (HQS, XPV)
TQR = (CDR, QGG)
GRA = (NNK, VNG)
RNS = (MBJ, PHD)
VFC = (GTJ, CBN)
PPC = (LFJ, KHL)
DDT = (STF, HNK)
NSD = (TCV, DDV)
VMC = (FDX, RLK)
QXS = (JPG, BHR)
PDF = (MBD, RSB)
QRV = (PCB, JNV)
QVJ = (KSX, LCN)
QDL = (GLH, SPJ)
MDJ = (GJJ, NVX)
HJP = (FVF, RLX)
FRS = (GLT, CDQ)
SBM = (FDD, XNG)
SMG = (CMQ, MGX)
TQJ = (NPH, CQS)
RHQ = (MJV, XTG)
FFD = (MSN, FKN)
CSS = (XQN, NNC)
PVD = (RQM, JJX)
GBS = (QRT, CCK)
JHH = (PNM, GHL)
QHL = (LLV, KRH)
"""

instructions = []
graph = {}

for i, line in enumerate(input.splitlines()):
    if line == "":
        pass
    elif "(" in line:
        # add to graph
        node, children = line.split(" = ")
        left, right = children[1:-1].split(", ")
        graph[node] = (left, right)
    else:
        # instructions
        instructions = [1 if c == "R" else 0 for c in line]


def find_cycle_data(node):
    i = 0
    end_node_indices = []
    # set(tuple(node, instruction_index))
    seen = {}
    cycle_offset = None
    while True:
        if (node, i % len(instructions)) in seen:
            cycle_offset = seen[(node, i % len(instructions))]
            break
        seen[(node, i % len(instructions))] = i
        if node.endswith("Z"):
            end_node_indices.append(i)
        node = graph[node][instructions[i % len(instructions)]]
        i += 1
    end_node_offset_within_cycle = end_node_indices[-1] - cycle_offset
    assert len(end_node_indices) == 1
    assert end_node_offset_within_cycle >= cycle_offset
    return {
        "cycle_offset": cycle_offset,
        "end_node_offset_within_cycle": end_node_offset_within_cycle,
        "cycle_length": i - cycle_offset,
        "end_node_offset": end_node_indices[-1],
    }


nodes = [k for k in graph.keys() if k.endswith("A")]
cycle_data = [find_cycle_data(node) for node in nodes]


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


total = 1
for data in cycle_data:
    total = lcm(total, data["end_node_offset"])

print(total)
