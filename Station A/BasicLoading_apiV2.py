# -*- coding: utf-8 -*-

metadata = {
    'protocolName': 'Multichannel Pipette Testing',
    'author': 'Lachlan <lajamu@biosustain.dtu.dk',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.2'
}

def run(protocol):
    tips200 = [protocol.load_labware('opentrons_96_tiprack_300ul', '1')]
   
    
    p50Multi = protocol.load_instrument(
        'p50_multi', 'right', tip_racks=tips200)

    plate_type = "nest_96_wellplate_100ul_pcr_full_skirt"
    plate1 = protocol.load_labware(plate_type, '3')
    reservoir1 = protocol.load_labware('agilent_1_reservoir_290ml', '2')
    


#Code to transfer sample to 96 well deep plate
#Currently set to 2 x 150uL. Can be modified to 2 x 100 by setting transferVol = 200
    def dispense_to_plate(vol, source, dest):
        for n in range(0,12):
            p50Multi.transfer(vol, source['A1'], dest.columns(n), new_tip="always", trash = False)
        
    
    dispense_to_plate(5, reservoir1, plate1)

    
