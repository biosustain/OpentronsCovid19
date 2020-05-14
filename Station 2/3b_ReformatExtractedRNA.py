

metadata = {
    'protocolName': 'DTU Sample Reformatting-Single Pipette',
    'author': 'Lachlan <lajamu@biosustain.dtu.dk',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.2'
}

#This protocol takes 4x 24 well sample racks and reformats into a 96 deep well plate and performs a lysis step.
#Requires 2x 20 µL Tip racks and 2x 200 µL Tip racks. 
#Adapted from opetrons protocol written by Chaz. Will require updating labware for samples and deepwell when specs are available. 
def get_rnaCols(plate):
    rnaCols = [plate.columns()[5][0], plate.columns()[11][0]]
    return(rnaCols)

def run(protocol):

    tips200 = [protocol.load_labware('opentrons_96_tiprack_300ul', '1')]
   
    
    p300Multi = protocol.load_instrument(
        'p300_multi', 'right', tip_racks=tips200)

    plate_type = "pentabase_plate_with_adaptor"
    rnaplate1 = protocol.load_labware(plate_type, '10')
    rnaplate2 = protocol.load_labware(plate_type, "11")
    rnaplate3 = protocol.load_labware(plate_type, "7")
    rnaplate4 = protocol.load_labware(plate_type, "8")
    rnaplate5 = protocol.load_labware(plate_type, "9")
    rnaplate6 = protocol.load_labware(plate_type, "6")
    
    rnaCols = get_rnaCols(rnaplate1) +\
    get_rnaCols(rnaplate2)+\
    get_rnaCols(rnaplate3)+\
    get_rnaCols(rnaplate4)+\
    get_rnaCols(rnaplate5)+\
    get_rnaCols(rnaplate6)
    
    outPlate = protocol.load_labware("nest_96_wellplate_100ul_pcr_full_skirt", "3")
    
    print(rnaCols)
    
    for i in range(12):
        p50Multi.transfer(50, rnaCols[i], outPlate.columns()[i], new_tip="always")
        
        