metadata = {
    'protocolName': 'Station C - Mastermix',
    'author': 'Mathew Jessop Fabre <mmjf@dtu.dk>',
    'source': 'COVID-19 Project - DTU',
    'apiLevel': '2.2'
}

### Protocol to set up a 96 qPCR plate filled with reaction master mix
# Based on the DiaPlex Q Novel Coronavirus Detection Kit protocol

def run(protocol):

    # tip racks - how many will be needed?
    #tip_racks_20 = [protocol.load_labware('opentrons_96_filtertiprack_20ul', '1')]
            
    tip_racks_200 = [protocol.load_labware('opentrons_96_filtertiprack_200ul', '1')]

    # Pipette - p20 single
    #p20s = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=tip_racks_20)
    p300s = protocol.load_instrument('p300_single', 'left', tip_racks=tip_racks_200)

    #p20s.flow_rate.aspirate = 10
    #p20s.flow_rate.dispense = 15
    #p20s.flow_rate.blow_out = 50

    p300s.flow_rate.aspirate = 10
    p300s.flow_rate.dispense = 15
    p300s.flow_rate.blow_out = 50

    # Setting the temperature module to 4 degrees and in position 4 on the deck
    tempdeck = protocol.load_module('tempdeck', '4')
    tempdeck.set_temperature(4)

    #this needs to be on the temp deck
    reagent_rack = tempdeck.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap')

    # qPCR plate - output
    qPCR_plate = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '2')

    onestep_buffer = reagent_rack.well('A1')
    onestep_enzyme = reagent_rack.well('A2')
    primer_probe = reagent_rack.well('A3')
    master_mix = reagent_rack.well('A4')

    reagents = [onestep_buffer, onestep_enzyme, primer_probe]
    vols = [1000, 200, 300]

    ### Amounts of reagent per 20 µl reaction
    # buffer - 10 µl
    # enzyme mix - 2 µl
    # primer probe - 3 µl
    # template - 5 µl
    # 
    # Total vol for 96 well plate (not inc template) is 1.5 mL - could use a 2mL eppendorf

    # Transfer enough for 100x to master mix tube

    for v, reag in enumerate(reagents):
        p300s.pick_up_tip()
        # Mixing step
        for _ in range(2):
            p300s.aspirate(200, reag)
            p300s.dispense(200, reag)

        p300s.transfer(vols[v], reag, master_mix, new_tip='never')

        # mix the mastermix on the final pass
        if v == 2:
            for _ in range(4):
                p300s.aspirate(200, master_mix)
                p300s.dispense(200, master_mix)   
        
        p300s.drop_tip()

    # Dispense the master mix (15 µL) to each 96 well in the qPCR plate
    # This will take a long time. Could be modified to fx place 15µl * 8 in column 1, and then use multichannel to transfer to the rest
    # Would probably need to transfer to column 1 of a different plate, otherwise there could be inconsistent vols
    '''    p20s.pick_up_tip()
    for well in qPCR_plate.wells():
        p20s.distribute(15, master_mix, well, new_tip='never')
    p20s.drop_tip()'''
    p300s.distribute(15, master_mix, qPCR_plate.wells(), mix_before=(2,200))


