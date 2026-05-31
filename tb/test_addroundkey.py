import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_addroundkey(dut):

    dut.state_in.value = int(
        "00112233445566778899aabbccddeeff", 16
    )

    dut.round_key.value = int(
        "000102030405060708090a0b0c0d0e0f", 16
    )

    await Timer(1, unit="ns")

    expected = int(
        "00102030405060708090a0b0c0d0e0f0", 16
    )

    result = int(dut.state_out.value)

    assert result == expected, \
        f"Expected {expected:032x}, Got {result:032x}"
