import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_rotword(dut):

    dut.word_in.value = 0x09cf4f3c

    await Timer(1, unit="ns")

    result = int(dut.word_out.value)

    assert result == 0xcf4f3c09, \
        f"Expected 0xcf4f3c09, got {result:#x}"
