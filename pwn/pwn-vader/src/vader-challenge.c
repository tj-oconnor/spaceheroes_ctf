#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__attribute__((constructor)) void ignore_me() {
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
	setbuf(stderr, NULL);
}

int gadget1() {
  asm("pop %rcx; pop %rdx; ret;");  
}

int gadget2() {
  asm("pop %r9; pop %r8; ret;");  
}

void print_darth() {
	printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMWXKOxdolc;',;;::llclodkOKNWMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMMMMMMMMMMWXOoc;::::::;;;clkKNXxlcccc:::::cdOXWMMMMMMMMMMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMMMMMWMMNkc,;clccc;,...    .:c:. ...,;:cccc:,,ckNMWMMMMMMMMMMMMMDARK\n");
	printf("MMMMMMMMMMMMMMMMMMXx;;lol:'            .'.           .':loc',xNMMMMMMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMMMMW0:;dxlcc'            .dO;             .::lxo':0MMMMMMMMMMMMS1D3\n");
	printf("MMMMMMMMMMMMMMMWk':Ol;x0c           ';oKK: .            cOo,dk;,OMMMMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMMMO':Ol:0Xc            l0OXNc.l'            cKO;o0;,KMMMMMMMMMMMMOF\n");
	printf("MMMMMMMMMMMMMMX:'Oo:KMd             o0ONWc'x,            .xM0:xk.lWMMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMMx.okcOMMk.            o0OWMl'x;            .xMMklOc'OMMMMMMMMMMTH3\n");
	printf("MMMMMMMMMMMMMWc'xldWMMWKx'          oOkNMo,x;          'oONMMWdod.oMMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMK;:dl0MMMMMXc          lOxNMo'd;          lWMMMMMOld;:NMMMMMMMFORC3\n");
	printf("MMMMMMMMMMMMMO':ldWMMMMWo           ckxNMd,d;          .kMMMMMNlc;,KMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMk';cxMMMMMWOl:,.       cxxNMx;d;       .,;l0MMMMMWdc;'0MMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMx',cOMMMWXOxoc;.       cxxNMkcx:       .cdkOXWMMMMd:;'0MMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMx';;l0xl,.    .       ,0xdWMOcOx.           .,lkXWd:;'OMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMd.ld:'    .',;::ccc:;,kWxxWMOlONo',:cc::,'...   'ood:'OMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMWl.xK:            .';coOXo:xxo:kKkl:;'.           .oXl.OMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMM0';d'       .......',;;''.    ..'',;,'......        lo.lWMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMX:,l'        ..      .',:;lo. ;d:;:,..     ..         c:.xWMMMMMMMMMM\n");
	printf("MMMMMMMMMMNc,o,                     '0XxoOWd.                    .l:,0MMMMMMMMMM\n");
	printf("MMMMMMMMMWd,o;                      .xMNXWWc                      .o::XMMMMMMMMM\n");
	printf("MMMMMMMMMk,oc                    .. .kXkdONc ..                    'd;oWMMMMMMMM\n");
	printf("MMMMMMMM0;lo.         .;:,'....  'cxxo;'''cxxo:. ......';'          :x:xWMMMMMMM\n");
	printf("MMMMMMMK:lx.           'xNNXXXKd;;::,.,l:..':c;,;xKKKXX0l.           oxcOMMMMMMM\n");
	printf("MMMMMMXcck,         ..   ,cloool:. .lc,,'.cx, .';looooc.             .kxlKMMMMMM\n");
	printf("MMMMMWoc0c      .'. .cdll;..',;lkOxxl:xOOxclddkkl:,''.';:cl'  ..      :KddNMMMMM\n");
	printf("MMMMWxc0x.       :o; .xWWKkdodkKWMMKlxWMMMKdOMMWXkdoloONMXc .cc.      .dXdxWMMMM\n");
	printf("MMMMOcOK;         'xd.'0MMMMMMMXk0Xc'dKXXKO:,0KkKWMMMMMMWo.;xl.        ,0XxOWMMM\n");
	printf("MMM0lkNo           .xO;cXWWMWXd:dx; ;d;,:l:  ;xd:l0WMMMWx,oO;           oWKx0MMM\n");
	printf("MMKokW0'            .dKdOWMNx;ckd:. lK,.cOd..lcdO:'oXMMKokO,            .OWKkXMM\n");
	printf("MXdxN0;              .kWNWXc.,d;.do lK,.:kd.,0l.;o,.:KWNNK,              ;KW0kNM\n");
	printf("NxdOc.                ,0MMd..;l''Oo lK,.;kd.;Ko .,,. lWMXc                'xXOOW\n");
	printf("xd0d.                  ;KMO,.c0ocXk;xXocxK0cdNOcol'''dWWd.                 .o0kO\n");
	printf(",xWX:                   :XXc.:oddxxxxxxddxxxxkkOko;.:KNd.                  'kN0l\n");
	printf(".,dOkdoc:,'..            .'..,lxkox0OO0kxOOxOOddxl,..,,.              ..,:lkKOl.\n");
	printf("x,...',;:cc::;,,'''...        .,;cdO0KKKXXKkdo:,,'.        ...'',,,,;;clllc;'..;\n");
	printf("MNKOxdoolcc::;;;;. ..             ..,;:clc;..              ...,;;;,,'',;;:clox0N\n");
	printf("MMMMMMMMMMMMMMMMW0;                                          'kKXXNNNWWMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMMMMMMNd,..          ........                .. .kWMMMMMMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMMMMMMMWKxl;..       'okOOko:,..     ..  ....';lKWMMMMMMMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMMMMMMMMMMXkdc'....   .,cc:,,'..  .'o0Oo:;:cokXMMMMMMMMMMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMMMMMMMMMMMMWXkdoc;''''',,;;:::::::ccllclx0NMMMMMMMMMMMMMMMMMMMMMMMM\n");
	printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkol:;,'.''''....,cokKWMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
}

//use the dark side of the force
//  rdi, rsi, rdx, rcx, r8, and r9.
//dark side of   the  force

int vader(char* a, char* b, char* c, char* d, char* e) {
	if (strcmp(a, "DARK") == 0) {
		if (strcmp(b, "S1D3") == 0) {
			if (strcmp(c, "OF") == 0) {
				if (strcmp(d, "TH3") == 0) {
					if (strcmp(e, "FORC3") == 0) {
						char flag[32] = {0};
						FILE *fd = NULL;
						fd = fopen("flag.txt", "r");
						fgets(flag, 0x30, fd);
						printf("\n\n <<< %s\n", flag);
					}
				}
			}
		}
		else {
			printf("\n\n You are a wretched thing, of weakness and fear.");
		}

		exit(1);
	}
}

int main() {
	print_darth();
	char buf[30];
	printf("\n\n When I left you, I was but the learner. Now I am the master >>> ");
	fgets(buf, 0x100, stdin);

}
