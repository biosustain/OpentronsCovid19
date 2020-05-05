
"""
Created on Mon May 20 09:47:23 2019

Protocol to test p1000 pipette and new tips.  


@author: lajamu
"""

from opentrons import labware, instruments, robot

#Remove robot.reset command for use with machine. 

robot.reset()

metadata = {
    'protocolName': 'Basic Loading',
    'author': 'Lachlan Munro',
    'source': 'Lachlan Munro',
    'apiLevel': '2.2'
    }

def run(protocol):
    
    tiprack1 = protocol.load_labware('opentrons_96_tiprack_1000ul', "1")
    # Load a P50 multi on the left slot
    p1 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack1])
    # Load a P1000 Single on the right slot, with two racks of tips

    rack = protocol.load_labware("nest_aluminium_24", "2")

    for i in range(12):
        p1.pick_up_tip()
        p1.aspirate(300, rack.wells()[0].top(-70))
        p1.dispense(300, rack.wells()[0])
        p1.return_tip()
        


