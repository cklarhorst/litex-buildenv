from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

_io = [
    # clock
    ("clk50", 0, Pins("J19"), IOStandard("LVCMOS33")),

    # leds
    ("user_led", 0, Pins("M21"), IOStandard("LVCMOS33")),
    ("user_led", 1, Pins("N20"), IOStandard("LVCMOS33")),
    ("user_led", 2, Pins("L21"), IOStandard("LVCMOS33")),
    ("user_led", 3, Pins("AA21"), IOStandard("LVCMOS33")),
    ("user_led", 4, Pins("R19"), IOStandard("LVCMOS33")),
    ("user_led", 5, Pins("M16"), IOStandard("LVCMOS33")),

    # flash
    ("flash", 0,
        Subsignal("cs_n", Pins("T19")),
        Subsignal("mosi", Pins("P22")),
        Subsignal("miso", Pins("R22")),
        Subsignal("vpp", Pins("P21")),
        Subsignal("hold", Pins("R21")),
        IOStandard("LVCMOS33")
    ),

    # serial
    ("serial", 0,
        Subsignal("tx", Pins("E14")),
        Subsignal("rx", Pins("E13")),
        IOStandard("LVCMOS33"),
    ),

    # dram
    ("ddram", 0,
        Subsignal("a", Pins(
            "U6 V4 W5 V5 AA1 Y2 AB1 AB3",
            "AB2 Y3 W6 Y1 V2 AA3"),
            IOStandard("SSTL15_R")),
        Subsignal("ba", Pins("U5 W4 V7"), IOStandard("SSTL15_R")),
        Subsignal("ras_n", Pins("Y9"), IOStandard("SSTL15_R")),
        Subsignal("cas_n", Pins("Y7"), IOStandard("SSTL15_R")),
        Subsignal("we_n", Pins("V8"), IOStandard("SSTL15_R")),
        Subsignal("dm", Pins("G1 H4 M5 L3"), IOStandard("SSTL15_R")),
        Subsignal("dq", Pins(
            "C2 F1 B1 F3 A1 D2 B2 E2",
            "J5 H3 K1 H2 J1 G2 H5 G3",
            "N2 M6 P1 N5 P2 N4 R1 P6",
            "K3 M2 K4 M3 J6 L5 J4 K6"),
            IOStandard("SSTL15_R"),
            Misc("IN_TERM=UNTUNED_SPLIT_40")),
        Subsignal("dqs_p", Pins("E1 K2 P5 M1"), IOStandard("DIFF_SSTL15_R")),
        Subsignal("dqs_n", Pins("D1 J2 P4 L1"), IOStandard("DIFF_SSTL15_R")),
        Subsignal("clk_p", Pins("R3"), IOStandard("DIFF_SSTL15_R")),
        Subsignal("clk_n", Pins("R2"), IOStandard("DIFF_SSTL15_R")),
        Subsignal("cke", Pins("Y8"), IOStandard("SSTL15_R")),
        Subsignal("odt", Pins("W9"), IOStandard("SSTL15_R")),
        Subsignal("reset_n", Pins("AB5"), IOStandard("LVCMOS15")),
        Subsignal("cs_n", Pins("V9"), IOStandard("SSTL15_R")),
        Misc("SLEW=FAST"),
    ),

    # pcie
    ("pcie_x1", 0,
        Subsignal("rst_n", Pins("E18"), IOStandard("LVCMOS33")),
        Subsignal("clk_p", Pins("F10")),
        Subsignal("clk_n", Pins("E10")),
        Subsignal("rx_p", Pins("D11")),
        Subsignal("rx_n", Pins("C11")),
        Subsignal("tx_p", Pins("D5")),
        Subsignal("tx_n", Pins("C5"))
    ),

    ("pcie_x2", 0,
        Subsignal("rst_n", Pins("E18"), IOStandard("LVCMOS33")),
        Subsignal("clk_p", Pins("F10")),
        Subsignal("clk_n", Pins("E10")),
        Subsignal("rx_p", Pins("D11 B10")),
        Subsignal("rx_n", Pins("C11 A10")),
        Subsignal("tx_p", Pins("D5 B6")),
        Subsignal("tx_n", Pins("C5 A6"))
    ),

    ("pcie_x4", 0,
        Subsignal("rst_n", Pins("E18"), IOStandard("LVCMOS33")),
        Subsignal("clk_p", Pins("F10")),
        Subsignal("clk_n", Pins("E10")),
        Subsignal("rx_p", Pins("D11 B10 D9 B8")),
        Subsignal("rx_n", Pins("C11 A10 C9 A8")),
        Subsignal("tx_p", Pins("D5 B6 D7 B4")),
        Subsignal("tx_n", Pins("C5 A6 C7 A4"))
    ),

    # ethernet
    ("eth_clocks", 0,
        Subsignal("ref_clk", Pins("D17")),
        IOStandard("LVCMOS33"),
    ),

    ("eth", 0,
        Subsignal("rst_n", Pins("F16")),
        Subsignal("rx_data", Pins("A20 B18")),
        Subsignal("crs_dv", Pins("C20")),
        Subsignal("tx_en", Pins("A19")),
        Subsignal("tx_data", Pins("C18 C19")),
        Subsignal("mdc", Pins("F14")),
        Subsignal("mdio", Pins("F13")),
        Subsignal("rx_er", Pins("B20")),
        Subsignal("int_n", Pins("D21")),
        IOStandard("LVCMOS33")
     ),

     # sdcard
     ("sdcard", 0,
        Subsignal("data", Pins("L15 L16 K14 M13"), Misc("PULLUP True")),
        Subsignal("cmd", Pins("L13"), Misc("PULLUP True")),
        Subsignal("clk", Pins("K18")),
        IOStandard("LVCMOS33"), Misc("SLEW=FAST")
    ),

    # hdmi in
    ("hdmi_in", 0,
        Subsignal("clk_p", Pins("L19"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("clk_n", Pins("L20"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data0_p", Pins("K21"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data0_n", Pins("K22"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data1_p", Pins("J20"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data1_n", Pins("J21"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data2_p", Pins("J22"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data2_n", Pins("H22"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("scl", Pins("T18"), IOStandard("LVCMOS33")),
        Subsignal("sda", Pins("V18"), IOStandard("LVCMOS33")),
    ),

    ("hdmi_in", 1,
        Subsignal("clk_p", Pins("Y18"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("clk_n", Pins("Y19"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data0_p", Pins("AA18"), IOStandard("TMDS_33")),
        Subsignal("data0_n", Pins("AB18"), IOStandard("TMDS_33")),
        Subsignal("data1_p", Pins("AA19"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data1_n", Pins("AB20"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data2_p", Pins("AB21"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data2_n", Pins("AB22"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("scl", Pins("W17"), IOStandard("LVCMOS33"), Inverted()),
        Subsignal("sda", Pins("R17"), IOStandard("LVCMOS33")),
    ),

    # hdmi out
    ("hdmi_out", 0,
        Subsignal("clk_p", Pins("W19"), Inverted(), IOStandard("TMDS_33")),
        Subsignal("clk_n", Pins("W20"), Inverted(), IOStandard("TMDS_33")),
        Subsignal("data0_p", Pins("W21"), IOStandard("TMDS_33")),
        Subsignal("data0_n", Pins("W22"), IOStandard("TMDS_33")),
        Subsignal("data1_p", Pins("U20"), IOStandard("TMDS_33")),
        Subsignal("data1_n", Pins("V20"), IOStandard("TMDS_33")),
        Subsignal("data2_p", Pins("T21"), IOStandard("TMDS_33")),
        Subsignal("data2_n", Pins("U21"), IOStandard("TMDS_33"))
    ),

    ("hdmi_out", 1,
        Subsignal("clk_p", Pins("G21"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("clk_n", Pins("G22"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data0_p", Pins("E22"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data0_n", Pins("D22"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data1_p", Pins("C22"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data1_n", Pins("B22"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data2_p", Pins("B21"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("data2_n", Pins("A21"), IOStandard("TMDS_33"), Inverted()),
        Subsignal("scl", Pins("P16"), IOStandard("LVCMOS33")),
        Subsignal("sda", Pins("R16"), IOStandard("LVCMOS33")),
    ),
]

_hdmi_infos = {
    "HDMI_OUT0_MNEMONIC": "TX1",
    "HDMI_OUT0_DESCRIPTION" : (
      "HDMI-A connector (marked TX0/J10H on PCB) located in the mounting bracket area, connector is the one closer to the DC Jack\\r\\n"
    ),

    "HDMI_OUT1_MNEMONIC": "TX2",
    "HDMI_OUT1_DESCRIPTION" : (
      "HDMI-D connector (marked TX1/P10H on PCB) located on the top edge of the board, connector is the one closer to the DC Jack\\r\\n"
    ),

    "HDMI_IN0_MNEMONIC": "RX1",
    "HDMI_IN0_DESCRIPTION" : (
      "HDMI-A connector (marked RX0/J11H on PCB) located in the mounting bracket area, connector is the one farther from the DC Jack\\r\\n"
    ),

    "HDMI_IN1_MNEMONIC": "RX2",
    "HDMI_IN1_DESCRIPTION" : (
      "HDMI-A connector (marked OVERLAY/J12H on PCB) located on the top edge of the board, connector is the one farther from the DC Jack\\r\\n"
    ),
}

class Platform(XilinxPlatform):
    name = "netv2"
    default_clk_name = "clk50"
    default_clk_period = 20.0
    hdmi_infos = _hdmi_infos

    # From https://www.xilinx.com/support/documentation/user_guides/ug470_7Series_Config.pdf
    gateware_size = 0x400000

    # FIXME: Create a "spi flash module" object in the same way we have SDRAM
    # module objects.
    spiflash_model = "mx25l6433f"
    spiflash_read_dummy_bits = 10
    spiflash_clock_div = 2
    spiflash_total_size = int((64/8)*1024*1024) # 64Mbit
    spiflash_page_size = 256
    spiflash_sector_size = 0x1000

    def __init__(self, toolchain="vivado", programmer="vivado", part="xc7a35t"):
        XilinxPlatform.__init__(self, part + "-fgg484-2", _io,
                                toolchain=toolchain)

        self.toolchain.bitstream_commands = [
            "set_property CONFIG_VOLTAGE 3.3 [current_design]",
            "set_property CFGBVS VCCO [current_design]",
            "set_property BITSTREAM.CONFIG.CONFIGRATE 40 [current_design]",
            "set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]",
        ]
        self.toolchain.additional_commands = \
            ["write_cfgmem -verbose -force -format bin -interface spix4 -size 16 "
             "-loadbit \"up 0x0 {build_name}.bit\" -file {build_name}.bin"]

        self.programmer = programmer

    def create_programmer(self):
        if self.programmer == "vivado":
            return VivadoProgrammer(flash_part="mx25l6433f-spi-x1_x2_x4")
        else:
            raise ValueError("{} programmer is not supported"
                             .format(self.programmer))
