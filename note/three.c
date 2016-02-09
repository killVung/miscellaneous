#include <stdio.h>

void main()
{
	int num[] = {900,1000};

	int cur_cnt,max_cnt,a,b,i;	
	int begin = num[0];
	int end = num[1];

	for(i = begin; i <= end; i++)
	{	
		cur_cnt = 1;		
		a = i;

		while(a != 1)
		{
			if(a % 2 == 0)
			{
				a /= 2;
				cur_cnt++;
			}
			else
			{
				a *= 3;
				a += 1;
				cur_cnt++;
			}
		}
		if(max_cnt < cur_cnt)
		{
			max_cnt = cur_cnt;
			b = i;
		}
	}
	printf("max_cnt: %d\n",max_cnt);
	printf("b: %d\n",b);

}