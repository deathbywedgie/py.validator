import unittest

from pyvalidator import *


class TestIsPassportNumber(unittest.TestCase):

    def test_valid_passport_number(self):
        self.assertTrue(is_passport_number('AF0549358', "AM"))
        self.assertTrue(is_passport_number('C1253473', "ID"))
        self.assertTrue(is_passport_number('B5948378', "ID"))
        self.assertTrue(is_passport_number('A4859472', "ID"))
        self.assertTrue(is_passport_number('AAC811035', "AR"))
        self.assertTrue(is_passport_number('P 1630837', "AT"))
        self.assertTrue(is_passport_number('P 4366918', "AT"))
        self.assertTrue(is_passport_number('N0995852', "AU"))
        self.assertTrue(is_passport_number('L4819236', "AU"))
        self.assertTrue(is_passport_number('A1234567', "BA"))
        self.assertTrue(is_passport_number('346395366', "BG"))
        self.assertTrue(is_passport_number('039903356', "BG"))
        self.assertTrue(is_passport_number('FZ973689', "BR"))
        self.assertTrue(is_passport_number('GH231233', "BR"))
        self.assertTrue(is_passport_number('MP3899901', "BY"))
        self.assertTrue(is_passport_number('GA302922', "CA"))
        self.assertTrue(is_passport_number('S1100409', "CH"))
        self.assertTrue(is_passport_number('X4028791', "CH"))
        self.assertTrue(is_passport_number('E00160027', "CN"))
        self.assertTrue(is_passport_number('EA1234567', "CN"))
        self.assertTrue(is_passport_number('K00000413', "CY"))
        self.assertTrue(is_passport_number('99003853', "CZ"))
        self.assertTrue(is_passport_number('42747260', "CZ"))
        self.assertTrue(is_passport_number('C01X00T47', "DE"))
        self.assertTrue(is_passport_number('900010172', "DK"))
        self.assertTrue(is_passport_number('855609385', "DZ"))
        self.assertTrue(is_passport_number('K4218285', "EE"))
        self.assertTrue(is_passport_number('KB0167630', "EE"))
        self.assertTrue(is_passport_number('AF238143', "ES"))
        self.assertTrue(is_passport_number('XP8271602', "FI"))
        self.assertTrue(is_passport_number('XD8500003', "FI"))
        self.assertTrue(is_passport_number('10CV28144', "FR"))
        self.assertTrue(is_passport_number('05RP34083', "FR"))
        self.assertTrue(is_passport_number('925076473', "GB"))
        self.assertTrue(is_passport_number('107182890', "GB"))
        self.assertTrue(is_passport_number('104121156', "GB"))
        self.assertTrue(is_passport_number('AE0000005', "GR"))
        self.assertTrue(is_passport_number('AK0219304', "GR"))
        self.assertTrue(is_passport_number('007007007', "HR"))
        self.assertTrue(is_passport_number('ZA084505', "HU"))
        self.assertTrue(is_passport_number('D23145890', "IE"))
        self.assertTrue(is_passport_number('X65097105', "IE"))
        self.assertTrue(is_passport_number('X0019390', "IN"))
        self.assertTrue(is_passport_number('A-1234567', "IN"))
        self.assertTrue(is_passport_number('J97634522', "IR"))
        self.assertTrue(is_passport_number('A01234567', "IR"))
        self.assertTrue(is_passport_number('A1197783', "IS"))
        self.assertTrue(is_passport_number('A2040611', "IS"))
        self.assertTrue(is_passport_number('YA8335453', "IT"))
        self.assertTrue(is_passport_number('KK0000000', "IT"))
        self.assertTrue(is_passport_number('NH1106002', "JP"))
        self.assertTrue(is_passport_number('TE3180251', "JP"))
        self.assertTrue(is_passport_number('XS1234567', "JP"))
        self.assertTrue(is_passport_number('M35772699', "KR"))
        self.assertTrue(is_passport_number('20200997', "LT"))
        self.assertTrue(is_passport_number('LB311756', "LT"))
        self.assertTrue(is_passport_number('JCU9J4T2', "LU"))
        self.assertTrue(is_passport_number('LV9000339', "LV"))
        self.assertTrue(is_passport_number('LV4017173', "LV"))
        self.assertTrue(is_passport_number('RJ45H4V2', "LY"))
        self.assertTrue(is_passport_number('1026564', "MT"))
        self.assertTrue(is_passport_number('AB0808212', "MZ"))
        self.assertTrue(is_passport_number('08AB12123', "MZ"))
        self.assertTrue(is_passport_number('A00000000', "MY"))
        self.assertTrue(is_passport_number('H12345678', "MY"))
        self.assertTrue(is_passport_number('XTR110131', "NL"))
        self.assertTrue(is_passport_number('XR1001R58', "NL"))
        self.assertTrue(is_passport_number('ZS 0000177', "PL"))
        self.assertTrue(is_passport_number('AN 3000011', "PL"))
        self.assertTrue(is_passport_number('I700044', "PT"))
        self.assertTrue(is_passport_number('K453286', "PT"))
        self.assertTrue(is_passport_number('05485968', "RO"))
        self.assertTrue(is_passport_number('040005646', "RO"))
        self.assertTrue(is_passport_number('014213789', "RS"))
        self.assertTrue(is_passport_number('2 32 636829', "RU"))
        self.assertTrue(is_passport_number('012 345321', "RU"))
        self.assertTrue(is_passport_number('59000001', "SE"))
        self.assertTrue(is_passport_number('PB0036440', "SL"))
        self.assertTrue(is_passport_number('P0000000', "SK"))
        self.assertTrue(is_passport_number('U 06764100', "TR"))
        self.assertTrue(is_passport_number('EH345655', "UA"))
        self.assertTrue(is_passport_number('AP841503', "UA"))
        self.assertTrue(is_passport_number('790369937', "US"))
        self.assertTrue(is_passport_number('340007237', "US"))
        print('OK - test_valid_passport_number')

    def test_invalid_passport_number(self):
        self.assertFalse(is_passport_number('A1054935', "AM"))
        self.assertFalse(is_passport_number('D39481728', "ID"))
        self.assertFalse(is_passport_number('A-3847362', "ID"))
        self.assertFalse(is_passport_number('324132132', "ID"))
        self.assertFalse(is_passport_number('A11811035', "AR"))
        self.assertFalse(is_passport_number('0 1630837', "AT"))
        self.assertFalse(is_passport_number('1A012345', "AU"))
        self.assertFalse(is_passport_number('ABC123456', "BA"))
        self.assertFalse(is_passport_number('ABC123456', "BG"))
        self.assertFalse(is_passport_number('ABX29332', "BR"))
        self.assertFalse(is_passport_number('345333454', "BY"))
        self.assertFalse(is_passport_number('FG53334542', "BY"))
        self.assertFalse(is_passport_number('AB0123456', "CA"))
        self.assertFalse(is_passport_number('AB123456', "CH"))
        self.assertFalse(is_passport_number('E-1234567', "CN"))
        self.assertFalse(is_passport_number('GO1234567', "CN"))
        self.assertFalse(is_passport_number('K10100', "CY"))
        self.assertFalse(is_passport_number('012345678', "CZ"))
        self.assertFalse(is_passport_number('AB123456', "CZ"))
        self.assertFalse(is_passport_number('A012345678', "DE"))
        self.assertFalse(is_passport_number('AS0123456', "DZ"))
        self.assertFalse(is_passport_number('K01234567', "EE"))
        self.assertFalse(is_passport_number('AF01234567', "ES"))
        self.assertFalse(is_passport_number('ABC012345', "FI"))
        self.assertFalse(is_passport_number('A01234567', "FI"))
        self.assertFalse(is_passport_number('012345678', "FR"))
        self.assertFalse(is_passport_number('AB0123456', "FR"))
        self.assertFalse(is_passport_number('A012345678', "GB"))
        self.assertFalse(is_passport_number('K000000000', "GB"))
        self.assertFalse(is_passport_number('A01234567', "GR"))
        self.assertFalse(is_passport_number('A01234567', "HR"))
        self.assertFalse(is_passport_number('A01234567', "HU"))
        self.assertFalse(is_passport_number('012345678', "HU"))
        self.assertFalse(is_passport_number('XND012345', "IE"))
        self.assertFalse(is_passport_number('AB-1234567', "IN"))
        self.assertFalse(is_passport_number('0123456789', "IN"))
        self.assertFalse(is_passport_number('0123456789', "IN"))
        self.assertFalse(is_passport_number('A0123456', "IR"))
        self.assertFalse(is_passport_number('A0123456Z', "IR"))
        self.assertFalse(is_passport_number('K0000000', "IS"))
        self.assertFalse(is_passport_number('01234567', "IS"))
        self.assertFalse(is_passport_number('01234567', "IT"))
        self.assertFalse(is_passport_number('X12345678', "JP"))
        self.assertFalse(is_passport_number('012345678', "JP"))
        self.assertFalse(is_passport_number('X12345678', "KR"))
        self.assertFalse(is_passport_number('LB01234567', "LT"))
        self.assertFalse(is_passport_number('JCU9J4T', "LU"))
        self.assertFalse(is_passport_number('LV01234567', "LV"))
        self.assertFalse(is_passport_number('4017173LV', "LV"))
        self.assertFalse(is_passport_number('P79JF34', "LY"))
        self.assertFalse(is_passport_number('MT01234', "MT"))
        self.assertFalse(is_passport_number('1AB011241', "MZ"))
        self.assertFalse(is_passport_number('ABAB01121', "MZ"))
        self.assertFalse(is_passport_number('A1234567', "MY"))
        self.assertFalse(is_passport_number('C01234567', "MY"))
        self.assertFalse(is_passport_number('XTR11013R', "NL"))
        self.assertFalse(is_passport_number('A1 0000177', "PL"))
        self.assertFalse(is_passport_number('K4532861', "PT"))
        self.assertFalse(is_passport_number('0511060461', "RO"))
        self.assertFalse(is_passport_number('R05485968', "RO"))
        self.assertFalse(is_passport_number('01A 3D5321', "RS"))
        self.assertFalse(is_passport_number('01A 3D5321', "RU"))
        self.assertFalse(is_passport_number('A 2R YU46J0', "RU"))
        self.assertFalse(is_passport_number('SE012345', "SE"))
        self.assertFalse(is_passport_number('SL0123456', "SL"))
        self.assertFalse(is_passport_number('SK012345', "SK"))
        self.assertFalse(is_passport_number('06764100U', "TR"))
        self.assertFalse(is_passport_number('01234567', "UA"))
        self.assertFalse(is_passport_number('012345EH', "UA"))
        self.assertFalse(is_passport_number('A012345P', "UA"))
        self.assertFalse(is_passport_number('US0123456', "US"))
        self.assertFalse(is_passport_number('US0123456', "US"))
        self.assertFalse(is_passport_number('7903699371', "US"))
        print('OK - test_invalid_passport_number')
