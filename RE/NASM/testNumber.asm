section .bss
	stringBuffer_in resb 20
	stringBuffer_out resb 20
	
	
section .data
	msg_yeuCauNhapChuoi db "Nhap vao so muon nhan doi: ",0
	msg_yeuCauNhapChuoi_len equ $ - msg_yeuCauNhapChuoi
	
	msg_xuatRaSoNhanDoi db "So sau khi nhan doi: ",0
	msg_xuatRaSoNhanDoi_len equ $ - msg_xuatRaSoNhanDoi
	
	msg_xuatRaLoi db "Trong dãy nhập vào có kí tự không phải số!",0
	msg_xuatRaLoi_len equ $ - msg_xuatRaLoi
section .text
	global _start
	
	
_start:
	;stdout: Yeu cau input
	mov rax,1
	mov rdi,1
	mov rsi,msg_yeuCauNhapChuoi
	mov rdx,msg_yeuCauNhapChuoi_len
	syscall

	;stdin: input
	mov rax,0
	mov rdi,0
	mov rsi,stringBuffer_in
	mov rdx,20
	syscall
	
	;rax la so luong byte sau syscall, rax -> rcx
	mov rcx, rax
	dec rcx ;bo 1 byte "/n'
	
	mov r8,rcx
	mov r9,0
	loop_covert_stringToNum:
		mov rbx,10
		mov r10, rcx
		sub r10, r8
		movzx r11,byte[stringBuffer_in + r10]
		add r11,-48
		cmp r11, 9
		jg loop_covert_stringToNum_error
		cmp r11,0
		jl loop_covert_stringToNum_error
		mov rax,r9
		mul rbx
		add rax,r11
		mov r9,rax
		dec r8
		test r8,r8
		jnz loop_covert_stringToNum	
	jmp loop_covert_stringToNum_Continue
	loop_covert_stringToNum_error:
		mov rax,1
		mov rdi,1
		mov rsi, msg_xuatRaLoi
		mov rdx, msg_xuatRaLoi_len
		syscall
		jmp exit
	loop_covert_stringToNum_Continue:
		
	mov rax,r9
	mov rbx,2
	mul rbx
	
	mov rdi, stringBuffer_out + 19
    mov byte [rdi], 10      ; newline
    dec rdi	
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

    
    ; ===== In Số =====
    mov rax, 1
    mov rsi, rdi
    mov rdi, 1
    mov rdx, stringBuffer_out + 20   ; rdx = địa chỉ outbuf + 20
	sub rdx, rdi           ; rdx = rdx - rdi

    syscall
	
	
	

exit:
	mov rax,60
	mov rdi,0
	syscall
