##############################################################################

import FWCore.ParameterSet.Config as cms

process = cms.Process("Test")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
# process.load("Configuration.StandardSequences.Geometry_cff")
#process.load("Configuration.Geometry.GeometryIdeal_cff")
#process.load('Configuration.Geometry.GeometryExtended2017Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2019Reco_cff')
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.Services_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

# from v7
#process.load("SimGeneral.MixingModule.pixelDigitizer_cfi")
# process.load("SimTracker.Configuration.SimTracker_cff")
process.load("SimG4Core.Configuration.SimG4Core_cff")

# process.load("SimGeneral.MixingModule.mixNoPU_cfi")
from SimGeneral.MixingModule.aliases_cfi import * 
from SimGeneral.MixingModule.mixObjects_cfi import *
# from SimGeneral.MixingModule.digitizers_cfi import *
from SimGeneral.MixingModule.pixelDigitizer_cfi import *
from SimGeneral.MixingModule.stripDigitizer_cfi import *
from SimGeneral.MixingModule.trackingTruthProducer_cfi import *

process.mix = cms.EDProducer("MixingModule",
#    digitizers = cms.PSet(theDigitizers),
#    digitizers = cms.PSet(
#      mergedtruth = cms.PSet(
#            trackingParticles
#      )
#    ),

  digitizers = cms.PSet(
   pixel = cms.PSet(
    pixelDigitizer
   ),
#  strip = cms.PSet(
#    stripDigitizer
#  ),
  ),

#theDigitizersValid = cms.PSet(
#  pixel = cms.PSet(
#    pixelDigitizer
#  ),
#  strip = cms.PSet(
#    stripDigitizer
#  ),
#  ecal = cms.PSet(
#    ecalDigitizer
#  ),
#  hcal = cms.PSet(
#    hcalDigitizer
#  ),
#  castor = cms.PSet(
#    castorDigitizer
#  ),
#  mergedtruth = cms.PSet(
#    trackingParticles
#  )
#),

    LabelPlayback = cms.string(' '),
    maxBunch = cms.int32(3),
    minBunch = cms.int32(-5), ## in terms of 25 ns

    bunchspace = cms.int32(25),
    mixProdStep1 = cms.bool(False),
    mixProdStep2 = cms.bool(False),

    playback = cms.untracked.bool(False),
    useCurrentProcessOnly = cms.bool(False),
    mixObjects = cms.PSet(
        mixTracks = cms.PSet(
            mixSimTracks
        ),
        mixVertices = cms.PSet(
            mixSimVertices
        ),
        mixSH = cms.PSet(
#            mixPixSimHits
# mixPixSimHits = cms.PSet(
    input = cms.VInputTag(cms.InputTag("g4SimHits","TrackerHitsPixelBarrelHighTof"), 
                          cms.InputTag("g4SimHits","TrackerHitsPixelBarrelLowTof"),
                          cms.InputTag("g4SimHits","TrackerHitsPixelEndcapHighTof"), 
                          cms.InputTag("g4SimHits","TrackerHitsPixelEndcapLowTof"), 
#                          cms.InputTag("g4SimHits","TrackerHitsTECHighTof"), 
#                          cms.InputTag("g4SimHits","TrackerHitsTECLowTof"), 
#                          cms.InputTag("g4SimHits","TrackerHitsTIBHighTof"),
#                          cms.InputTag("g4SimHits","TrackerHitsTIBLowTof"), 
#                          cms.InputTag("g4SimHits","TrackerHitsTIDHighTof"), 
#                          cms.InputTag("g4SimHits","TrackerHitsTIDLowTof"), 
#                          cms.InputTag("g4SimHits","TrackerHitsTOBHighTof"), 
#                          cms.InputTag("g4SimHits","TrackerHitsTOBLowTof")
    ),
    type = cms.string('PSimHit'),
    subdets = cms.vstring(
        'TrackerHitsPixelBarrelHighTof',
        'TrackerHitsPixelBarrelLowTof',
        'TrackerHitsPixelEndcapHighTof',
        'TrackerHitsPixelEndcapLowTof',
#        'TrackerHitsTECHighTof',
#        'TrackerHitsTECLowTof',
#        'TrackerHitsTIBHighTof',
#        'TrackerHitsTIBLowTof',
#        'TrackerHitsTIDHighTof',
#        'TrackerHitsTIDLowTof',
#        'TrackerHitsTOBHighTof',
#        'TrackerHitsTOBLowTof'
    ),
    crossingFrames = cms.untracked.vstring(),
#        'MuonCSCHits',
#        'MuonDTHits',
#        'MuonRPCHits'),
#)   
        ),
        mixHepMC = cms.PSet(
            mixHepMCProducts
        )
    )
)

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
#     simMuonCSCDigis = cms.PSet(
#        initialSeed = cms.untracked.uint32(1234567),
#        engineName = cms.untracked.string('TRandom3')
#    ),
     mix = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('TRandom3')
   )
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(
       'file:/afs/cern.ch/work/a/ahazi/public/datas/CMSSW_6_2_0_SLHC13-RelValSingleMuPt1-GEN-SIM-DES19_62_V8_UPG2019-v1/D4BD2CC3-B2E5-E311-876F-002590593876.root'
       #'file:/afs/cern.ch/work/a/ahazi/public/datas/gensim8k_cmssw710pre1/MinBias_8TeV_GEN_SIM_2000k_13_1_DUJ.root'
  )
)

# Choose the global tag here:
# for v7.0
#process.GlobalTag.globaltag = 'MC_70_V1::All'

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS1', '')

process.o1 = cms.OutputModule("PoolOutputModule",
            outputCommands = cms.untracked.vstring('drop *','keep *_*_*_Test'),
      fileName = cms.untracked.string('file:digis_phaseI_2019.root')
#      fileName = cms.untracked.string('file:dummy.root')
)

process.g4SimHits.Generator.HepMCProductLabel = 'source'

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.phase1TkCustoms
from SLHCUpgradeSimulations.Configuration.phase1TkCustoms import customise

#call to customisation function customise imported from SLHCUpgradeSimulations.Configuration.phase1TkCustoms
process = customise(process)

# modify digitizer parameters
#process.simSiPixelDigis.ThresholdInElectrons_BPix = 3500.0 
process.mix.digitizers.pixel.ThresholdInElectrons_BPix = 3500.0
process.mix.digitizers.pixel.LorentzAngle_DB = False
process.mix.digitizers.pixel.AddPixelInefficiencyFromPython = False
process.mix.digitizers.pixel.useDB = False

#This process is to run the digitizer, pixel gitizer is now clled by the mix module
process.p1 = cms.Path(process.mix)

process.outpath = cms.EndPath(process.o1)


