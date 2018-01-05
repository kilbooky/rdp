''' 
rdp 293 

If you cut a white cable you can't cut white or black cable.
If you cut a red cable you have to cut a green one
If you cut a black cable it is not allowed to cut a white, green or orange one
If you cut a orange cable you should cut a red or black one
If you cut a green one you have to cut a orange or white one
If you cut a purple cable you can't cut a purple, green, orange or white cable

clever C soln
C, using a state machine. The state machine is packed into a 64-bit integer (rules = 0x2a140b3bcULL), which is used as an array of six 6-bit integers. Each 6-bit integer has a bit set for each edge. An input that doesn't match an edge is a failure. That is, I've encoded the challenge description into a single integer.
To map a color name to the range 0–5, I'm using a dumb trick with strstr() so that I don't have to write the loop. It scans the string of color names to find its offset, each divisible by 6 (maximum string length). It's actually less efficient than have separate strings since it tries to match between strings. But, hey, it makes my program a little shorter!

#include <stdio.h>
#include <string.h>

const char *colors = "white black purplered   green orange";
const unsigned long long rules = 0x2a140b3bcULL;

int
main(void)
{
    unsigned next = 0x3f;
    char color[8];
    while (scanf("%s", color) == 1) {
        int i = (strstr(colors, color) - colors) / 6;
        if ((1u << i) & next) {
            next = (rules >> (6 * i)) & 0x3f;
        } else {
            puts("Boom!");
            return -1;
        }
    }
    puts("Bomb defused.");
    return 0;
}

 
'''
colors = ('w','r','b','o','g','p')
input1 = ('red', 'white', 'green', 'white')
input2 = ('white', 'orange', 'green', 'white')

# rules = {
	# 'w': res = lambda w : w, b = 0,
	# 'r': res = lambda r : r = rules['g']
	# 'b': res = lambda b : 
	
# }
w = True
r = True
b = True
o = True
g = True
p = True

def white():
	w = False;
	b = False;
	return w, b

def red():
	g = True
	green()

if __name__ == '__main__':
	print (white(), red() )

	