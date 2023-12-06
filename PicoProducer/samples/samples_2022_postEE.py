from TauFW.PicoProducer.storage.Sample import MC as M
from TauFW.PicoProducer.storage.Sample import Data as D
storage  = "/eos/cms/store/group/phys_tau/irandreo/Run3_22/$DAS"
storage_postEE  = "/eos/cms/store/group/phys_tau/irandreo/Run3_22_postEE_new/$DAS"
url      = "root://cms-xrd-global.cern.ch/"
filelist = None 
samples  = [
  
  # DRELL-YAN
  # M('DY','DYJetsToLL_M-50',
  #   "/DYJetsToLL_M-50",
  #   store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYto2L-4Jets_MLL-50',
    "DYto2L-4Jets_MLL-50",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYto2L-4Jets_MLL-50_1J',
  "DYto2L-4Jets_MLL-50_1J",
  store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYto2L-4Jets_MLL-50_2J',
  "DYto2L-4Jets_MLL-50_2J",
  store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYto2L-4Jets_MLL-50_3J',
  "DYto2L-4Jets_MLL-50_3J",
  store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYto2L-4Jets_MLL-50_4J',
  "DYto2L-4Jets_MLL-50_4J",
  store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYto2TautoMuTauh_M-50',
    "DYto2TautoMuTauh_M-50",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),

  # # SM Higgs
  # M('SMH','GluGluHToTauTau_M125_v2',
  #   "GluGluHToTauTau_M125_v2",
  #   store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  # M('SMH','GluGluHToTauTau_M125_v3',
  #   "GluGluHToTauTau_M125_v3",
  #   store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  # M('SMH','VBFHToTauTau_M125_Poisson60KeepRAW',
  #   "VBFHToTauTau_M125_Poisson60KeepRAW",
  #   store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  # M('SMH','VBFHToTauTau_M125_v2_Poisson70KeepRAW',
  #   "VBFHToTauTau_M125_v2_Poisson70KeepRAW",
  #   store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),

  # ST
  M('ST','TbarBQ_t-channel',
    "TbarBQ_t-channel",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('ST','TbarWplusto2L2Nu',
    "TbarWplusto2L2Nu",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('ST','TbarWplustoLNu2Q',
    "TbarWplustoLNu2Q",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('ST','TBbarQ_t-channel',
    "TBbarQ_t-channel",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('ST','TWminusto2L2Nu',
    "TWminusto2L2Nu",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('ST','TWminustoLNu2Q',
    "TWminustoLNu2Q",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,zpt=True"),

  # TTBAR
  M('TT','TTTo2L2Nu',
    "/TTTo2L2Nu",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('TT','TTto4Q',
    "/TTto4Q",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('TT','TTtoLNu2Q',
    "/TTtoLNu2Q",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,toppt=True"),

  # W JETS
  M('W','WJetstoLNu_2Jets',
    "/WJetstoLNu_2Jets",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('W','WtoLNu-4Jets',
    "/WtoLNu-4Jets",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('W','WJetstoLNu-4Jets_1J',
    "/WJetstoLNu-4Jets_1J",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('W','WJetstoLNu-4Jets_2J',
    "WJetstoLNu-4Jets_2J",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('W','WJetstoLNu-4Jets_3J',
    "WJetstoLNu-4Jets_3J",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('W','WtoLNu-4Jets_4J',
    "WtoLNu-4Jets_4J",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True,toppt=True"),

  
  # DIBOSON
  M('VV','WW',
    "/WW",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True"),
  M('VV','WZ',
    "/WZ",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True"),
  M('VV','ZZ',
    "/ZZ",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True"),
  
  #THREE-BOSON
  M('VVV','WWW_4F',
    "/WWW_4F",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True"),
  M('VVV','WWZ_4F',
    "/WWZ_4F",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True"),
  M('VVV','WZZ',
    "/WZZ",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True"),
  M('VVV','ZZZ',
    "/ZZZ",
    store=storage_postEE,url=url,files=filelist,opts="useT1=True"),

  # EGAMMA
  D('Data','EGamma_Run2022E',"/EGamma_Run2022E",
   store=storage_postEE,url=url,files=filelist,opts="useT1=True",channels=["skim*",'etau','ee']),
  D('Data','EGamma_Run2022F',"/EGamma_Run2022F",
   store=storage_postEE,url=url,files=filelist,opts="useT1=True",channels=["skim*",'etau','ee']),
  D('Data','EGamma_Run2022G',"/EGamma_Run2022G",
   store=storage_postEE,url=url,files=filelist,opts="useT1=True",channels=["skim*",'etau','ee']),

  # # JETMET
  # D('Data','JetMet_Run2022E',"/JetMet_Run2022E",
  #  store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),
  # D('Data','JetMet_Run2022F',"/JetMet_Run2022F",
  #  store=storage_postEE,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),
  # D('Data','JetMet_Run2022G',"/JetMet_Run2022G",
  #  store=storage_postEE,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),

  # MUONEG
  D('Data','MuonEG_Run2022E',"/MuonEG_Run2022E",
   store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),
  D('Data','MuonEG_Run2022F',"/MuonEG_Run2022F",
   store=storage_postEE,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),
  D('Data','MuonEG_Run2022G',"/MuonEG_Run2022G",
   store=storage_postEE,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),

  # MUON
  D('Data','Muon_Run2022E',"/Muon_Run2022E",
   store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),
  D('Data','Muon_Run2022F',"/Muon_Run2022F",
   store=storage_postEE,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),
  D('Data','Muon_Run2022G',"/Muon_Run2022G",
   store=storage_postEE,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),

  # TAU

  D('Data','Tau_Run2022E',"/Tau_Run2022E",
   store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'tautau']),
  D('Data','Tau_Run2022F',"/Tau_Run2022F",
   store=storage_postEE,url=url,files=filelist,opts="useT1=True",channels=["skim*",'tautau']),
  D('Data','Tau_Run2022G',"/Tau_Run2022G",
   store=storage_postEE,url=url,files=filelist,opts="useT1=True",channels=["skim*",'tautau']),
    
]