

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
    
    
 
    tips1000= [protocol.load_labware('opentrons_96_tiprack_1000ul', '10')]
   
    
    p300 = protocol.load_instrument(
        'p1000_single', 'right', tip_racks=tips1000)

    plate_type = "pentabase_plate_with_adaptor"
    plate1 = protocol.load_labware(plate_type, "7")
    plate2 = protocol.load_labware(plate_type, "9")
    plate3 = protocol.load_labware(plate_type, "4") 
    plate4 = protocol.load_labware(plate_type, "6")
    plate5 = protocol.load_labware(plate_type, "3" )
    plate6 = protocol.load_labware(plate_type,"1" )
    
    all_loadwells = get_loadwells(plate1)+\
                    get_loadwells(plate2)+\
                    get_loadwells(plate3)+\
                    get_loadwells(plate4)+\
                    get_loadwells(plate5)+\
                    get_loadwells(plate6)
                    
    

    
    #Load sample racks
    tuberack = "nunc_24_aluminium"
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


    p300.flow_rate.aspirate = 150
    p300.flow_rate.dispense = 300
    p300.flow_rate.blow_out = 300

    
    transferVol = 300
    x = 0
    for src, dest in zip(samps, all_loadwells):
        if x != 48:
            p300.pick_up_tip()
            for _ in range(1):
                p300.transfer(transferVol, src, dest.top(-6), 
                              new_tip='never')
                p300.blow_out(dest.top(-6))
                p300.touch_tip()
            p300.drop_tip()
            x+=1
        else:
            protocol.pause("Empty Bin")
            x+=1

    protocol.comment("Congratulations! \nRun Complete. Seal and refridgerate deep-well plate.")

