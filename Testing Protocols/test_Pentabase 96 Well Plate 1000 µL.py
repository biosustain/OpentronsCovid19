import json
from opentrons import protocol_api, types

CALIBRATION_CROSS_COORDS = {
    '1': {
        'x': 12.13,
        'y': 9.0,
        'z': 0.0
    },
    '3': {
        'x': 380.87,
        'y': 9.0,
        'z': 0.0
    },
    '7': {
        'x': 12.13,
        'y': 258.0,
        'z': 0.0
    }
}
CALIBRATION_CROSS_SLOTS = ['1', '3', '7']
TEST_LABWARE_SLOT = '3'

RATE = 0.25  # % of default speeds
SLOWER_RATE = 0.1

PIPETTE_MOUNT = 'right'
PIPETTE_NAME = 'p300_single'

TIPRACK_SLOT = '5'
TIPRACK_LOADNAME = 'opentrons_96_tiprack_300ul'

LABWARE_DEF_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"pentabase","brandId":["26025X"]},"metadata":{"displayName":"Pentabase 96 Well Plate 1000 µL","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.76,"yDimension":85.47,"zDimension":41.6},"wells":{"A1":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":10.14,"y":76.27,"z":3.71},"B1":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":10.14,"y":67.51,"z":3.71},"C1":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":10.14,"y":58.75,"z":3.71},"D1":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":10.14,"y":49.99,"z":3.71},"E1":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":10.14,"y":41.23,"z":3.71},"F1":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":10.14,"y":32.47,"z":3.71},"G1":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":10.14,"y":23.71,"z":3.71},"H1":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":10.14,"y":14.95,"z":3.71},"A2":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":18.9,"y":76.27,"z":3.71},"B2":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":18.9,"y":67.51,"z":3.71},"C2":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":18.9,"y":58.75,"z":3.71},"D2":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":18.9,"y":49.99,"z":3.71},"E2":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":18.9,"y":41.23,"z":3.71},"F2":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":18.9,"y":32.47,"z":3.71},"G2":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":18.9,"y":23.71,"z":3.71},"H2":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":18.9,"y":14.95,"z":3.71},"A3":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":27.66,"y":76.27,"z":3.71},"B3":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":27.66,"y":67.51,"z":3.71},"C3":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":27.66,"y":58.75,"z":3.71},"D3":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":27.66,"y":49.99,"z":3.71},"E3":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":27.66,"y":41.23,"z":3.71},"F3":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":27.66,"y":32.47,"z":3.71},"G3":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":27.66,"y":23.71,"z":3.71},"H3":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":27.66,"y":14.95,"z":3.71},"A4":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":36.42,"y":76.27,"z":3.71},"B4":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":36.42,"y":67.51,"z":3.71},"C4":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":36.42,"y":58.75,"z":3.71},"D4":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":36.42,"y":49.99,"z":3.71},"E4":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":36.42,"y":41.23,"z":3.71},"F4":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":36.42,"y":32.47,"z":3.71},"G4":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":36.42,"y":23.71,"z":3.71},"H4":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":36.42,"y":14.95,"z":3.71},"A5":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":45.18,"y":76.27,"z":3.71},"B5":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":45.18,"y":67.51,"z":3.71},"C5":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":45.18,"y":58.75,"z":3.71},"D5":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":45.18,"y":49.99,"z":3.71},"E5":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":45.18,"y":41.23,"z":3.71},"F5":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":45.18,"y":32.47,"z":3.71},"G5":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":45.18,"y":23.71,"z":3.71},"H5":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":45.18,"y":14.95,"z":3.71},"A6":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":53.94,"y":76.27,"z":3.71},"B6":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":53.94,"y":67.51,"z":3.71},"C6":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":53.94,"y":58.75,"z":3.71},"D6":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":53.94,"y":49.99,"z":3.71},"E6":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":53.94,"y":41.23,"z":3.71},"F6":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":53.94,"y":32.47,"z":3.71},"G6":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":53.94,"y":23.71,"z":3.71},"H6":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":53.94,"y":14.95,"z":3.71},"A7":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":62.7,"y":76.27,"z":3.71},"B7":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":62.7,"y":67.51,"z":3.71},"C7":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":62.7,"y":58.75,"z":3.71},"D7":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":62.7,"y":49.99,"z":3.71},"E7":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":62.7,"y":41.23,"z":3.71},"F7":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":62.7,"y":32.47,"z":3.71},"G7":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":62.7,"y":23.71,"z":3.71},"H7":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":62.7,"y":14.95,"z":3.71},"A8":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":71.46,"y":76.27,"z":3.71},"B8":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":71.46,"y":67.51,"z":3.71},"C8":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":71.46,"y":58.75,"z":3.71},"D8":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":71.46,"y":49.99,"z":3.71},"E8":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":71.46,"y":41.23,"z":3.71},"F8":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":71.46,"y":32.47,"z":3.71},"G8":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":71.46,"y":23.71,"z":3.71},"H8":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":71.46,"y":14.95,"z":3.71},"A9":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":80.22,"y":76.27,"z":3.71},"B9":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":80.22,"y":67.51,"z":3.71},"C9":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":80.22,"y":58.75,"z":3.71},"D9":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":80.22,"y":49.99,"z":3.71},"E9":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":80.22,"y":41.23,"z":3.71},"F9":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":80.22,"y":32.47,"z":3.71},"G9":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":80.22,"y":23.71,"z":3.71},"H9":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":80.22,"y":14.95,"z":3.71},"A10":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":88.98,"y":76.27,"z":3.71},"B10":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":88.98,"y":67.51,"z":3.71},"C10":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":88.98,"y":58.75,"z":3.71},"D10":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":88.98,"y":49.99,"z":3.71},"E10":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":88.98,"y":41.23,"z":3.71},"F10":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":88.98,"y":32.47,"z":3.71},"G10":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":88.98,"y":23.71,"z":3.71},"H10":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":88.98,"y":14.95,"z":3.71},"A11":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":97.74,"y":76.27,"z":3.71},"B11":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":97.74,"y":67.51,"z":3.71},"C11":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":97.74,"y":58.75,"z":3.71},"D11":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":97.74,"y":49.99,"z":3.71},"E11":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":97.74,"y":41.23,"z":3.71},"F11":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":97.74,"y":32.47,"z":3.71},"G11":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":97.74,"y":23.71,"z":3.71},"H11":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":97.74,"y":14.95,"z":3.71},"A12":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":106.5,"y":76.27,"z":3.71},"B12":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":106.5,"y":67.51,"z":3.71},"C12":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":106.5,"y":58.75,"z":3.71},"D12":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":106.5,"y":49.99,"z":3.71},"E12":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":106.5,"y":41.23,"z":3.71},"F12":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":106.5,"y":32.47,"z":3.71},"G12":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":106.5,"y":23.71,"z":3.71},"H12":{"depth":37.89,"totalLiquidVolume":1000,"shape":"rectangular","xDimension":7.8,"yDimension":7.8,"x":106.5,"y":14.95,"z":3.71}},"groups":[{"metadata":{"displayName":"Pentabase 96 Well Plate 1000 µL","displayCategory":"wellPlate","wellBottomShape":"u"},"brand":{"brand":"pentabase","brandId":["26025X"]},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"rna_ext_plate"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""
LABWARE_DEF = json.loads(LABWARE_DEF_JSON)
LABWARE_LABEL = LABWARE_DEF.get('metadata', {}).get(
    'displayName', 'test labware')

metadata = {'apiLevel': '2.0'}


def uniq(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res

def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware(TIPRACK_LOADNAME, TIPRACK_SLOT)
    pipette = protocol.load_instrument(
        PIPETTE_NAME, PIPETTE_MOUNT, tip_racks=[tiprack])

    test_labware = protocol.load_labware_from_definition(
        LABWARE_DEF,
        TEST_LABWARE_SLOT,
        LABWARE_LABEL,
    )

    num_cols = len(LABWARE_DEF.get('ordering', [[]]))
    num_rows = len(LABWARE_DEF.get('ordering', [[]])[0])
    well_locs = uniq([
        'A1',
        '{}{}'.format(chr(ord('A') + num_rows - 1), str(num_cols))])

    pipette.pick_up_tip()

    def set_speeds(rate):
        protocol.max_speeds.update({
            'X': (600 * rate),
            'Y': (400 * rate),
            'Z': (125 * rate),
            'A': (125 * rate),
        })

        speed_max = max(protocol.max_speeds.values())

        for instr in protocol.loaded_instruments.values():
            instr.default_speed = speed_max

    set_speeds(RATE)

    for slot in CALIBRATION_CROSS_SLOTS:
        coordinate = CALIBRATION_CROSS_COORDS[slot]
        location = types.Location(point=types.Point(**coordinate),
                                  labware=None)
        pipette.move_to(location)
        protocol.pause(
            f"Confirm {PIPETTE_MOUNT} pipette is at slot {slot} calibration cross")

    pipette.home()
    protocol.pause(f"Place your labware in Slot {TEST_LABWARE_SLOT}")

    for well_loc in well_locs:
        well = test_labware.well(well_loc)
        all_4_edges = [
            [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
            [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
            [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
            [well._from_center_cartesian(x=0, y=1, z=1), 'back']
        ]

        set_speeds(RATE)
        pipette.move_to(well.top())
        protocol.pause("Moved to the top of the well")

        for edge_pos, edge_name in all_4_edges:
            set_speeds(SLOWER_RATE)
            edge_location = types.Location(point=edge_pos, labware=None)
            pipette.move_to(edge_location)
            protocol.pause(f'Moved to {edge_name} edge')

        set_speeds(RATE)
        pipette.move_to(well.bottom())
        protocol.pause("Moved to the bottom of the well")

        pipette.blow_out(well)

    set_speeds(1.0)
    pipette.return_tip()
