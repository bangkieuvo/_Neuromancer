section .bss
    buffer resb 256         ; lưu chuỗi nhập vào
    buffer_len resb 20 
section .data
	msg_bang db "bang 16 ",0
	msg_bang_len equ $ - msg_bang
	
	msg_LonHon db "lon hon 16",0
	msg_LonHon_len equ $ - msg_LonHon

	msg_BeHon db "be hon 16",0
	msg_BeHon_len equ $ - msg_BeHon
section .text
	global _start
	
	
_start:
	equal:
		mov rax,1
		mov rdi,1
		mov rsi,msg_bang
		mov rdx,msg_bang_len
		syscall
	mov rax,17
	;mov rbx,2
	;mul rbx
	;div rbx
	mov rcx,rax
	
;	cmp rax,17
;	je equal
	
	
	
	mov rdi, buffer_len + 19
    mov byte [rdi], 10      ; newline
    dec rdi	
	mov rax, rcx
	
    
	itoa_loop:
		mov rdx, 0
		mov rbx, 10
		div rbx
		add dl, 48
		mov [rdi], dl
		dec rdi
		test rax, rax
		jnz itoa_loop
	
	inc rdi

    
    ; ===== In độ dài =====
    mov rax, 1
    mov rsi, rdi
    mov rdi, 1
    mov rdx, buffer_len + 20   ; rdx = địa chỉ outbuf + 20
	sub rdx, rdi           ; rdx = rdx - rdi

    syscall
	
	mov rax,60
	mov rdi,0
	syscall
