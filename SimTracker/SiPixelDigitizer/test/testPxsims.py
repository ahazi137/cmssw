
#
import FWCore.ParameterSet.Config as cms

process = cms.Process("simTest")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('PixelSimHitsTest'),
    destinations = cms.untracked.vstring('cout'),
#    destinations = cms.untracked.vstring("log","cout"),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
    )
#    log = cms.untracked.PSet(
#        threshold = cms.untracked.string('DEBUG')
#    )
)

process.source = cms.Source("PoolSource",
    fileNames =  cms.untracked.vstring(
#    '/store/user/kotlinski/mu100/simhits/simHits.root',
#    'file:simHits.root'
#    'file:/afs/cern.ch/work/d/dkotlins/public//MC/mu/pt100/simhits/simHits1.root'
     'file:/afs/cern.ch/work/a/ahazi/public/datas/CMSSW_6_2_0_SLHC13-RelValSingleMuPt1-GEN-SIM-DES19_62_V8_UPG2019-v1/D4BD2CC3-B2E5-E311-876F-002590593876.root'
    )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('sim_histos.root')
)

#process.load("Configuration.Geometry.GeometryIdeal_cff")
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load('Configuration.Geometry.GeometryExtended2019Reco_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load("Configuration.StandardSequences.MagneticField_38T_cff")

# needed for global transformation
# process.load("Configuration.StandardSequences.FakeConditions_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")# Choose the global tag here:
#process.GlobalTag.globaltag = 'MC_53_V15::All'
#process.GlobalTag.globaltag = 'DESIGN53_V15::All'
#process.GlobalTag.globaltag = 'START53_V15::All'
# ideal
#process.GlobalTag.globaltag = 'MC_70_V1::All'
# realistiv alignment and calibrations 
#process.GlobalTag.globaltag = 'START70_V1::All'
# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS1', '')

process.analysis =  cms.EDAnalyzer("PixelSimHitsTest",
	src = cms.string("g4SimHits"),
#	list = cms.string("TrackerHitsPixelBarrelLowTof"),
#	list = cms.string("TrackerHitsPixelBarrelHighTof"),
	list = cms.string("TrackerHitsPixelEndcapLowTof"),
#	list = cms.string("TrackerHitsPixelEndcapHighTof"),
        Verbosity = cms.untracked.bool(False),
#        mode = cms.untracked.string("bpix"),
        mode = cms.untracked.string("fpix"),
)

process.p = cms.Path(process.analysis)


# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.phase1TkCustoms
from SLHCUpgradeSimulations.Configuration.phase1TkCustoms import customise

#call to customisation function customise imported from SLHCUpgradeSimulations.Configuration.phase1TkCustoms
process = customise(process)
