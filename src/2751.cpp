//quick sort
//merge sort
//STL sort
#include <stdio.h>
#include <stdlib.h>

using namespace std;

void swap(int &x, int &y) {
    int z = x;
    x = y;
    y = z;
}

int choosePivot(int low, int high) {
    return low + (high - low) / 2;
}

int partition(int *a, int low, int high) {
    int pivotIndex = choosePivot(low, high);
    int pivotValue = a[pivotIndex];
    swap(a[pivotIndex], a[high]);
    int storeIndex = low;
    for(int i = low; i < high; i++) {
        if(a[i] < pivotValue) {
            swap(a[i], a[storeIndex]);
            storeIndex += 1;
        }
    }
    swap(a[storeIndex], a[high]);
    return storeIndex;
}

void quicksort(int *a, int low, int high) {
    if(low < high) {
        int pivot = partition(a, low, high);
        quicksort(a, low, pivot - 1);
        quicksort(a, pivot + 1, high);
    }
}

void quicksort2(int *a, int left, int right) {
    int i = left; int j = right;
    int pivot = a[(left + right) / 2];
    do {
        while(a[i] < pivot) {
            i++;
        }
        while(a[j] > pivot) {
            j--;
        }
        if(i <= j) {
            swap(a[i], a[j]);
            i++; j--;
        }
    } while(i <= j);

    if(left < j) {
        quicksort2(a, left, j);
    }

    if(i < right) {
        quicksort2(a, i, right);
    }
}

void quickSortPr(int *a, int left, int right) {
    int i = left; int j = right;
    int pivot = a[(left + right) / 2];
    do {
        while(a[i] < pivot) {
            i++;
        }
        while(a[j] > pivot) {
            j--;
        }
        if(i <= j) {
            swap(a[i], a[j]);
            i++; j--;
        }
    } while(i <= j);
    if(i < right) {
        quickSortPr(a, i, right);
    }
    if(j > left) {
        quickSortPr(a, left, j);
    }
}

int main() {
    int n;
    scanf("%d", &n);

    int *a = (int *)malloc(sizeof(int)*n);

    for(int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    quicksort(a, 0, n-1);

    for(int i = 0; i < n; i++) {
        printf("%d\n", a[i]);
    }

    return 0;
}