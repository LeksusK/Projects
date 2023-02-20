#include <iostream>
#include <time.h>

const int size = 100;
int mass[size];

void qsort(int begin, int end) {
	int left = begin;
	int right = end;
	int ell = mass[(left + right) / 2]; // пусть средний эл. будет опорным
	while(left <= right) {
		while(mass[left] < ell) {
			left++;
		}
		while(mass[right] > ell) {
			right--;
		}
		if(left <= right) {
			std::swap(mass[left++], mass[right--]);
		}
	}
	if(begin < right) {
		qsort(begin, right);
	}
	if(end > left) {
		qsort(left, end);
	}
}

int main() {
	if (size == 1) {
		std::cout << "Сортировка завершена:\n" << mass[0] << std::endl;
	}
	srand(time(NULL));
	// заполнение матрицы ГСЧ
	for (int i = 0; i < size; i++) {
		mass[i] = 1 + rand() % 4000;
		std::cout << mass[i] << " ";
	}
	std::cout << " \n" << std::endl;
	std::cout << "______________________________________________________________________________________________" << std::endl;
	std::cout << "Отсортированный массив:" << std::endl;
	std::cout << " \n";
	// вывод отсортированного массива
	qsort(0, 99);
	for (int i = 0; i < size; ++i) {
		std::cout << mass[i] << ", ";
	}

	return 0;
}
