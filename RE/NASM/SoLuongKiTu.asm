section .bss
	string_buffer resb 256
	string_len_buffer resb 20
section .data
	msg db "Nhập vào chuỗi:",10
	msg_len equ $ - msg
	_MAX_STRING_LENGTH equ 256
section .text
	global _start

_start:
	mov rax,1
	mov rdi,1
	mov rsi,msg
	mov rdx, msg_len
	syscall
	
	mov rax,0
	mov rdi,0
	mov rsi,string_buffer
	mov rdx, _MAX_STRING_LENGTH
	syscall
	
	mov rcx, rax
	dec rcx
	
	mov rax,1
	mov rdi,1
	mov rsi,string_buffer
	mov rdx,_MAX_STRING_LENGTH
	syscall
	
	
	mov rax, 60
	mov rdi, 0
	syscall
