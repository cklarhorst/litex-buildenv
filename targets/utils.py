#!/usr/bin/env python3

import difflib
import pprint


def round_up_to_4(i):
    return int((i + 3) / 4) * 4


def dict_set_max(d, key, value):
    d[key] = max(d[key], value) if key in d else value


def period_ns(freq):
    return 1e9/freq


def assert_pll_clock(requested_freq, input, feedback, divide, msg):
    output_freq = int(input * feedback / divide / 1e6)
    assert output_freq == int(requested_freq / 1e6), (
        "%s wants %s but got %i MHz (input=%i MHz feedback=%i divide=%i)" % (
            msg, requested_freq, output_freq, int(input/1e6), feedback, divide))


class MHzType(int):
    """
    >>> a = MHzType(1)
    >>> a == int(1e9)
    True
    >>> print(a)
    1 MHz
    >>> b = 5 * MHzType(1)
    >>> b == int(5e9)
    True
    >>> b
    5.000000 * MHz()
    >>> print(b)
    5 MHz
    >>> c = 200 * MHzType(1)
    >>>
    """

    def __new__(cls, x):
        return int.__new__(cls, int(x * 1e6))

    def __str__(self):
        return "%i MHz" % int(self / 1e6)

    def __repr__(self):
        return "%f * MHz()" % float(self / 1e6)

    def __mul__(self, o):
        return MHz.__class__(float(self) * o / 1e6)

    def __rmul__(self, o):
        return MHz.__class__(float(self) * o / 1e6)

    def to_ns(self):
        return 1e9/self


MHz = MHzType(1)


test_build_template = [
    "yosys -q -l {build_name}.rpt {build_name}.ys",
    "nextpnr-ice40 --json {build_name}.json --pcf {build_name}.pcf",
    "icepack {build_name}.txt {build_name}.bin"
]


def _platform_toolchain_cmd_split(template):
    """

    >>> cmds = _platform_toolchain_cmd_split(test_build_template)
    >>> cmds["icepack"]
    (2, ['icepack', '{build_name}.txt', '{build_name}.bin'])
    >>> pprint.pprint(cmds["nextpnr-ice40"])
    (1,
     ['nextpnr-ice40', '--json', '{build_name}.json', '--pcf', '{build_name}.pcf'])
    >>> cmds["yosys"]
    (0, ['yosys', '-q', '-l', '{build_name}.rpt', '{build_name}.ys'])

    """
    cmds = {}
    for i, cmdline in enumerate(template):
        cmdline_parts = cmdline.split()
        cmds[cmdline_parts[0]] = (i, list(cmdline_parts))
    return cmds


def _platform_toolchain_cmd_join(cmds):
    """

    >>> cmds = _platform_toolchain_cmd_split(test_build_template)
    >>> out_template = _platform_toolchain_cmd_join(cmds)
    >>> "\\n".join(difflib.context_diff("\\n".join(test_build_template), "\\n".join(out_template)))
    ''
    >>> pprint.pprint(out_template)
    ['yosys -q -l {build_name}.rpt {build_name}.ys',
     'nextpnr-ice40 --json {build_name}.json --pcf {build_name}.pcf',
     'icepack {build_name}.txt {build_name}.bin']

    """
    template = []
    while len(template) < len(cmds):
        for i, cmdline_parts in cmds.values():
            if i != len(template):
                continue
            template.append(" ".join(cmdline_parts))
            break
        else:
            raise ValueError("{} not found\n{}\n{}\n".format(len(template), template, cmds))
    return template


def _add_switch(cmds, cmdname, argument):
    """

    >>> cmds = _platform_toolchain_cmd_split(test_build_template)
    >>> _add_switch(cmds, 'icepack', '-s')
    >>> out_template = _platform_toolchain_cmd_join(cmds)
    >>> pprint.pprint(out_template)
    ['yosys -q -l {build_name}.rpt {build_name}.ys',
     'nextpnr-ice40 --json {build_name}.json --pcf {build_name}.pcf',
     'icepack -s {build_name}.txt {build_name}.bin']

    """
    assert argument.startswith('-'), argument
    assert cmdname in cmds, (cmdname, cmds)
    cmds[cmdname][-1].insert(1, argument)


def platform_toolchain_extend(platform, cmdname, argument):
    bt = platform.toolchain.build_template
    cmds = _platform_toolchain_cmd_split(bt)
    _add_switch(cmds, cmdname, argument)
    bt.clear()
    bt.extend(_platform_toolchain_cmd_join(cmds))

def define_flash_constants(soc):
    soc.add_constant("FLASH_BOOT_ADDRESS", soc.flash_boot_address)
    if soc.cpu_variant == "linux":
        soc.add_constant("KERNEL_IMAGE_FLASH_OFFSET", 0x00000000)
        soc.add_constant("ROOTFS_IMAGE_FLASH_OFFSET", 0x00500000)
        soc.add_constant("DEVICE_TREE_IMAGE_FLASH_OFFSET", 0x00D00000)
        soc.add_constant("EMULATOR_IMAGE_FLASH_OFFSET", 0x00D80000)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
