.globl _start
_start:
	.thumb
	mov ip, r5
	
	add r5, pc, #8
	
	ldr r5, [r5]
	
	push {r5}
	
	mov r5, ip
	
	pop {pc}

	