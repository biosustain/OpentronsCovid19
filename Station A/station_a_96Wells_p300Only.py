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

    #set_lights(button=None, rails=None)
    tips200 = [protocol.load_labware('opentrons_96_tiprack_300ul', '9'), \
               protocol.load_labware('opentrons_96_tiprack_300ul', '11')]
   
    
    p300 = protocol.load_instrument(
        'p300_single', 'left', tip_racks=tips200)
    
    
    tempdeck= protocol.load_module('tempdeck', '1')
    tempdeck.set_temperature(4)
    plate = tempdeck.load_labware('nunc_96_wellplate_1300ul', '1')
     
    #Select number of wells to run. 
    platewells = plate.wells()

    #Load sample racks
    samplerack1 = protocol.load_labware('bpg_24_tuberack_2ml', '5')
    samplerack2 = protocol.load_labware('bpg_24_tuberack_2ml', '6')
    samplerack3 = protocol.load_labware('bpg_24_tuberack_2ml', '2')
    samplerack4 = protocol.load_labware('bpg_24_tuberack_2ml', '3')
    
    #Sample plate and sample selection
    samps = samplerack1.wells()[:]+\
    samplerack2.wells()[:]+\
    samplerack3.wells()[:]+\
    samplerack4.wells()[:]
   
    
    
    p300.flow_rate.aspirate = 150
    p300.flow_rate.dispense = 300
    p300.flow_rate.blow_out = 300


#Code to transfer sample to 96 well deep plate
    for src, dest in zip(samps, platewells):
        p300.pick_up_tip()
        p300.transfer(150, src.bottom(9), dest.top(-6), new_tip='never')
        p300.dispense(100, dest.top(-6))
        p300.transfer(50, src.bottom(1.5), dest.top(-6), new_tip="never")
        p300.dispense(300, dest.top(-6))
        p300.drop_tip()


