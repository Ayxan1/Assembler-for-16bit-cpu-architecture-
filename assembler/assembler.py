from assembler_instruction_convert import Table_converter


machine_code=[]

final_machine_code_line = ''

table_convert = Table_converter()



file_name = input("Please enter file name:")

with open(file_name + ".asm", "r") as f:
    data = f.readlines()
#data=data.rstrip("\n")

for line in data:
    if (line[0]!='/' and line[0]!='\n'):

        if line[0]=='@': # A instruction
            address = ''.join(line)

            if '//' in address:
                final_point_char = '/'
            else:
                final_point_char = '\n'
            final_point = address.index(final_point_char)
            decimal_number = int(address[1:final_point].strip())
            binary_number_frame = "0000000000000000"


            binary_number = bin(decimal_number)[2:]
            starting_point = 16 - len(binary_number)
            final_machine_code = binary_number_frame[0:starting_point] + binary_number
            machine_code.append(final_machine_code)


        else:  # C instruction  dest = comp;jmp
            c_instruction = ''.join(line)
            if "=" in c_instruction:
                # Picking dest part from instruction
                print(c_instruction)
                final_point = c_instruction.index("=")
                dest_part = c_instruction[0:final_point]

                print("________________________________")
                print(dest_part)
                print(table_convert.dest_converter(dest_part))
                print("________________________________")

                destination_machine_code = table_convert.dest_converter(dest_part)



                # Picking comp part from instruction
                if ';' in c_instruction:
                    final_point_char = ';'
                else:
                    final_point_char = '\n'

                start_point = final_point + 1
                final_point = c_instruction.index(final_point_char)
                comp_part = c_instruction[start_point:final_point]
                comp_part = comp_part.strip(' ')

                """
                print("\n________________________________")
                print(comp_part)
                print(table_convert.comp_converter(comp_part))
                print("________________________________\n")
                """
                final_machine_code_line = '111' + table_convert.comp_converter(comp_part)
                final_machine_code_line += destination_machine_code

            else:
                # Picking comp part from instruction where there is no destination in instruction
                final_point_char = ';'
                start_point = final_point + 1
                final_point = c_instruction.index(final_point_char)
                comp_part = c_instruction[0:final_point]
                comp_part = comp_part.strip(' ')
                """
                print("\n________________________________")
                print(comp_part)
                print(table_convert.comp_converter(comp_part))
                print("________________________________\n")
                """
                final_machine_code_line = '111' + table_convert.comp_converter(comp_part)
                final_machine_code_line += table_convert.dest_converter('null')



            # If there is jump then pick jump part of instruction
            if final_point_char == ';':
                start_point = final_point + 1

                if '//' in c_instruction:
                    final_point_char = '/'
                else:
                    final_point_char = '\n'

                final_point = c_instruction.index(final_point_char)
                jump_part = c_instruction[start_point:final_point]
                jump_part = jump_part.strip(' ')
            else:
                jump_part = 'null'

            """
            print("\n________________________________")
            print(jump_part)
            print(table_convert.jump_converter(jump_part))
            print("________________________________\n")
            """
            final_machine_code_line += table_convert.jump_converter(jump_part)
            machine_code.append(final_machine_code_line)


print(machine_code)

f = open(file_name + ".hack", "w")
for line in machine_code:
    f.write(line+'\n')
