class Table_converter:
    def __init__(self):
        self.dest_table = {
            'null': '000',
            'M':    '001',
            'D':    '010',
            'MD':   '011',
            'A':    '100',
            'AM':   '101',
            'AD':   '110',
            'AMD':  '111'
        }

        """
            000     null    The value is not stored anywhere
            001     M       Memory[A] (memory register addressed by A)
            010     D       D register
            011     MD      Memory[A] and D register
            100     A       A register
            101     AM      A register and Memory[A]
            110     AD      A register and D register
            111     AMD
        """







        """
        0       101010
        1       111111
        -1      111010
        D       001100
        A       110000      M
        !D      001101
        !A      110001      !M
        -D      001111
        -A      110011      -M
        D+1     011111
        A+1     110111      M+1
        D-1     001110
        A-1     110010      M-1
        D+A     000010      D+M
        D-A     010011      D-M
        A-D     000111      M-D
        D&A     000000      D&M
        D|A     010101      D|M
        """

        self.a_comp_instructions = ['M', '!M', '-M', 'M+1', 'M-1', 'D+M', 'D-M', 'M-D', 'D&M', 'D|M']

        self.comp_table = {
            '0'    :   '101010',
            '1'    :   '111111',
            '-1'   :   '111010',
            'D'    :   '001100',
            'A'    :   '110000',
            '!D'   :   '001101',
            '!A'   :   '110001',
            '-D'   :   '001111',
            '-A'   :   '110011',
            'D+1'  :   '011111',
            'A+1'  :   '110111',
            'D-1'  :   '001110',
            'A-1'  :   '110010',
            'D+A'  :   '000010',
            'D-A'  :   '010011',
            'A-D'  :   '000111',
            'D&A'  :   '000000',
            'D|A'  :   '010101',
            'M'    :   '110000',
            '!M'   :   '110001',
            '-M'   :   '110011',
            'M+1'  :   '110111',
            'M-1'  :   '110010',
            'D+M'  :   '000010',
            'D-M'  :   '010011',
            'M-D'  :   '000111',
            'D&M'  :   '000000',
            'D|M'  :   '010101'
        }








        """
        000     null    No jump
        001     JGT     If out > 0 jump
        010     JEQ     If out ¼ 0 jump
        011     JGE     If out b 0 jump
        100     JLT     If out < 0 jump
        101     JNE     If out 0 0 jump
        110     JLE     If out a 0 jump
        111     JMP     Jump
        """

        self.jump_table = {
             'null'   :    '000',
             'JGT'    :    '001',
             'JEQ'    :    '010',
             'JGE'    :    '011',
             'JLT'    :    '100',
             'JNE'    :    '101',
             'JLE'    :    '110',
             'JMP'    :    '111'
        }





    def dest_converter(self, dest):
        dest_machine_code = self.dest_table[dest]
        return dest_machine_code









    def comp_converter(self, comp):
        comp_machine_code = self.comp_table[comp]
        a=0
        if comp in self.a_comp_instructions:
            a=1
        comp_machine_code = str(a) + comp_machine_code
        return comp_machine_code





    def jump_converter(self, jump):
        jump_machine_code = self.jump_table[jump]
        return jump_machine_code
