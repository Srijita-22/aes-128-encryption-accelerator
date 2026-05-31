import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mixcolumns(dut):

    # AES standard example
    dut.col_in.value = 0xdb135345

    await Timer(1, unit="ns")

    result = int(dut.col_out.value)

    assert result == 0x8e4da1bc, \
        f"Expected 0x8e4da1bc, got {result:#x}"
