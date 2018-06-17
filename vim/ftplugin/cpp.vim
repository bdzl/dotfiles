map <F9> <ESC>:w<CR>:make -f ~/.vim/makefile %< <CR>
map! <F9> <ESC>:w<CR>:make -f ~/.vim/makefile %< <CR>
map <F8> <ESC>:!time ./%< <CR>
map! <F8> <ESC>:!time ./%< <CR>
map <F5> :call CppSwitchSourceHeader()<CR>
