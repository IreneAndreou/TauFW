from TauFW.PicoProducer.storage.Sample import MC as M
from TauFW.PicoProducer.storage.Sample import Data as D
storage  = "/eos/cms/store/group/phys_tau/irandreo/Run3_22/"
url      = "root://cms-xrd-global.cern.ch/"
filelist = None 
samples  = [
  
  # DRELL-YAN
  M('DY','DYJetsToLL_M-50',
    "/DYJetsToLL_M-50",
    store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYto2L-4Jets_MLL-50',
    "DYto2L-4Jets_MLL-50",
    store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYto2L-4Jets_MLL-50_1J',
  "/DYto2L-4Jets_MLL-50_1J",
  store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYto2L-4Jets_MLL-50_2J',
  "/DYto2L-4Jets_MLL-50_2J",
  store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYto2L-4Jets_MLL-50_3J',
  "DYto2L-4Jets_MLL-50_3J",
  store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYto2L-4Jets_MLL-50_4J',
  "DYto2L-4Jets_MLL-50_4J",
  store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYTo2L_MLL-4to50',
  "DYTo2L_MLL-4to50",
  store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYTo2L_MLL-50',
  "/DYTo2L_MLL-50",
  store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('DY','DYto2TautoMuTauh_M-50',
    "DYto2TautoMuTauh_M-50",
    store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),

  # # SM Higgs
  # M('SMH','GluGluHToTauTau_M125_v3',
  #   "GluGluHToTauTau_M125_v3",
  #   store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  # M('SMH','VBFHToTauTau_M125_v3',
  #   "VBFHToTauTau_M125_v3",
  #   store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),

  # ST
  M('ST','TbarBQ_t-channel',
    "TbarBQ_t-channel",
    store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('ST','TbarWplusto2L2Nu',
    "TbarWplusto2L2Nu",
    store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('ST','TbarWplustoLNu2Q',
    "TbarWplustoLNu2Q",
    store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('ST','TBbarQ_t-channel',
    "TBbarQ_t-channel",
    store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('ST','TWminusto2L2Nu',
    "TWminusto2L2Nu",
    store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),
  M('ST','TWminustoLNu2Q',
    "TWminustoLNu2Q",
    store=storage,url=url,files=filelist,opts="useT1=True,zpt=True"),

  # TTBAR
  M('TT','TT',
    "/TT",
    store=storage,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('TT','TT_ext1',
    "/TT_ext1",
    store=storage,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('TT','TTTo2L2Nu',
    "/TTTo2L2Nu",
    store=storage,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('TT','TTto4Q',
    "/TTto4Q",
    store=storage,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('TT','TTtoLNu2Q',
    "/TTtoLNu2Q",
    store=storage,url=url,files=filelist,opts="useT1=True,toppt=True"),

  # W JETS
  M('W','WJetsToLNu-2Jets',
    "/WJetsToLNu-2Jets",
    store=storage,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('W','WJetsToLNu-4Jets',
    "/WJetsToLNu-4Jets",
    store=storage,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('W','WJetsToLNu-4Jets_1J',
    "/WJetsToLNu-4Jets_1J",
    store=storage,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('W','WJetsToLNu-4Jets_2J',
    "/WJetsToLNu-4Jets_2J",
    store=storage,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('W','WJetsToLNu-4Jets_3J',
    "WJetsToLNu-4Jets_3J",
    store=storage,url=url,files=filelist,opts="useT1=True,toppt=True"),
  M('W','WJetsToLNu-4Jets_4J',
    "/WJetsToLNu-4Jets_4J",
    store=storage,url=url,files=filelist,opts="useT1=True,toppt=True"),

  
  # DIBOSON
  M('VV','WW',
    "/WW",
    store=storage,url=url,files=filelist,opts="useT1=True"),
  M('VV','WZ',
    "/WZ",
    store=storage,url=url,files=filelist,opts="useT1=True"),
  M('VV','ZZ',
    "/ZZ",
    store=storage,url=url,files=filelist,opts="useT1=True"),
  
  #THREE-BOSON
  M('VVV','WWW_4F',
    "/WWW_4F",
    store=storage,url=url,files=filelist,opts="useT1=True"),
  M('VVV','WWZ_4F',
    "/WWZ_4F",
    store=storage,url=url,files=filelist,opts="useT1=True"),
  M('VVV','WZZ',
    "/WZZ",
    store=storage,url=url,files=filelist,opts="useT1=True"),
  M('VVV','ZZZ',
    "/ZZZ",
    store=storage,url=url,files=filelist,opts="useT1=True"),

  # EGAMMA
  D('Data','EGamma_Run2022C',"/EGamma_Run2022C",
   store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'etau','ee']),
  D('Data','EGamma_Run2022D',"/EGamma_Run2022D",
   store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'etau','ee']),

  # # JETMET
  # D('Data','JetMet_Run2022C',"/JetMet_Run2022C",
  #  store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),
  # D('Data','JetMet_Run2022D',"/JetMet_Run2022D",
  #  store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),

  # MUONEG
  D('Data','MuonEG_Run2022C',"/MuonEG_Run2022C",
   store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),
  D('Data','MuonEG_Run2022D',"/MuonEG_Run2022D",
   store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),

  # MUON
  D('Data','Muon_Run2022C',"/Muon_Run2022C",
   store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),
  D('Data','Muon_Run2022D',"/Muon_Run2022D",
   store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),

  # TAU

  D('Data','Tau_Run2022C',"/Tau_Run2022C",
   store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'tautau']),
  D('Data','Tau_Run2022D',"/Tau_Run2022D",
   store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'tautau']),
    
  # SINGLE MUON
  D('Data','SingleMuon_Run2022C',"/SingleMuon_Run2022C",
   store=storage,url=url,files=filelist,opts="useT1=True",channels=["skim*",'mutau','mumu','emu']),
]