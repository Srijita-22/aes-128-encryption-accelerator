import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_subbytes_basic(dut):

    test_vectors = {
        0x00: 0x63,
        0x01: 0x7C,
        0x02: 0x77,
        0x03: 0x7B,
        0x04: 0xF2,
    }

    for inp, expected in test_vectors.items():

        dut.data_in.value = inp

        await Timer(1, units="ns")

        result = int(dut.data_out.value)

        assert result == expected, \
            f"Input={inp:#x}, Expected={expected:#x}, Got={result:#x}"
