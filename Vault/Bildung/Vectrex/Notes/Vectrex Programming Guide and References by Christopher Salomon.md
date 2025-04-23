# Memory Map
Memory map (hardware):  
(taken from Keith Wilkins 'internal.txt')

**0000-7fff**
Cartridge ROM Space, the CART line is also gated with ~E to produce a signal that can be fed directly to the output enable of a ROM. This address range is not gated with the read-write line but this line is fed to the cartridge connector. (r/w)

**8000-C7FF**
Unmapped space.
  
**C800-CFFF**
Vectrex RAM Space 1Kx8, shadowed twice. (r/w)
  
**D000-D7FF**
6522VIA shadowed 128 times (r/w)
  
**D800-DFFF**
Don't use this area. Both the 6522 and RAM are selected in any reads/writes to this area.
  
**E000-FFFF**
System ROM Space 8Kx8 (r/w)

  
**C800-C880**
is RAM used by the vectrex BIOS for housekeeping. (see appendix B) CBEA-CBFE is RAM used by the vectrex BIOS for housekeeping. (see appendix B)
  
**C880-CBEA**
is RAM that can be used by the programmer!

**E000-EFFF**
is ROM, the built in game MINE STORM.

# Structure of program

Keeping the above said in mind, a vectrex program most of the time has following basic structure:

> -init_code-

main_loop:

> -sound update-  
> -recalibration-  
> -sound output-  
> -input handling-  
> -some other stuff-  
> -screen update-  
> 
> repeat main_loop until exit


# Timing
The Wait_Recal routine waits for that timer to expire before continuing and recalibrating the vector system. This BIOS timing information can be set at BIOS RAM location Vec_Rfrsh ($C83D), which is a word pointer, $C83D is the timer low byte, $C83E is the timer high byte. Thus a value of the above 30,000=$7530 would be stored to the BIOS RAM location with a sequence like:

LDD #$3075

STD Vec_Rfrsh

# Hello World
'''
	;***************************************************************************
	; DEFINE SECTION
	;***************************************************************************
	Intensity_5F    EQU     $F2A5                   ; BIOS Intensity routine
	Print_Str_d     EQU     $F37A                   ; BIOS print routine
	Wait_Recal      EQU     $F192                   ; BIOS recalibration
	music1          EQU     $FD0D                   ; address of a (BIOS ROM)
	                                                ; music
	; start of vectrex memory with cartridge name...
	                ORG     0
	;***************************************************************************
	; HEADER SECTION
	;***************************************************************************
	                DB      "g GCE 1998", $80       ; 'g' is copyright sign
	                DW      music1                  ; music from the rom
	                DB      $F8, $50, $20, -$56     ; height, width, rel y, rel x
	                                                ; (from 0,0)
	                DB      "HELLO WORLD PROG 1",$80; some game information,
	                                                ; ending with $80
	                DB      0                       ; end of game header
	;***************************************************************************
	; CODE SECTION
	;***************************************************************************
	; here the cartridge program starts off
	main:
	                JSR     Wait_Recal              ; Vectrex BIOS recalibration
	                JSR     Intensity_5F            ; Sets the intensity of the
	                                                ; vector beam to $5f
	                LDU     #hello_world_string     ; address of string
	                LDA     #$10                    ; Text position relative Y
	                LDB     #-$50                   ; Text position relative X
	                JSR     Print_Str_d             ; Vectrex BIOS print routine
	                BRA     main                    ; and repeat forever
	;***************************************************************************
	; DATA SECTION
	;***************************************************************************
	hello_world_string:
	                DB   "HELLO WORLD"              ; only capital letters
	                DB   $80                        ; $80 is end of string
	;***************************************************************************
	                END  main
	;***************************************************************************
'''