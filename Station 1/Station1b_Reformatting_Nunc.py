

metadata = {
    'protocolName': 'DTU Sample Reformatting-Single Pipette',
    'author': 'Lachlan <lajamu@biosustain.dtu.dk',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.2'
}

#This protocol reformats from 4 x 24 well racks filled with sample tubes into 6x16 preloaded pentabase plates.
#This protocol is calibrated to the taller Nunc tube variant.


def get_loadwells(plate):
    """Returns the 1st and 7th column of a plate. Used to determine 
    where to load the pentabase preloaded extraction plates."""
    loadwells = plate.columns()[0] + plate.columns()[6]
    return(loadwells)
        

def run(protocol):
    """
    Uses a p1000 tip to transfer from sample tubes to pentabase RNA extraction plates.
    Protocol takes approximately 45 minutes to run in the robot.
    There is a defined pause at the halfway point, at which time the tip trash should be emptied to prevent 
    too many tips preventing ejection.
    """
 
    tips1000= [protocol.load_labware('opentrons_96_tiprack_1000ul', '10')]
   
    
    p300 = protocol.load_instrument(
        'p1000_single', 'left', tip_racks=tips1000)

 
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

#Set defined flow rates.
    p300.flow_rate.aspirate = 150
    p300.flow_rate.dispense = 300
    p300.flow_rate.blow_out = 300
    

    transferVol = 300
    x = 0
    for src, dest in zip(samps, all_loadwells):
        p300.pick_up_tip()
        for _ in range(1):
        	#2 mm of the bottom of the tube works effectively with both taller Nunc variant and the standard Nunc tubes. 
            p300.transfer(transferVol, src.bottom(z=2), dest.top(-6), 
                              new_tip='never')
            p300.blow_out(dest.top(-6))
            p300.touch_tip()
        p300.drop_tip()
        if x != 47:
            x+=1
        else:
            protocol.pause("Check Tip Trash")
            x+=1

    protocol.comment("Congratulations! \nRun Complete. Refridgerate deep-well plate.")

