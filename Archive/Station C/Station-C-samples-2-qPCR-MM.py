metadata = {
    'protocolName': 'Station C - Samples to qPCR',
    'author': 'Mathew Jessop Fabre <mmjf@dtu.dk>',
    'source': 'COVID-19 Project - DTU',
    'apiLevel': '2.2'
}

### Protocol to transfer the purified RNA samples to the qPCR mastermix plate
# Based on the DiaPlex Q Novel Coronavirus Detection Kit protocol

def run(protocol):

    # tip racks - how many will be needed?
    tip_racks_10m = [protocol.load_labware('opentrons_96_filtertiprack_20ul', '1')]

    # tip racks - how many will be needed?
    tip_racks_20s = [protocol.load_labware('opentrons_96_filtertiprack_20ul', '2')]

    # Pipette - p10 multi
    p10m = protocol.load_instrument('p10_multi', 'left', tip_racks=tip_racks_10m)

    # Pipette - p20 single
    p20s = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=tip_racks_20s)

    p10m.flow_rate.aspirate = 10
    p10m.flow_rate.dispense = 15
    p10m.flow_rate.blow_out = 50

    p20s.flow_rate.aspirate = 10
    p20s.flow_rate.dispense = 15
    p20s.flow_rate.blow_out = 50

    # Setting the temperature module to 4 degrees and in position 4 on the deck
    tempdeck = protocol.load_module('tempdeck', '3')
    tempdeck.set_temperature(4)

    #this needs to be on the temp deck
    reagent_rack = tempdeck.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', '4')

    # qPCR plate with master mix loaded (15 µl)
    qPCR_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '5')

    sample_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '6')

    COV19_RNA = reagent_rack.well('A1') #Positive control
    N_control = reagent_rack.well('A2') #Negative control sample
    NTC = reagent_rack.well('A3') #Non-template control - RNAase free water

    # Need to find out how many and what controls we have
    controls = [COV19_RNA, N_control, NTC, COV19_RNA, N_control, NTC]

    # add the controls to the first 3 wells (A1, B1, C1) of the qPCR plate
    for well, control in enumerate(controls):
        p20s.pick_up_tip()
        for _ in range(2):
            p20s.aspirate(10, control)
            p20s.dispense(10, control)
        p20s.transfer(5, control, qPCR_plate.wells(well), new_tip='never')
        p20s.drop_tip()

    #transfer the samples into the remaining 90 wells - column wise using the multichannel
    for col in range(12):
        p10m.pick_up_tip()

        #mix the Purified RNA samples before transfer
        for _ in range(2):
            p10m.aspirate(10, sample_plate.wells()[col*8])
            p10m.dispense(10, sample_plate.wells()[col*8])

        p10m.transfer(5, sample_plate.wells()[col*8], qPCR_plate.wells()[col*8], new_tip='never')

        p10m.drop_tip()
