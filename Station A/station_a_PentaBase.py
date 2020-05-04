

metadata = {
    'protocolName': 'DTU Sample Reformatting-Single Pipette',
    'author': 'Lachlan <lajamu@biosustain.dtu.dk',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.2'
}

#This protocol takes 4x 24 well sample racks and reformats into a 96 deep well plate and performs a lysis step.
#Requires 2x 20 µL Tip racks and 2x 200 µL Tip racks. 
#Adapted from opetrons protocol written by Chaz. Will require updating labware for samples and deepwell when specs are available. 
def get_loadwells(plate):
    loadwells = plate.columns()[0] + plate.columns()[6]      
    return(loadwells)
    

def run(protocol):
    
    
 
    tips200 = [protocol.load_labware('opentrons_96_tiprack_300ul', '3')]
   
    
    p300 = protocol.load_instrument(
        'p300_single', 'right', tip_racks=tips200)

    plate_type = "rna_ext_plate"
    plate1 = protocol.load_labware(plate_type, "10")
    plate2 = protocol.load_labware(plate_type, "9")
    plate3 = protocol.load_labware(plate_type, "7") 
    plate4 = protocol.load_labware(plate_type, "6")
    plate5 = protocol.load_labware(plate_type, "4" )
    plate6 = protocol.load_labware(plate_type,"1" )
    
    all_loadwells = get_loadwells(plate1)+\
                    get_loadwells(plate2)+\
                    get_loadwells(plate3)+\
                    get_loadwells(plate4)+\
                    get_loadwells(plate5)+\
                    get_loadwells(plate6)
                    
    

    
    #Load sample racks
    tuberack = "opentrons_24_tuberack_generic_2ml_screwcap"
    samplerack1 = protocol.load_labware(tuberack, '11')
    samplerack2 = protocol.load_labware(tuberack, '8')
    samplerack3 = protocol.load_labware(tuberack, '5')
    samplerack4 = protocol.load_labware(tuberack, '2')
    
    
    s1 = samplerack1.wells()
    s2 = samplerack2.wells()
    s3 = samplerack3.wells()
    s4 = samplerack4.wells()
    
    s2.reverse()
    s4.reverse()
    
    samps = s1 + s2 + s3 + s4
#    #Sample plate and sample selection
#    samps = samplerack1.wells()[:]+\
#    samplerack2.wells()[:].reverse()+\
#    samplerack3.wells()[:]+\
#    samplerack4.wells()[:].reverse()
#   
    #print(samps)
#    
##    
    p300.flow_rate.aspirate = 150
    p300.flow_rate.dispense = 300
    p300.flow_rate.blow_out = 300
#
#
#Code to transfer sample to 96 well deep plate
#Currently set to 2 x 150uL. Can be modified to 2 x 100 by setting transferVol = 200
    
    transferVol = 200
    for src, dest in zip(samps, all_loadwells):
        p300.pick_up_tip()
        for _ in range(1):
            p300.transfer(transferVol, src, dest.top(-6), 
                          new_tip='never')
            p300.blow_out(dest.top(-6))
            p300.touch_tip()
        p300.drop_tip()
    protocol.comment("Congratulations! \nRun Complete. Seal and refridgerate deep-well plate.")

