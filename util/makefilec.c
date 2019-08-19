#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int findDotPosition(char* argv) {
    int pntPos = -1;
    int namesize = strlen(argv) - 1;
    for(int i = namesize; i >= 0; i--) {
        if(argv[i] == '.') {
            pntPos = i;
            break;
        }
    }
    return pntPos;
}

int main(int argc, char* argv[]) {
    pid_t ppid, cpid;
    int state;
    int pntPos = -1;
    char filename[100] = {0, };
    pntPos = findDotPosition(argv[1]);
    if(pntPos == -1) {
        printf("Error: Can't find dot position!\n");
        return 0;
    }

    strncpy(filename, argv[1], pntPos);
    filename[pntPos] = '\0';

    ppid = fork();
    if(ppid < 0) {
        printf("fork error!");
        return 0;
    }
    else if(ppid == 0) {
        execlp("gcc", "gcc", "-o", filename, argv[1], NULL);
    }
    else {
        cpid = wait(&state);
        execlp(filename, filename, NULL);
    }
    printf("fork coding error!");
    return 0;
}