set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'wombat256.vim'
Plugin 'itchyny/lightline.vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'fatih/vim-go'

call vundle#end()

function! CppSwitchSourceHeader()
    if (expand('%:e') == "cpp")
        find %:r.h
    else
        find %:r.cpp
    endif
endfunction

filetype plugin on

syntax enable

set backspace=indent,eol,start
set number
set wildmenu
set shiftwidth=4
set smartindent
set smarttab
set ts=4
set expandtab
set list
set listchars=tab:>\ ,
set ruler
set encoding=utf-8
set fileencodings=utf-8
set colorcolumn=100
set nowrap

colorscheme wombat256mod
highlight ColorColumn ctermbg=DarkGrey

highlight ExtraWhitespace ctermbg=red guibg=red
match ExtraWhitespace /\s\+$/
autocmd BufWinEnter * match ExtraWhitespace /\s\+$/
autocmd InsertEnter * match ExtraWhitespace /\s\+\%#\@<!$/
autocmd InsertLeave * match ExtraWhitespace /\s\+$/
autocmd BufWinLeave * call clearmatches()

hi Error NONE
hi ErrorMsg NONE

""""" lightline
set laststatus=2

let g:lightline = {
    \ 'component_function': {
    \    'filename': 'LightLineFilename'
    \ }
\ }

function! LightLineFilename()
    return expand('%:p')
endfunction

""""" YouCompleteMe
set completeopt-=preview
let g:ycm_show_diagnostics_ui=0
let g:ycm_extra_conf_globlist=['~/.ycm_extra_conf.py']
noremap <C-]> :YcmCompleter GoTo<CR>

""""" nerdtree
let g:NERDTreeShowHidden=1
map <F2> :NERDTree<CR>
map <F3> :NERDTreeFind<CR>
map <F4> :NERDTreeClose<CR>
