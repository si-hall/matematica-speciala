#include <stdio.h>
int lista(int* arr, int ver)
    {
       int d = 0;
       for (int i = 0; i < ver; i++)
            for (int j = 0; j < ver*ver; j++)
                {
                    printf("Enter the %d track for %d point: ",j+1,i+1);
                    scanf("%d",&arr[i * ver + j]);
                    if ( arr[i * ver + j] == 0)
                        {
                            d = d + j;
                            break;
                        }
                }
        return d;
    }

int listb(int* arr, int* arr1, int d, int ver)
    {
        int k = 0;
        for (int i = 0; i < ver; i++)
            {
            int j = 0;
            while ( 1 > 0)
                {
                   if (arr[i * ver + j] != 0)
                    {
                        if (arr[i * ver + j] == i+1)
                            {
                                arr1[k * ver + i] = 2;
                                j++;
                                k++;
                            }
                        else
                            {
                                arr1[k * ver + i] = -1;
                                arr1[k * ver + (arr[i * ver + j]-1)] = 1;
                                j++;
                                k++;
                            }
                    }
                   else
                    {
                        break;
                    }
                }
        }
    }

int listc(int* arr,int* arr2, int ver)
    {
       for (int i = 0; i < ver; i++)
            {
                int j = 0;
                while ( 1 > 0)
                    {
                        if (arr[i * ver + j] == 0)
                            {
                                break;
                            }
                        else
                        {
                            if (arr[i * ver + j] == i + 1)
                                {
                                    arr2[i * ver + (arr[i * ver + j]-1)] = 2;
                                    j++;
                                }
                            else
                                {
                                    arr2[i * ver + (arr[i * ver +j]-1)] = 1;
                                    j++;
                                }
                        }
                    }
            }
    }

int matrixi(int* arr1, int ver, int d)
    {
        for (int i = 0; i < d; i++)
            for (int j = 0; j < ver; j++)
                {
                    printf("Enter %d element for %d line: ",j+1,i+1);
                    scanf("%d",&arr1[i * ver + j]);
                }
    }

int matrixl(int *arr1, int* arr, int d, int ver)
    {
        int one, two = 0;
        for (int i = 0; i < d; i++)
          {
            for (int j = 0; j < ver; j++)
                {
                    if (arr1[i * ver +j] == 1 || arr1[i * ver +j] == 2)
                        {
                            two = j+1;
                            if (arr1[i * ver +j] == 2)
                                {
                                    one = j;
                                }
                        }
                    else
                        {
                            if (arr1[i * ver + j] == -1)
                                {
                                    one = j;
                                }
                        }
                }
                int k = 0;
            while ( 1 > 0 )
                {
                    if (arr[one * ver + k] == 0)
                        {
                            arr[one * ver + k] = two;
                            break;
                        }
                    else
                        {
                            k++;
                        }
                }
           }
    }

int matrixa(int* arr2, int ver)
    {
        for (int i = 0; i < ver; i++)
            for (int j = 0; j < ver; j++)
                {
                    printf("Enter the %d element of %d line: ", j+1,i+1);
                    scanf("%d", &arr2[i * ver +j]);
                }
    }

int matrixla(int* arr2, int* arr, int ver)
    {
        int cc = 0;
        for (int i = 0; i < ver; i++)
          {
           int k = 0;
            for (int j = 0; j < ver; j++)
                {
                    if (arr2[i * ver + j] == 1)
                        {
                            arr[i * ver + k] = j + 1;
                            k++;
                            cc++;
                        }
                    if (arr2[i * ver + j] == 2)
                        {
                            arr[i * ver + k] = i+1;
                            k++;
                            cc++;
                        }
                }
          }
        return cc;
    }

int main()
{
 int ver, m = 0, p = 1, d = 0;
 printf("Enter the ver: \n");
 scanf("%d",&ver);
int arr[ver][ver], arr1[ver*ver][ver], arr2[ver][ver];
 if (ver == 1)
    {
        int arr[ver+1][ver];
    }
for (int i = 0; i < ver; i++)
    for (int j = 0; j < ver; j++)
                {
                    arr[i][j] = 0;
                    arr2[i][j] = 0;
                }
for (int i = 0; i < ver*ver; i++)
    for (int j = 0; j < ver; j++)
                {
                    arr1[i][j] = 0;
                }
 printf("How you want to enter graph? \n 1 - Ajacency matrix \n 2 - Incidence matrix \n 3 - Adjacency list \n");
 scanf("%d",&m);
    switch (m)
    {
    case 1:
        //enter adjacency matrix
        matrixa(*arr2,ver);
        d = matrixla(*arr2, *arr, ver);
        listb(*arr,*arr1,d,ver);
        break;
    case 2:
        //enter matrix incidence
        printf("Enter the number of track: ");
        scanf("%d",&d);
        matrixi(*arr1,ver,d);
        matrixl(*arr1,*arr,d,ver);
        listc(*arr, *arr2, ver);
        break;
    case 3:
        //enter adjacency list
        d = lista(*arr,ver);
        listb(*arr, *arr1, d, ver);
        listc(*arr, *arr2, ver);
        break;
    default:
        break;
    }
while (p != 0)
    {
        printf("Select one of the option: \n 1 - Show Adjacency matrix \n 2 - Show Incidence matrix \n 3 - Show Adjacency list \n 4 - Exit the program\n");
        scanf("%d",&m);
        switch (m)
        {
        case 1:
            //Show the adjacency matrix
            for (int i = 0; i < ver; i++)
                {
                    printf("\n");
                    for (int j = 0; j < ver; j++)
                        {
                            printf("%d ", arr2[i][j]);
                        }
                }
            printf("\n");
            break;
        case 2:
            //Show the incedency matrix
            for (int i = 0; i < d; i++)
                {
                printf("\n");
                for (int j = 0; j < ver; j++)
                    printf("%d  ",arr1[i][j]);
                }
            printf("\n");
            break;
        case 3:
            //Show the adjacency list
            for (int i = 0; i < ver; i++)
            {
                    printf("%d - ",i+1);
                for (int j = 0; j < ver; j++)
                    {
                        if (arr[i][j] == 0)
                            {
                                printf("%d ", arr[i][j]);
                                printf("\n");
                                break;
                            }
                        else
                            {
                              printf("%d, ", arr[i][j]);
                            }
                    }
              }
            break;
        case 4:
            // exit the program
            return 0;
            break;
        default:
            break;
        }
    }
}
