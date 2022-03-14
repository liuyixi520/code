#include <iostream>
#include <math.h>
#include <stdio.h>

//最小二乘法回归系数
double *least_square(double *x, double *y, int n)
{
    double *a = new double[2];
    double sum_x = 0, sum_y = 0, sum_xy = 0, sum_x2 = 0;
    for (int i = 0; i < n; i++)
    {
        sum_x += x[i];
        sum_y += y[i];
        sum_xy += x[i] * y[i];
        sum_x2 += x[i] * x[i];
    }
    a[0] = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x);
    a[1] = (sum_y - a[0] * sum_x) / n;
    return a;
}

//测试用例
int main()
{
    double x[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    double y[] = {1, 3, 2, 5, 7, 8, 8, 9, 10, 12};
    double *a = least_square(x, y, 10);
    std::cout << "y=" << a[0] << "x+" << a[1] << std::endl;
    return 0;
}