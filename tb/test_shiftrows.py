import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_shiftrows(dut):

    dut.state_in.value = int(
        "00112233445566778899aabbccddeeff", 16
    )

    await Timer(1, unit="ns")

    result = int(dut.state_out.value)

    dut._log.info(f"ShiftRows Output = {result:032x}")
