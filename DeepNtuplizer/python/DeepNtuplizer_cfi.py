import FWCore.ParameterSet.Config as cms

deepntuplizer = cms.EDAnalyzer('DeepNtuplizer',
                                vertices   = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                secVertices = cms.InputTag("slimmedSecondaryVertices"),
                                jets       = cms.InputTag("slimmedJets"),
                                pupInfo = cms.InputTag("slimmedAddPileupInfo"),
                                rhoInfo = cms.InputTag("fixedGridRhoFastjetAll"),	
                                SVs  = cms.InputTag("slimmedSecondaryVertices"),
                                LooseSVs = cms.InputTag("inclusiveCandidateSecondaryVertices"),
                                genJetMatchWithNu = cms.InputTag("patGenJetMatchWithNu"),
                                genJetMatchRecluster = cms.InputTag("patGenJetMatchRecluster"),
                                pruned = cms.InputTag("prunedGenParticles"),
                                muons = cms.InputTag("slimmedMuons"),
                                electrons = cms.InputTag("slimmedElectrons"),
                                jetPtMin     = cms.double(20.0),
                                jetPtMax     = cms.double(1000),
                                jetAbsEtaMin = cms.double(0.0),
                                jetAbsEtaMax = cms.double(2.4),
                                gluonReduction = cms.double(0.0),
                                tagInfoName = cms.string('deepNN'),
                                bDiscriminators = cms.vstring(),
                                nCollinear = cms.uint32(0), #no splitting
                                )
