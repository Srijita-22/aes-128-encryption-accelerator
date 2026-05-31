import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_rcon(dut):

    expected = {
        1: 0x01,
        2: 0x02,
        3: 0x04,
        4: 0x08,
        5: 0x10,
        6: 0x20,
        7: 0x40,
        8: 0x80,
        9: 0x1B,
        10: 0x36
    }

    for rnd, value in expected.items():
        dut.round.value = rnd

        await Timer(1, unit="ns")

        assert int(dut.rcon_out.value) == value
