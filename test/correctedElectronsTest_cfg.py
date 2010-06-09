import FWCore.ParameterSet.Config as cms

process = cms.Process("CorrectedElectrons")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

process.load("RecoEgamma.EgammaTools.correctedElectronsProducer_cfi")
 
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
    )

process.source = cms.Source ("PoolSource",
                             fileNames =  cms.untracked.vstring(    
    '/store/relval/CMSSW_3_6_1/RelValZEE/GEN-SIM-RECO/MC_36Y_V7A-v1/0020/D6ED2A95-515D-DF11-ABD2-0018F3D096DC.root',
    '/store/relval/CMSSW_3_6_1/RelValZEE/GEN-SIM-RECO/MC_36Y_V7A-v1/0020/9C8E3A46-2A5D-DF11-A735-002618943877.root'
    ))

process.out = cms.OutputModule("PoolOutputModule",
                               outputCommands = cms.untracked.vstring('keep *'),
                               fileName = cms.untracked.string('test.root')
                               )

process.p = cms.Path(process.gsfElectrons)

process.outpath = cms.EndPath(process.out)
process.GlobalTag.globaltag = 'MC_36Y_V7A::All'
