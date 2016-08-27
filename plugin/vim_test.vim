" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

function! UpdateBuffer()
python << endOfPython

from vim_test import update_buffer

update_buffer()

endOfPython
endfunction

function! SleepPrint()
python << endOfPython

from vim_test import sleep_print

sleep_print()

endOfPython
endfunction

command! UpdateBuffer call UpdateBuffer()
command! SleepPrint call SleepPrint()
