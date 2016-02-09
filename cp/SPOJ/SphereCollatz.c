#include <stdio.h>

int main()
{	
		int begin,end,i,cur_cnt,max_cnt,a;		

		scanf("%d",&begin);	
		scanf("%d",&end);

		while( (begin != '\0' || end != '\0') )
		{	
			if(begin > end){
				int jaime; 
				jaime = begin;
				begin = end;
				end = jaime;
			}
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
				}		
			}
			printf("%d %d %d\n",begin,end,max_cnt);
			begin = 0;
			end = 0;
			i = 0;
			cur_cnt = 0;
			max_cnt = 0;
			a = 0;
			scanf("%d",&begin);	
			scanf("%d",&end);
		}
		
			

}