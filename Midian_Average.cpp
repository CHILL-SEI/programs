#include<stdio.h>
#include<stdlib.h>
#include<math.h>

//配列の平均値を求める関数
int average_function(int Sum, int Len) { 

	float Ave = (Sum / Len);

	return Ave;

}

//配列を昇順に並び変える関数
void sort_function(int* array, int Len) {

	int z;

	for (int x = 0; x < Len; x++) {

		for (int y = x + 1; y < Len; y++) {

			if (array[x] > array[y]) {

				z = array[x];
				array[x] = array[y];
				array[y] = z;

			}
		}
	}
}

//main関数
int main(void) {

	int RanLis[10];

	for (int i = 0; i < 9; i++) {	//インデックス０～８までを１～９までのランダムな整数値で埋める

		int RanNum = rand() % 9 + 1;

		RanLis[i] = RanNum;

	}

	RanLis[9] = 0;	//インデックス９には０を代入

	for (int m = 0; m < 10; m++) {

		printf("%d", RanLis[m]);	//ソートする前の配列を表示する

	}

	printf("\n");	

	int Sum = 0;

	for (int j = 0; j < 10; j++) {	//RanLisのすべての要素の合計値を変数Sumに代入

		Sum += RanLis[j];
	
	}

	int Len_R = sizeof(RanLis) / sizeof(RanLis[0]);	//RanLisの要素数を変数Len_Rに代入

	sort_function(RanLis, Len_R);	//RanLisを昇順にソート

	float Mid;	//中央値を求める

	if (Len_R % 2 == 0) { 

		Mid = RanLis[Len_R / 2];

	}

	else {

		Mid = (RanLis[(Len_R - 1) / 2] + RanLis[(Len_R - 1) / 2 + 1]) / 2;

	}

	float Ave = average_function(Sum, Len_R);	//SumとLen_Rを使って平均値を求める

	int AbsLis[10];	//平均とRanLisの各要素の差の絶対値を格納するリスト

	for (int n = 0; n < 10; n++) {

		double Abs = fabsf(RanLis[n] - Ave);
		AbsLis[n] = Abs;

	}

	int Len_A = sizeof(AbsLis) / sizeof(AbsLis[0]);

	sort_function(AbsLis, Len_A);
	
	int Nea = 0;

	for (int l = 0; l < 10; l++) {	//差を昇順にソートしたのち、その最小値を出した要素を変数Neaに代入

		if ((AbsLis[0]) == fabsf(RanLis[l] - Ave)) {

			Nea = RanLis[l];

		}
	}

	printf("the midian is %f", Mid);
	printf("\n");
	printf("the closest number to average is %d", Nea);

	return 0;

}