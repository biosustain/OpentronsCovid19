metadata = {
    'protocolName': 'BP Genomics Station A',
    'author': 'Chaz <chaz@opentrons.com',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.2'
}


def run(protocol):
    tips200 = [protocol.load_labware('opentrons_96_tiprack_300ul', '9')]
    tips20 = [protocol.load_labware('opentrons_96_filtertiprack_20ul', '8')]
    p300 = protocol.load_instrument(
        'p300_single_gen2', 'left', tip_racks=tips200)
    p20 = protocol.load_instrument(
        'p20_single_gen2', 'right', tip_racks=tips20)
    plate = protocol.load_labware('nest_96_deepwell_2ml', '1')
    
    #Select number of wells to run. 
    
    platewells = plate.wells()[:24]
    spikewells = plate.wells()[:24]
    #Don't know what this spikewells pop does. 
    spikewells.pop(6)
    samplerack = protocol.load_labware('bpg_24_tuberack_2ml', '5')
    
    #Sample plate and sample selection
    samps = samplerack.wells()[:24]
    
    
    tempdeck = protocol.load_module('tempdeck', '7')
    temprack = tempdeck.load_labware(
        'opentrons_96_aluminumblock_generic_pcr_strip_200ul')
    tempdeck.set_temperature(4)
    reagentrack = protocol.load_labware(
        'opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap',
        '4', 'Opentrons 24 TubeRack with Reagents')

    pk = reagentrack['D2']
    lysis_wells = [reagentrack['C1'], reagentrack['D1']]
    spike = temprack['H1']

    p20.flow_rate.aspirate = 10
    p20.flow_rate.dispense = 20
    p20.flow_rate.blow_out = 100
    p300.flow_rate.aspirate = 150
    p300.flow_rate.dispense = 300
    p300.flow_rate.blow_out = 300

    p20.pick_up_tip()
    for well in platewells:
        p20.transfer(20, pk, well, new_tip='never')
        p20.blow_out(well.top(-6))
    p20.drop_tip()

#Code to transfer sample to 96 well deep plate
    for src, dest in zip(samps, platewells):
        p300.pick_up_tip()
        p300.transfer(150, src.bottom(9), dest.top(-6), new_tip='never')
        p300.blow_out(dest.top(-6))
        p300.transfer(150, src.bottom(9), dest, new_tip='never')
        p300.blow_out(dest.top(-6))
        p300.drop_tip()

#Code to transfer last bit at the bottom of the sample wells
    for src, dest in zip(samps, platewells):
        p20.pick_up_tip()
        for _ in range(5):
            p20.transfer(20, src.bottom(1.5), dest.top(-6), new_tip='never')
            p20.blow_out(dest.top(-6))
        p20.drop_tip()
        
#Add lysis buffer to deep well plate
    for idx, well in enumerate(platewells):
        lysis = lysis_wells[0] if idx < 4 else lysis_wells[1]
        p300.pick_up_tip()
        p300.flow_rate.aspirate = 50
        p300.flow_rate.dispense = 150
        for _ in range(2):
            p300.transfer(150, lysis, well.top(-2), new_tip='never')
        p300.flow_rate.aspirate = 150
        p300.flow_rate.dispense = 300
        p300.aspirate(200, well)
        for _ in range(10):
            p300.dispense(180, well)
            p300.aspirate(180, well)
        p300.dispense(200, well)
        p300.drop_tip()
        
#Incubation with lysis buffer
    protocol.delay(minutes=25)
    
#Add cold reagent from spike
    for well in spikewells:
        p20.pick_up_tip()
        p20.transfer(4, spike, well, new_tip='never')
        p20.drop_tip()
