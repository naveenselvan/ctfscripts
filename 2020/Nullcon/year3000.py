#Few line Optimized from https://x3ero0.tech/posts/year3000/ without disasm

import base64
import sys
import os
from pathlib import Path

def solve(filename):
	file = open(filename, "rb").read()
	ELF64_Addr = 0x1010
	ELF32_Addr = 0x1008
	
	Format = ord(file[0x04])
	if (Format == 2):
                code_count=(ord(file[0x819]))
                code_value=chr(ord(file[0x820]))
		value = file[ELF64_Addr : ELF64_Addr+8]
		
             	flag = code_value * code_count + value

	elif(Format == 1):

                code_count=(ord(file[0x661]))
                code_value=chr(ord(file[0x668]))
		value = file[ELF32_Addr:ELF32_Addr+4]

		flag = code_value * code_count + value
	
        print(flag)
	#return flag




def main():
    solve(sys.argv[1])



if __name__ == "__main__":
	main()
