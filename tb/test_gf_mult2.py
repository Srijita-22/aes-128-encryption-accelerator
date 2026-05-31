import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_gf_mult2(dut):

    dut.data_in.value = 0x57

    await Timer(1, unit="ns")

    result = int(dut.data_out.value)

    assert result == 0xAE, \
        f"Expected 0xAE, Got {result:#x}"
