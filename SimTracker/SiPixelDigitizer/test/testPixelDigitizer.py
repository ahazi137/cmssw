##############################################################################

import FWCore.ParameterSet.Config as cms

process = cms.Process("Test")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
# process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.Geometry.GeometryIdeal_cff")
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

process.mix.digitizers.pixel.DeadModules_DB = cms.bool(True)
#ROC killing
## process.mix.digitizers.pixel.DeadModules = cms.VPSet(
##                                                cms.PSet(Dead_detID = cms.int32(302055952), Module = cms.string("tbmA"), Dead_RocID = 
##                                                cms.vint32(1,4)) #lay1_lad4_mod-1;multiple test!z<0
##                                                ,cms.PSet(Dead_detID = cms.int32(302055956), Module = cms.string("none"),Dead_RocID = cms.vint32(6,13,10))
## #lay1_lad4_mod1;multiple test!z>0
##                                                ,cms.PSet(Dead_detID = cms.int32(302056720), Module = cms.string("none"),Dead_RocID = cms.vint32(0,7)) #half test lay1_lad1_mod1
##                                                #,cms.PSet(Dead_detID = cms.int32(302057744), Module = cms.string("none"), Dead_RocID = 
##                                                #cms.int32(14)) #lay1_lad-4_mod-1;multiple test
                                              
##                                                ,cms.PSet(Dead_detID = cms.int32(344019464), Module = cms.string("none"), Dead_RocID = 
##                                                cms.vint32(0,1,2)) #disk -1 Blade 11, panel 2, Module 2 multiple test
##                                                ,cms.PSet(Dead_detID = cms.int32(302056220), Module = cms.string("none"), Dead_RocID = 
##                                                cms.vint32(-1)) #lay1 lad6 mod-2 multiple test
##                                                 )


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
    input = cms.untracked.int32(10)
)

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(
       'file:/data/store/relval/CMSSW_7_1_0_pre1/GEN-SIM/A4846C0D-0B86-E311-8B2E-003048FEB9EE.root'
  )
)
###PU related START
PileupInput = cms.untracked.vstring(
#    # cern
#    #'/store/caf/user/jkarancs/MinBias_TuneZ2star_8TeV_GENSIM_CMSSW_7_1_0pre1/MinBias_8TeV_GEN_SIM_2000k_1_1_FQV.root'
#    # ui3 local
    'file:/data/store/relval/CMSSW_7_1_0_pre1/GEN-SIM/88CDC2A6-1186-E311-A9F5-02163E00E5C7.root'
#    # kfki - use these with crab when running on T2_HU_Budapest
)

# Input pileup distribution for MixingModule
# Can use the same file in TimingStudy for pileup reweighting
# Note: the desired mc_input distribution has to be shifted by -1 wrt mcpileup
PileupHistoInput = cms.untracked.string(
    'file:PileupHistogram_201278_flatpileupMC.root' # Flat Pileup
    #'file:PileupHistogram_201278.root' # 201278 Pileup
)
PileupHistoName=cms.untracked.string('mc_input')

# configuration to model pileup for initial physics phase
# mix
#process.load("SimGeneral.MixingModule.mixNoPU_cfi") # No Pileup
process.load('SimGeneral.MixingModule.mix_2012_201278_1_cfi') # Silvias pileup mixing

# Change MinBias input file and Input Pileup Distribution

process.mix.input = cms.SecSource("PoolSource",
    type = cms.string('histo'),
    nbPileupEvents  = cms.PSet(
        fileName = PileupHistoInput,
        histoName = PileupHistoName,
    ),
    sequential = cms.untracked.bool(False),
    manage_OOT = cms.untracked.bool(True),
    OOT_type = cms.untracked.string('Poisson'),
    fileNames = PileupInput
)
###PU related END

# Choose the global tag here:
# for v7.0
process.GlobalTag.globaltag = 'MC_70_V1::All'


#change to local tag
"""
import CalibTracker.Configuration.Common.PoolDBESSource_cfi

process.myLocalDB = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(
       connect = cms.string (
        'sqlite_file:/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERCALIB/Pixels/PixelDB2013/SiPixelQuality/SiPixelQuality_620p5/builder/deadModule_v20.db'
        ),
        toGet = cms.VPSet(cms.PSet(
                record = cms.string('SiPixelQualityFromDbRcd'),
                tag = cms.string('SiPixelQuality_v20')
                                  )
                         )
        )
process.es_prefer_Quality = cms.ESPrefer("PoolDBESSource","myLocalDB")

"""

process.o1 = cms.OutputModule("PoolOutputModule",
      #      outputCommands = cms.untracked.vstring('drop *','keep *_*_*_Test'),
      fileName = cms.untracked.string('file:digis_0.root')
#      fileName = cms.untracked.string('file:dummy.root')
)

process.g4SimHits.Generator.HepMCProductLabel = 'source'

# modify digitizer parameters
#process.simSiPixelDigis.ThresholdInElectrons_BPix = 3500.0 
process.mix.digitizers.pixel.ThresholdInElectrons_BPix = 3500.0 

#This process is to run the digitizer, pixel gitizer is now clled by the mix module
process.p1 = cms.Path(process.mix)

#process.outpath = cms.EndPath(process.o1)


