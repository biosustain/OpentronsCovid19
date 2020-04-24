

metadata = {
    'protocolName': 'DTU Sample Reformatting-Single Pipette',
    'author': 'Lachlan <lajamu@biosustain.dtu.dk',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.2'
}

#This protocol takes 4x 24 well sample racks and reformats into a 96 deep well plate and performs a lysis step.
#Requires 2x 20 µL Tip racks and 2x 200 µL Tip racks. 
#Adapted from opetrons protocol written by Chaz. Will require updating labware for samples and deepwell when specs are available. 

def run(protocol):

 
    tips200 = [protocol.load_labware('opentrons_96_tiprack_300ul', '4')]
   
    
    p300 = protocol.load_instrument(
        'p300_single', 'right', tip_racks=tips200)

    plate = protocol.load_labware('nunc_96_wellplate_1300ul', '1')
     
    #Select number of wells to run. 
    platewells = plate.wells()

    #Load sample racks
    tuberack = "opentrons_24_tuberack_generic_2ml_screwcap"
    samplerack1 = protocol.load_labware(tuberack '5')
    samplerack2 = protocol.load_labware(tuberack, '6')
    samplerack3 = protocol.load_labware(tuberack, '2')
    samplerack4 = protocol.load_labware(tuberack, '3')
    
    #Sample plate and sample selection
    samps = samplerack1.wells()[:]+\
    samplerack2.wells()[:]+\
    samplerack3.wells()[:]+\
    samplerack4.wells()[:]
   
    
    
    p300.flow_rate.aspirate = 150
    p300.flow_rate.dispense = 300
    p300.flow_rate.blow_out = 300


#Code to transfer sample to 96 well deep plate
#Currently set to 2 x 150uL. Can be modified to 2 x 100 by setting transferVol = 200
    
    transferVol = 300
    for src, dest in zip(samps, platewells):
        p300.pick_up_tip()
        p300.transfer(transferVol/2, src.bottom(3), dest.top(-6), new_tip='never')
        p300.transfer(transferVol/2, src.bottom(3), dest.top(-6), new_tip="never")
        p300.blow_out(dest.top(-6))
        p300.drop_tip()
    protocol.comment("Congratulations! \nRun Complete. Seal and refridgerate deep-well plate.")

