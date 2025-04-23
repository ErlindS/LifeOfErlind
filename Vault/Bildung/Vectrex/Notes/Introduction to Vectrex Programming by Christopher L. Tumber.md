**p. 0-8** 
already known. Nothing interesting. 

**p. 9 Nice analogy** 
ROM: we can look into the locker but we can't EVER change the contents.
RAM: we can look in the locker AND we can change the contents at any time. We can store anything we want in there.

**p. 10 memory Layout - nice**
- locker numbers $0000 to $7FFF contain our program (game) max 32K
- it (essentially) goes to the first locker, at $0000 and looks for the first
instruction.
- C880 to $CBFF usable ram
- $E000 to $FFFF are also ROM (not usable, BIOS)

**p. 11/12 Format**
Well assemblerformat:

$1000 deca
^          ^
|            |
|             ---------- The instruction
|
------------------- The address

The purpose of an ASSEMBLER is to take our mnemonics like "deca" and translate them to their real

**p. 13/14**
We tell the ASSEMBLER where to start with a line like:
		ORG $1000
This line, which you'll find near the begining of every Vectrex program tells
the ASSEMBLER "Start putting program code in memory location $1000".

So, instead of our code looking like this:
		$1000 sta $C880
		$1003 deca
		$1004 tsta
		
It's just going to look like this:
			  sta $C880
			  deca
			  tsta

what if we move this piece of code around? What if we put something in the locker in front of it, so it all gets moved down a locker? That's what a label is for.

kill_ship:
		sta $C880
		deca
		tsta

**p. 15 Constants**
If you look at any Vectrex source code you will generally see a list of such constants. Constants look like:
user_RAM        EQU               $C880

user_RAM        EQU               $C880
kill_ship:
        sta user_RAM
		deca
		tsta

In addition, constants MUST all be placed at the very begining of your source code, BEFORE any actual instructions.

**p. 16/17 Registers**

If lockers contain data, there's generally not much you can do with it while it's sitting in the locker. You have to take it out to use it. To do this, you take data out of a locker and put it in your pocket.

The Vectrex's pocket's are called REGISTERS. The registers are called (rather unimaginatively) A,B,D,X,Y,U,S,PC,DP and CC.

A is the right hand pocket. B is the little change pocket. The D register is these two pockets combined! The D register is a 16-bit (2 byte) register that is actually a combination of A and B.

The X and Y registers are two 16-bit registers. They're usually used as pointers in Indexed Mode Instructions (see below).

U and S are both Stack Pointers (more on that later).

PC is the program counter. This is the number of the current locker being checked to see what instruction to execute.

CC is the Condition Code Register. It tells you the results of some types of instructions the Vectrex just did.

**p. 18/19 opcodes**
LDA - Load a value into the A register
LDB - Load a value into the B register
LDD - Load a value into the D register
LDS - Load a value into the S register
LDU - Load a value into the U register
LDX - Load a value into the X register
LDY - Load a value into the Y register

e.g.
LDA #3

That takes a copy of whatever is in $C880 and copies it into register A. $C880 is itself not changed and keeps whatever was there. In effect, taking something from a locker (memory) and putting it into your pocket (register) only copies and doesn't actually move it.

ST is an abbreviation for STore.

STA $C880

The instruction: DECA Will reduce the value of register A by one.
The instruction: INCA Will increase the value of register of A by one.

**p. 20/21/22 addressing Modes**

The addressing modes Inherent, Immediate, Extended, Direct, Indexed
and they look like this:
DECA - Inherent
LDA #$00 - Immediate
LDA $C880 - Extended
LDA $80 - Direct
LDA #$80,X - Indexed
LDA B,X - Indexed
LDA ,X++ - Indexed
LDA [$C880] - Indexed


Immediate mode means that the target of the instruction is an actual value, and that value will follow the instruction immediately. So, LDA #$00 Puts the actual value #$00 (Zero) into register A.

Extended mode means the target of the instruction is a MEMORY LOCATION, and the memory location follows the instruction. So, LDA $C880 Copies whatever was in memory location (locker number) $C880 into register A

Inherent mode stands alone and unlike Immediate or Extended takes no further
arguments like #$00 or $C880. Instead, the effect of the instruction is completely self-contained. These are really the simplest of instructions. DECA

Direct addressing is actually very similar to Extended. Picture if you will
some code which looks like this:

LDA $C880
STA $C881
LDA $C882
STA $C883
LDA $C884
STA $C885
LDA $C886
STA $C887
LDA $C888
STA $C889

 all this does is move some values around. From $C880 to $C881,
from $C882 to $C883. 

With Direct addressing, we could instead do this:
LDA #$C8
TFR A,DP
LDA $80
STA $81
LDA $82
STA $83
LDA $84
STA $85
LDA $86
STA $87
LDA $88
STA $89

When the 6809 encounters a Direct mode instruction, it consults the DP register and using the value in DP, acts like an Extended mode instruction, but with that DP value as the first two digits in the address. 
So, if DP is equal to #$C8 then:
LDA $00

is the same as:
LDA #$C800

**p.23/24/25/26/27**

JMP (JuMP) and BRA (BRanch Always) are unconditional jumps.

LDA $C880
STA $C881
JMP another_section

another_section:


The difference between JMP and BRA is that JMP can jump to ANY place in the program. BRA on the other hand is limited, it can only go a maximum of 127 bytes ahead or behind.
All RTS means is ReTurn from Subroutine. As soon as the program hits one of these, it goes back to where it hit the last JSR and resumes just after that JSR.

The other branching commands are all conditional. They only do the jumping if
a certain condition has been met. These conditions/Bits are: Half Carry (H), Negative (N), Zero (Z), Overflow (V) and Carry (C).

kill_ship:
DEC ships_left ;Decrement the number of ships left by 1
BEQ game_over ;Check if that was the last ship, and branch if it was

BNE (Branch Not Equal) is the exact opposite of BEQ. This instruction branches only if the Zero bit had NOT been set.

The other branch instructions are all fairly simple. The MC6809E Microprocessor Programming Manual from Motorola gives a description of them all, as will most other reference materials.

So, BRA is a short jump instruction and LBRA is the same instruction, but will handle long jumps. The difference is that LBRA takes an extra byte. The other thing to keep in mind is that some assemblers treat Relative and Absolute jumps differently and can give you weird results if you mix them. The BRA, BEQ, BNE, BSR (all of the starting with B) jumps and their L prefixed equivalents (LBRA, LBEQ, LBNE, LBSR) are all Relative jumps. JMP and JSR are absolute jumps.

**p. 28/29/30/31**

loop_variable EQU $C880 ;Create a variable for looping
	LDA #$05 ;Initialise our loop
	STA loop_variable ;variable with a value of 5
loop_start: ;This is the label at the start of the loop
	LDA $C880 ;These are the instructions we want to repeat 5 times
	STA $C881 ;These are the instructions we want to repeat 5 times
	DEC loop_variable ;Subtract the loop_variable by 1
	BNE loop_start ;If the loop variable is not Zero, jump to loop_start

**p. 32/33**

This is about the simplest, most basic program you can write for the Vectrex
which will actually assemble and run:
	ORG $0000
; Magic Init Block
	FCB $67,$20
	FCC "GCE XXXX"
	FCB $80
	FDB music
	FDB $f850
	FDB $30b8
	FCC "SIMPLE"
	FCB $80,$0
start:
	bra start
music:
	FDB $fee8
	FDB $feb6
	FCB $0,$80
	FCB $0,$80

ORG $0000
This line tells the assembler to start assembling code at memory location
$0000. For the Vectrex, ALL code begins at $0000.


; Magic Init Block
	FCB $67,$20
	FCC "GCE XXXX"
	FCB $80
	FDB music
	FDB $f850
	FDB $30b8
	FCC "SIMPLE"
	FCB $80,$0
This actually contains all the information the Vectrex needs to compose the
screen you see at startup. "GCE XXXX" is the copyright info. "SIMPLE" is
the
name of the program/game.

The actual program is:
start:
	bra start

music:
	FDB $fee8
	FDB $feb6
	FCB $0,$80
	FCB $0,$80
I won't go into the format for music here, but this code just tells the Vectrex not to play any music.


**p. 34/35 first programm**


waitrecal EQU $f192
move_pen7f_to_d EQU $f2fc
intensity_to_A EQU $f2ab
draw_to_d EQU $f3df
	ORG $0000
; Magic Init Block
	FCB $67,$20
	FCC "GCE XXXX"
	FCB $80
	FDB music
	FDB $f850
	FDB $30b8
	FCC "LINE"
	FCB $80,$0
start:
;Draws a big line from the middle of screen to right edge.
	draw_line:
	jsr waitrecal                 ;Reset the CRT
	lda #00                        ;Get y
	ldb #00                        ;Get x
	jsr move_pen7f_to_d   ;go to (x,y)
	lda #$7f                       ;Get the Intensity
	jsr intensity_to_A         ;Set intensity
	lda #00                        ;Get y
	ldb #127                      ;Get x
	jsr draw_to_d              ;draw a line to (x,y)
	bra draw_line
music:
	FDB $fee8
	FDB $feb6
	FCB $0,$80
	FCB $0,$80

Explanation
	ORG -> Starting Point
	Magic Init BLock -> first things to see on a screen
	music -> No music at all
	draw_line: actually draws a line. comments a pretty nice and selfexplaining


**p. 36/37/38/39 Indexing**

volcano EQU $C900

LDA #$05
STA volcano

LDX #$ C880            ;Set register X to #$C880
LDA volcano,X         ;LoaD register A with the value stored in the memory location 
				;which is the sum of the value in register X and the value
				;in memory location volcano
In this case, register A will wind up with whatever is in memory locarion $C885
($C880+$05).


LDX #$C880
LDB #$02
LDA B,Y ( :( I guess typo )
Will LoaD the register A with whatever is in memory location $C880
($C880+$02)


LDX #$C880
LDA ,X+
Will LoaD register A with the contents of memory location $C880. Then, the
value of X is increased by 1.

LDA ,-X
Will do the same, but decrease X by 1.
LDA ,X++
LDA ,--X

LDA [$C880]
This LoaDs the register A with the value in the memory location that is
pointed to by $C880 and $C881. So, if $C880 has a value of $E000 then
register A is LoaDed with the value contained in memory address $E000.


number_aliens EQU $C880 ;Create a variable to hold the number of aliens
level EQU $C881 ;Create a variable to hold the level

LDA #$01
STA level ;Set the level to 1

LDX #number_aliens_table ;Setup the start of the table
LDA level,X ;Get the number of aliens and put it in A

number_aliens_table: fcb #00,#10,#12,#14,#16,#18,#20 ;The table The only thing you haven't seen yet is fcb. All fcb does is tell the assembler to put this ACTUAL VALUE in the code and not interpret it as an instruction. So the values of #00,#10,#12,#14,#16,#18 and #20 are put here. That way you can put static data right into the code.