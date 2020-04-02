metadata = {
    'protocolName': 'Station C - Consolidated',
    'author': 'Mathew Jessop Fabre <mmjf@dtu.dk>',
    'source': 'COVID-19 Project - DTU',
    'apiLevel': '2.2'
}

### Protocol to set up a 96 qPCR plate filled with reaction master mix
# and then add the RNA samples to the mastermix
# Based on the DiaPlex Q Novel Coronavirus Detection Kit protocol

def run(protocol):

    # tip racks - how many will be needed?
    tip_racks_20 = [protocol.load_labware('opentrons_96_filtertiprack_20ul', '1')]
            
    tip_racks_200 = [protocol.load_labware('opentrons_96_filtertiprack_200ul', '2')]

    # Pipette - p20 single
    p10m = protocol.load_instrument('p10_multi', 'right', tip_racks=tip_racks_20)
    p300s = protocol.load_instrument('p300_single', 'left', tip_racks=tip_racks_200)

    p10m.flow_rate.aspirate = 10
    p10m.flow_rate.dispense = 15
    p10m.flow_rate.blow_out = 50

    p300s.flow_rate.aspirate = 10
    p300s.flow_rate.dispense = 15
    p300s.flow_rate.blow_out = 50

    # Setting the temperature module to 4 degrees and in position 4 on the deck
    tempdeck = protocol.load_module('tempdeck', '4')
    tempdeck.set_temperature(4)

    #this needs to be on the temp deck
    reagent_rack = tempdeck.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap')

    # qPCR plate - output
    qPCR_plate = protocol.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', '3')

    onestep_buffer = reagent_rack.well('A1')
    onestep_enzyme = reagent_rack.well('A2')
    primer_probe = reagent_rack.well('A3')
    master_mix = reagent_rack.well('A4')
    COV19_RNA = reagent_rack.well('B1') #Positive control
    N_control = reagent_rack.well('B2') #Negative control sample
    NTC = reagent_rack.well('B3') #Non-template control - RNAase free water

    # Need to find out how many and what controls we have
    controls = [COV19_RNA, N_control, NTC, COV19_RNA, N_control, NTC]

    sample_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '5')

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

    p300s.distribute(15, master_mix, qPCR_plate.wells(), mix_before=(2,200))

    # add the controls to the first 3 wells (A1, B1, C1) of the qPCR plate
    for well, control in enumerate(controls):
        p300s.pick_up_tip()
        for _ in range(2):
            p300s.aspirate(30, control)
            p300s.dispense(30, control)
        p300s.transfer(5, control, qPCR_plate.wells(well), new_tip='never')
        p300s.drop_tip()

    #transfer the samples into the remaining 90 wells - column wise using the multichannel
    for col in range(12):
        p10m.pick_up_tip()

        #mix the Purified RNA samples before transfer
        for _ in range(2):
            p10m.aspirate(10, sample_plate.wells()[col*8])
            p10m.dispense(10, sample_plate.wells()[col*8])

        p10m.transfer(5, sample_plate.wells()[col*8], qPCR_plate.wells()[col*8], new_tip='never')

        p10m.drop_tip()


