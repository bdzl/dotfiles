COMPILER = g++
FLAGS = -std=c++0x -O2 -Wall -Wno-unused-const-variable -g -Wl,-stack_size,0x10000000

%: %.cpp; $(COMPILER) $(FLAGS) -D LOCAL -o $(@) $(^)
%: %.cc; $(COMPILER) $(FLAGS) -D LOCAL -o $(@) $(^)
%: %.c; $(COMPILER) $(FLAGS) -D LOCAL -o $(@) $(^)
